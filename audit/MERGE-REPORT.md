# Merge and content review

Reviewed all tracked files from both pinned snapshots (see source-files.json); 459 + 13 = 472 source resource entries. The resulting README contains 455 primary resource entries. Each original entry is accounted for in entry-decisions.json.

## Decisions

- Used the larger list’s category hierarchy and descriptions as the starting point; compared every smaller-list entry against it.
- Kept distinct projects and forks even when names resemble one another. A project root, releases, store listing and hosted app may be complementary links inside one entry.
- Removed MCO Advanced from the main list: public GET and authenticated GitHub API both returned 404. This could be deleted, renamed or private; no replacement was established.
- Merged MeshCore Open / Android releases and MeshCore TEAM / Google Play; corrected TEAM’s conflicting closed-source label.
- Merged MC-T5-Pro into MeshCore PaperUI based on its repository redirect.
- Merged the hosted gessaman key generator with its linked agessaman source repository.
- Removed the second subreddit entry; preserved the primary social listing.
- Added MeshCore.co.uk as an additional MeshCore homepage; removed its duplicate UK-community classification. Its flasher is a JavaScript redirect to a legacy UK flasher; the .io flasher remains canonical.
- Kept the distinct Facebook page alongside the Facebook group. Consolidated the older Discord invite into meshcore.gg, which resolves to a different invite; the old invite did not establish active membership.
- Preserved Andy Kirby under Guides and Learning, rather than claiming it is an official MeshCore account.
- Updated verified OwlShack repository moves and OwlBot name. Labeled SigurdOS Client archived, waev:outpost standalone retired, XIAO updater superseded, and MultiMote Cardputer development paused.
- Marked aXistem companion web distribution closed-source, as its own repository description states.

## Verification limits

Categories were compared with destination titles, repository descriptions and available README/page text. Software was not installed or tested, every feature claim was not independently proven, and live map telemetry / invite membership was not validated. Protected destinations retain source descriptions and are explicitly listed as uncertain. These records distinguish HTTP reachability from maintenance, accuracy and functionality.

## Repository actions

Source repositories were cloned read-only and never pushed. The target already existed with no commits. A minimal main-branch base was required to enable a review PR; the complete list is on a separate branch. The link-check workflow is manual, pins verified action versions, and treats 403/429/503 as findings instead of successes; gated social resources require manual review. Original source history is credited rather than transplanted; snapshots and file hashes make the comparison reproducible.
