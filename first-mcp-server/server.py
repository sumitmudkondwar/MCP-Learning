
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("First MCP Server")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def get_cloud_status(service: str) -> str:
    """Return simulated cloud service status."""
    return f"{service}: HEALTHY (simulated demo data)"


if __name__ == "__main__":
    mcp.run()
