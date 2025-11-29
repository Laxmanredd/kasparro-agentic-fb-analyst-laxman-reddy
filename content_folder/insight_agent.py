import json
import numpy as np

# Safely convert None values
def safe(x):
    return x if x is not None else 0

# Calculate percent change
def percentage_change(old, new):
    if old is None or old == 0 or new is None:
        return None
    return ((new - old) / old) * 100

def generate_insights(summary):
    overall = summary.get("overall", {})
    last_14 = summary.get("last_14", {})
    last_7  = summary.get("last_7", {})

    # Compute changes
    roas_change_14 = percentage_change(overall.get("roas_mean"), last_14.get("roas_mean"))
    ctr_change_14  = percentage_change(overall.get("ctr_mean"), last_14.get("ctr_mean"))
    purchases_14   = safe(last_14.get("purchases"))

    hypotheses = []

    # Hypothesis 1 — Creative Fatigue
    if ctr_change_14 is not None and ctr_change_14 < -10:
        hypotheses.append({
            "hypothesis": "Creative fatigue",
            "reasoning": "A large drop in CTR suggests the same creatives are being shown repeatedly.",
            "evidence": f"CTR dropped by {ctr_change_14:.2f}% over the last 14 days.",
            "confidence": 0.65
        })

    # Hypothesis 2 — Spend Inefficiency
    if last_14.get("total_spend", 0) > safe(overall.get("total_spend")) * 0.5:
        hypotheses.append({
            "hypothesis": "Spend increased but efficiency did not improve",
            "reasoning": "High spend without proportional ROAS growth indicates inefficiency.",
            "evidence": f"14-day spend: {last_14.get('total_spend')}",
            "confidence": 0.55
        })

    # Hypothesis 3 — Low-CTR Campaigns (Audience Saturation)
    if summary.get("lowest_ctr_campaigns"):
        hypotheses.append({
            "hypothesis": "Audience saturation in low-CTR campaigns",
            "reasoning": "Consistently low CTR often means the target audience is no longer engaging.",
            "evidence": f"Low CTR campaigns: {summary['lowest_ctr_campaigns']}",
            "confidence": 0.60
        })

    # If no hypotheses triggered
    if not hypotheses:
        hypotheses.append({
            "hypothesis": "Stable performance",
            "reasoning": "No strong negative indicators detected.",
            "evidence": "ROAS/CTR changes within stable range.",
            "confidence": 0.40
        })

    # Final JSON structure
    return {
        "roas_trend": f"ROAS 14-day change: {roas_change_14}",
        "ctr_pattern": f"CTR 14-day change: {ctr_change_14}",
        "purchases_pattern": f"Purchases (last 14 days): {purchases_14}",
        "primary_hypotheses": hypotheses
    }


# MAIN EXECUTION
if __name__ == "__main__":
    with open("reports/data_summary.json") as f:
        summary = json.load(f)

    insights = generate_insights(summary)

    with open("reports/insights.json", "w") as f:
        json.dump(insights, f, indent=2)

    print("Generated → reports/insights.json")
