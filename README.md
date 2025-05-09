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

## Workflow:

![image](https://github.com/user-attachments/assets/daf85b02-1ea1-406b-b08b-2ae7c213a7fd)
