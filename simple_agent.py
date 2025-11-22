"""
Simple Agent Example - No API Key Required

This is a basic demonstration of agent-like behavior without requiring
external API keys. It shows the concept of an agent making decisions
and using tools.
"""


class SimpleTool:
    """A simple tool that the agent can use."""
    
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, input_data):
        """Execute the tool."""
        return self.func(input_data)


class SimpleAgent:
    """A simple agent that can use tools to answer questions."""
    
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}
    
    def decide_tool(self, query):
        """Decide which tool to use based on the query."""
        query_lower = query.lower()
        
        # Simple keyword-based decision making
        # Check for time/date first as it's most specific
        if any(word in query_lower for word in ["time", "date", "when"]):
            return "DateTime"
        # Check for calculation keywords or operators
        elif any(word in query_lower for word in ["calculate", "math"]) or any(op in query for op in ["+", "-", "*", "/"]):
            return "Calculator"
        # Default to search for informational queries
        elif any(word in query_lower for word in ["search", "what", "who", "define", "is"]):
            return "Search"
        else:
            return None
    
    def run(self, query):
        """Run the agent with a query."""
        print(f"\nQuery: {query}")
        print("-" * 50)
        
        # Step 1: Decide which tool to use
        tool_name = self.decide_tool(query)
        
        if not tool_name:
            return "I'm not sure how to help with that query."
        
        print(f"Agent Thought: I should use the {tool_name} tool")
        
        # Step 2: Use the selected tool
        tool = self.tools.get(tool_name)
        if tool:
            print(f"Agent Action: Using {tool_name}")
            result = tool.run(query)
            print(f"Agent Observation: {result}")
            return result
        else:
            return f"Tool {tool_name} not found."


# Tool functions
def calculator_tool(input_str):
    """Simple calculator tool."""
    # Extract numbers and operators from the string
    import re
    
    # Try to find a complete mathematical expression
    # Remove everything that's not a number, operator, parenthesis, or dot
    expr = re.sub(r'[^0-9+\-*/().\s]', '', input_str)
    expr = expr.strip()
    
    if expr and any(c.isdigit() for c in expr):
        try:
            result = eval(expr, {"__builtins__": {}}, {})
            return f"The result is: {result}"
        except Exception as e:
            # If full expression fails, try simple two-number operation
            match = re.search(r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)', input_str)
            if match:
                try:
                    num1, operator, num2 = match.groups()
                    simple_expr = f"{num1}{operator}{num2}"
                    result = eval(simple_expr, {"__builtins__": {}}, {})
                    return f"The result is: {result}"
                except Exception:
                    return f"Error in calculation: {str(e)}"
            return f"Error in calculation: {str(e)}"
    
    return "No valid mathematical expression found."


def search_tool(query):
    """Mock search tool with predefined knowledge."""
    knowledge_base = {
        "langchain": "LangChain is a framework for developing applications powered by language models. It provides tools for creating chains, agents, and more.",
        "agent": "An agent is an autonomous system that uses a language model to decide which actions to take and in what order.",
        "ai": "Artificial Intelligence (AI) refers to computer systems that can perform tasks that typically require human intelligence.",
        "python": "Python is a high-level programming language known for its simplicity and readability.",
        "agentic ai": "Agentic AI refers to AI systems that can act autonomously, make decisions, and take actions to achieve goals.",
    }
    
    query_lower = query.lower()
    
    for key, value in knowledge_base.items():
        if key in query_lower:
            return value
    
    return "I don't have information about that topic in my knowledge base."


def datetime_tool(query):
    """Get current date and time."""
    from datetime import datetime
    now = datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"


def main():
    """Main function to demonstrate the simple agent."""
    print("=" * 50)
    print("Simple AgenticAI Challenge Demo")
    print("=" * 50)
    print("\nThis is a simplified agent that demonstrates:")
    print("1. Decision making (choosing which tool to use)")
    print("2. Tool usage (calculator, search, datetime)")
    print("3. Reasoning process (showing thought process)")
    
    # Create tools
    tools = [
        SimpleTool(
            name="Calculator",
            description="Performs mathematical calculations",
            func=calculator_tool
        ),
        SimpleTool(
            name="Search",
            description="Searches the knowledge base",
            func=search_tool
        ),
        SimpleTool(
            name="DateTime",
            description="Gets current date and time",
            func=datetime_tool
        )
    ]
    
    # Create agent
    agent = SimpleAgent(tools)
    
    # Example queries
    queries = [
        "What is 25 * 4?",
        "What is LangChain?",
        "What time is it?",
        "Define agentic AI",
        "Calculate 100 + 50 - 25"
    ]
    
    print("\n" + "=" * 50)
    print("Running Example Queries")
    print("=" * 50)
    
    for query in queries:
        result = agent.run(query)
        print(f"Final Answer: {result}\n")
    
    # Interactive mode
    print("\n" + "=" * 50)
    print("Interactive Mode (type 'quit' to exit)")
    print("=" * 50)
    
    while True:
        try:
            user_query = input("\nYour question: ").strip()
            if user_query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            if user_query:
                result = agent.run(user_query)
                print(f"Final Answer: {result}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
