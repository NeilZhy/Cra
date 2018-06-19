# -*- coding: utf-8 -*-
import string
import re
class getIntro():

    def get_introduction(self,text):
        try:
            # identify = string.maketrans('', '')
            # delEStr =' '  # ASCII标点符号,空格和数字，字母
            # s = text.translate(identify, delEStr)  # 去掉空格
            result = text.encode("utf-8").replace(" ","")

            # s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！｀／｜“，。：？”、~@#￥%……&*（）《》［］｛｝‘ ’]+".decode("utf8"),"".decode("utf8"), temp)
            return result
        except Exception as err:
            print err