from utils import load_documents, split_documents, langc_bm25_retriever
import pickle


whole_docs = load_documents(parquet_path = "data/processed/product_documents.parquet", 
                           text_col= "document")
split_docs = split_documents(whole_docs)


bm25_retriever = utils.langc_bm25_retriever(split_docs)

with open("langc_bm25_retriever.pkl", "wb") as f:
    pickle.dump(bm25_retriever, f)
