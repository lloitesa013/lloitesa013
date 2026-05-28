# lloitesa013

**I build reference architectures for verifying AI claims and decisions.**

I do not build more impressive AI outputs. I build systems that test whether AI
outputs can be trusted, scoped, traced, and sealed as evidence.

## Portfolio

### Financial Agent Evidence OS

Financial AI claim verification reference architecture.

- Verifies scoped performance claims with benchmark gates, release gates, and
  evidence manifests.
- Preserves non-claims: no financial advice, no live trading readiness, and no
  future-return guarantee.
- Latest: v0.3.1 Presentation UI and v0.3 Real Market Data Defense.

Repo: [stock-agent-harness-v0-2-0-defense](https://github.com/lloitesa013/stock-agent-harness-v0-2-0-defense)

### Cognitive OS API

LLM decision, gate, and trace verification reference architecture.

- Compiles profile policy, analyzes candidate output, and emits
  `ALLOW`, `DEGRADE`, `DENY`, or `HANDOFF` decision envelopes.
- Redacts public trace output by default; raw traces require explicit local
  opt-in.
- Reports 100% gate accuracy, trace completeness, and conformance pass rate on
  the included seed benchmark suite.

Repo: [cognitive-os-api](https://github.com/lloitesa013/cognitive-os-api)

## Proof Surface

Python - FastAPI - Streamlit - CI gates - benchmark harnesses - evidence
manifests - release gates

## Current Focus

- Claim-governed AI systems
- Reproducible evaluation harnesses
- Decision envelopes and trace privacy
- Evidence-first product surfaces

## Claim Boundary

This portfolio does not claim external adoption, global SOTA status, live
trading readiness, investment performance, or complete AI safety. Its claims are
scoped to the included reference architectures, benchmark suites, and published
evidence artifacts.
