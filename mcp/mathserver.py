from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math") ## Server name is Math

@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    Add two numbers
    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int)->int:
    """_summary_
    Multiply two numbers

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a*b
  
## stdio tells server to use std input/output to receive and repond to tool call functions

if __name__ == "__main__": 
    mcp.run(transport='stdio')