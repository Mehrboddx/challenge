# AgenticAI Challenge with LangChain

Welcome to the AgenticAI Challenge! This repository contains examples and demonstrations of building agentic AI systems using LangChain.

## 🎯 What is Agentic AI?

Agentic AI refers to AI systems that can:
- Make autonomous decisions
- Use tools and resources to accomplish tasks
- Reason through complex problems
- Take actions to achieve specific goals

## 📋 Features

This repository includes:

1. **Simple Agent** (`simple_agent.py`) - A basic agent implementation that doesn't require API keys
   - Decision-making capabilities
   - Tool selection and usage
   - Knowledge base search
   - Calculator functionality
   - Interactive mode

2. **LangChain Agent** (`agent.py`) - A more advanced agent using LangChain framework
   - Integration with OpenAI's GPT models
   - ReAct (Reasoning + Acting) pattern
   - Multiple tool usage
   - Error handling

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mehrboddx/challenge.git
cd challenge
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start - Simple Agent (No API Key Required)

Run the simple agent to see agentic behavior without needing any API keys:

```bash
python simple_agent.py
```

This will:
- Run example queries demonstrating the agent's capabilities
- Enter interactive mode where you can ask your own questions

Example queries you can try:
- "What is 25 * 4?"
- "What is LangChain?"
- "What time is it?"
- "Define agentic AI"

### Advanced - LangChain Agent (Requires OpenAI API Key)

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your-actual-api-key-here
```

3. Run the LangChain agent:
```bash
python agent.py
```

## 🛠️ How It Works

### Simple Agent Architecture

```
User Query → Agent (Decision Making) → Tool Selection → Tool Execution → Result
```

The simple agent:
1. Receives a user query
2. Analyzes keywords to decide which tool to use
3. Executes the appropriate tool
4. Returns the result

### LangChain Agent Architecture

```
User Query → LLM (Reasoning) → Tool Selection → Tool Execution → LLM (Synthesis) → Result
```

The LangChain agent:
1. Uses a language model to understand the query
2. Reasons about which tools to use (ReAct pattern)
3. Executes tools in sequence if needed
4. Synthesizes the final answer

## 📚 Project Structure

```
challenge/
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── requirements.txt     # Python dependencies
├── simple_agent.py      # Simple agent (no API key needed)
└── agent.py            # LangChain agent (requires API key)
```

## 🔧 Available Tools

### Simple Agent Tools:
- **Calculator**: Performs mathematical calculations
- **Search**: Searches a predefined knowledge base
- **DateTime**: Returns current date and time

### LangChain Agent Tools:
- **Calculator**: Advanced mathematical operations
- **Search**: Information retrieval about AI and LangChain concepts

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)
- [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629)

## 🤝 Contributing

This is a challenge repository for learning agentic AI. Feel free to:
- Add new tools
- Improve agent reasoning
- Add more examples
- Enhance documentation

## 📝 License

This project is open source and available for educational purposes.

## 🎯 Challenge Ideas

Try extending this project with:

1. **New Tools**: Add tools for weather, news, file operations, etc.
2. **Memory**: Implement conversation memory for context-aware responses
3. **Multi-Agent Systems**: Create multiple agents that collaborate
4. **Custom Chains**: Build specialized chains for specific tasks
5. **Evaluation**: Add metrics to measure agent performance

## 💡 Tips

- Start with `simple_agent.py` to understand basic agent concepts
- Use verbose mode in LangChain to see the agent's reasoning process
- Experiment with different prompts and tools
- Monitor token usage when using API-based agents

## 🐛 Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution**: Make sure you've created a `.env` file and added your API key.

### Issue: Import errors
**Solution**: Make sure you've installed dependencies: `pip install -r requirements.txt`

### Issue: Simple agent not working
**Solution**: The simple agent requires no dependencies except Python's standard library. Check Python version (3.8+).

## 📞 Support

For questions or issues, please open an issue in the GitHub repository.

---

Happy coding! 🚀 Explore the world of agentic AI!