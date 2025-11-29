import json

def adjust_confidence(initial, strength):
    if strength == "strong":
        return min(initial + 0.20, 1.0)
    if strength == "medium":
        return min(initial + 0.10, 1.0)
    return max(initial - 0.10, 0.10)


def evaluate_hypotheses(insights, summary):
    output = {"evaluated_hypotheses": []}

    overall_roas = summary["overall"].get("roas_mean")
    last14_roas = summary.get("last_14", {}).get("roas_mean")
    overall_ctr = summary["overall"].get("ctr_mean")
    last14_ctr = summary.get("last_14", {}).get("ctr_mean")

    # Calculate numeric trends
    roas_drop = None
    if overall_roas and last14_roas:
        roas_drop = ((last14_roas - overall_roas) / overall_roas) * 100

    ctr_drop = None
    if overall_ctr and last14_ctr:
        ctr_drop = ((last14_ctr - overall_ctr) / overall_ctr) * 100

    for h in insights["primary_hypotheses"]:
        name = h["hypothesis"]
        initial_conf = h["confidence"]
        evidence_summary = ""

        strength = "weak"

        if name == "Creative fatigue":
            if ctr_drop is not None and ctr_drop < -10:
                strength = "strong"
                evidence_summary = f"CTR dropped {ctr_drop:.2f}%."
            else:
                evidence_summary = f"CTR drop not significant ({ctr_drop})."

        elif name == "Spend increased but efficiency did not improve":
            spend14 = summary.get("last_14", {}).get("total_spend", 0)
            spend_total = summary["overall"].get("total_spend", 1)
            if spend14 > spend_total * 0.5:
                strength = "medium"
                evidence_summary = "Spend spike confirmed."
            else:
                evidence_summary = "Spend spike not confirmed."

        elif name == "Audience saturation in low-CTR campaigns":
            low_ctr_list = summary.get("lowest_ctr_campaigns", [])
            if len(low_ctr_list) > 0:
                strength = "medium"
                evidence_summary = "Multiple low-CTR campaigns detected."
            else:
                evidence_summary = "Low-CTR pattern not strong."

        elif name == "Stable performance":
            if roas_drop is not None and abs(roas_drop) < 5:
                strength = "medium"
                evidence_summary = "ROAS stable."
            else:
                evidence_summary = "ROAS variation detected."

        # Adjust confidence score
        adjusted = adjust_confidence(initial_conf, strength)

        output["evaluated_hypotheses"].append({
            "hypothesis": name,
            "initial_confidence": initial_conf,
            "evidence_validation": evidence_summary,
            "adjusted_confidence": adjusted
        })

    return output


if __name__ == "__main__":
    with open("reports/insights.json") as f:
        insights = json.load(f)

    with open("reports/data_summary.json") as f:
        summary = json.load(f)

    evaluated = evaluate_hypotheses(insights, summary)

    with open("reports/evaluated_insights.json", "w") as f:
        json.dump(evaluated, f, indent=2)

    print("Generated → reports/evaluated_insights.json")
