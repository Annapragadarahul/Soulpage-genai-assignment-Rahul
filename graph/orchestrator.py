from typing import TypedDict, List
from langgraph.graph import StateGraph
from agents.review_collector import review_collector_agent
from agents.review_analyst import review_analyst_agent
from agents.movie_knowledge_agent import movie_knowledge_agent


class MovieState(TypedDict):
    movie: str
    reviews: List[str]
    analysis: str
    metadata: dict


def collector_node(state: MovieState):
    result = review_collector_agent(state["movie"])
    state["movie"] = result["movie"]
    state["reviews"] = result["reviews"]
    return state


def analyst_node(state: MovieState):
    result = review_analyst_agent(state)
    state["analysis"] = result["analysis"]
    return state


def knowledge_node(state: MovieState):
    state["metadata"] = movie_knowledge_agent(state["movie"])
    return state


workflow = StateGraph(MovieState)

workflow.add_node("collector", collector_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("knowledge", knowledge_node)

workflow.set_entry_point("collector")
workflow.add_edge("collector", "analyst")
workflow.add_edge("analyst", "knowledge")

app = workflow.compile()


def run_movie_review_analyzer(movie_name: str):
    return app.invoke({
        "movie": movie_name,
        "reviews": [],
        "analysis": "",
        "metadata": {}
    })
