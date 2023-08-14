from langchain.embeddings import SentenceTransformerEmbeddings
import numpy as np

print("================使用嵌入向量化模型将数据向量化=================")
# embedding_model = "/mnt/e/ai/models/m3e-base"
embedding_model = "/mnt/e/ai/models/text2vec-large-chinese"
embeddings = SentenceTransformerEmbeddings(model_name=embedding_model)


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

from sentence_transformers import SentenceTransformer
pmmb_model = SentenceTransformer('/mnt/e/ai/models/paraphrase-multilingual-mpnet-base-v2')

tt0 = pmmb_model.encode(test_text0)
tt1 = pmmb_model.encode(test_text1)
tt2 = pmmb_model.encode(test_text2)
print(np.dot(tt0, tt0))
print(np.dot(tt0, tt1))
print(np.dot(tt0, tt2))