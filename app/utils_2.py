# ========================================== IMPORTS ==========================================
############################## Core Imports  ##############################

import pickle  # used in: build_hybrid_retriever
from pathlib import Path  # used in: download_request
import requests  # used in: download_request
import pandas as pd  # used in: load_documents, hybrid_run_queries
from tqdm import tqdm  # used in: download_request

############################## LangChain core objects  ##############################

from langchain_core.documents import Document  # used in: load_documents, build_context
from langchain_core.prompts import ChatPromptTemplate  # used in: run_chain
from langchain_core.runnables import RunnablePassthrough, RunnableLambda  # used in: run_chain
from langchain_core.output_parsers import StrOutputParser  # used in: run_chain

############################## LangChain retrieval / vector stores ##############################

import faiss
from langchain_text_splitters import RecursiveCharacterTextSplitter  # used in: split_documents
from langchain_community.vectorstores import FAISS  # used in: build_vect_retriever
from langchain_community.embeddings import HuggingFaceEmbeddings  # used in: build_vect_retriever
from langchain_community.retrievers import BM25Retriever  # used in: build_bm25_retriever
from langchain_classic.retrievers import EnsembleRetriever  # used in: build_hybrid_retriever

############################## LLM integrations ##############################

from langchain_groq import ChatGroq  # used in: build_llm_model

from langchain_huggingface import HuggingFacePipeline  # used in: build_llm_model
from transformers import pipeline  # used in: build_llm_model


# ========================================== FUNCTIONS ==========================================


def build_vect_retriever(faiss_folder = "data/retrievers/semantic_index",
                        model= "sentence-transformers/all-MiniLM-L6-v2", 
                        k=5):
    """
    Load a FAISS vectorstore from disk and return a retriever that can be used in the RAG chain.

    Args:
        faiss_folder (str): Path to saved FAISS index.
        model (str): Embedding model name.
        k (int): Top-k retrieval size.

    Returns:
        Retriever: LangChain retriever wrapper.
    """
    embeddings = HuggingFaceEmbeddings(model_name= model)
    vectorstore = FAISS.load_local(faiss_folder, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})
    return retriever


def bm25_search(query, bm25_retriever, k = 5):
    """
    Search using BM25 retriever and return top-k documents.

    Args:
        query (str): Search query.
        bm25_retriever (BM25Retriever): Trained retriever.
        k (int): Number of results.

    Returns:
        list[tuple[Document, float]]: Ranked results.
    """
    #tokenize the query safeguard
    if hasattr(bm25_retriever, "preprocess_func"):
            query_tokens = bm25_retriever.preprocess_func(query)
    else:
        query_tokens = query.lower().split() #just as a fall back for tokenizing 

    
    bm25_scores = bm25_retriever.vectorizer.get_scores(query_tokens)
    bm25_docs = bm25_retriever.docs

    ranked = sorted(zip(bm25_docs, bm25_scores), 
                    key=lambda x: x[1], 
                    reverse=True)

    top_k_docs = ranked[:k]
    return top_k_docs