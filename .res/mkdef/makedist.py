import json

roomcfg = json.load(open("./.res/mkdef/example.json",encoding="utf-8",errors="ignore"))
print(roomcfg)

with open(file=f"./.res/mkdef/dump.txt",mode="w",encoding="utf-8",errors="ignore") as cookies:
    cookies.write(str(roomcfg))