# 告警消息转发平台
特性：
1. 支持graylog3,自研平台
2. 根据对应系统，定义消息内容的key，并且根据key的value选择对应模板
3. 支持钉钉，微信告警渠道配置，可同时支持多个
4. 采用jinja2模板引擎

平台逻辑架构
![](img/logic.png)

调用方法：  
http://127.0.0.1/[系统]/[渠道]/alert  
举例：  
http://127.0.0.1/graylog3/wxtest/alert  
http://127.0.0.1/portmanage/wx/alert  
http://127.0.0.1/portmanage/dd/alert  



