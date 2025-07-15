from fastmcp import FastMCP
import random

# In-memory weather database
known_weather_data = {}

# Create the MCP server instance
mcp = FastMCP("WeatherAgent 🌤️")

@mcp.tool
def get_weather(city: str) -> float:
    """
    Get the temperature for a given city.

    Parameters:
        city (str): The name of the city to retrieve the temperature for.

    Returns:
        float: The temperature in Celsius. Returns a random value if the city is not found in the known data.
    """
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)

@mcp.tool
def set_weather(city: str, temp: float) -> None:
    """
    Set the temperature for a given city.

    Parameters:
        city (str): The name of the city.
        temp (float): The temperature in Celsius to store for the city.

    Returns:
        None
    """
    city = city.strip().lower()
    known_weather_data[city] = temp

# Entry point to run as a standalone server
if __name__ == "__main__":
    mcp.run()