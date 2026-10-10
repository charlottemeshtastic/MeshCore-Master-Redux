# Link verification report

Checked October 9, 2026 (America/New_York). Followed HTTP redirects with GET requests, a 25-second request limit and one automatic retry. ESTMesh additionally succeeded on a separate retry. GitHub 404 was checked again using authenticated API. Full destination/status/title evidence is in link-checks.json. Configuration regex patterns are not URLs and were excluded from the final audit.

Results for 473 distinct external URLs across source files: Counter({'reachable': 435, 'uncertain': 37, 'broken-candidate': 1}). “Reachable” means HTTP 2xx and no detected challenge title, not verified functionality. Social pages/invites are uncertain even when they return 200.

## Broken or uncertain

| URL | HTTP | Finding / action |
| --- | --- | --- |
| https://analyzer.letsmesh.net/ | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://discord.gg/6KSQBqaTmw | 200 | Retained where relevant; manual access/functionality verification required. MESHCORE GREECE |
| https://discord.gg/CnnDfER3Yt | 200 | Retained where relevant; manual access/functionality verification required. Cascadia Mesh |
| https://discord.gg/XFSA9f5kqM | 200 | Retained where relevant; manual access/functionality verification required. Central Washington Hackers |
| https://discord.gg/ZVH2ujy9ex | 200 | Legacy invite consolidated into meshcore.gg; invite validity uncertain. Discord |
| https://discord.gg/tKGFwFYvsT | 200 | Retained where relevant; manual access/functionality verification required. LoRa Mesh Comms ZA |
| https://forum.letsmesh.net/ | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://github.com/HDDen/meshcore-open | 404 | Removed from main list; no verified replacement. Page not found · GitHub · GitHub |
| https://matrix.to/#/#meshcore-netzwerk-de:matrix.org | 200 | Retained where relevant; manual access/functionality verification required. You're invited to talk on Matrix |
| https://meshcore.gg | 200 | Retained where relevant; manual access/functionality verification required. MeshCore.io |
| https://meshcore.hu/ | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://old.reddit.com/r/meshcore/ | 200 | Duplicate removed; redirects to login. Welcome to Reddit |
| https://t.me/MeshCore_KRD | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @MeshCore_KRD |
| https://t.me/MeshCore_offline_network | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @MeshCore_offline_network |
| https://t.me/Meshcore_Rostov_na_Donu | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @Meshcore_Rostov_na_Donu |
| https://t.me/meshcore_ita | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @meshcore_ita |
| https://t.me/meshcore_rulang | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @meshcore_rulang |
| https://t.me/meshcoreat | 200 | Retained where relevant; manual access/functionality verification required. Telegram: Contact @meshcoreat |
| https://t.me/meshcorebrasil | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @meshcorebrasil |
| https://t.me/meshcorede | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @meshcorede |
| https://t.me/meshcoremoscow | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @meshcoremoscow |
| https://t.me/meshtastic_stv | 200 | Retained where relevant; manual access/functionality verification required. Telegram: View @meshtastic_stv |
| https://tdeck.ubnzeek.com/ | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.facebook.com/MeshCoreOfficial | 200 | Retained where relevant; manual access/functionality verification required. MeshCore |
| https://www.facebook.com/groups/meshcore | 200 | Retained where relevant; manual access/functionality verification required. MeshCore Official |
| https://www.printables.com/model/1490873-the-corebell-a-meshcoremeshtastic-solar-node | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.printables.com/model/1767610-meshcore-mast-enclosure-heltec-v3 | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.reddit.com/r/MeshCoreIndia/ | 200 | Retained where relevant; manual access/functionality verification required. Reddit |
| https://www.reddit.com/r/meshcore/ | 200 | Retained where relevant; manual access/functionality verification required. Reddit |
| https://www.thingiverse.com/thing:7383479 | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.thingiverse.com/thing:7390213 | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.thingiverse.com/thing:7394936 | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.thingiverse.com/thing:7395161 | 403 | Retained where relevant; manual access/functionality verification required. Just a moment... |
| https://www.youtube.com/@andykirby | 200 | Retained where relevant; manual access/functionality verification required. andy kirby - YouTube |
| https://www.youtube.com/@meshcore-official | 200 | Retained where relevant; manual access/functionality verification required. MeshCore - YouTube |
| https://www.youtube.com/playlist?list=PLshzThxhw4O4WU_iZo3NmNZOv6KMrUuF9 | 200 | Retained where relevant; manual access/functionality verification required. MeshCore QuickStart - YouTube |
| https://www.youtube.com/watch?v=t1qne8uJBAc | 200 | Retained where relevant; manual access/functionality verification required. How to get started with MeshCore off grid text messaging - YouTube |
| https://x.com/mesh_core | 200 | Retained where relevant; manual access/functionality verification required. MeshCore (@mesh_core) / X |

