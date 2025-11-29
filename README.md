
#   Kasparro Agentic Facebook Performance Analyst — Laxman Reddy

This project implements a fully autonomous multi-agent system that analyzes Facebook Ads performance, identifies reasons for ROAS changes, and generates improved creative recommendations.

This system follows Kasparro’s assignment specification:

*   **Planner Agent**
*   **Data Agent**
*   **Insight Agent**
*   **Evaluator Agent**
*   **Creative Agent**
*   **Final Report Generator**

## ➒ Folder Structure
```
kasparro-agentic-fb-analyst-laxman-reddy/
│
└── README.md
└── requirements.txt
└── run.py
└── Makefile (optional)
│
└── config/
│   └── config.yaml
│
└── prompts/
│   └── data_agent_prompt.md
│   └── insight_agent_prompt.md
│   └── evaluator_agent_prompt.md
│   └── creative_agent_prompt.md
│
└── src/
│   └── agents/
│   │     └── data_agent.py
│   │     └── insight_agent.py
│   │     └── evaluator_agent.py
│   │     └── creative_agent.py
│   └── orchestrator/
│   │     └── run_orchestrator.py
│   └── utils/
│         └── logger.py
│
└── data/
│   └── synthetic_fb_ads_undergarments.csv
│
└── reports/
│   └── data_summary.json
│   └── insights.json
│   └── evaluated_insights.json
│   └── creatives.json
│   └── report.md
│
└── logs/
└── agent_logs.json

```

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

## ✅ How to Run the System

```bash
python run.py "Analyze last 14 days performance"
```
The system will automatically:

*   Load dataset
*   Generate data summary
*   Produce insights
*   Validate insights
*   Generate creative recommendations
*   Create final report in `reports/report.md`

## ✨ Agent Architecture Overview

*   **Data Agent**: Summarizes dataset
*   **Insight Agent**: Generates hypotheses (Think → Analyze → Conclude)
*   **Evaluator Agent**: Performs quantitative validation
*   **Creative Agent**: Proposes improved creatives
*   **Orchestrator**: Manages full pipeline

See `agent_graph.md` for diagram & flow.

##   Example Output Files

*   `reports/data_summary.json`
*   `reports/insights.json`
*   `reports/evaluated_insights.json`
*   `reports/creatives.json`
*   `reports/report.md`
=======
📌 1. Overview

This project implements a multi-agent, fully autonomous Facebook Ads Performance Analyst.

The system:

Diagnoses ROAS fluctuations

Detects performance drivers such as audience fatigue, creative decline, spend spikes, and CTR drops

Generates structured hypotheses

Validates them with quantitative evidence

Produces improved creative suggestions for low-CTR campaigns

Outputs a marketer-ready final performance report

The entire workflow uses structured agentic reasoning with multiple collaborating agents.

🧠 2. Agentic Architecture

The system consists of five specialized agents, each performing a focused task in the intelligence pipeline.

🔹 Planner Agent

Decomposes the query into substeps and orchestrates the sequence of agents.

🔹 Data Agent

Loads, cleans, and summarizes the dataset.
Extracts key signals including:

Overall performance

ROAS and CTR trends

Recent 14-day metrics

Low-CTR campaigns

Spend and revenue patterns

🔹 Insight Agent

Uses structured reasoning (Think → Analyze → Conclude) to generate hypotheses explaining why ROAS or CTR changed.

🔹 Evaluator Agent

Validates hypotheses using:

Percentage drops

Spend ratios

Campaign-level evidence

Quantitative thresholds

Confidence levels are strengthened or reduced based on the evidence.

🔹 Creative Agent

Enhances creative assets for low-CTR campaigns by generating:

New headlines

Better primary text

Strong CTAs

Messaging aligned with the original tone

🚀 3. Quick Start
Clone the repository
git clone https://github.com/<username>/kasparro-agentic-fb-analyst-laxman-reddy
cd kasparro-agentic-fb-analyst-laxman-reddy

Install dependencies
pip install -r requirements.txt

Run the multi-agent system
python run.py "Analyze ROAS drop"

Outputs generated automatically:

reports/report.md

reports/insights.json

reports/evaluated_insights.json

reports/creatives.json

logs/agent_logs.json

📊 4. Example Outputs
🔍 Insight Example (insights.json)
{
  "roas_trend": "ROAS dropped -18% in the last 14 days",
  "primary_hypotheses": [
    {
      "hypothesis": "Audience saturation in low-CTR campaigns",
      "evidence": "CTR = 0.00 on 5 campaigns",
      "confidence": 0.6
    }
  ]
}

🎨 Creative Suggestion Example (creatives.json)
{
  "campaign_name": "Women Seamless Everyday",
  "new_headline": "Your Perfect Fit Awaits!",
  "cta": "Shop Now"
}

🧪 5. Tests

Run evaluator tests:

pytest tests/

⚙️ 6. Configuration Example

The file config/config.yaml contains flexible settings:

thresholds:
  ctr_drop_alert: -10
  roas_drop_alert: -10
  spend_spike_ratio: 0.5

📝 7. Reproducibility

The project ensures reproducibility via:

Pinned dependencies

Deterministic summarization

Seeded randomness

Included dataset

📌 8. Logging

All agents record structured logs to:

logs/agent_logs.json


Logs include:

timestamps

agent name

event description

data snapshot

🏁 9. Self-Review Summary (PR Description)

Title: Self-Review — Agentic Facebook Performance Analyst
Summary:
This PR implements the complete multi-agent system required for the Kasparro Applied AI Engineer assignment.
The design uses modular agents, structured prompts, deterministic evaluation logic, observability through logs, and reproducibility. The pipeline autonomously generates insights, validates hypotheses, and produces actionable creative recommendations.

🏷 10. Release Tag

Create a GitHub release:

Tag: v1.0

Name: Agentic FB Analyst — Initial Release

Description:
Contains all agents, prompts, dataset, reports, tests, config files, and the CLI execution script.

