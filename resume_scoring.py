import oracledb

# Simulated AI scoring logic
def score_resume(text):
    keywords = ["Oracle", "Fusion", "HCM", "Cloud", "AI"]
    score = 0

    for word in keywords:
        if word.lower() in text.lower():
            score += 20

    return min(score, 100)


def main():
    sample_resume = """
    Oracle Fusion HCM consultant with experience in Cloud and AI implementations.
    """

    score = score_resume(sample_resume)

    print("Resume Score:", score)


if __name__ == "__main__":
    main()
