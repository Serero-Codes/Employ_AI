import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Replace with your actual key or use environment variable
client = Groq(api_key= os.getenv("GROQ_API_KEY"))

@app.route('/')
def index(): return render_template('index.html')

@app.route('/analyze')
def analyze_form(): return render_template('form.html')

@app.route('/dashboard')
def dashboard(): return render_template('dashboard.html')

@app.route('/api/process', methods=['POST'])
def process_data():
    user_data = request.json
    
    # The "Economist" Prompt
    prompt = f"""
    Act as a Senior Labor Market Economist and AI Career Strategist. 
    Analyze this specific profile for the 2024/2025 South African and Global job market:
    
    USER PROFILE:
    - Age: {user_data.get('age')} | Gender: {user_data.get('gender')}
    - Qualification: {user_data.get('title')} (Level: {user_data.get('nqf')})
    - Field: {user_data.get('field')}
    - Core Concepts: {user_data.get('concepts')}
    - Tech Stack: {user_data.get('tech')}
    - Certifications: {user_data.get('certs')}
    - Experience: {user_data.get('exp')} years in {user_data.get('industry')}
    - Current Location: {user_data.get('location')}

    TASK:
    1. Calculate an Employability Score (0-100).
    2. Compare 'Market Job Availability' vs 'User Employability' for this specific niche.
    3. Provide employment rates for young professionals (Age {user_data.get('age')}) with the same qualification.
    4. Rank top 5 provinces by real-time demand.
    5. Identify critical skill gaps.

    RETURN ONLY JSON:
    {{
        "score": int,
        "peer_employment_rate": int,
        "market_stats": {{
            "job_availability": int, 
            "user_match_percentage": int
        }},
        "regional_trends": [{{ "province": "string", "opportunity_index": int }}],
        "salary_benchmark": "string",
        "skills_gap": ["string"],
        "career_roadmap": ["string"],
        "peer_comparison_insight": "string"
    }}
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return completion.choices[0].message.content
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)