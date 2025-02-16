import os 

from decouple import config

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')

if __name__ == 'main':
    file_path = '/app/rag/data/CV_VINICIUS_PERRONE_2024.pdf'
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(
        documents=docs
    )

    persist_directory = '/app/chroma_data'

    embedding = HuggingFaceEmbeddings()
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory
    )
    vector_store.add_documents(
        documents=chunks
    )
