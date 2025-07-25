# Getting Started with NewsFlow Agent Network

Welcome to your LangGraph learning journey! This guide will get you up and running quickly.

## 🚀 Quick Start

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/MaxGaipl/newsflow-agent-network.git
cd newsflow-agent-network

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
# At minimum, you'll need an OpenAI or Anthropic API key
```

### 3. Test Your Setup
```bash
# Run the basic example
cd examples/phase-1
python basic_state_example.py
```

If you see output showing articles being processed, you're ready to go! 🎉

## 📚 Learning Path

The project is designed as a progressive learning experience:

### Phase 1: Foundation (Start Here!)
- **Issue #1**: Environment Setup and Basic State Management
- **Issue #2**: Checkpointing and Memory Persistence  
- **Issue #3**: Mock News Data Processing Pipeline
- **Issue #4**: Conditional Routing and Dynamic Workflows

### Phase 2: Agent Basics
- **Issue #5**: Tool Integration and Agent Patterns
- **Issue #6**: Agent Memory and Context Management
- More issues will be added as you progress!

### Phase 3 & 4: Coming Soon
- Multi-agent systems
- Knowledge graphs
- Advanced features

## 🛠️ Development Workflow

### Working on Issues
1. **Pick an issue** from the [Issues page](https://github.com/MaxGaipl/newsflow-agent-network/issues)
2. **Create a feature branch**: `git checkout -b feature/issue-1-setup`
3. **Work on the implementation** following the issue guidance
4. **Test your code** thoroughly
5. **Create a pull request** to merge into `main`

### Branch Strategy
- `main`: Stable, production-ready code
- `dev`: Development branch (you're currently here!)
- `feature/*`: Feature branches for specific issues

### Example Workflow
```bash
# Start working on Issue #1
git checkout dev
git pull origin dev
git checkout -b feature/issue-1-setup

# Do your work...
git add .
git commit -m "Implement basic state management for Issue #1"
git push origin feature/issue-1-setup

# Create PR on GitHub: feature/issue-1-setup -> main
```

## 📁 Project Structure

```
newsflow-agent-network/
├── src/newsflow/           # Main package
│   ├── agents/             # Agent implementations  
│   ├── graphs/             # LangGraph workflows
│   ├── state/              # State management
│   ├── tools/              # Custom tools
│   └── utils/              # Helper functions
├── examples/               # Learning examples
│   ├── phase-1/            # Foundation examples
│   ├── phase-2/            # Agent examples (coming)
│   └── ...
├── data/
│   ├── mock/               # Mock data for learning
│   └── checkpoints/        # Saved states
├── docs/
│   ├── learning-notes/     # Your learning journey
│   └── architecture/       # System design
└── tests/                  # Test suite
```

## 🔧 Available Commands

### Running Examples
```bash
# Basic state management
python examples/phase-1/basic_state_example.py

# Checkpointing demo
python examples/phase-1/checkpointing_example.py
```

### Testing
```bash
# Run tests (when available)
pytest src/tests/

# Type checking
mypy src/

# Code formatting
black src/
```

## 🎯 Your First Session

Recommended first session (1-2 hours):

1. **Setup** (30 min)
   - Clone repo and setup environment
   - Run basic examples
   - Explore the codebase

2. **Learn** (30 min)
   - Read through the basic example code
   - Understand the state structure
   - Try modifying simple things

3. **Start Issue #1** (30 min)
   - Read the issue description carefully
   - Start implementing your own basic workflow
   - Ask questions in the issue comments

## 🆘 Getting Help

- **Issues**: Use GitHub issues for questions and discussion
- **Documentation**: Check `docs/` for additional resources
- **Examples**: Study `examples/` for patterns and inspiration
- **Code Comments**: The codebase is well-commented for learning

## 🎉 Ready to Start!

You're all set! Head over to [Issue #1](https://github.com/MaxGaipl/newsflow-agent-network/issues/1) to begin your LangGraph learning journey.

Remember: This is a learning project, so take your time, experiment, and don't be afraid to break things. That's how we learn! 🚀
