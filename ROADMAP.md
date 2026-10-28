# AI Full-Stack Engineer Roadmap (~6 months, 1 hr/day)

Format: **Prereq** (what to know/read) → **Task** (≤1 hr) → **Done when**.
Tick `[x]` when finished. Missed a day? Just continue from the first unchecked item.

## Phase 1 — Python + LLM foundations (Weeks 1–3)
- [X] **D1** Prereq: Python venv basics. Task: create a venv in this repo, `pip install google-adk tzdata`, `pip freeze > requirements.txt`. Done when: `adk web` runs from the venv.
- [X] **D2** Prereq: Python functions/type hints. Task: add type hints + docstrings to `get_current_time`; add 5 more cities. Don when: agent answers all of them.
- [X] **D3** Prereq: dicts/lists/comprehensions. Task: replace the city dict with a lookup of any IANA zone name given by the user. Done when: "time in Paris" works.
- [X] **D4** Prereq: what is a token, context window, temperature. Task: read Anthropic/Google prompting intro; write 3 system prompts for `time_agent`. Done when: you can explain tokens in 2 sentences.
- [X] **D5** Prereq: pydantic. Task: return the tool result using a pydantic model. Done when: validated output.
- [ ] **D6** (Sat) Build: call Gemini or Claude API directly from a 20-line Python script. Done when: script prints a response.
- [ ] **D7** (Sun) Plan next week; note 3 things you learned.
- [ ] **D8–D10** Python `async/await` + `requests`/`httpx`; write an async function fetching a public API.
- [ ] **D11–D14** FastAPI: hello world, GET/POST endpoints, `/docs`. Expose `get_current_time` as an endpoint.
- [ ] **D15–D18** Structured output (JSON schema) from an LLM; parse into pydantic.
- [ ] **D19–D21** Mini-project: CLI "ask the LLM to extract data from text" with validation. Push to GitHub.

## Phase 2 — Agents (Weeks 4–7)
- [ ] **D22–D26** ADK deep dive: tools, multiple tools, tool docstrings → schema. Add a weather tool.
- [ ] **D27–D31** Sessions & state in ADK; memory across turns.
- [ ] **D32–D36** Sub-agents / multi-agent routing (time agent + weather agent + coordinator).
- [ ] **D37–D41** MCP: what it is; connect an MCP server as a tool.
- [ ] **D42–D46** Mini-project: "Travel assistant" agent (time, weather, currency). GitHub + README.

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
- [ ] **D107–D111** Observability: logging, tracing LLM calls, cost tracking.
- [ ] **D112–D116** Security: prompt injection, secrets, input validation, rate limiting.
- [ ] **D117–D121** Evals in CI; regression tests for prompts.
- [ ] **D122–D128** Project 2: agent that performs real tasks (calendar/GitHub/email via MCP).
- [ ] **D129–D134** Resume + LinkedIn reposition: "Full-stack engineer building AI agents".
- [ ] **D135–D140** System design basics + interview practice (LLM app design questions).
- [ ] **D141–D150** Apply, network, write 1–2 blog posts about projects.

## Lifelong habits (after Phase 5)
- Weekly (Sun, 1 hr): read model/framework release notes.
- Monthly: ship one small AI project.
- Quarterly: refresh skills — new model, new framework, one deep topic (fine-tuning, voice, vision).
- Keep fundamentals alive: system design, SQL, testing, security.
- Public learning: GitHub + short posts. Visibility = job security.
