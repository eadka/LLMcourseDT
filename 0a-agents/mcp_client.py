import asyncio
from fastmcp import Client  # Make sure you have mcp-client installed

async def main():
    async with Client("weather_server01.py") as mcp_client:
        tools = await mcp_client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")

if __name__ == "__main__":
    test = asyncio.run(main())