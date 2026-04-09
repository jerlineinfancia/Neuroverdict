from groq import Groq

def run_analysis(api_key, url_a, url_b):
    client = Groq(api_key=api_key)
    prompt = f"""
    Analyze and compare these two product links for conversion psychology: 
    Link Alpha: {url_a} 
    Link Beta: {url_b}
    Provide scores out of 100, primary triggers, and a final verdict.
    """
    
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content