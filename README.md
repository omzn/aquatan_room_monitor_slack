あくあたん在室管理システム Slack フロントエンド
===============================================

あくあたん在室管理システムの[バックエンド](https://github.com/omzn/aquatan_room_monitor_backend)が稼働した状態で動作するSlackフロントエンドです．

### 何をするの?

ある日の最初にビーコンが検知されたときに，「おかえり」の挨拶をslackでリプしてくれます．また，ボットにメンションで「誰かいるの？」などと問いかけると，現在の検知状況を知らせてくれます．

* `welcomeback.py`: Slackerによる実装で，定期的にDBをチェックして「おかえり」をリプします．
* `who.py`: Slackbotによる実装で，「誰か」に対してリプを返して，現在の在室状況を知らせます．

### バックエンドの設定

* `ble_tag`テーブルの`slack`に，ビーコンに対応するmember IDを記載しておきます．

### Slack botの設定

* ワークスペースでbotを1つ作成し，tokenを取得します．
* `slackbot_settings.py`に設定を記述します．

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

### 実行

2つのプログラムとも無限ループしますので，バックグラウンド実行させます．pm2などのプロセス管理ツールを使うと便利です．

```sh
$ python3 who.py &
$ python3 welcomeback.py &
```

pm2を利用した設定例
```sh
$ pm2 start who.py --interpretor python3 --name slack-who
$ pm2 start welcomeback.py --interpretor python3 --name slack-welcomeback
$ pm2 save
```
