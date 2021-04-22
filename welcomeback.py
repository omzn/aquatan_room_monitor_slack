#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

import slackbot_settings
import re
import time
from slacker import Slacker
from datetime import datetime
from db import DB

def sayWelcomeback():
    ibeacondb = DB(slackbot_settings.DB_HOST,slackbot_settings.DB_NAME,slackbot_settings.DB_USER,slackbot_settings.DB_PASS)
    ib_list = ibeacondb.ibeaconList()
    for ib in ib_list:
        if ib[0] in slackbot_settings.EXCEPT_BEACON_SAY_HELLO:
            continue
        ib_mon = ibeacondb.n("target_{}_status".format(ib[0]))
        if ib_mon:
            dt_now = datetime.now().strftime("%Y-%m-%d")
            found_t = datetime.strptime(ib_mon[1], "%Y-%m-%d  %H:%M:%S").strftime("%Y-%m-%d")
            hello = ibeacondb.n("hello_slack_{}".format(ib[0]))
            if not hello and re.match(r'Found',ib_mon[0]) and dt_now == found_t:
                ibeacondb.set_n("hello_slack_{}".format(ib[0]),dt_now)
                slack = Slacker(slackbot_settings.API_TOKEN)
                slack.chat.post_message(
                    slackbot_settings.RESPOND_CHANNEL,
                    "<@{}> おかえりー".format(ib[2]),
                    as_user=True
                )

if __name__ == '__main__':
    while True:
        sayWelcomeback()
        time.sleep(60)
