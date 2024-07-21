import os
import json
from loguru import logger
from dotenv import load_dotenv

default={'chat': {'282873551': {'command': {'debug': 'vcbot-bili with default rule'}}, 'global': {'command': {'about': 'vcbot-bili v0.1.3 by VCBots', 'about-rule': 'default rule v1.0'}, 'plugins': {'at': True, 'blind': True, 'followed': True, 'gift': True, 'guard': True, 'welcome': True}, 'schedule': [{'content': '主包记得喝水！', 'minute': 30}, {'content': '关注上舰送灯牌，寻找主包不迷路～', 'minute': 15}]}}, 'connected': '连接成功!'}

def loadroomcfg():
    load_dotenv(dotenv_path="./.env")
    global room
    room=os.environ["roomid"]
    global term_env
    term_env = os.environ["term_env"]
    global roomcfg
    try:
        roomcfg = json.load(open(f"./{room}.json",encoding="utf-8",errors="ignore"))
    except:
        roomcfg = default
        _make_default_cfg()
    finally:
        logger.info(str(roomcfg))
    return

def _make_default_cfg():
    with open(file=f"./{room}.json",mode="w",encoding="utf-8",errors="ignore") as cookies:
        cookies.write(json.dumps(default,ensure_ascii=False))