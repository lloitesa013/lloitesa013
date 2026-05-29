# Verification Principles

My GitHub should not say "I am impressive." It should show that the work can be checked.

The final standard is:

**Works. Reproducible. Measured. Understandable. Bounded.**

## 1. It Works

Code should actually run.

- Quick start commands execute.
- Tests pass.
- Demo UI or API opens.
- Example input produces example output.

## 2. It Is Reproducible

A reviewer should be able to check where a result came from.

- Environment notes are present.
- Commands are listed.
- Seeds, benchmark names, input data, or release artifacts are identified.
- Expected output or pass/fail result is documented.

## 3. It Is Measurable

Claims should be tied to metrics or gates, not vague confidence.

Examples:

- Gate Accuracy
- Trace Completeness
- Conformance Pass Rate
- latency
- correlation
- coverage
- PASS / FAIL / PENDING

## 4. It Is Understandable

A first-time reader should understand the project without private context.

- One-sentence thesis.
- What it is.
- What it verifies.
- How to run it.
- Architecture diagram or visual evidence when useful.
- What it does not claim.

## 5. It Does Not Overclaim

Boundaries are part of the evidence, not a footnote.

This portfolio does not claim:

- AGI
- guaranteed safety
- financial advice
- live trading readiness
- universal benchmark dominance
- complete AI alignment

## Release Gate

Before a project is treated as public-ready, it should answer:

| Principle | Gate question |
| --- | --- |
| Works | Can someone run the code or demo from the README? |
| Reproducible | Can someone rerun or verify the evidence path? |
| Measured | Are there tests, metrics, validators, or pass/fail gates? |
| Understandable | Can a first-time reader explain the project in 30 seconds? |
| Bounded | Are limitations and non-claims visible next to the evidence? |

