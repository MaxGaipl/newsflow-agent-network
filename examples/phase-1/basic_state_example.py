"""Phase 1 Example: Basic State Management and Linear Workflow

This example demonstrates:
- Basic TypedDict state management
- Simple nodes with state updates
- Linear workflow construction
- Basic logging and debugging

Run this example to understand the fundamentals before moving to complex patterns.
"""

from typing import Dict, Any, List
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasicNewsState(TypedDict):
    """Simple state for basic news processing."""
    current_step: str
    articles: List[Dict[str, Any]]
    processed_count: int
    results: List[str]


def load_news(state: BasicNewsState) -> Dict[str, Any]:
    """Load mock news data - Step 1."""
    logger.info("Step 1: Loading news data...")
    
    # Mock news data (replace with actual file loading)
    mock_articles = [
        {
            "id": "1",
            "title": "AI Breakthrough Announced",
            "content": "Scientists have made a significant breakthrough..."
        },
        {
            "id": "2", 
            "title": "Climate Summit Results",
            "content": "World leaders agreed on new climate targets..."
        }
    ]
    
    return {
        "current_step": "data_loaded",
        "articles": mock_articles,
        "processed_count": 0
    }


def process_articles(state: BasicNewsState) -> Dict[str, Any]:
    """Process loaded articles - Step 2."""
    logger.info(f"Step 2: Processing {len(state['articles'])} articles...")
    
    results = []
    for article in state['articles']:
        # Simple processing: extract title and word count
        word_count = len(article['content'].split())
        result = f"Article '{article['title']}' has {word_count} words"
        results.append(result)
        logger.info(f"Processed: {article['title']}")
    
    return {
        "current_step": "articles_processed",
        "processed_count": len(state['articles']),
        "results": results
    }


def generate_summary(state: BasicNewsState) -> Dict[str, Any]:
    """Generate final summary - Step 3."""
    logger.info("Step 3: Generating summary...")
    
    summary = f"Processed {state['processed_count']} articles successfully"
    logger.info(f"Summary: {summary}")
    
    return {
        "current_step": "completed",
        "results": state['results'] + [summary]
    }


def create_basic_workflow() -> StateGraph:
    """Create the basic news processing workflow."""
    
    # Create the workflow
    workflow = StateGraph(BasicNewsState)
    
    # Add nodes
    workflow.add_node("load_news", load_news)
    workflow.add_node("process_articles", process_articles)
    workflow.add_node("generate_summary", generate_summary)
    
    # Add edges (linear flow)
    workflow.add_edge(START, "load_news")
    workflow.add_edge("load_news", "process_articles")
    workflow.add_edge("process_articles", "generate_summary")
    workflow.add_edge("generate_summary", END)
    
    return workflow


def main():
    """Run the basic workflow example."""
    print("🚀 Running Phase 1 Example: Basic State Management")
    print("=" * 50)
    
    # Create and compile workflow
    workflow = create_basic_workflow()
    graph = workflow.compile()
    
    # Initial state
    initial_state = {
        "current_step": "starting",
        "articles": [],
        "processed_count": 0,
        "results": []
    }
    
    # Run the workflow
    try:
        result = graph.invoke(initial_state)
        
        print("\n✅ Workflow completed successfully!")
        print(f"Final step: {result['current_step']}")
        print(f"Articles processed: {result['processed_count']}")
        print("\nResults:")
        for i, result_item in enumerate(result['results'], 1):
            print(f"  {i}. {result_item}")
            
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        logger.error(f"Workflow error: {e}")


if __name__ == "__main__":
    main()
