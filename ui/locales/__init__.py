import json
import os
lang_code="zh-CN"
def set_lang_code(code):
    global lang_code
    lang_code=code
def t(key):
    with open(os.path.join("ui","locales",lang_code+".json"),encoding="utf-8") as f:
        langs=json.load(f)
    key_list=key.split(".")
    value=langs
    for i in key_list:
        value=value[i]
    return value
def get_lang_list():
    with open("ui/locales/langs.json",encoding="utf-8") as f:
        langs=json.load(f)
    lang_list=langs["lang_list"]
    export=[]
    for i in lang_list:
        export.append({
            "lang_code":i,
            "lang_name":langs[i]
        })
    return export