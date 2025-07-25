# Phase 1 Examples

This directory contains practical examples for Phase 1 concepts. Work through these examples to build your understanding before tackling the issues.

## Examples

### 1. Basic State Management (`basic_state_example.py`)
**Concepts**: TypedDict, simple nodes, linear workflows

```bash
python basic_state_example.py
```

This example shows:
- How to define state with TypedDict
- Creating simple nodes that update state
- Building linear workflows
- Basic logging and debugging

### 2. Checkpointing and Memory (`checkpointing_example.py`)
**Concepts**: MemorySaver, thread persistence, state inspection

```bash
python checkpointing_example.py
```

Run this multiple times to see:
- State persistence across sessions
- Thread-based memory management
- State history and debugging
- Manual state updates

## Learning Path

1. **Start with `basic_state_example.py`** to understand fundamentals
2. **Experiment with the code** - modify nodes, add logging, change state structure
3. **Move to `checkpointing_example.py`** to see persistence in action
4. **Try the exercises below** to test your understanding

## Exercises

After running the examples, try these modifications:

### Basic State Exercise
- Add a new node that counts words across all articles
- Implement error handling for missing article data
- Add validation that ensures articles have required fields

### Checkpointing Exercise
- Create different thread IDs to manage multiple sessions
- Implement a function that cleans up old checkpoints
- Add metadata tracking to see performance across runs

### Challenge Exercise
- Combine both examples into a single workflow
- Add conditional logic that skips processing for already-seen articles
- Implement a resume mechanism that can continue from any checkpoint

## Troubleshooting

**Import Errors**: Make sure you've installed requirements: `pip install -r requirements.txt`

**No Output**: Check that logging is enabled and review the console output

**State Not Persisting**: Ensure you're using the same thread ID across runs

## Next Steps

Once you understand these examples:
1. Work on Issue #1 (Environment Setup)
2. Implement your own variations
3. Move to Issue #2 (Checkpointing) when ready
4. Document what you learned in `docs/learning-notes/`
