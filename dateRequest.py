from pprint import pprint
from langchain.document_loaders import UnstructuredMarkdownLoader
import urllib3
import requests
import json
import re
import os.path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch(pid):
    title = ""
    content = ""
    wiki_url = "https://172.16.14.66:8889/server/index.php?s=/api/page/info"
    response = requests.post(wiki_url, data={ "page_id" : pid }, verify=False)
    json_ret = json.loads(response.text)
    if json_ret["error_code"] == 0:
        data = json_ret["data"]
        title = data["page_title"]
        content = data["page_content"]
    return title, content

wiki_dir = "/root/workspace/wiki"

print("================写出爬取文本数据=================")
index_content = fetch(189)[-1]
data = []
if len(index_content) > 0:
    # match #### [飞腾环境下图形化界面问题](https://172.16.14.66:8889/web/#/6/23 "飞腾环境下图形化界面问题")
    pattern = r"\((.*?)\s+(.*?)\)"
    lines = index_content.split("\n")
    for line in lines:
        print(line)
        match = re.search(pattern, line)
        if match:
            url = match.group(1)
            pid = url.rsplit("/", 1)[-1]
            title = match.group(2)[1:-1]
            data.append((title, url, pid))
pprint(data)

def documentsData():
    documents = []
    for tuple in data:
        path = f"{wiki_dir}/{tuple[-1]}.md"
        if not os.path.exists(path):
            [title, content] = fetch(tuple[-1])
            with open(path, "w") as f:
                f.write(content)
                f.close()

        stat = os.stat(path)
        if stat.st_size > 0:
            loader = UnstructuredMarkdownLoader(path)
            docs = loader.load()
            for doc in docs:
                md = doc.metadata
                md["title"] = title
                md["id"] = tuple[-1]
            documents.extend(docs)
    len(documents)
    pprint(documents[0])
    return documents
documents = documentsData()


# 获取 document 中的文本内容
def mapDocs(documents):
    docs = []
    for doc in documents:
        docs.append(doc.page_content)
    return docs

