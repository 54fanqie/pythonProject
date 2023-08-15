from pprint import pprint
from langchain.embeddings import SentenceTransformerEmbeddings
import numpy as np
from dateRequest import  mapDocs
from textSplitter import txt_docs

print("================使用嵌入向量化模型将数据向量化=================")
from langchain.embeddings import SentenceTransformerEmbeddings
# embedding_model = "/mnt/e/ai/models/m3e-base"
embedding_model = "/mnt/e/ai/models/text2vec-base-chinese"
embeddings = SentenceTransformerEmbeddings(model_name=embedding_model)
test_ret = embeddings.embed_query("hello, world")
pprint(len(test_ret))


print("================向量化文档分段数据================")
st_embedded_docs = embeddings.embed_documents(mapDocs(txt_docs))
pprint(st_embedded_docs[0])

print("================向量化模型切换=================")
from sentence_transformers import SentenceTransformer
pmmb_model = SentenceTransformer('/mnt/e/ai/models/paraphrase-multilingual-mpnet-base-v2')

print("================向量化后，通过余弦相识度，计算topk=================")
test_text0 = "轻阅读无法启动"
test_text1 = "转换服务无法启动"
test_text2 = "字体安装问题"
tt0 = embeddings.embed_query(test_text0)
tt1 = embeddings.embed_query(test_text1)
tt2 = embeddings.embed_query(test_text2)
print(np.dot(tt0, tt0))
print(np.dot(tt0, tt1))
print(np.dot(tt0, tt2))
# print(np.dot(st_embedded_docs[0], st_embedded_docs[0]))
# print(np.dot(st_embedded_docs[0], st_embedded_docs[1]))
#numpy 余弦相似度
cos_sim = np.array(tt0).dot(tt0) / (np.linalg.norm(tt0) * np.linalg.norm(tt0))
print(cos_sim)
cos_sim = np.array(tt0).dot(tt1) / (np.linalg.norm(tt0) * np.linalg.norm(tt1))
print(cos_sim)
cos_sim = np.array(tt0).dot(tt2) / (np.linalg.norm(tt0) * np.linalg.norm(tt2))
print(cos_sim)


tt0 = pmmb_model.encode(test_text0)
tt1 = pmmb_model.encode(test_text1)
tt2 = pmmb_model.encode(test_text2)
print(np.dot(tt0, tt0))
print(np.dot(tt0, tt1))
print(np.dot(tt0, tt2))



