あくあたん在室管理システム Slack フロントエンド
===============================================

あくあたん在室管理システムのバックエンドが稼働した状態で動作するSlackフロントエンドです．

### 


### 設定

`slackbot_settings.py`に設定を記述します．

* `API_TOKEN`: slackワークスペースのbotにアクセスするためのトークンを記述します．（必須）
* `RESPOND_CHANNEL`: botが反応するチャンネルを指定します．
* `EXCEPT_BEACON_SAY_HELLO`: botが反応しないbeaconのminorナンバーを列挙
* `DB_*`: データベースへの接続情報

```python
# coding: utf-8
# botアカウントのトークンを指定
API_TOKEN = "tokentokentoken"
# しゃべったり，反応したりするチャンネル
RESPOND_CHANNEL="general"
# 除外するアカウント
EXCEPT_BEACON_SAY_HELLO=[15001]
# DBの接続情報
DB_HOST = 'localhot'
DB_NAME = 'ibeacon'
DB_USER = 'aquatan'
DB_PASS = 'aquatan'
```
