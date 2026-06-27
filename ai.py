import ollama

def generate_ai_feedback(resume_text):

    prompt = f"""
You are an ATS Resume Expert.

Analyze the following resume and return the result in exactly this format.

Overall ATS Resume Score: (Do not calculate score, just explain)

Strengths:
- Point 1
- Point 2
- Point 3

Areas to Improve:
- Point 1
- Point 2
- Point 3

Recommended Job Roles:
- Role 1
- Role 2
- Role 3

Career Advice:
Write only one short paragraph (3-4 lines).

Resume:

{resume_text}
"""

    try:
        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Error: {e}"