import time
import requests
import pytest
import threadpool

base_url = "http://127.0.0.1:7861/chat"

data = {
    "model": "glm4-chat",
    "messages": [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好，我是人工智能大模型"},
        {"role": "user", "content": "请用100字左右的文字介绍自己"},
    ],
    "stream": True,
    "temperature": 0.7,
}

def test_llm():
    pool = threadpool.ThreadPool(3)
    requests = threadpool.makeRequests(llm, range(9))
    [pool.putRequest(req) for req in requests]
    pool.wait()


def llm(index):
    t_start = time.perf_counter()

    response = requests.post(f"{base_url}/chat/completions", json=data, stream=False)

    i = 0
    for line in response.iter_content(None, decode_unicode=True):
        print("------ %d-%d " % (index+1, i+1))
        print(line, end="", flush=True)
        print("\n")
        i += 1

    t_dur = time.perf_counter() - t_start
    print("====== %d dur = %d\n" % (index+1, t_dur))
