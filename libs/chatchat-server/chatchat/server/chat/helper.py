import time
import re
import jieba.posseg as pseg
from xinference_client.client.restful.restful_client import RESTfulModelHandle

from chatchat.server.utils import get_base_url


def get_embedding_model() -> RESTfulModelHandle:
    from xinference_client import RESTfulClient as Client
    from chatchat.server.utils import get_default_embedding, get_model_info

    embedding_model_name = get_default_embedding()
    embedding_model_info = get_model_info(model_name=embedding_model_name)

    xf_url = get_base_url(embedding_model_info.get("api_base_url"))
    xf_client = Client(xf_url)
    embedding_model = xf_client.get_model(embedding_model_name)

    return embedding_model


def create_embedding(embedding_model: RESTfulModelHandle, text: str):
    t_start = int(time.time() * 1000)

    embedding_text = embedding_model.create_embedding(text)

    t_end = int(time.time() * 1000)

    t_dur = t_end - t_start
    print("=== embedding dur = %d" % t_dur)

    return embedding_text


def cut_sentences(text):
    """中文句子分割"""
    # 使用jieba的分句模块
    sentences = pseg.cut(text)
    result = []
    tmp = []
    for word, flag in sentences:
        if word in ['。', '！', '？'] and flag == 'x':  # 'x'表示单独一个句子
            tmp.append(word)
            if tmp:
                result.append(''.join(tmp))
                tmp = []
        else:
            tmp.append(word)
    if tmp:
        result.append(''.join(tmp))
    return result

    # sentences = re.split('。|！|？', text)
    # return sentences

def computer_cosine(srcDict, resultDict):
    from scipy import spatial

    t_start = int(time.time() * 1000)

    min = 0.4
    for result_key in resultDict:
        for src_key in srcDict:
            v1 = resultDict[result_key]["embedding"]["data"][0]["embedding"]
            v2 = srcDict[src_key]["embedding"]["data"][0]["embedding"]

            cos_sim = 1 - spatial.distance.cosine(v1, v2)
            print(f"cos_sim = {cos_sim}")

            if cos_sim > min:
                srcDict[src_key]["marks"].append(resultDict[result_key]["content"])

    t_end = int(time.time() * 1000)

    t_dur = t_end - t_start
    print("=== cosine total = %d" % t_dur)