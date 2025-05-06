# Voice Agent

This is a simple voice agent that includes two core components:  
- *STT (Speech-to-Text)*: Converts spoken audio to text.  
- *TTS (Text-to-Speech)*: Converts text responses back into spoken audio.  

The agent leverages OpenAI APIs and can be easily run locally.

> This project is developed and tested with *Python 3.11*. Please ensure you are using Python 3.11 for compatibility.


## 🚀 Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/prarththanan98/voice-agent.git
cd voice-agent
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Copy the sample file and add your OpenAI API key:
```bash
cp .env-sample .env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Voice Agent

```bash
python main.py
```