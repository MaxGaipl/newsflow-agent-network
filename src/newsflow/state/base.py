"""Base state definitions for NewsFlow agents."""

from typing import List, Optional, Dict, Any
from typing_extensions import TypedDict, NotRequired
from datetime import datetime


class NewsFlowState(TypedDict):
    """Base state for NewsFlow agent network.
    
    This will evolve throughout the learning phases:
    - Phase 1: Basic fields
    - Phase 2: Tool integration fields
    - Phase 3: Multi-agent coordination fields
    - Phase 4: Knowledge graph fields
    """
    # Core fields (Phase 1)
    messages: NotRequired[List[Dict[str, Any]]]
    current_step: NotRequired[str]
    session_id: NotRequired[str]
    timestamp: NotRequired[datetime]
    
    # News processing fields (Phase 1)
    raw_news_data: NotRequired[List[Dict[str, Any]]]
    processed_topics: NotRequired[List[str]]
    
    # Tool integration fields (Phase 2)
    search_results: NotRequired[List[Dict[str, Any]]]
    fact_check_results: NotRequired[Dict[str, Any]]
    
    # Multi-agent fields (Phase 3)
    active_agents: NotRequired[List[str]]
    agent_outputs: NotRequired[Dict[str, Any]]
    
    # Knowledge graph fields (Phase 4)
    knowledge_graph: NotRequired[Dict[str, Any]]
    entity_relationships: NotRequired[List[Dict[str, Any]]]
