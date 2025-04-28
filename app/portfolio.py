import csv
import uuid
import chromadb
from chromadb.config import Settings
import os

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = []
        if not os.path.exists('vectorstore'):
            os.makedirs('vectorstore')
        self.chroma_client = chromadb.PersistentClient(
            path="vectorstore",
            tenant="default_tenant",  
            database="default_database" , 
            settings=Settings(allow_reset=True)   # <-- important
)
        self.chroma_client.reset()  
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
        self._is_loaded = False

    def load_portfolio(self):
        if self._is_loaded:
            return

        if self.collection.count() == 0:
            print("No data in collection. Loading portfolio...")

            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]

            for row in self.data:
                techstack = str(row.get("Techstack", ""))
                links = str(row.get("Links", ""))
                self.collection.add(
                    documents=[techstack],
                    metadatas=[{"links": links}],
                    ids=[str(uuid.uuid4())]
                )

            print("Portfolio loaded.")
        else:
            print("Portfolio already exists.")

        self._is_loaded = True

    def query_links(self, skills):
        if not skills:
            return []
        result = self.collection.query(query_texts=skills, n_results=2)
        return result.get('metadatas', [])
