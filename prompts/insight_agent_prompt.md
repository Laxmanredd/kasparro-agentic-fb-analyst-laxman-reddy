# INSIGHT AGENT — THINK → ANALYZE → CONCLUDE

## Goal
Given a data summary, detect why ROAS changed and generate hypotheses.

## Required Reasoning Format
1. Think
2. Analyze
3. Conclude

## Output Format (JSON ONLY)
{
  "roas_trend": "...",
  "ctr_pattern": "...",
  "purchases_pattern": "...",
  "primary_hypotheses": [
    {
      "hypothesis": "",
      "reasoning": "",
      "evidence": "",
      "confidence": 0.0
    }
  ]
}
