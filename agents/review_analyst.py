def review_analyst_agent(state: dict):
    """
    Agent 2: Multi-language review analyzer + rating generator
    """

    reviews = state.get("reviews", [])

    # Neutral fallback for unknown movies
    if not reviews:
        return {
            "analysis": """
Overall Sentiment: Neutral

Rating: ⭐⭐⭐ (3.0 / 5)

Explanation:
No structured reviews were available for this movie.
A neutral rating is assigned based on general audience expectation.
"""
        }

    # Language-agnostic sentiment cues
    positive_keywords = [
        "amazing", "great", "excellent", "brilliant", "good",
        "awesome", "superb", "fantastic", "outstanding",
        "blockbuster", "hit", "must watch",
        "अच्छा", "शानदार", "बेहतरीन",
        "అద్భుతం", "చాలా బాగుంది",
        "சிறந்த", "அருமை"
    ]

    negative_keywords = [
        "bad", "boring", "slow", "confusing", "poor",
        "worst", "disappointing", "waste",
        "खराब", "बोरिंग",
        "బోరింగ్", "చెత్త",
        "மோசம்"
    ]

    pos, neg = 0, 0
    positives, negatives = [], []

    for review in reviews:
        text = review.lower()
        if any(word in text for word in positive_keywords):
            pos += 1
            positives.append(review)
        if any(word in text for word in negative_keywords):
            neg += 1
            negatives.append(review)

    # Rating calculation
    total = max(len(reviews), 1)
    score = (pos - neg) / total

    if score >= 0.6:
        rating = 5.0
        sentiment = "Very Positive"
    elif score >= 0.3:
        rating = 4.0
        sentiment = "Positive"
    elif score >= 0:
        rating = 3.0
        sentiment = "Mixed"
    elif score >= -0.3:
        rating = 2.5
        sentiment = "Negative"
    else:
        rating = 2.0
        sentiment = "Very Negative"

    stars = "⭐" * int(round(rating))

    analysis = f"""
Overall Sentiment: {sentiment}

Rating: {stars} ({rating} / 5)

Key Positive Points:
""" + "\n".join(f"- {p}" for p in positives) + """

Key Negative Points:
""" + "\n".join(f"- {n}" for n in negatives) + """

Final Verdict:
Based on multilingual review signals, the movie received a {rating}/5 rating.
"""

    return {
        "analysis": analysis
    }
