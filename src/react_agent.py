# Minimal ReAct Agent

# -----------------------------
# TOOL DEFINITIONS
# -----------------------------

def calculator(expression):
    """Simple calculator tool"""
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"


# -----------------------------
# REACT AGENT
# -----------------------------

def react_agent(user_query):

    print(f"User Query: {user_query}\n")

    # Step 1 - Thought
    print("Thought: I should identify whether I need a tool.\n")

    # Step 2 - Decide tool usage
    if any(op in user_query for op in ["+", "-", "*", "/"]):

        print("Thought: This looks like a math problem.")
        print("Action: Use Calculator Tool\n")

        # Extract math expression
        expression = user_query.replace("What is", "").strip().replace("?", "")

        print(f"Action Input: {expression}\n")

        # Step 3 - Tool call
        observation = calculator(expression)

        print(f"Observation: {observation}\n")

        # Step 4 - Final answer
        print("Thought: I now know the answer.\n")

        final_answer = f"The answer is {observation}"

    else:
        print("Thought: No tool is required.\n")
        final_answer = "I can only solve simple math queries."

    print(f"Final Answer: {final_answer}")

    return final_answer


# -----------------------------
# TEST THE AGENT
# -----------------------------


react_agent("What is 100 * 4?")