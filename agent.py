import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_reply(ticket_text):
    prompt = f"""
    You are an IT Service Desk Engineer.

    Analyze this ticket and provide a professional solution.

    Ticket:
    {ticket_text}
    """

    response = model.generate_content(prompt)
    return response.text
