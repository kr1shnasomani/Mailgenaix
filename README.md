<h1 align="center">Mailgenaix</h1>
<p align="center" style="margin-top:30px;">
  <img src="https://github.com/user-attachments/assets/e68cb7ff-fbd8-4fa4-ac59-4f22a16952e7" height="250cm"/>
</p>
Cold email generator for a services company using Groq, LangChain, and Streamlit. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links, sourced from a vector database, based on the specific job descriptions. 

## Execution Guide:
1. Clone the repoistory:
   ```
   git clone https://github.com/ak8057/Mailgenaix.git
   cd Mailgenaix
   ```
   
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Configure API key:
   - Visit **https://console.groq.com/keys** and create an API key.
   - Create a `.env` file inside the `app/` directory with the following content:
     ```
     GROQ_API_KEY = your_api_key_here
     ```
     Note: Replace `your_api_key_here` with your actual Groq API key.
   
4. Run the Streamlit App:
   ```
   streamlit run app/main.py
   ```

## Repository Structure:
The structure of the repository is:
```
Mailgenaix/
├── app/
│   ├── resource/
│   │   └── my_portfolio.csv
│   ├── .DS_Store
│   ├── chains.py
│   ├── main.py
│   ├── portfolio.py
│   └── utils.py
├── imgs/
│   ├── .DS_Store
│   ├── architecture.png
│   └── img.png
├── vectorstore/
│   ├── 91ca355b-d93e-43fb-b635-16521af44e52/
│   │   ├── data_level0.bin
│   │   ├── header.bin
│   │   ├── length.bin
│   │   └── link_lists.bin
│   ├── 9fc860f5-8064-46f0-83d0-b75fe3ee6710/
│   │   ├── data_level0.bin
│   │   ├── header.bin
│   │   ├── length.bin
│   │   └── link_lists.bin
│   ├── .DS_Store 
│   └── chroma.sqlite3
├── .DS_Store 
├── .gitignore
├── README.md
├── email_generator.ipynb
├── my_portfolio.csv
└── requirements.txt
```

## How It Works:
Mailgenaix is a streamlined tool designed to automate cold email outreach for service companies, using job listings scraped directly from company career pages. Here's a step-by-step breakdown of how the system operates:

1. **Input a Careers Page URL:** The user provides a URL pointing to a company’s careers or jobs page via the Streamlit interface.

2. **Job Listings Extraction:** Mailgenaix uses built-in scraping utilities to parse and extract relevant job postings from the given URL. This includes job titles, descriptions, and other metadata.

3. **Job Description Analysis via Groq:** Each job description is processed through a Groq LLM (Large Language Model) via the Groq API. The model identifies:
   - Key skills and requirements
   - Role-specific context
   - Language tone and expectations

4. **Portfolio Matching via Vector Database:** The tool uses a vector database (stored in vectorstore/) to semantically compare job descriptions against your portfolio data (my_portfolio.csv). It retrieves the most relevant portfolio pieces to include in the email, ensuring personalized and targeted communication.

5. **Cold Email Generation:** A cold email is generated for each job listing using LangChain to chain prompts and structure outputs. Each email:
   - References the job title and requirements
   - Includes portfolio links relevant to the role
   - Maintains a professional, personalized tone

6. **Email Preview in UI:** The final emails are displayed in the Streamlit web interface, where users can copy, review, or save them for outreach.
