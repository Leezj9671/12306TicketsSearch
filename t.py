# coding: utf-8
"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
import requests
from docopt import docopt
from pprint import pprint
from prettytable import PrettyTable

from stations import stations

header = '车次 车站 时间 历时 商务座 一等 二等 软卧 硬卧 硬座 无座'.split()
code2stations = {v:k for k,v in stations.items()}

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    # 参数 
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    # URL经常会变, 注意更改
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station
    )
    r = requests.get(url, verify=False)
    rts = r.json()['data']['result']

    tablev = PrettyTable()
    tablev._set_field_names(header)

    for rt in rts:
        cm = rt.split('|')
        if not cm[3][0].lower() in options:
            continue
        # train_no = cm[2];
        station_train_code = cm[3];
        # start_station_telecode = cm[4];
        # end_station_telecode = cm[5];
        from_station_telecode = cm[6];
        to_station_telecode = cm[7];
        start_time = cm[8];
        arrive_time = cm[9];
        lishi = cm[10];
        canWebBuy = cm[11];
        # yp_info = cm[12];
        start_train_date = cm[13];
        # train_seat_feature = cm[14];
        location_code = cm[15];
        # from_station_no = cm[16];
        # to_station_no = cm[17];
        # is_support_card = cm[18];
        # controlled_train_flag = cm[19];
        # gg_num = cm[20];
        # 高级软卧
        gr_num = cm[21] or '--';
        # qt_num = cm[22];
        #软卧 
        rw_num = cm[23] or '--';
        # rz_num = cm[24];
        tz_num = cm[25] or '--';
        # 无座 
        wz_num = cm[26] or '--';
        # yb_num = cm[27];
        # 硬卧 
        yw_num = cm[28] or '--';
        # 硬座 
        yz_num = cm[29] or '--';
        # 二等座 
        ze_num = cm[30] or '--';
        # 一等座 
        zy_num = cm[31] or '--';
        # 商务座 
        swz_num = cm[32] or '--';
        # 动卧 
        srrb_num = cm[33];
        # yp_ex = cm[34];
        # seat_types = cm[35];
        tablev.add_row([
            station_train_code,
            '\n'.join([
                code2stations[from_station_telecode],
                code2stations[to_station_telecode]]),
            '\n'.join([
                start_time,
                arrive_time]),
            lishi,
            swz_num,
            zy_num,
            ze_num,
            rw_num,
            yw_num,
            yz_num,
            wz_num
            ])
    print(tablev)
    
    
if __name__ == '__main__':
    cli()