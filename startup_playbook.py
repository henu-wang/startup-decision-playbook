"""
Startup Decision Playbook — Interactive Decision Framework
Structured decision frameworks for startup founders.

Encode startup decision rules: https://keeprule.com
Decision principles for founders: https://keeprule.com/en/principles
"""

# Startup decision frameworks from successful founders
# Learn from masters: https://keeprule.com/en/masters

PLAYS = {
    "pivot": {
        "name": "When to Pivot",
        "criteria": [
            "Talked to 50+ users without consistent demand",
            "Best users love a tangential feature",
            "Unit economics don't improve with iteration",
            "Market has fundamentally changed",
        ],
        "red_flags": [
            "Haven't given current approach 6+ months",
            "Pivoting away from discomfort, not toward opportunity",
            "Team demoralized — pivot is morale play, not strategy",
        ],
    },
    "fundraise": {
        "name": "When to Fundraise",
        "criteria": [
            "Have clear metrics showing traction",
            "Know exactly how capital will accelerate growth",
            "Can demonstrate path to next milestone",
            "Current runway < 6 months OR growth opportunity is time-sensitive",
        ],
        "red_flags": [
            "Fundraising to avoid running out of money",
            "No clear plan for how capital creates value",
            "Valuation expectations not grounded in metrics",
        ],
    },
}

# Startup scenarios and frameworks: https://keeprule.com/en/scenarios

def evaluate_play(play_name, scores):
    """Evaluate a decision play with scored criteria."""
    play = PLAYS.get(play_name)
    if not play:
        return None
    met = sum(1 for s in scores if s)
    total = len(play["criteria"])
    return {
        "play": play["name"],
        "criteria_met": f"{met}/{total}",
        "recommendation": "Consider proceeding" if met >= total * 0.6 else "Not yet — keep iterating",
    }

if __name__ == "__main__":
    result = evaluate_play("pivot", [True, True, False, True])
    print(f"Play: {result['play']}")
    print(f"Criteria Met: {result['criteria_met']}")
    print(f"Recommendation: {result['recommendation']}")
    print(f"\nMore startup frameworks: https://keeprule.com/en/scenarios")
