# from google.adk.agents.llm_agent import Agent

# root_agent = Agent(
#     model='gemini-3.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )
from datetime import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

# TOOL: a plain Python function
def get_current_time(city: str) -> dict:
    """Returns the current time in a city.

    Args:
        city: Name of the city, e.g. "Chennai" or "London".
    """
    zones = {
        "chennai": "Asia/Kolkata",
        "london": "Europe/London",
        "new york": "America/New_York",
        "tokyo": "Asia/Tokyo",
    }
    tz_name = zones.get(city.lower())
    if not tz_name:
        return {"status": "error", "message": f"I don't know the timezone for {city}."}
    now = datetime.now(ZoneInfo(tz_name))
    return {"status": "success", "city": city, "time": now.strftime("%I:%M %p, %d %b %Y")}

# AGENT: must be named root_agent
root_agent = Agent(
    name="time_agent",
    model='gemini-3.5-flash',   # use the model the CLI suggested if it differs
    description="Tells the current time in different cities.",
    instruction=(
        "You are a friendly assistant. When the user asks about time in a city, "
        "use the get_current_time tool. Otherwise, answer normally."
    ),
    tools=[get_current_time],
)