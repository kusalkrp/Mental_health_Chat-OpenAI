from langchain_openai import OpenAIEmbeddings
from src.helper import load_pdf,text_split
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
OpenAI_API_KEY = os.environ.get('OpenAI_API_KEY')

extracted_data = load_pdf("data")
text_chunks = text_split(extracted_data)
embeddings =OpenAIEmbeddings(openai_api_key=OpenAI_API_KEY)

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
index_name = "mental-chatbot"

# Create the wrapper around your index

# Assuming LP is an alias for LangchainPinecone
docsearch = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name=index_name
)
