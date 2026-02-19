import json

# Simulated AI resume scoring logic aligned with OCI AI Foundations concepts

def score_resume(text):
    keywords = {
        "Oracle": 20,
        "Fusion": 20,
        "HCM": 20,
        "Cloud": 20,
        "AI": 20
    }

    score = 0

    for word, weight in keywords.items():
        if word.lower() in text.lower():
            score += weight

    return min(score, 100)


def generate_ai_insight(score):
    if score >= 80:
        return "Strong Oracle ecosystem candidate"
    elif score >= 50:
        return "Moderate alignment with Oracle stack"
    else:
        return "Limited Oracle ecosystem exposure"


def main():
    sample_resume = """
    Oracle Fusion HCM consultant with experience in Cloud and AI implementations.
    """

    score = score_resume(sample_resume)
    insight = generate_ai_insight(score)

    result = {
        "candidate_score": score,
        "ai_insight": insight
    }

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
