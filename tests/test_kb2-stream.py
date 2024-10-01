import openai

base_url = "http://127.0.0.1:7861/knowledge_base/local_kb/wiki"

data = {
    "model": "glm4-chat",
    "messages": [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好，我是人工智能大模型"},
        {"role": "user", "content": "提取器怎么用？"},
    ],
    "stream": True,
    "temperature": 0.7,
    "extra_body": {
      "top_k": 3,
      "score_threshold": 2.0,
      "return_direct": False,
    },
}

def test_kb2():
    import requests
    response = requests.post(f"{base_url}/chat/completions", json=data, stream=True)
    for line in response.iter_content(None, decode_unicode=True):
        print(line, end="", flush=True)
        print("\n")
