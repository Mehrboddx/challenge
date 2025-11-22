"""
AgenticAI Challenge with LangChain

This module demonstrates a basic LangChain agent implementation
for the agenticAI challenge.
"""

import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain.agents import Tool
from langchain_openai import ChatOpenAI
from langchain import hub

# Load environment variables
load_dotenv()


def calculator(input_str: str) -> str:
    """Simple calculator tool for the agent."""
    try:
        # Only evaluate simple arithmetic expressions
        result = eval(input_str, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


def search_tool(query: str) -> str:
    """Mock search tool that returns pre-defined information."""
    search_results = {
        "langchain": "LangChain is a framework for developing applications powered by language models.",
        "agent": "An agent is a system that uses a language model to decide which actions to take.",
        "ai": "Artificial Intelligence (AI) is the simulation of human intelligence by machines.",
    }
    
    for key, value in search_results.items():
        if key.lower() in query.lower():
            return value
    
    return "No relevant information found for your query."


def create_agent():
    """Create and configure the LangChain agent."""
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found. Please set it in your .env file or environment variables."
        )
    
    # Initialize the language model
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Define tools available to the agent
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for performing mathematical calculations. Input should be a valid mathematical expression."
        ),
        Tool(
            name="Search",
            func=search_tool,
            description="Useful for searching information about LangChain, agents, and AI concepts."
        )
    ]
    
    # Get the ReAct prompt from LangChain hub
    prompt = hub.pull("hwchase17/react")
    
    # Create the agent
    agent = create_react_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5
    )
    
    return agent_executor


def run_agent(query: str):
    """Run the agent with a given query."""
    try:
        agent_executor = create_agent()
        result = agent_executor.invoke({"input": query})
        return result
    except Exception as e:
        return f"Error running agent: {str(e)}"


if __name__ == "__main__":
    print("AgenticAI Challenge with LangChain")
    print("=" * 50)
    
    # Example queries
    examples = [
        "What is 25 * 4 + 10?",
        "What is LangChain?",
        "Calculate 100 / 5 and tell me what an agent is."
    ]
    
    print("\nRunning example queries...\n")
    
    for i, query in enumerate(examples, 1):
        print(f"\nExample {i}: {query}")
        print("-" * 50)
        try:
            result = run_agent(query)
            print(f"Result: {result.get('output', result)}")
        except Exception as e:
            print(f"Error: {str(e)}")
        print()
