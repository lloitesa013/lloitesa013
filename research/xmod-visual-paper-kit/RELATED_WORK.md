# Related Work Positioning

This is a public positioning map, not a complete literature survey. It explains where X-MoD sits and what still needs to be compared before making broader research claims.

| Area | Typical Focus | What X-MoD Borrows | What X-MoD Adds | Current Gap |
| --- | --- | --- | --- | --- |
| Mixture-of-experts / conditional routing | Route inputs to specialized experts | Explicit router weights and specialized expert heads | Drive-named routing tied to decision values | Needs direct external MoE driving baselines |
| Interpretable autonomous driving | Explain decisions after or during policy execution | Human-readable axes and event labels | Falsifiable gate-event alignment checks | Needs richer visual traces and more event types |
| Safety monitors / runtime shields | Block unsafe actions or trigger fallback | Separation between policy proposal and gate decision | Lightweight decision layer with traceable gate reason | Needs broader closed-loop stress tests |
| Imitation learning / behavior cloning | Learn action policies from recorded data | Offline supervised protocol and aggregate metrics | Negative controls for semantic alignment | Needs data coverage analysis beyond aggregate CSV |
| Closed-loop evaluation | Test agents in simulator scenarios | Scenario-level collision and route metrics | Links offline gate alignment to later gating studies | Needs public reproducibility package with sanitized protocol |
| Claim-boundary reporting | State what a system does and does not show | Explicit non-claims and limitations | Drive-level validation matrix | Needs full references and citations in paper form |

## Public Boundary

The current kit supports a narrow statement: safety-gate alignment evidence under the included offline protocol.

It does not claim that all four drives are equally validated, that the raw workspace is ready for public release, or that X-MoD dominates external autonomous-driving systems.
