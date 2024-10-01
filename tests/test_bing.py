import time
import pytest
import openai

base_url = "http://127.0.0.1:7861/knowledge_base/search_engine/bing"

data = {
    "model": "glm4-chat",
    "messages": [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好，我是人工智能大模型"},
        {"role": "user", "content": "deeptest是什么？"},
    ],
    "stream": False,
    "temperature": 0.7,
    "extra_body": {
      "top_k": 3,
      "score_threshold": 0.1,
      "return_direct": False,
      "prompt_name": "default"
    },
}

@pytest.mark.benchmark
def test_bing(benchmark):
    result = benchmark(bing, duration=2)
    # assert result == True

def bing():
    t_start = int(time.time() * 1000)

    client = openai.Client(base_url=base_url, api_key="EMPTY")
    resp = client.chat.completions.create(**data)

    print(resp)
    print("\n")

    t_dur = int(time.time() * 1000) - t_start
    print("!!!!!! test_bing dur = %d\n" % t_dur)
