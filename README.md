# Lab D6 — Minimal Python ReAct Agent

## Name
Kavya Sebastian

## Track
Front End Dev

## Lab Name
Minimal Python ReAct Agent

## Description
This project demonstrates a simple ReAct (Reason + Act) AI agent built using Python in Google Colab.

The agent:
- Accepts a user query
- Performs step-by-step reasoning
- Decides whether to use a tool
- Calls a calculator tool
- Observes the result
- Returns the final answer

## Technologies Used
- Python
- Google Colab

## Example Query
```python
react_agent("What is 25 * 4?")
```

## Example Output
```text
Final Answer: The answer is 100
```

# How to Run

## Option 1 — Run in Google Colab

1. Open Google Colab:
   https://colab.research.google.com

2. Create a new notebook

3. Copy the contents of:
   `/src/react_agent.py`

4. Paste into a Colab code cell

5. Click the ▶ Run button
   OR press:
   Shift + Enter

6. The output will display below the code cell

---

## Option 2 — Run Locally Using VS Code

### Step 1 — Install Python

Download Python:
https://www.python.org/downloads/

---

### Step 2 — Open Project Folder in VS Code

Open the folder:

```text
Lab_D6_Kavya_Sebastian
```

---

### Step 3 — Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

---

### Step 4 — Run the Script

Execute:

```bash
python src/react_agent.py
```

---

## Expected Output

```text
User Query: What is 25 * 4?

Thought: I should identify whether I need a tool.

Thought: This looks like a math problem.
Action: Use Calculator Tool

Action Input: 25 * 4

Observation: 100

Thought: I now know the answer.

Final Answer: The answer is 100
```
