# -*- encoding: utf-8 -*-
import web,requests,json
import logging,logging.config
from jinja2 import Environment, PackageLoader
from configparser import ConfigParser

urls = (
    '/(.+)/(.+)/alert', 'alert'
)

class alert:

    def __init__(self):

        file = open('conf/urlmap', 'r', encoding='utf-8')
        self.url_map = json.loads(file.read())
        file.close()

        self.wxmdbody = {"msgtype":"markdown", "markdown": {}}
        self.ddmdbody = {"msgtype":"markdown", "markdown": {}}

    def POST(self, sys, im_type):

        logging.config.fileConfig("conf/log.conf")
        # create logger
        # debug, info, warn, error, critical
        logger_name = "alertlog"
        logger = logging.getLogger(logger_name)

        cfg = ConfigParser()
        cfg.read('conf/channel')
        im_url = cfg.get('Alert_Channel', im_type)

        data = web.data()
        encoding = 'utf-8'
        data = json.loads(str(data, encoding))
        logger.info(data)

        keycfg = ConfigParser()
        keycfg.read('conf/keyword')
        keyword = keycfg.get('keyword_define', sys)

        if 'weixin' in im_url:

            env = Environment(loader=PackageLoader('AlertSource.' + sys + '.'+ 'wx'))
            for key, value in self.url_map.items():
                if data[keyword] == value:
                    template = env.get_template( key + '.j2')
                    self.wxmdbody["markdown"]["content"] = template.render(data)
                    r = requests.post(im_url, data=json.dumps(self.wxmdbody))
                    logger.info(r.text)

        elif 'dingtalk' in im_url:

            print(data[keyword])

            env = Environment(loader=PackageLoader('AlertSource.' + sys + '.'+ 'dd'))
            headers = {'Content-Type': 'application/json;charset=utf-8'}
            for key, value in self.url_map.items():
                if data[keyword] == value:
                    template = env.get_template( key + '.j2')
                    self.ddmdbody["markdown"]["title"] = data[keyword]
                    self.ddmdbody["markdown"]["text"] = template.render(data)
                    r = requests.post(im_url, headers=headers, data=json.dumps(self.ddmdbody))
                    logger.info(r.text)

        return r.text

if __name__ == "__main__":
    app = web.application(urls, globals())  # 初始化web应用
    app.run()  # 启动web应用
