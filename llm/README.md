# Backend for langchain-sd-handson

## Sec. 2
### OutputParser
- StrOutputParser
  - 単一文字列でReturnする
- JsonOutputParser
  - JSON形式でReturnする(★参考になる！！)
  - https://github.com/mkazutaka/software-design-202408-llmapp/blob/main/chapter2-and-5/outputparser_json.py

## Sec. 4
### set up
- OpenAIに代わってClaudeを利用
  - 参考
    - https://python.langchain.com/docs/integrations/chat/bedrock/
    - https://python.langchain.com/docs/langserve/

```bash
cd src
AWS_PROFILE={profile in your credential} uvicorn main:app --reload
```

以下のように「LANGSERVE」と表示されれば成功です
```bash
INFO:     Started server process [43193]
INFO:     Waiting for application startup.

     __          ___      .__   __.   _______      _______. _______ .______     ____    ____  _______
    |  |        /   \     |  \ |  |  /  _____|    /       ||   ____||   _  \    \   \  /   / |   ____|
    |  |       /  ^  \    |   \|  | |  |  __     |   (----`|  |__   |  |_)  |    \   \/   /  |  |__
    |  |      /  /_\  \   |  . `  | |  | |_ |     \   \    |   __|  |      /      \      /   |   __|
    |  `----./  _____  \  |  |\   | |  |__| | .----)   |   |  |____ |  |\  \----.  \    /    |  |____
    |_______/__/     \__\ |__| \__|  \______| |_______/    |_______|| _| `._____|   \__/     |_______|
```

- 以下URLにアクセスして、起動サーバを確認することができる
  - Playgroundで操作
    - http://127.0.0.1:8000/anthropic/playground/
    - Humanを選択して、チャットを行う
  - APIドキュメントを確認
    - http://127.0.0.1:8000/docs/

- 上記ドキュメントページからinvokeのパスを確認して、Curlを実行する
```bash
curl -X POST 'http://127.0.0.1:8000/anthropic/invoke' -H 'Content-Type: application/json' -d '{"input": [{"type": "human", "content": "hello"}]}'
```
以下のようなレスポンスが取得可能
```json
{"output":{"content":"Hello! How can I assist you today?","additional_kwargs":{"usage":{"prompt_tokens":8,"completion_tokens":12,"total_tokens":20},"stop_reason":"end_turn","model_id":"anthropic.claude-3-haiku-20240307-v1:0"},"response_metadata":{"usage":{"prompt_tokens":8,"completion_tokens":12,"total_tokens":20},"stop_reason":"end_turn","model_id":"anthropic.claude-3-haiku-20240307-v1:0"},"type":"ai","name":null,"id":"run-99ac0855-9ee3-49c1-ae38-93c1eaa1c511-0","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":{"input_tokens":8,"output_tokens":12,"total_tokens":20}},"metadata":{"run_id":"99ac0855-9ee3-49c1-ae38-93c1eaa1c511","feedback_tokens":[]}}%
```
