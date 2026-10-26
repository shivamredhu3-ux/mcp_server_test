
from fastmcp import FastMCP

mcp = FastMCP("SimpleServer")


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
