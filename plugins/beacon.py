# coding: utf-8
import random
import time
import os
import re
import io
import slackbot_settings

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ

from db import DB

@listen_to(r'^(誰|だれ)')
def show_who(message,keyword):
    if message.channel == slackbot_settings.RESPOND_CHANNEL:
        message.react("aquatan")
        mydb = DB(slackbot_settings.DB_HOST,slackbot_settings.DB_NAME,slackbot_settings.DB_USER,slackbot_settings.DB_PASS)
        result = mydb.ibeaconList()
        slist = {}
        for r in result:
            slist.setdefault(r[1], [])
            slist[r[1]].append("<@" + r[2] + ">")
            print("{} {}".format(r[1],r[2]))
        msg = ""
        for k in slist.keys():
            msg += " と ".join(slist[k]) + "が、" + str(k) + "にいるよ。"
        if msg == "":
            msg = "誰もいないよ。"
        message.reply(msg)

