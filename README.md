EmployAI — Quantum Career Analytics

EmployAI is an immersive, high-fidelity AI-powered career mapping platform custom-tailored for the South African and global technical labor ecosystem. By leveraging Llama 3.3 70B via the high-throughput Groq Cloud API, the application functions as a senior labor market economist—instantly processing user profile variables (such as South African NQF levels, tech stacks, certifications, and geography) into rich, interactive dashboards.

⚡ Core Capabilities

Senior Labor Market Prompt Engine: Structures a deep analytical system prompt targeting real-time economic indicators.

Futuristic High-Fidelity UI: Embraces a dark cyber terminal aesthetic featuring custom-lagged dual cursors, floating kinetic particle fields, and responsive glass panels.

Multiphase Segmented Profiler: Allows seamless transition through demographic, educational (NQF), technical, and professional indicators without interface interruptions.

Robust Localized Visualizations: Converts state outputs into interactive provincial opportunity indices, skill gap matrices, and salary benchmarking curves via ApexCharts.

🛠️ Technology Stack

Backend Architecture: Python, Flask, Groq API, python-dotenv

Frontend Architecture: HTML5 Boilerplate, Tailwind CSS, Javascript (ES6+)

Visual Analytics: ApexCharts JS Integration

Cognitive Engine: Llama-3.3-70b-versatile (Structured JSON Output Model)

📂 Repository File Mapping

├── app.py              # Main Flask controller hosting JSON API processors and prompts
├── templates/
│   ├── base.html       # Outer document shell carrying core cursor and particle models
│   ├── index.html      # Landing page displaying market tickers & platform features
│   ├── form.html       # Multiphase progressive profile engine with active step-trackers
│   └── dashboard.html  # Analytics workspace populated by ApexCharts data visualizations
├── .env                # Local secrets environment containing Groq Cloud API credentials
└── README.md           # Repository documentation


🚀 Quick Start Deployment

Ensure you have Python installed, then run:

# 1. Clone the repository
git clone [https://github.com/Serero-Codes/employai-quantum-analytics.git](https://github.com/your-username/employai-quantum-analytics.git)
cd employai-quantum-analytics

# 2. Build and boot the virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Pull python packages
pip install flask groq python-dotenv

# 4. Generate local environment file (.env)
echo "GROQ_API_KEY=your_actual_groq_api_key" > .env

# 5. Execute production sandbox
python app.py


Access the application via your secure local loop: http://127.0.0.1:5000

© 2025 EmployAI Analytics Platform — Engineered for the Future of Work in South Africa.
