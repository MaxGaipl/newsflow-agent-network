"""Phase 1 Example: Checkpointing and Memory Persistence

This example demonstrates:
- MemorySaver checkpointer integration
- Thread-based state persistence
- State inspection and debugging
- Resuming interrupted workflows

Run this multiple times to see how state persists across sessions.
"""

from typing import Dict, Any, List
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
import logging
import uuid

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PersistentNewsState(TypedDict):
    """State with persistence capabilities."""
    session_id: str
    current_step: str
    articles_processed: List[str]
    total_count: int
    session_notes: List[str]


def start_session(state: PersistentNewsState) -> Dict[str, Any]:
    """Initialize or continue a processing session."""
    session_id = state.get('session_id', str(uuid.uuid4())[:8])
    
    logger.info(f"Starting session: {session_id}")
    
    return {
        "session_id": session_id,
        "current_step": "session_started",
        "session_notes": state.get('session_notes', []) + [f"Session {session_id} started"]
    }


def process_batch(state: PersistentNewsState) -> Dict[str, Any]:
    """Process a batch of articles."""
    logger.info(f"Processing batch in session: {state['session_id']}")
    
    # Simulate processing some articles
    new_articles = [f"article_{i}" for i in range(3)]
    current_processed = state.get('articles_processed', [])
    
    return {
        "current_step": "batch_processed",
        "articles_processed": current_processed + new_articles,
        "total_count": len(current_processed) + len(new_articles),
        "session_notes": state['session_notes'] + [f"Processed batch of {len(new_articles)} articles"]
    }


def finalize_session(state: PersistentNewsState) -> Dict[str, Any]:
    """Finalize the processing session."""
    logger.info(f"Finalizing session: {state['session_id']}")
    
    return {
        "current_step": "session_completed",
        "session_notes": state['session_notes'] + [f"Session completed with {state['total_count']} articles"]
    }


def create_persistent_workflow() -> StateGraph:
    """Create workflow with checkpointing."""
    
    workflow = StateGraph(PersistentNewsState)
    
    # Add nodes
    workflow.add_node("start_session", start_session)
    workflow.add_node("process_batch", process_batch)
    workflow.add_node("finalize_session", finalize_session)
    
    # Add edges
    workflow.add_edge(START, "start_session")
    workflow.add_edge("start_session", "process_batch")
    workflow.add_edge("process_batch", "finalize_session")
    workflow.add_edge("finalize_session", END)
    
    return workflow


def demonstrate_checkpointing():
    """Demonstrate checkpointing capabilities."""
    print("🚀 Running Phase 1 Example: Checkpointing and Memory")
    print("=" * 50)
    
    # Create workflow with checkpointer
    workflow = create_persistent_workflow()
    checkpointer = MemorySaver()
    graph = workflow.compile(checkpointer=checkpointer)
    
    # Configuration for thread-based persistence
    thread_id = "news_processing_session_1"
    config = {"configurable": {"thread_id": thread_id}}
    
    print(f"Using thread ID: {thread_id}")
    
    # Check if we have existing state
    try:
        current_state = graph.get_state(config)
        if current_state.values:
            print("📋 Found existing state!")
            print(f"   Current step: {current_state.values.get('current_step', 'unknown')}")
            print(f"   Articles processed: {current_state.values.get('total_count', 0)}")
            
            # Show state history
            print("\n📚 State History:")
            for i, state_snapshot in enumerate(graph.get_state_history(config)):
                print(f"   {i+1}. Step {state_snapshot.metadata.get('step', '?')}: {state_snapshot.values.get('current_step', 'unknown')}")
                if i >= 2:  # Limit history display
                    break
        else:
            print("📋 No existing state found. Starting fresh.")
    except Exception as e:
        print(f"📋 No existing state: {e}")
    
    # Initial state
    initial_state = {
        "session_id": "",
        "current_step": "initializing",
        "articles_processed": [],
        "total_count": 0,
        "session_notes": []
    }
    
    # Run the workflow
    try:
        print("\n🔄 Running workflow...")
        result = graph.invoke(initial_state, config)
        
        print("\n✅ Workflow completed!")
        print(f"Session ID: {result['session_id']}")
        print(f"Final step: {result['current_step']}")
        print(f"Total articles: {result['total_count']}")
        print("\nSession Notes:")
        for note in result['session_notes']:
            print(f"  • {note}")
        
        # Demonstrate state inspection
        print("\n🔍 Final State Inspection:")
        final_state = graph.get_state(config)
        print(f"   Thread ID: {config['configurable']['thread_id']}")
        print(f"   Checkpoint ID: {final_state.config.get('configurable', {}).get('checkpoint_id', 'unknown')}")
        print(f"   Next steps: {final_state.next}")
        
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        logger.error(f"Workflow error: {e}")


def demonstrate_state_updates():
    """Demonstrate manual state updates."""
    print("\n🔧 Demonstrating Manual State Updates")
    print("=" * 40)
    
    workflow = create_persistent_workflow()
    checkpointer = MemorySaver()
    graph = workflow.compile(checkpointer=checkpointer)
    
    thread_id = "state_update_demo"
    config = {"configurable": {"thread_id": thread_id}}
    
    # Create initial state
    initial_state = {
        "session_id": "demo_session",
        "current_step": "manual_update_test",
        "articles_processed": ["article_1"],
        "total_count": 1,
        "session_notes": ["Initial state created"]
    }
    
    # Invoke once to create checkpoint
    graph.invoke(initial_state, config)
    
    # Now update state manually
    print("📝 Updating state manually...")
    new_config = graph.update_state(
        config,
        values={
            "total_count": 5,
            "session_notes": ["State updated manually", "Added 4 more articles"]
        },
        as_node="process_batch"
    )
    
    # Check updated state
    updated_state = graph.get_state(new_config)
    print(f"✅ State updated successfully!")
    print(f"   New total count: {updated_state.values['total_count']}")
    print(f"   Latest notes: {updated_state.values['session_notes'][-1]}")


def main():
    """Run all checkpointing examples."""
    demonstrate_checkpointing()
    demonstrate_state_updates()
    
    print("\n💡 Key Takeaways:")
    print("   • State persists across workflow runs")
    print("   • Thread IDs allow multiple independent sessions")
    print("   • State history enables debugging and time-travel")
    print("   • Manual state updates allow corrections and adjustments")
    print("\n   Try running this script multiple times to see persistence in action!")


if __name__ == "__main__":
    main()
