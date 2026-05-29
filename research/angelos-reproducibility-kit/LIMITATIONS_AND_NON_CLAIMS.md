# Angelos Limitations And Non-Claims

## Limitations

- The evidence is local to CARLA 0.9.15, Town03, two scenario families, and stored baselines.
- The pedestrian scenario must be interpreted as pedestrian-priority behavior, not as route-completion dominance.
- The primary pedestrian anchor still includes caveats: non-zero red-light violation rate and a minority of over-conservative near-zero-route behavior.
- Later pedestrian variants expose mobility freeze. They are failure-analysis evidence, not replacement anchors.
- Intervention, near-miss, and critical-event differences are not uniformly dominant across both scenarios.
- This package is sanitized. It does not include the full raw workspace, external repos, datasets, or environment folders.

## Non-Claims

- No real-world autonomous-driving deployment readiness claim.
- No universal safety superiority claim.
- No claim that CARLA local evidence transfers directly to road deployment.
- No claim that all driving scenarios are solved.
- No claim that the raw workspace is ready to publish as-is.

## Public Use Rule

Use the phrase "protocol-frozen CARLA evidence for a top-level judgment layer" rather than broad deployment or universal safety language.

