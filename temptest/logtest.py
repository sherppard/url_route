# -*- encoding: utf-8 -*-
import requests,json
import ast
from jinja2 import Environment, PackageLoader

file = open('json-data', 'r', encoding='utf-8')
dict_data = ast.literal_eval(file.read())
data = json.loads(json.dumps(dict_data))
file.close()

body = {"msgtype":"markdown", "markdown": {}}
key = 'login_fail_type_3'
im_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2effe5dc-b9d0-491f-94b0-82609b568396"

print(data)

env = Environment(loader=PackageLoader('AlertSource.graylog3.wx'))
template = env.get_template( key + '.j2')
body["markdown"]["content"] = template.render(data)

r = requests.post(im_url, data=json.dumps(body))
print(r.text)