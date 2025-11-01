#  uv run simple_calculator.py

# uv run fastmcp dev simple_calculator.py

from fastmcp import FastMCP
import random

# Initialize MCP server
mcp = FastMCP("Simple Calculator Server")



# Add tools to your server
@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b



@mcp.tool()
def generate_random_number(min_val: int = 0, max_val: int = 100) -> int:
    """Generate a random number between min and max values."""
    return random.randint(min_val, max_val)



# Add resources
@mcp.resource("server://info")
def get_server_info():
    """Get information about this server."""
    return {
        "name": "Simple Calculator Server",
        "description": "Simple Calculator Server",
        "tools": ["add_numbers", "generate_random_number"],
        "version": "1.0.0",
        "status": "running"
    }



# Key difference for remote server: Use HTTP transport
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)