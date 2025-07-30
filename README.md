# 🤖 TalentScout - Intelligent Hiring Assistant

TalentScout is an intelligent recruitment chatbot designed to streamline the **initial screening of candidates**.  
It collects essential candidate information, evaluates their **tech stack**, and generates **customized technical interview questions** using a Large Language Model (LLM).  


##  *Features*
1. Professional **Streamlit UI** for interaction  
2. **Candidate details collection** (Name, Email, Phone, Experience, Position, Location, Tech Stack)  
3. **Custom technical questions** based on declared tech stack  
4. **Step-by-step question answering** interface  
5. **Conversation context maintained** throughout the session  
6. **Data stored in CSV** for recruiter review  
7. **LLM-powered question generation** using Mistral 7B via OpenRouter API  

---

## ⚙️ **Installation Instructions**

```bash
## 1. Clone the REpository
git clone https://github.com/your-username/TalentScout.git
cd TalentScout

## 2. Create Virtual Environment 
python -m venv venv
venv\Scripts\Activate.ps1 

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Set API Key
'''Create a .env file in the project root: '''
OPENROUTER_API_KEY=your_api_key_here 

## 5. Run the Application
streamlit run app.py


#  Usage Guide  #
1. Start the app with streamlit run app.py

2. Greeting Screen → Click Start Interview

3. Fill candidate details ( name, email, tech stack, etc.)

4. Technical questions are generated based on tech stack

5. Answer each question one by one

6. Finish interview → Data is stored in candidates.csv

## 🛠 **Tech Stack**

- **Frontend:** Streamlit  
- **LLM:** Mistral 7B / OpenRouter API  
- **Backend:** Python  
- **Storage:** CSV for candidate data (simulated data for privacy)  

#  Prompt Design  #
'''Prompts are stored in prompts.py: '''

##
| Challenge                          | Solution                                                |
| ---------------------------------- | ------------------------------------------------------- |
| API returning 404 errors           | Switched to OpenRouter-compatible model endpoint        |
| Conflicts in GitHub push           | Created repo without default README / .gitignore        |
| Textbox not clearing after answers | Added `st.session_state` fix for better user experience |




