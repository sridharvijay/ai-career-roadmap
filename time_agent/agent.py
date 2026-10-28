from datetime import datetime
from typing import Literal
from zoneinfo import ZoneInfo
from pydantic import BaseModel, Field
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# RESULT MODELS: pydantic validates the shape of every tool result (like a TS interface + runtime check)
class TimeSuccess(BaseModel):
    status: Literal["success"] = "success"
    timezone: str
    time: str
    utc_time: str   # filled in with now.astimezone(ZoneInfo("UTC")).strftime("%I:%M %p")
    utc_offset: str = Field(pattern=r"^[+-]\d{2}:\d{2}$")  # e.g. +05:30


class TimeError(BaseModel):
    status: Literal["error"] = "error"
    message: str


# TOOL: a plain Python function
def get_current_time(timezone_name: str) -> dict[str, str]:
    """Returns the current time for an IANA timezone name.

    Args:
        timezone_name: IANA timezone name, e.g. "Asia/Kolkata" or "Europe/London".
    """
    try:
        now = datetime.now(ZoneInfo(timezone_name))
    except (KeyError, ValueError):
        return TimeError(message=f"Unknown IANA timezone: {timezone_name}.").model_dump()
    offset = now.strftime("%z")  # "+0530"
    result = TimeSuccess(
        timezone=timezone_name,
        time=now.strftime("%I:%M %p, %d %b %Y"),
        utc_time=now.astimezone(ZoneInfo("UTC")).strftime("%I:%M %p"),
        utc_offset=f"{offset[:3]}:{offset[3:]}",
    )

    return result.model_dump()  # ADK sends tool results to the model as JSON-able dicts

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
