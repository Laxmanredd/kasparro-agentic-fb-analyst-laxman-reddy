# DATA AGENT — SUMMARIZE DATA

## Goal
Given a raw dataset, generate a summary of key metrics and trends.

## Output Format (JSON ONLY)
{
  "overall": {
    "total_spend": "...",
    "impressions": "...",
    "clicks": "...",
    "ctr_mean": "...",
    "purchases": "...",
    "revenue": "...",
    "roas_mean": "..."
  },
  "last_14": {
    "total_spend": "...",
    "impressions": "...",
    "clicks": "...",
    "ctr_mean": "...",
    "purchases": "...",
    "revenue": "...",
    "roas_mean": "..."
  },
  "lowest_ctr_campaigns": [
    {
      "campaign_name": "...",
      "ctr": "..."
    }
  ],
  "sample_creatives_low_ctr": [
    {
      "campaign_name": "...",
      "creative_message": "..."
    }
  ]
}
