# AI Full-Stack Engineer Roadmap (~6 months, 1 hr/day)

Format: **Prereq** (what to know/read) → **Task** (≤1 hr) → **Done when**.
Tick `[x]` when finished. Missed a day? Just continue from the first unchecked item.

## Why this plan (job security in the AI era)
Tools and frameworks change every few months; these things last. Everything below builds toward them:
1. **Fundamentals that AI can't replace**: Python, SQL, HTTP/APIs, testing, system design, security.
2. **Reliability of AI systems**: evals, tracing, cost control, guardrails. This is what companies pay for when "the demo works" turns into "production is on fire".
3. **Your React edge**: few AI engineers can also ship a polished streaming UI. Keep it sharp (TypeScript + Vercel AI SDK alongside Python).
4. **Using AI coding tools well** (Claude Code, Copilot): the engineer who reviews, tests, and directs AI output is more valuable than one who ignores it.
5. **Visibility**: GitHub, README, live demos, short posts. Proof beats certificates.

**Busy-day rule:** can't do 1 hr? Do 15 minutes (read one section or run one example) and tick nothing. Never skip two days in a row.

## NEXT STEPS (do these in order, starting now)
- [ ] **N1** Finish D8–D10 below (async + httpx). Add `pytest` and write 2 tests for `get_current_time` (valid zone, invalid zone).
- [ ] **N2** Learn Git properly alongside: branch, commit, push. Create a GitHub repo for this project, push with a README. Commit at the end of every study day.
- [ ] **N3** Do D11–D14 (FastAPI). Add TypeScript: call your FastAPI endpoint from a tiny React/Vite page. This links your 7 years of React to the new skills.
- [ ] **N4** Do D15–D21 (structured output + CLI mini-project). Add 5 pytest cases for the validation logic.
- [ ] **N5** Weekly Sunday review (30 min): update `LEARNINGS.md` with 3 lessons in your own words, then ask yourself "could I explain each in 2 sentences?"

## Phase 1 — Python + LLM foundations (Weeks 1–3)
- [X] **D1** Prereq: Python venv basics. Task: create a venv in this repo, `pip install google-adk tzdata`, `pip freeze > requirements.txt`. Done when: `adk web` runs from the venv.
- [X] **D2** Prereq: Python functions/type hints. Task: add type hints + docstrings to `get_current_time`; add 5 more cities. Don when: agent answers all of them.
- [X] **D3** Prereq: dicts/lists/comprehensions. Task: replace the city dict with a lookup of any IANA zone name given by the user. Done when: "time in Paris" works.
- [X] **D4** Prereq: what is a token, context window, temperature. Task: read Anthropic/Google prompting intro; write 3 system prompts for `time_agent`. Done when: you can explain tokens in 2 sentences.
- [X] **D5** Prereq: pydantic. Task: return the tool result using a pydantic model. Done when: validated output.
- [X] **D6** (Sat) Build: call Gemini or Claude API directly from a 20-line Python script. Done when: script prints a response.
- [X] **D7** (Sun) Plan next week; note 3 things you learned.
- [ ] **D8–D10** Python `async/await` + `requests`/`httpx`; write an async function fetching a public API.
- [ ] **D11–D14** FastAPI: hello world, GET/POST endpoints, `/docs`. Expose `get_current_time` as an endpoint.
- [ ] **D15–D18** Structured output (JSON schema) from an LLM; parse into pydantic.
- [ ] **D19–D21** Mini-project: CLI "ask the LLM to extract data from text" with validation. Push to GitHub.

## Phase 2 — Agents (Weeks 4–7) — LangChain/LangGraph primary, ADK secondary
- [ ] **D22–D26** LangChain basics: chat model, tools (`@tool`), docstrings → schema. Rebuild `time_agent` in LangChain; add a weather tool.
- [ ] **D27–D31** LangGraph: state, nodes, edges, checkpointer (memory across turns).
- [ ] **D32–D36** Multi-agent routing in LangGraph (time agent + weather agent + coordinator).
- [ ] **D37–D41** MCP: what it is; connect an MCP server as a tool (langchain-mcp-adapters).
- [ ] **D42–D46** Mini-project: "Travel assistant" agent (time, weather, currency) in LangGraph. GitHub + README. Add a short ADK-vs-LangGraph comparison (blog material).

## Phase 3 — RAG + data (Weeks 8–11)
- [ ] **D47–D51** Embeddings concept; embed 20 sentences, cosine similarity in Python.
- [ ] **D52–D56** Chunking + vector store (Chroma/pgvector); ingest a PDF.
- [ ] **D57–D61** Retrieval + answer with citations; handle "I don't know".
- [ ] **D62–D66** Basic evals: 20 Q&A test set, measure accuracy.
- [ ] **D67–D71** SQL basics (SELECT/JOIN/GROUP BY) + Postgres local.
- [ ] **D72–D76** Mini-project: "Chat with your docs" backend.

## Phase 4 — Full-stack AI app (Weeks 12–16) — your React strength
- [ ] **D77–D81** FastAPI streaming (SSE) endpoint from an agent.
- [ ] **D82–D86** React chat UI with streaming tokens, loading/error states.
- [ ] **D87–D91** Auth (JWT/OAuth), per-user chat history in DB.
- [ ] **D92–D96** Docker for backend + frontend; docker-compose.
- [ ] **D97–D101** Deploy (Cloud Run / Render / Vercel); env secrets.
- [ ] **D102–D106** Project 1 polish: "AI chat with docs" live demo + README + screenshots.

## Phase 5 — Production + career (Weeks 17–22)
- [ ] **D107–D111** Observability: logging, tracing LLM calls (LangSmith), cost tracking.
- [ ] **D112–D116** Security: prompt injection, secrets, input validation, rate limiting.
- [ ] **D117–D121** Evals in CI; regression tests for prompts.
- [ ] **D122–D128** Project 2: agent that performs real tasks (calendar/GitHub/email via MCP).
- [ ] **D129–D134** Resume + LinkedIn reposition: "Full-stack engineer building AI agents".
- [ ] **D135–D140** System design basics + interview practice (LLM app design questions).
- [ ] **D141–D150** Apply, network, write 1–2 blog posts about projects.

## Parallel career-security track (15–30 min/week, any time)
- **Testing**: pytest basics now; later add tests for every tool and prompt.
- **SQL**: one query a day on a practice site once Phase 3 starts.
- **Cloud basics**: what a container, a VM, a managed DB, and a secret manager are (needed by Phase 4).
- **System design**: read one "design X" write-up a week; sketch it yourself first.
- **AI coding tools**: use Claude Code to scaffold, but always read the diff, run the tests, and explain each change before committing.
- **Know the landscape**: LangGraph (primary), ADK, OpenAI/Claude SDKs, MCP, vector DBs, evals. You don't need depth in all, but you should be able to explain each.

## Lifelong habits (after Phase 5)
- Weekly (Sun, 1 hr): read model/framework release notes.
- Monthly: ship one small AI project.
- Quarterly: refresh skills — new model, new framework, one deep topic (fine-tuning, voice, vision).
- Keep fundamentals alive: system design, SQL, testing, security.
- Public learning: GitHub + short posts. Visibility = job security.
