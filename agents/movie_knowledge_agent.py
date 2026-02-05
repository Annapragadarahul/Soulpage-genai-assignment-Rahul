import json

def movie_knowledge_agent(movie_name: str):
    """
    Agent 3: Provides movie summary, genre, cast, release date
    """

    with open("data/movie_metadata.json", "r") as f:
        metadata = json.load(f)

    for key in metadata:
        if key.lower() == movie_name.lower():
            return metadata[key]

    # Fallback for unknown movies
    return {
        "summary": "Detailed information is not available for this movie.",
        "genres": ["Unknown"],
        "cast": ["Information not available"],
        "release_date": "Unknown"
    }
