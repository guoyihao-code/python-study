import os
import sys
import requests

API_URL = "https://api.deepseek.com/chat/completions"


def ask(q: str) -> str:
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        print("没读到 DEEPSEEK_API_KEY，先 set 环境变量", file=sys.stderr)
        sys.exit(1)

    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": q}],
        },
        timeout=30,
    )
    print("status:", resp.status_code)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    question = sys.argv[1] if len(sys.argv) > 1 else "用一句话介绍你自己"
    print(ask(question))