import json

def review_collector_agent(movie_name: str):
    """
    Agent 1: Fetches movie reviews (case-insensitive)
    """

    with open("data/reviews.json", "r") as file:
        data = json.load(file)

    normalized = movie_name.strip().lower()

    for key in data:
        if key.lower() == normalized:
            return {
                "movie": key,
                "reviews": data[key]
            }

    return {
        "movie": movie_name,
        "reviews": []
    }
