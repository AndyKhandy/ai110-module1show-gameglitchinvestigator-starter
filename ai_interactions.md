# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
* I asked Claude code to look at the check_guess function and describe what it is currently doing and if there were any bugs to report it

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
* The agent read the app.py file, worked on the check_guess function, replaced the return ouputs of the two conditionals for checking if guess > secret and if it was less than secret. Then prompting me to accept the changes or not.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
The thing that I had to verify was ensuring that the web application showed the right output even though the function gave me the right output. 

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Empty Strings in guess | Can you create a pytest test for parse_guess to see if empty inputs would be treated correctly | it made the test_parse_guess_empty_and_whitespace() function  | It past the test | I tested it out on the web application and it worked as intended |
| Negative integers in guess | Can you create a pytest test for parse_guess to see if negative numbers won't crash the application | it made test_parse_guess_negative_number() function | The tests past | I looked through the assertions and they looked correct |
|Non numeric strings in guess | Can you create a function similar to the past two for parse_guess for non-numeric strings | It made the test_parse_guess_non_numeric_string() function| It passed | The test worked as intended and I verified the inputs |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
