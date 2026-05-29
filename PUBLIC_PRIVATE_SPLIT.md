# Public / Private Split

This document defines what can be public and what stays in the private master
archive.

## Public

Safe to include in GitHub profile or public repositories:

- Cognitive OS API repo and sanitized docs.
- Financial Agent Evidence OS repo and sanitized evidence docs.
- X-MoD / Angelos research lineage summaries.
- Claim boundaries and non-claims.
- Evidence matrices.
- Reproduction commands for public repos.
- Product maps that describe future implementation without private context.

## Private

Keep out of public repositories:

- Admissions PDFs and application material.
- Essays, personal statements, and school explanations.
- Personal contact information, addresses, phone numbers, and applicant IDs.
- Rough emotional notes and private motivation.
- Broken PDF exports or corrupted text.
- Unreviewed drafts that contain overbroad claims or sensitive context.

## Rewrite Before Public

These can become public only after rewriting:

- Personal origin story.
- Early supplementary papers.
- Early autonomous driving reports.
- Raw CARLA workspaces that contain mixed experiments, generated artifacts, or
  private notes.
- Failed experiments.
- Notes that mention external people, schools, or private circumstances.

Rewrite requirements:

- Remove personal identifiers.
- Replace emotional/private context with research context.
- Add claim boundaries.
- Add non-claims.
- Make status clear: concept, prototype, benchmarked result, or product idea.
- Publish only the sanitized reproduction surface, not the entire local
  research workspace.

## Never Publish As-Is

- Application PDFs.
- Raw personal documents.
- Screenshots containing private identifiers.
- Any file with phone numbers, addresses, applicant IDs, or family details.

## Public Claim Rule

Terms such as global SOTA status, AGI, safety, performance, and guarantee must
not appear as standalone public claims. If they appear, they must be inside a
boundary or non-claim statement.
