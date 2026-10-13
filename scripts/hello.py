import os
from dotenv import load_dotenv
from openai import OpenAI


# 读 .env；override=True 让 .env 优先于系统里已有的环境变量
load_dotenv(override=True)

# OpenAI 兼容端点，换厂商只改这两行
client = OpenAI(api_key=os.environ["LLM_API_KEY"],
                base_url=os.environ["LLM_BASE_URL"])
resp = client.chat.completions.create(
    model=os.environ["LLM_MODEL"],
    messages=[{"role": "user", "content": "用一句话介绍你自己"}],
)
print(resp.choices[0].message.content)