import time
import openai
import pytest
import threadpool

base_url = "http://127.0.0.1:7861/knowledge_base/local_kb/wiki"

data = {
    "model": "glm4-chat",
    "messages": [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好，我是人工智能大模型"},
        {"role": "user", "content": "提取器怎么用？"},
    ],
    "stream": False,
    "temperature": 0.7,
    "extra_body": {
      "top_k": 3,
      "score_threshold": 2.0,
      "return_direct": False,
    },
}

@pytest.mark.benchmark
def test_kb2(benchmark):
    result = benchmark(kb2)
    # assert result == True

def kb2():
    t_start = int(time.time() * 1000)

    client = openai.Client(base_url=base_url, api_key="EMPTY")
    resp = client.chat.completions.create(**data)

    print(resp)
    print("\n")

    t_dur = int(time.time() * 1000) - t_start
    print("!!!!!! test_kb2 dur = %d\n" % t_dur)
