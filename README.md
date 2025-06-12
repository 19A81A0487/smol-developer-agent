# smol-developer-agent
Code generation agent using Hugging Face Codegen


🤖 Smol Developer Agent — “Agents that think in code”
What if agents could write code like developers, think in code, and continuously improve?
Smol Developer Agent is a minimal yet powerful agent framework designed to run self-improving AI agents that generate and refine code using LLMs (Large Language Models).

🎯 Mission
Smol Developer Agent reimagines LLMs as autonomous programmers — not just for completing code, but reasoning in code.


🧠 Key Highlights
✨ Simplicity
The agent's core logic fits in under 200 lines of Python. No bloated abstractions — just pure, clean code that’s easy to modify or extend.

🧑‍💻 Code-Native Reasoning
SmolDeveloperAgent’s unique power lies in reasoning directly in Python. Prompts are code seeds, and the agent generates complete code blocks — just like a developer.

It’s not about “agents used to write code”.
It’s about “agents that think in code.”


🔐 Sandboxed Execution
Secure and test the code you generate. You can:

Use local .py execution for fast prototyping

Easily extend with Docker or E2B environments for safe, sandboxed agent runs



🤗 Hugging Face Native
Instantly swap or extend your base model from Hugging Face with:

Salesforce/codegen-350M-mono (default)

bigcode/starcoder, phind, deepseek, or others

Local LLMs via transformers, GGUF, or ollama


🔌 Model-Agnostic by Design
Works with any LLM — local or cloud:

✅ Hugging Face Transformers

✅ OpenAI (gpt-3.5, gpt-4)

✅ Anthropic (Claude)

✅ Mistral, Cohere, Together.AI, Groq via LiteLLM

✅ Ollama for local devs



🛠️ Tool-Agnostic
Integrate your own tools or use:

🧩 LangChain tools

🧪 LangGraph flows

🧰 SmolToolHub agents

📦 MCP servers

🎛️ Hugging Face Spaces as callable APIs



🌐 Multi-Modality Ready
Coming soon — support for agents that understand:

📝 Text

🖼️ Vision (image-to-code)

🎙️ Audio input

🎥 Video-based logic building


🚀 Use-Cases

| Use-Case                         | Description                                                   |
| -------------------------------- | ------------------------------------------------------------- |
| 🔧 Function Generator            | Generate Python functions from text prompts                   |
| 🔍 Auto Code Review              | Use agents to find bugs or inefficiencies in code             |
| 📜 Docstring Generator           | Automatically create documentation for functions/classes      |
| 🧪 Test Case Builder             | Generate test cases from function signatures                  |
| 🛠️ Refactor Agent               | Rewrites and optimizes old code                               |
| 🧬 Multi-agent collaborative dev | Chain agents that design, build, and debug a project together |




🧩 Example Prompt
# Python 3
# Function to compute the nth Fibonacci number using memoization




Output:

def fibonacci(n: int) -> int:
    memo = {0: 0, 1: 1}
    def fib(n):
        if n in memo:
            return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)




🧰 Project Philosophy
Build agents that write, test, refactor, and learn — all in Python.

Inspired by tools like smol-ai/smol-developer, LangGraph, and OpenInterpreter, this project is minimal, modular, and made for power-users and researchers alike.


