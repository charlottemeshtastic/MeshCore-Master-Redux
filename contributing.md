# Contribution Guidelines

Thanks for helping keep this list useful.

## Adding an entry

- Open a pull request that adds one entry per line, in this format:
  `- [Name](https://example.com) - Short description.`
- Keep the description short, factual and ending with a period.
- Place the entry in the most specific existing section. Only propose a new
  section when several entries would live in it.
- Keep entries in alphabetical order within their section (case-insensitive,
  ignoring a leading "The"). Entries described as "Official" stay at the top.
  Official Resources, Social Media, Supported Devices and Pre-built Devices
  keep their curated order.
- Mark closed-source apps with a trailing lock emoji (🔒) right after the
  link, before the dash: `- [Name](url) 🔒 - Description.` Keep the
  description's first word capitalized so `npx awesome-lint` does not flag
  the line.
- Entries must be MeshCore-related, working and maintained. Confirmed dead links are removed from the main list and recorded in the audit.
  Retired projects may be retained with an explicit historical or migration note.
- Check that the entry is not already listed elsewhere in the readme; duplicate resources should be consolidated, preserving distinct source, download
  and hosted links within one entry.
- Do not add your own project more than once, and do not add affiliate links.

## Quality bar

An entry needs a reason to exist: firmware, client, library, tool, map,
documentation or community that a MeshCore operator would actually use.
Marketing pages, link farms and empty repositories are rejected.

## Before opening the pull request

- Check headings, table-of-contents anchors and duplicate resources.
- Verify every link you added resolves (the scheduled and manually triggered `Check resource links` workflow runs
  [lychee](https://github.com/lycheeverse/lychee) on all Markdown files).
- Use a descriptive pull request title, for example `Add MeshCore Foo`.

## Updating or removing an entry

Review the audit reports for unresolved protected links. Do not treat 403, 429,
login walls or timeouts as proof that a resource is dead.

Corrections, renames and removals of dead projects are welcome. Explain the
reason in the pull request description.

## Guides, comparisons and verification

Use the issue and pull-request templates. Cite primary project documentation for app capabilities, distinguish packaged downloads from source builds, and use “not documented” for unestablished features. Update a document’s manual review date only after reviewing its content. Automated link checks run weekly and for documentation pull requests; results appear in the workflow summary and downloadable report. Gated social links still require manual review.
