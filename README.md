# 告警消息转发平台
特性：
1. 支持graylog3,自研平台
2. 根据对应系统，定义消息内容的key，并且根据key的value选择对应模板
3. 支持钉钉，微信告警渠道配置，可同时支持多个
4. 采用jinja2模板引擎

###### 平台逻辑架构
![](img/logic.png)

###### API调用方法：
只支持POST方法
http://[IP]:[port]/[系统]/[渠道]/alert 
[系统]： 系统识别关键字(keyword)
[渠道]： 告警渠道配置(channel)

举例：  
http://127.0.0.1/graylog3/wxtest/alert  
http://127.0.0.1/portmanage/wx/alert  
http://127.0.0.1/portmanage/dd/alert  
  
###### 告警渠道配置
配置文件路径：conf/channel
支持自定义命名（举例）：
[渠道] = 机器人的webhook链接
```
wx = https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2effe5dc-b9xx-491f-94b0-826xxxx96
```

###### 系统识别关键字
配置文件路径：conf/keyword
[系统] = 请求json的key
配置举例：
```
graylog3 = event_definition_title
portmanage = system_key
```

###### 模板映射
配置文件路径：conf/urlmap
使用json格式的配置文件
{"[模板名称]":"[匹配关键字]"}
配置举例：
```
{
    "login_fail_type_3": "登录失败",
    "rdp_brute_force": "3389暴力破解",
    "test": "Event Definition Test Title",
    "ali_riskport": "ali_sec_group",
    "ucloud_riskport": "ucloud_fw_group",
    "fw_riskport": "fw_port_map"
}
```







