# GitHub Copilot Instructions — preferred style for this repository

Purpose
- Provide clear, beginner-friendly guidance for GitHub Copilot (or other AI assistants) so suggestions match the project style and expectations.

Tone & approach
- Be beginner-friendly: prefer clear, short explanations and in-line examples.
- Focus on clarity over cleverness: simple, readable code is better than dense, one-line solutions.
- When multiple options exist, give the simplest working option first and then (briefly) mention alternatives.

Code structure and responsibilities
- Keep business logic separate from I/O and UI layers:
  - Put pure computations, parsing, transformations, and API calls in a `logic` module (no input(), print(), GUI code, or file I/O inside these functions).
  - Keep CLI/GUI/IO code in separate files that call the logic functions.
- Prefer small, single-purpose functions with descriptive names.
- Use explicit function signatures and docstrings. If appropriate, include type hints.

Naming and style
- Follow common Python naming conventions (PEP 8): `snake_case` for functions and variables, `PascalCase` for classes.
- Use descriptive variable and function names — avoid one-letter names except for short loop indices.

Error handling and validation
- Validate external inputs at the edges (UI/CLI layer) and raise or return clear errors from logic functions.
- For external requests, handle HTTP errors and timeouts gracefully (use exceptions with helpful messages).

Testing
- Suggest unit tests for business logic. Tests should be small, deterministic, and not require network access (use mocking for HTTP requests).
- Make tests easy to run (e.g., `pytest`), and include simple examples where relevant.

Documentation
- Add short docstrings for all public functions (what it does, args, return value, exceptions).
- If generating or modifying files, briefly comment the rationale in code or commit message.

Commits and PRs
- Keep commits small and focused; each commit should have a clear message describing what changed and why.
- Prefer creating a small branch and opening a PR for larger changes.

When to ask for more details
- If the prompt is ambiguous (unclear requirements, multiple possible behaviors), ask one concise clarifying question rather than guessing.
- Suggest a reasonable default and explain the assumption in the code or a comment.

Examples and snippets
- Prefer short, copy-paste-ready examples that show how to call the function from a CLI or test.
- When recommending libraries, prefer well-known, maintained libraries and include a brief note about why it was chosen.

Formatting of responses from Copilot
- Return code blocks only for code; annotate small explanations in plain text.
- When returning multiple options, number them and highlight the recommended choice.

Security and privacy
- Avoid embedding secrets, API keys, or other sensitive information directly into code.
- If showing examples that require credentials, show placeholders and document how to provide the real values via environment variables or config files.

If you are not confident
- If Copilot cannot fully implement the request safely or correctly, provide a partial implementation and clearly state what remains to be done and why.

---

Thank you — these instructions aim to make Copilot suggestions easy to review and safe for learners. If you prefer a different emphasis (for example, performance over readability), update this file to reflect that preference.