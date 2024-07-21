from loguru import logger
from .libs import config

def get_danmaku_content(event:str):
    uid=event["data"]["info"][2][0]
    content=event["data"]["info"][1]
    logger.info(content)
    try:
        contents=config.roomcfg["chat"][f"{uid}"]["command"][content]
    except:
        try:
            contents=config.roomcfg["chat"]["global"]["command"][content]
            logger.info("Reply:"+str(contents))
        except KeyError as e:
            return ""
    return contents
