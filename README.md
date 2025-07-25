# NewsFlow Agent Network 🤖📰

> A progressive LangGraph learning project: Build a multi-agent news research system from basic concepts to advanced state graphs

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-latest-green.svg)](https://langchain-ai.github.io/langgraph/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-orange.svg)](https://langchain.com/)

## 🎯 Project Overview

NewsFlow Agent Network is a **progressive learning project** designed to master LangGraph and LangChain concepts by building a sophisticated multi-agent news research system. Starting from basic state management and building up to complex agent orchestration, this project serves as both a learning journey and a practical tool.

## 🚀 What You'll Build

A multi-agent system that:
- **Monitors** news sources and extracts key topics
- **Researches** topics using intelligent web search
- **Fact-checks** information against reliable sources  
- **Builds** a dynamic knowledge graph of interconnected facts
- **Generates** comprehensive reports and insights
- **Coordinates** multiple specialized agents working in parallel

## 📚 Learning Progression

### Phase 1: Foundation (Weeks 1-2) 🌱
**Core Concepts**: State Management, Basic Nodes, Linear Workflows
- [ ] Basic LangGraph state with TypedDict
- [ ] Simple nodes and sequential edges
- [ ] Checkpointing and memory persistence
- [ ] Mock news data processing

### Phase 2: Agent Basics (Weeks 3-4) 🔧
**Core Concepts**: Tools, Conditional Routing, Agent Patterns
- [ ] Tool integration and agent decision making
- [ ] Conditional edges and dynamic routing
- [ ] Memory management across sessions
- [ ] Error handling and recovery

### Phase 3: Multi-Agent System (Weeks 5-8) 🤝
**Core Concepts**: Parallel Agents, Complex State, Sub-graphs
- [ ] Multiple specialized agents
- [ ] Parallel processing and coordination
- [ ] Sub-graphs and agent handoffs
- [ ] Human-in-the-loop workflows

### Phase 4: Advanced Features (Weeks 9-12) 🚀
**Core Concepts**: Knowledge Graphs, Advanced Persistence, Real-world Integration
- [ ] Dynamic knowledge graph construction
- [ ] Advanced persistence patterns
- [ ] Performance optimization
- [ ] Real-world data integration ready

## 🛠️ Technical Stack

- **Core Framework**: LangGraph + LangChain
- **Language**: Python 3.11+
- **State Management**: TypedDict, Pydantic Models
- **Persistence**: Various checkpointers (Memory, SQLite, Redis)
- **Tools**: Web search, data processing, fact-checking APIs
- **Knowledge Graph**: NetworkX (Phase 4)
- **Testing**: pytest, mock data generators

## 📁 Project Structure

```
newsflow-agent-network/
├── src/
│   ├── newsflow/
│   │   ├── __init__.py
│   │   ├── agents/          # Individual agent implementations
│   │   ├── graphs/          # LangGraph workflows
│   │   ├── state/           # State management
│   │   ├── tools/           # Custom tools and integrations
│   │   └── utils/           # Helper functions
│   ├── tests/
│   └── examples/            # Phase-by-phase examples
├── data/
│   ├── mock/                # Mock news data for learning
│   └── checkpoints/         # Saved agent states
├── docs/
│   ├── learning-notes/      # Your learning journey
│   └── architecture/        # System design docs
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 🎓 Learning Approach

Each phase includes:
- **📖 Conceptual Overview**: Understanding the LangGraph concepts
- **💻 Hands-on Implementation**: Building working code
- **🧪 Testing & Validation**: Ensuring your implementation works
- **📝 Reflection**: Documenting what you learned
- **🔄 Iteration**: Improving and extending your solution

## 🚦 Getting Started

### Prerequisites
- Python 3.11+
- Basic familiarity with LangChain/LangGraph
- Git and GitHub account

### Quick Start
```bash
# Clone the repository
git clone https://github.com/MaxGaipl/newsflow-agent-network.git
cd newsflow-agent-network

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start with Phase 1
cd examples/phase-1
python basic_state_example.py
```

## 📋 Development Workflow

This project follows a structured development approach:
1. **Development Branch**: All work happens in `dev` branch
2. **Pull Requests**: Features are merged via PRs to `main`
3. **Issues**: Each learning milestone has dedicated issues
4. **Milestones**: Track progress through the 4 phases

## 🎯 Current Milestone

**Phase 1: Foundation** - Building the basic state management and workflow patterns.

See [Issues](https://github.com/MaxGaipl/newsflow-agent-network/issues) for current tasks and progress.

## 🤝 Contributing

This is primarily a learning project, but feedback and suggestions are welcome! Feel free to:
- Open issues for questions or improvements
- Share your own learning insights
- Suggest additional features or learning exercises

## 📄 License

MIT License - Feel free to use this project for your own learning journey!

## 🔗 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Project Issues](https://github.com/MaxGaipl/newsflow-agent-network/issues)
- [Learning Notes](./docs/learning-notes/)

---
*Built with ❤️ for learning LangGraph and LangChain*