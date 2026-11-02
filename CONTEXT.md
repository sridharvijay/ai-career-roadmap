# CONTEXT — Read this first

## Who I am
- Frontend developer, **React JS, 7 years**.
- Some knowledge of core Python and Spring Boot.
- Email: sridharvijay44@gmail.com

## My goal
Build a **long-term, secure career in the AI era**. Not a short-term switch: I want to stay relevant for life.

## Target role
**AI-powered full-stack engineer**: React frontend + Python AI backend (agents, LLM apps, RAG), shipped to production.

## Time budget
**1 hour per day.** Mon–Fri learn + build, Sat build/review, Sun rest/plan.

## Current progress
- D1–D7 done (see [ROADMAP.md](ROADMAP.md); tick checkboxes as I finish each day). Next: **D8–D10** (async/await + httpx), plus NEXT STEPS N1–N5 in the roadmap.
- Built: `time_agent/agent.py` (Google ADK agent, local Ollama model via LiteLlm, `get_current_time` tool, pydantic result models, 3 system prompts) and `ask_llm.py` (direct Gemini API call).
- Fixed Windows `ZoneInfoNotFoundError` with `pip install tzdata`.
- `LEARNINGS.md` holds my own answers to recap questions plus Claude's corrections. Weak spots found: what `Literal` does, token vs context window, and why tool errors are returned as dicts for the LLM to read.
- Framework decision: LangChain/LangGraph is now the primary agent framework (better job market); ADK is secondary. Phase 2 in the roadmap was changed accordingly.
- Priority: long-term job security. The roadmap has a "Why this plan" section and a parallel career-security track (testing, SQL, cloud, system design, using AI coding tools with review).
- Life is busy: on hard days do 15 minutes, never skip two days in a row.

## How Claude should help me
- Explain simply; assume strong frontend/JS knowledge, beginner-to-intermediate Python and AI.
- Each session: look at ROADMAP.md, find the first unchecked day, give today's prerequisite + task.
- If I missed days, don't skip; continue from the first unchecked item.
- Prefer building inside this repo (`c:\Project\Google-adk`) over theory.
- Windows 11 + PowerShell. Python projects use pip.
- Keep answers short and practical; tell me the "why" for career relevance.
- Teaching style: explain concepts with JS/React analogies and let ME write the code step by step. Don't write it for me unless I ask. After I answer, check my answers and correct mistakes.
