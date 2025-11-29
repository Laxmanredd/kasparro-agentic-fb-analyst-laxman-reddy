# EVALUATOR AGENT — VALIDATE WITH DATA

## Goal
Evaluate each hypothesis from insight_agent using:
- Numeric evidence
- CTR change
- ROAS change
- Spend patterns
- Campaign-level metrics

## Output Format (JSON ONLY)
{
  "evaluated_hypotheses": [
    {
      "hypothesis": "",
      "initial_confidence": 0.0,
      "evidence_validation": "",
      "adjusted_confidence": 0.0
    }
  ]
}
