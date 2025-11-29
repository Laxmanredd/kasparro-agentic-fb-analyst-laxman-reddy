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
