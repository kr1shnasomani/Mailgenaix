import streamlit as st
import urllib.parse
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:")
    submit_button = st.button("Submit")
   

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()

            jobs = llm.extract_jobs(data)

            for idx, job in enumerate(jobs):
                try:
                    st.write(f"🔍 Processing job {idx}: {job}")

                    skills = job.get('skills', [])
                    st.write(f"Skills extracted: {skills} (type: {type(skills)})")

                    if not skills:
                        st.warning(f"⚠️ No skills found for job {idx}, skipping.")
                        continue

                    links = portfolio.query_links(skills)
                    st.write(f"Links found: {links}")

                    email = llm.write_mail(job, links)
                    
                    st.subheader(f"📧 Generated Cold Email for Job {idx}")
                    st.code(email, language='markdown')

              
                    subject = f"Application: {job.get('title', 'Job Application')}"
                    body_encoded = urllib.parse.quote(email)
                    
                 
                    mailto_link = f"mailto:recipient@example.com?subject={urllib.parse.quote(subject)}&body={body_encoded}"
                    

                    st.markdown(f'''
                        <a href="{mailto_link}" target="_blank">
                            <button style="background-color:#4CAF50; color:white; border:none; padding:10px 24px; border-radius:4px; cursor:pointer;">
                                Send Email
                            </button>
                        </a>
                    ''', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"🔥 Error processing job {idx}: {e}")

        except Exception as e:
            st.error(f"❌ Top level error: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
