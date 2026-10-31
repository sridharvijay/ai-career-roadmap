1.Why does the LLM need a docstring on a tool?
A docstring is usefull for LLM can use which tool need to call and identify based on user prompt. It decides what the tool actioned in run time.

**Claude's answer:** The LLM can't see the Python code. It only sees the tool's name, docstring, and type hints. It uses the docstring to decide when to call the tool and what arguments to send (e.g. `timezone_name` should look like `Asia/Kolkata`).

2.Why return an error as a dict and not raise an exception?
exception in the sense its return normal information to user but dict type is returning key and value kind of error information to user. so user can understand clearly.

**Claude's answer:** An exception can crash the run. A returned error dict is data the LLM can read, so it can fix its input and retry (e.g. `Paris` -> `Europe/Paris`), or explain the problem politely to the user. The reader of the error is the LLM, not the end user.

3.What does Literal["success"] do?

Literal is one kind of object it return two things either success or error.

**Claude's answer:** `Literal["success"]` restricts a field to one exact value. Pydantic rejects anything else, so a success result can never be labelled "error". The "success or error" choice comes from having two separate classes (`TimeSuccess` and `TimeError`), each with its own locked `status`. TypeScript equivalent: `status: "success"`.

4.What's the difference between a token and a context window?

Token means chunk of words . it split the words by using some methods like 3/4 of words. while send the prompt from user input to llm and back response to user

Context window is maintain a history of records, suppose a user alreay asking some question . now try to ask same context then LLM before take response check context window.

**Claude's answer:** A token is a small chunk of text, about 3/4 of an English word (roughly 4 characters). It is the unit models read, write, and charge by. The context window is the maximum number of tokens the model can hold in one request: system prompt + history + tool results + reply. If it overflows, old content is cut or the call fails. Analogy: token = a word on a page; context window = how many pages fit on the desk at once.

5.What is an agent, in one sentence?

Agent mean it combine LLM, tool and information ,
Instead of direct response from LLM , it take consume minimum time and give a clear input to user

**Claude's answer:** An agent is an LLM with tools and instructions that decides what actions to take, calls those tools, and uses the results to answer. (It is usually slower than a plain LLM call because it makes several calls; the benefit is that it can do things and fetch real data.)
