import pandas as pd
import json
from datetime import timedelta

def build_data_summary(df):
    summary = {}

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        dr = df["date"].dropna()

        summary["date_min"] = str(dr.min().date()) if not dr.empty else None
        summary["date_max"] = str(dr.max().date()) if not dr.empty else None

        if not dr.empty:
            max_date = dr.max()
            last14 = df[df["date"] >= (max_date - timedelta(days=14))]
            last7 = df[df["date"] >= (max_date - timedelta(days=7))]
            summary["rows_last_14"] = len(last14)
            summary["rows_last_7"] = len(last7)
    else:
        last14 = df
        last7 = df

    def metrics(subdf):
        return {
            "total_spend": float(subdf["spend"].sum()) if "spend" in subdf else None,
            "impressions": int(subdf["impressions"].sum()) if "impressions" in subdf else None,
            "clicks": int(subdf["clicks"].sum()) if "clicks" in subdf else None,
            "ctr_mean": float(subdf["ctr"].mean()) if "ctr" in subdf else None,
            "purchases": int(subdf["purchases"].sum()) if "purchases" in subdf else None,
            "revenue": float(subdf["revenue"].sum()) if "revenue" in subdf else None,
            "roas_mean": float(subdf["roas"].mean()) if "roas" in subdf else None
        }

    summary["overall"] = metrics(df)
    summary["last_14"] = metrics(last14)
    summary["last_7"] = metrics(last7)

    if "campaign_name" in df.columns:
        grp = df.groupby("campaign_name").agg({
            "spend": "sum",
            "impressions": "sum",
            "clicks": "sum",
            "purchases": "sum",
            "revenue": "sum"
        }).reset_index()

        grp["ctr"] = grp["clicks"] / grp["impressions"]
        grp["roas"] = grp["revenue"] / grp["spend"].replace({0: pd.NA})

        summary["top_campaigns_by_spend"] = grp.sort_values("spend", ascending=False)\
            .head(5)[["campaign_name", "spend", "roas", "ctr"]].to_dict(orient="records")

        summary["lowest_ctr_campaigns"] = grp.sort_values("ctr", ascending=True)\
            .head(5)[["campaign_name", "ctr"]].to_dict(orient="records")

        sample_creatives_list = []
        for low_ctr_campaign_info in summary["lowest_ctr_campaigns"]:
            campaign_name = low_ctr_campaign_info["campaign_name"]
            if "creative_message" in df.columns:
                creative_messages_for_campaign = df[df["campaign_name"] == campaign_name]["creative_message"]
                if not creative_messages_for_campaign.empty:
                    creative_message = creative_messages_for_campaign.iloc[0]
                else:
                    creative_message = ""
            else:
                creative_message = ""

            sample_creatives_list.append({
                "campaign_name": campaign_name,
                "creative_message": creative_message
            })
        summary["sample_creatives_low_ctr"] = sample_creatives_list

    return summary

if __name__ == "__main__":
    # This part would typically be called by an orchestrator
    # For standalone testing, you'd need to load a DataFrame first
    print("Data Agent: Summary generation functionality is ready.")
