import urllib3
from dateRequest import documents

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


print("================ document 中的文本内容分隔=================")
# 获取 document 中的文本内容
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap  = 5,
    length_function = len,
    add_start_index = True,
)
txt_docs = text_splitter.split_documents(documents)


print("================模型语句 token 拆分器=================")
from langchain.text_splitter import SentenceTransformersTokenTextSplitter
pmmb_model = "/mnt/e/ai/models/paraphrase-multilingual-mpnet-base-v2"
st_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0, model_name=pmmb_model)
st_docs = st_splitter.split_documents(documents)