## Redirects

| Original | Destination |
| --- | --- |
| https://awesome.re | https://github.com/sindresorhus/awesome#readme |
| https://discord.gg/6KSQBqaTmw | https://discord.com/invite/6KSQBqaTmw |
| https://discord.gg/CnnDfER3Yt | https://discord.com/invite/CnnDfER3Yt |
| https://discord.gg/XFSA9f5kqM | https://discord.com/invite/XFSA9f5kqM |
| https://discord.gg/ZVH2ujy9ex | https://discord.com/invite/ZVH2ujy9ex |
| https://discord.gg/tKGFwFYvsT | https://discord.com/invite/tKGFwFYvsT |
| https://github.com/dz0ny/meshcore-t5-epaper-s3-pro | https://github.com/dz0ny/meshcore-paperui |
| https://github.com/meshcore-go/meshcore-bot | https://github.com/OwlShack/OwlBot |
| https://github.com/meshcore-go/meshcore-go | https://github.com/OwlShack/meshcore-go |
| https://gulfcoastmesh.org | https://www.gulfcoastmesh.org/ |
| https://localmesh.de/karte/ | https://www.localmesh.de/karte/ |
| https://localmesh.nl/en/map/ | https://www.localmesh.nl/en/map/ |
| https://loramesh.fr/ | https://www.loramesh.fr/ |
| https://loramesh.fr/carte/ | https://www.loramesh.fr/carte/ |
| https://map.meshcore.dev/ | https://map.meshcore.io/ |
| https://meshcore.coloradomesh.org/ | https://wiki.coloradomesh.org/index.php/MeshCore |
| https://meshcore.gg | https://discord.com/invite/fUfWevRXAg |
| https://meshcore.pt/ | https://www.meshcore.pt/en/home |
| https://meshcoreeurope.org/ | https://meshcoreeurope.org/en/ |
| https://meshcoretel.io/ | https://meshcoretel.io/en |
| https://meshcoretel.ru/ | https://meshcoretel.ru/ru |
| https://old.reddit.com/r/meshcore/ | https://old.reddit.com/login/?reason=lor2&dest=https%3A%2F%2Fold.reddit.com%2Fr%2Fmeshcore%2F |
| https://tdeck.ubnzeek.com/ | https://www.patreon.com/UBNZeek/posts/meshultra-now-167932266 |
| https://umap.openstreetmap.de/en/map/meshcore-defyi_130650 | https://umap.openstreetmap.de/en/map/meshcore-defyi-region-map_130650 |
| https://wiki.mesh-idf.fr | https://wiki.mesh-idf.fr/fr/home |
| https://www.contributor-covenant.org/version/2/1/code_of_conduct.html | https://www.contributor-covenant.org/version/2/1/code_of_conduct/ |

The flasher.meshcore.co.uk page also contains a JavaScript redirect to https://www.meshcore.co.uk/flasher.html; HTTP redirects alone do not capture it. Root domains that add www or a language path are retained as stable entrypoints. Login and Patreon redirects were not substituted as canonical resource URLs.
