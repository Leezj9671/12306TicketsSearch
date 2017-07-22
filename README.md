# 12306火车票查询
本项目是从实验楼[Python3 实现火车票查询工具](https://www.shiyanlou.com/courses/623/labs/2072/document)借鉴并自己完成所得。
## 要点
### 页面数据API
 - https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-07-22&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
### 页面JS
- https://kyfw.12306.cn/otn/resources/merged/queryLeftTicket_end_UAM_js.js?scriptVersion=1.9026
- http://tool.oschina.net/codeformat/js/ 格式化JS line2772处找到相关函数

## 准备
```bash
pip3 install -r requirements.txt
```
## 运行
### Usage:
```bash
tickets [-gdtkz] <from> <to> <date>
```

### Options:
- -h,--help   显示帮助菜单
- -g          高铁
- -d          动车
- -t          特快
- -k          快速
- -z          直达

### Example:
```bash
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
```
## TODO
- 封装成类
- setuptools进行SETUP
