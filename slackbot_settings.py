# coding: utf-8

# botアカウントのトークンを指定
API_TOKEN = ""
# しゃべったり，反応したりするチャンネル
RESPOND_CHANNEL="lab_status"
# 除外するアカウント
EXCEPT_BEACON_SAY_HELLO=[15001]
# DBの接続情報
DB_HOST = 'localhot'
DB_NAME = 'ibeacon'
DB_USER = 'aquatan'
DB_PASS = 'aquatan'

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "研究して．"
# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
