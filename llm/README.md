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
AWS_PROFILE=hands-on-fuji-dev uvicorn main:app --reload
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

