# -*- coding:utf-8 -*-

import random
import requests
import json
from hashlib import md5
import settings



class BaiDuFanYi():
    """通过百度翻译API实现翻译功能"""

    def __init__(self,mes,source,target):
        self.url = settings.baiDuApiUrl
        self.appId = settings.baiDuAppId
        self.secretKey = settings.baiDuSecretKey
        self.mes = mes
        self.source = source
        self.target = target
        self.Random = random.randint(1,10000)


    def encryptMes(self):
        """获取需要翻译的内容，并按照百度API需求加密处理
        默认源语言为自动识别，默认翻译为中文
        """
        appId = self.appId
        secretKey = self.secretKey
        Random = self.Random

        # 按照API要求进行字符串拼接，并使用md5加密
        str1 = str(appId) + self.mes + str(Random) + secretKey
        sign = md5(str1.encode("utf-8")).hexdigest()
        return sign.lower()

    def queryData(self,Token):
        AppID = self.appId
        Random = self.Random
        source = self.source
        target = self.target
        # print(target)

        """拼凑出用于请求的data
        """
        data = {
            "q":self.mes,
            "from":source,
            "to":target,
            "appid":AppID,
            "salt":Random,
            "sign":Token
        }

        return data

    def QueryApi(self,data):
        URL = self.url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        res = requests.get(URL,params=data)
        return res.text

    def main(self):
        fanyi = BaiDuFanYi(self.mes,self.source,self.target)
        token = fanyi.encryptMes()
        Data = fanyi.queryData(token)
        Res = fanyi.QueryApi(Data)
        return Res


if __name__ == '__main__':
    app = BaiDuFanYi(mes='Apple',source='auto',target='jp')
    Json = json.loads(app.main())
    print(Json['trans_result'][0]['dst'])