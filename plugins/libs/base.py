import config

def get_danmaku_on_gift(event:str):
    info = event['data']['data']
    giftname=info['giftName']
    name= info['uname']
    #try:
    #    contents=str(config.roomcfg["chat"]["global"]["events"]['gifts'])
    #    content_name=contents.replace(" {user} ",f"{name}")
    #    contented=content_name.replace(" {gift} ",f"{giftname}")
    #except:
    #    logger.info("Reply:"+str(contented))
    contented=f'谢谢{name}的{giftname}喵～'
    return contented

def get_danmaku_on_wuser(event:str):
    info = event['data']['data']
    name= info['uname']
    #try:
    #    contents=str(config.roomcfg["chat"]["global"]["events"]['welcome'])
    #    content_name=contents.replace(" {user} ",f"{name}")
    #except:
    #    logger.info("reply:"+str(content_name))
    content_name=f'欢迎{name}进入直播间'
    return content_name

def get_danmaku_on_buyguard(event:str):
    info = event['data']['data']
    print(info)
    giftname=info['gift_name']
    name= info['username']
    num= info['num']
    #try:
    #    contents=str(config.roomcfg["chat"]["global"]["events"]['guard'])
    #    content_name=contents.replace(" {user} ",f"{name}")
    #    content_num=content_name.replace(" {type} ",f"{giftname}")
    #    contented=content_num.replace(" {num} ",f"{num}")
    #except:
    #    logger.info("Reply:"+str(contented))
    contented=f'感谢{name}开通{giftname}x{num}喵～'
    return contented

def get_danmaku_on_user_followed(event:str):
    print(event)
    info = event['data']['data']
    name= info['uname']
    #try:
    #    contents=str(config.roomcfg["chat"]["global"]["events"]['followed'])
    #    content_name=contents.replace(" {user} ",f"{name}")
    #except:
    #    logger.info("reply:"+str(content_name))
    content_name=f'感谢{name}的关注喵～'
    return content_name

def _get_guard_type(num:int):
    if num == 1:
        return "总督"
    if num == 2:
        return "提督"
    if num == 3:
        return "舰长"
    