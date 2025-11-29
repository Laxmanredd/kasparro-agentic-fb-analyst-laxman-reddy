import json

def generate_report(summary, insights, evaluated, creatives):
    report = []

    # Title
    report.append("# 📊 Facebook Ads Performance Report\n")

    # Section 1: ROAS & CTR Overview
    report.append("## 1. Overall Performance Summary\n")
    report.append(f"- **ROAS (overall avg)**: {summary['overall'].get('roas_mean')}\n")
    report.append(f"- **CTR (overall avg)**: {summary['overall'].get('ctr_mean')}\n")
    report.append(f"- **Total Spend**: {summary['overall'].get('total_spend')}\n")
    report.append(f"- **Total Revenue**: {summary['overall'].get('revenue')}\n")

    report.append("\n### Recent Trends (Last 14 Days)\n")
    report.append(f"- ROAS Change: {insights['roas_trend']}\n")
    report.append(f"- CTR Change: {insights['ctr_pattern']}\n")
    report.append(f"- Purchases (14 Days): {insights['purchases_pattern']}\n")

    # Section 2: Hypotheses & Validation
    report.append("\n## 2. Insight Agent Hypotheses\n")
    for h in insights["primary_hypotheses"]:
        report.append(f"- **Hypothesis**: {h['hypothesis']}")
        report.append(f"  - Reasoning: {h['reasoning']}")
        report.append(f"  - Evidence: {h['evidence']}")
        report.append(f"  - Initial Confidence: {h['confidence']}\n")

    report.append("\n## 3. Evaluator Agent Validation\n")
    for ev in evaluated["evaluated_hypotheses"]:
        report.append(f"- **{ev['hypothesis']}**")
        report.append(f"  - Evidence Validation: {ev['evidence_validation']}")
        report.append(f"  - Adjusted Confidence: {ev['adjusted_confidence']}\n")

    # Section 4: Creative Suggestions
    report.append("\n## 4. Creative Improvement Suggestions\n")
    for c in creatives["campaign_creative_suggestions"]:
        report.append(f"### Campaign: {c['campaign_name']}")
        report.append(f"- **Old Message**: {c['old_creative_message']}")
        report.append(f"- **New Headline**: {c['new_headline']}")
        report.append(f"- **New Primary Text**: {c['new_primary_text']}")
        report.append(f"- **CTA**: {c['new_cta']}")
        report.append(f"- Reasoning: {c['reasoning']}\n")

    return "\n".join(report)


if __name__ == "__main__":
    with open("reports/data_summary.json") as f:
        summary = json.load(f)

    with open("reports/insights.json") as f:
        insights = json.load(f)

    with open("reports/evaluated_insights.json") as f:
        evaluated = json.load(f)

    with open("reports/creatives.json") as f:
        creatives = json.load(f)

    md_report = generate_report(summary, insights, evaluated, creatives)

    with open("reports/report.md", "w") as f:
        f.write(md_report)

    print("Generated → reports/report.md")
