"""
Tests for the simple agent implementation.

These tests verify that the agent can correctly:
1. Decide which tool to use
2. Execute tools properly
3. Return expected results
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simple_agent import SimpleAgent, SimpleTool, calculator_tool, search_tool, datetime_tool


def test_calculator_tool():
    """Test the calculator tool."""
    print("Testing calculator tool...")
    
    # Test basic arithmetic
    assert "100" in calculator_tool("What is 25 * 4?")
    assert "125" in calculator_tool("Calculate 100 + 50 - 25")
    assert "10" in calculator_tool("5 + 5")
    
    print("✓ Calculator tool tests passed")


def test_search_tool():
    """Test the search tool."""
    print("Testing search tool...")
    
    # Test knowledge base queries
    result = search_tool("What is LangChain?")
    assert "LangChain" in result and "framework" in result
    
    result = search_tool("What is an agent?")
    assert "agent" in result.lower()
    
    result = search_tool("unknown topic")
    assert "don't have information" in result
    
    print("✓ Search tool tests passed")


def test_datetime_tool():
    """Test the datetime tool."""
    print("Testing datetime tool...")
    
    result = datetime_tool("What time is it?")
    assert "Current date and time:" in result
    assert "2025" in result  # Current year
    
    print("✓ DateTime tool tests passed")


def test_agent_decision_making():
    """Test that the agent makes correct tool choices."""
    print("Testing agent decision making...")
    
    tools = [
        SimpleTool(name="Calculator", description="Math", func=calculator_tool),
        SimpleTool(name="Search", description="Search", func=search_tool),
        SimpleTool(name="DateTime", description="Time", func=datetime_tool)
    ]
    
    agent = SimpleAgent(tools)
    
    # Test calculator decision
    assert agent.decide_tool("What is 5 + 5?") == "Calculator"
    assert agent.decide_tool("Calculate 10 * 2") == "Calculator"
    
    # Test search decision
    assert agent.decide_tool("What is LangChain?") == "Search"
    assert agent.decide_tool("Define AI") == "Search"
    
    # Test datetime decision
    assert agent.decide_tool("What time is it?") == "DateTime"
    assert agent.decide_tool("What is the date?") == "DateTime"
    
    print("✓ Agent decision making tests passed")


def test_agent_execution():
    """Test full agent execution."""
    print("Testing agent execution...")
    
    tools = [
        SimpleTool(name="Calculator", description="Math", func=calculator_tool),
        SimpleTool(name="Search", description="Search", func=search_tool),
        SimpleTool(name="DateTime", description="Time", func=datetime_tool)
    ]
    
    agent = SimpleAgent(tools)
    
    # Test calculation
    result = agent.run("What is 10 + 5?")
    assert "15" in result
    
    # Test search
    result = agent.run("What is LangChain?")
    assert "framework" in result
    
    print("✓ Agent execution tests passed")


def main():
    """Run all tests."""
    print("=" * 50)
    print("Running Simple Agent Tests")
    print("=" * 50)
    print()
    
    try:
        test_calculator_tool()
        test_search_tool()
        test_datetime_tool()
        test_agent_decision_making()
        test_agent_execution()
        
        print()
        print("=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
        return 0
    
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
