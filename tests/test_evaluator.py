# Placeholder for unit tests

import unittest
import json
from src.agents.evaluator_agent import evaluate_hypotheses, adjust_confidence

class TestEvaluatorAgent(unittest.TestCase):

    def test_adjust_confidence_strong(self):
        self.assertAlmostEqual(adjust_confidence(0.5, "strong"), 0.7)
        self.assertAlmostEqual(adjust_confidence(0.9, "strong"), 1.0)

    def test_adjust_confidence_medium(self):
        self.assertAlmostEqual(adjust_confidence(0.5, "medium"), 0.6)
        self.assertAlmostEqual(adjust_confidence(0.95, "medium"), 1.0)

    def test_adjust_confidence_weak(self):
        self.assertAlmostEqual(adjust_confidence(0.5, "weak"), 0.4)
        self.assertAlmostEqual(adjust_confidence(0.1, "weak"), 0.1)

    def test_evaluate_hypotheses(self):
        summary_data = {
            "overall": {"roas_mean": 10, "ctr_mean": 0.02, "total_spend": 1000},
            "last_14": {"roas_mean": 8, "ctr_mean": 0.015, "total_spend": 1200},
            "lowest_ctr_campaigns": [{"campaign_name": "Low CTR Test", "ctr": 0.005}]
        }
        insights_data = {
            "roas_trend": "...",
            "ctr_pattern": "...",
            "purchases_pattern": "...",
            "primary_hypotheses": [
                {"hypothesis": "Creative fatigue", "reasoning": "...", "evidence": "...", "confidence": 0.65},
                {"hypothesis": "Spend increased but efficiency did not improve", "reasoning": "...", "evidence": "...", "confidence": 0.55},
                {"hypothesis": "Audience saturation in low-CTR campaigns", "reasoning": "...", "evidence": "...", "confidence": 0.60},
                {"hypothesis": "Stable performance", "reasoning": "...", "evidence": "...", "confidence": 0.40}
            ]
        }

        evaluated = evaluate_hypotheses(insights_data, summary_data)
        self.assertIsInstance(evaluated, dict)
        self.assertIn("evaluated_hypotheses", evaluated)
        self.assertEqual(len(evaluated["evaluated_hypotheses"]), 4)

        # Check creative fatigue hypothesis (CTR dropped from 0.02 to 0.015 = -25%, which is < -10%)
        creative_fatigue_eval = next(h for h in evaluated["evaluated_hypotheses"] if h["hypothesis"] == "Creative fatigue")
        self.assertAlmostEqual(creative_fatigue_eval["adjusted_confidence"], 0.65 + 0.20)

        # Check spend increase (spend14=1200, total_spend=1000. 1200 > 1000 * 0.5)
        spend_inefficiency_eval = next(h for h in evaluated["evaluated_hypotheses"] if h["hypothesis"] == "Spend increased but efficiency did not improve")
        self.assertAlmostEqual(spend_inefficiency_eval["adjusted_confidence"], 0.55 + 0.10)

        # Check audience saturation (lowest_ctr_campaigns is not empty)
        audience_saturation_eval = next(h for h in evaluated["evaluated_hypotheses"] if h["hypothesis"] == "Audience saturation in low-CTR campaigns")
        self.assertAlmostEqual(audience_saturation_eval["adjusted_confidence"], 0.60 + 0.10)

        # Check stable performance (ROAS dropped by -20%, which is > 5% variation)
        stable_performance_eval = next(h for h in evaluated["evaluated_hypotheses"] if h["hypothesis"] == "Stable performance")
        self.assertAlmostEqual(stable_performance_eval["adjusted_confidence"], 0.40 - 0.10)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
