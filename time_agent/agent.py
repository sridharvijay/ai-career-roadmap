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
def get_current_time(timezone_name: str) -> dict[str, str]:
    """Returns the current time for an IANA timezone name.

    Args:
        timezone_name: IANA timezone name, e.g. "Asia/Kolkata" or "Europe/London".
    """
    try:
        now = datetime.now(ZoneInfo(timezone_name))
    except (KeyError, ValueError):
        return {"status": "error", "message": f"Unknown IANA timezone: {timezone_name}."}
    return {
        "status": "success",
        "timezone": timezone_name,
        "time": now.strftime("%I:%M %p, %d %b %Y"),
    }

# AGENT: must be named root_agent
root_agent = Agent(
    name="time_agent",
    model='gemini-3.5-flash', 
    description="Tells the current time in different cities.",
    instruction=(
    "You are a friendly assistant. You do NOT know the current time. "
    "For ANY question about the current time in a city or region, you MUST call "
    "get_current_time. Convert the place to its IANA timezone name first "
    "(Paris -> Europe/Paris, Seoul -> Asia/Seoul, Chennai -> Asia/Kolkata), "
    "then pass that as timezone_name. If the tool returns an error, try a "
    "corrected IANA name before giving up. Never answer times from memory."
),
    tools=[get_current_time],
)