# coding: utf-8
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options: 
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
"""
from docopt import docopt

QUERY_URL = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'

class TrainTicketQuery(object):
    def __ini__(self):
        pass

    def query_by_command(self):
        """command-line interface""" 
        arguments = docopt(__doc__)
        from stations import stations
        from_station = stations.get(arguments['<from>'])
        to_station = stations.get(arguments['<to>'])
        train_type = []
        all_train_type = ['-d', '-g', '-t', '-k', '-z']
        for key in all_train_type:
            if arguments[key]:
                train_type.append(key[1:].upper())
        if len(train_type) == 0:
            train_type = [x[1:].upper() for x in all_train_type]
            
        date = arguments['<date>']
        # 构建URL
        url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date,from_station, to_station)
        import requests
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, verify = False)
        rows = r.json()['data']['datas']
        
        from ticketSearch import TrainCollection
        t = TrainCollection(rows, train_type)
        t.print_pretty()
    
if __name__ == '__main__': 
    TrainTicketQuery().query_by_command()
