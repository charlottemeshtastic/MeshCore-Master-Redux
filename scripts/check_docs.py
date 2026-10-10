"""Check local Markdown targets, heading anchors and duplicate README URLs."""
import collections
import pathlib
import re
import unicodedata
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parents[1]

def anchors(text):
    seen = collections.Counter()
    result = set()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = ''.join(c for c in heading.lower() if c in ' -_' or unicodedata.category(c)[0] in 'LN')
        slug = slug.replace(' ', '-')
        count = seen[slug]
        seen[slug] += 1
        result.add(slug if count == 0 else f'{slug}-{count}')
    return result

errors = []
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text()
    clean = re.sub(r'```.*?```|`[^`\n]*`', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)]+)\)', clean):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        file, _, fragment = unquote(target).partition('#')
        destination = path.parent / file if file else path
        if not destination.is_file():
            errors.append(f'{path.relative_to(ROOT)}: missing {target}')
        elif fragment and destination.suffix == '.md' and fragment not in anchors(destination.read_text()):
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')
readme = (ROOT / 'README.md').read_text()
urls = [u.lower().rstrip('/') for u in re.findall(r'\]\((https?://[^)]+)\)', readme)]
for url, count in collections.Counter(urls).items():
    if count > 1:
        errors.append(f'README.md: duplicate external URL {url}')
if errors:
    raise SystemExit('\n'.join(errors))
print('Markdown paths, anchors and README URL uniqueness passed.')
