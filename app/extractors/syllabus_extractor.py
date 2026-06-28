def extract_topics(text: str):
    keywords = [
        "history", "geography", "polity", "economy",
        "environment", "science", "technology",
        "society", "security", "international"
    ]

    topics = []

    sentences = text.split(".")

    for s in sentences:
        s = s.strip().lower()

        if any(k in s for k in keywords):
            topics.append({
                "raw": s,
                "type": "topic"
            })

    return topics