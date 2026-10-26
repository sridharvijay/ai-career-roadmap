from datetime import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

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

# SYSTEM PROMPTS: swap the one passed to `instruction` below, then start a NEW session.
PROMPT_TERSE = "Call get_current_time for any question about the current time."

PROMPT_STRICT = (
    "You do NOT know the current time. For ANY time question you MUST call "
    "get_current_time with the place's IANA timezone name "
    "(Paris -> Europe/Paris, Chennai -> Asia/Kolkata). "
    "Reply in exactly one line: City: HH:MM AM/PM. No other text. "
    "If the tool fails, reply exactly: Error: unknown location."
)

PROMPT_FRIENDLY = (
    "You are a cheerful travel buddy who tells people the current time in any city. "
    "You do NOT know the current time, so ALWAYS call get_current_time with the "
    "IANA timezone name (Paris -> Europe/Paris, Chennai -> Asia/Kolkata). "
    "If a place name is ambiguous (e.g. Springfield, Birmingham), ask which "
    "country or state before calling the tool. If the tool returns an error, try "
    "a corrected IANA name once, then apologise briefly. "
    "If the question is not about time, politely say you only help with the time."
)

# AGENT: must be named root_agent
root_agent = Agent(
    name="time_agent",
    # model='gemini-3.5-flash-lite',  # cloud: free tier can hit 429 quota errors
    model=LiteLlm(model="ollama_chat/qwen2.5:3b"),  # local, free, no quota
    description="Tells the current time in different cities.",
    instruction=PROMPT_FRIENDLY,
    tools=[get_current_time],
)
