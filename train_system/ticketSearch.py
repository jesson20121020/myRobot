#coding=utf-8
from prettytable import PrettyTable

class TrainCollection(object):
    """解析列车信息"""
    # 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
    header = "序号 车次 出发站/到达站 出发时间/到达时间 历时 商务座 一等座 二等座 软卧 硬卧 硬座 无座".split()

    def __init__(self,rows,traintypes):
        self.rows = rows
        self.traintypes = traintypes

    def _get_duration(self,row):
        """获取车次运行的时间"""
        duration = row.get("lishi").decode('utf-8').replace(":",u"小时") + u"分"
        if duration.startswith("00"):
            return duration[4:]
        elif duration.startswith("0"):
            return duration[1:]
        return duration

    @property
    def trains(self):
        result = []
        flag = 0
        for row in self.rows:
            if row["station_train_code"][0] in self.traintypes:
                flag += 1
                train = [# 序号
                        flag,# 车次
                        row["station_train_code"],# 出发、到达站点
                        "/".join([row["from_station_name"],row["to_station_name"]]),# 成功、到达时间
                        "/".join([row["start_time"],row["arrive_time"]]),# duration 时间
                        self._get_duration(row),# 商务座
                        row["swz_num"],# 一等座
                        row["zy_num"],# 二等座
                        row["ze_num"],# 软卧
                        row["rw_num"],# 硬卧
                        row["yw_num"],# 硬座
                        row["yz_num"],# 无座
                        row["wz_num"]]
                result.append(train)
        return result
                
    def print_pretty(self):
        """打印列车信息"""
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

if __name__ == "__main__":
    t = TrainCollection()

