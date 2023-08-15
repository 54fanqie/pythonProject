from pprint import pprint

from langchain.vectorstores import FAISS


from embedding import embeddings
from textSplitter import txt_docs

db = FAISS.from_documents(txt_docs, embedding=embeddings)
# db.save_local("faiss_db")
# db = FAISS.load_local("faiss_db", embeddings=embeddings)
search_ret = db.similarity_search_with_score("安装字体", k=3)
pprint(search_ret)
search_ret = db.similarity_search_with_score("安装字体", k=3, filter={"id": "451"})
pprint(search_ret)