---
description: Generate a pytest test file with edge cases for a CodePath problem
---

Given this problem statement and function signature:

$ARGUMENTS

1. Pick a slug: `p<N>_<function_name>` where N is the next unused number in `problems/`.
2. Create `problems/<slug>/` if it doesn't exist, with an empty `__init__.py` inside it (and one in `problems/` itself if missing). This gives each problem its own importable package and avoids test-module name collisions between problems.
3. If `problems/<slug>/solution.py` does not exist, create it containing the function signature and `pass` (do not implement the solution). At the top of the file, above the function definition, add this docstring-style block for jotting down thought process:
   ```
   """
   UNDERSTAND:
   Input:
   Output:
   Edge Cases:

   PLAN:

   IMPLEMENT: (below)
   """
   ```
4. Write `problems/<slug>/test_solution.py` importing the function with the full dotted path, e.g. `from problems.<slug>.solution import <function_name>` — never a bare `from solution import ...`, since that collides across problem folders. Include 5-8 pytest test cases: the example usage from the prompt, a typical case, and boundary/edge cases appropriate to the input types described (empty input, single element, all-duplicates, negative numbers, etc. — pick what's relevant to this specific problem, don't pad with irrelevant cases). Double-check each expected value by hand before writing it.
5. Report the slug and remind the user to run: `pytest problems/<slug> -v`
