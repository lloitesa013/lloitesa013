# AI Verification Portfolio

I build judgment layers for AI systems: reference architectures that make model
decisions traceable, safely gated, user-governed, and evidence-bound.

This document is the public portfolio hub. It is intentionally selective. The
private archive keeps rough notes, drafts, admissions material, failed runs, and
personal context. This public hub keeps only research and code that can be shown
safely.

## Core Thesis

Modern AI systems can generate persuasive outputs faster than people can verify
them. The hard problem is not only generation. It is knowing whether a model
decision or system claim is reproducible, scoped, auditable, and safe to present.

My work has two connected tracks:

- **AI decision verification**: can a model output be gated, traced, redacted,
  and reviewed before it becomes an action?
- **AI claim verification**: can a benchmark or product claim survive evidence
  gates, release gates, and non-claim boundaries?

## Flagship Projects

### Cognitive OS API

**Purpose:** place a decision protocol above upstream LLM outputs.

**System shape:** profile policy is compiled into a Cognitive Configuration
Profile, candidate model output is analyzed, and the system emits `ALLOW`,
`DEGRADE`, `DENY`, or `HANDOFF` with a public decision envelope.

**Evidence surface:**

- API endpoints for profile compilation, run, compare, trace, and validation.
- Redacted public traces with raw local traces disabled from public output by
  default.
- Seed benchmark and conformance runners.
- Non-claims around AGI, global safety status, universal blocking, and complete
  safety guarantees.

Repo: [cognitive-os-api](https://github.com/lloitesa013/cognitive-os-api)

### Financial Agent Evidence OS

**Purpose:** verify financial-agent claims without presenting the system as a
trading bot or investment tool.

**System shape:** benchmark gates, release gates, evidence manifests, and
reviewer-facing packets test whether a claim is scoped, reproducible, and
properly bounded.

**Evidence surface:**

- Downside-aware backtest verification harness.
- Evidence packets, release seals, and reproduction commands.
- Public non-claims around financial advice, live trading readiness, future
  return promises, and market dominance.
- Real-market defense material that preserves weak evidence instead of turning
  every result into promotion.

Repo: [stock-agent-harness-v0-2-0-defense](https://github.com/lloitesa013/stock-agent-harness-v0-2-0-defense)

### X-MoD / Angelos OS Research Line

**Purpose:** show where the judgment-layer architecture came from before it was
generalized to LLMs and agent evidence.

**System shape:** X-MoD routes driving decisions over explicit drives such as
safety, legality, comfort, and efficiency. Angelos OS adds a top-level judgment
layer that can restrain, gate, and explain candidate actions in CARLA scenarios.

**Evidence surface:**

- Offline routing evaluation, ablations, negative controls, and multi-seed
  stability reports.
- Closed-loop CARLA protocol runs with scenario-specific result tables.
- Failure analysis around mobility freeze, legality tradeoffs, and scope limits.
- Papers and technical reports kept as research artifacts, not as deployment
  claims.

Public status: summarized here as research lineage. The raw local workspace
should be sanitized before any standalone public release.

## Research Lineage

The earlier research line connects autonomous driving explainability to LLM and
agent governance.

| Stage | Recipe | What it contributed |
| --- | --- | --- |
| Flow-Based AI Ethics Model | Ethical cognition flow | Emotion, perception, simulation, evaluation, and decision as a structured loop. |
| Explainable Autonomous Simulation | CARLA interpretability demo | A first attempt to make autonomous decisions visible rather than opaque. |
| X-MoD | Explainable routing | Explicit drives such as safety, legality, comfort, and efficiency. |
| Angelos OS | Safety-gated judgment | A model-agnostic restraint layer above autonomous policies. |
| Cognitive OS | User-owned policy | Policy profiles and decision gates above LLM outputs. |
| Evidence OS | Claim verification | Evidence packets and release gates for agent claims. |

Full lineage: [AI_JUDGMENT_LINEAGE.md](AI_JUDGMENT_LINEAGE.md)

## Evidence Matrix

| Project | Code | Tests / gates | Evidence artifacts | Public role |
| --- | --- | --- | --- | --- |
| Cognitive OS API | Yes | Benchmark and conformance runners | Decision envelopes and traces | Flagship decision protocol |
| Financial Agent Evidence OS | Yes | Benchmark, release, and replay gates | Evidence packets and release seals | Evidence discipline |
| X-MoD / Angelos OS | Local research artifacts | Offline and CARLA evaluation reports | Papers and technical reports | Research lineage |
| Flow-Based AI Ethics Model | Conceptual paper | Not a benchmarked system | Architecture note | Concept origin |

## What This Shows

- I can design systems around traceability, scope, and reviewable evidence.
- I can turn prototypes into reference architectures with docs, tests, gates,
  and release artifacts.
- I can preserve unfavorable results instead of hiding them.
- I can separate demo value from public claim boundaries.

## What This Does Not Claim

- No external adoption claim.
- No global SOTA status outside the included benchmark suites.
- No AGI claim.
- No live trading readiness or investment-performance claim.
- No complete AI safety guarantee.
- No claim that these reference architectures are enterprise-ready without
  further hardening.

## Next Work

The next implementation phase should start from the product map rather than from
new unrelated projects. The priority order is:

1. Cognitive OS demo polish.
2. Evidence OS dashboard polish.
3. X-MoD visual paper kit.
4. Angelos/CARLA reproducibility kit.

See: [PRODUCT_MAP.md](PRODUCT_MAP.md)
