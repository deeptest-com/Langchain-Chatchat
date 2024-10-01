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
        {"role": "user", "content": "提取器怎么用？"},
    ],
    "stream": False,
    "temperature": 0.7,
    "tool_choice": "search_local_knowledgebase",
    "tools": ['search_local_knowledgebase'],
    "tool_input": {'database': 'wiki', 'query': '提取器怎么用？'},

    "chat_model_config": {'preprocess_model': {'glm4-chat': {'model': '', 'temperature': 0.05, 'max_tokens': 4096, 'history_len': 10, 'prompt_name': 'default', 'callbacks': False}}, 'llm_model': {'glm4-chat': {}}, 'action_model': {'glm4-chat': {'model': '', 'temperature': 0.01, 'max_tokens': 4096, 'history_len': 10, 'prompt_name': 'ChatGLM3', 'callbacks': True}}, 'postprocess_model': {'glm4-chat': {'model': '', 'temperature': 0.01, 'max_tokens': 4096, 'history_len': 10, 'prompt_name': 'default', 'callbacks': True}}, 'image_model': {'sd-turbo': {'model': 'sd-turbo', 'size': '256*256'}}},
    "conversation_id": 'd79ee87bf3cc4769ad2ca30ef57f1ee5'
}

def test_kb():
    kb()

def kb():
    t_start = int(time.time() * 1000)

    response = requests.post(f"{base_url}/chat/completions", json=data, stream=False)
    for line in response.iter_content(None, decode_unicode=True):
        print(line, end="", flush=True)
        print("\n")

    t_dur = int(time.time() * 1000) - t_start
    print("!!!!!! test_kb dur = %d\n" % t_dur)
