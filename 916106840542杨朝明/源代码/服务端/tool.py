import os
from datetime import datetime, timedelta

class dinner:
    def __init__(self):
        self.seats = {}
        '''
        key = 'yyyy-mm-dd'
        '''
        self.order_list = []
        self.scc = 1

    
    def get_table(self, query_time):
        query_hour = query_time.hour
        now_time = datetime.now()
        chk1,chk2 = now_time.day,now_time.day+1
        if now_time.hour > 19:
            chk1 += 1
            chk2 += 1
        if query_time.day == chk1 or query_time.day == chk2:
            return self.get_table_key(query_time.strftime('%Y-%m-%d'))
        else:
            return -1

    def get_table_key(self, key):
        if not self.seats.has_key(key):
            self.seats[key] = [([0] * 8) for i in range(6)]
        return self.seats[key]

    def check_phone(self, s):
        phoneprefix=['130','131','132','133','134','135','136','137','138','139','150','151','152','153','156','158','159','170','183','182','185','186','188','189']
        if len(s)<>11:
            return False
        else:
            if  s.isdigit():
                if s[:3] in phoneprefix:
                    return True
                else:
                    return False
            else:
                return False
    
    def query_by_phone(self, num):
        for i in self.order_list:
            if i['phone'] == num:
                return i
        return None

    def add_seat(self, key, num, magic):
        for i in range(6):
            for j in range(8):
                if self.seats[key][i][j] == 0 and num > 0:
                    self.seats[key][i][j] = magic
                    num -= 1
                    


    def add_ord(self, date, num ,phone):
        key = date.strftime('%Y-%m-%d')
        self.add_seat(key,num,self.scc)
        add = {}
        add['date'] = key
        add['num'] = num
        add['phone'] = phone
        add['magic'] = self.scc
        self.scc += 1
        self.order_list.append(add)

    def delete_by_phone(self, num):
        magic = 0
        for i in self.order_list:
            if i['phone'] == num:
                self.order_list.remove(i)
                magic = i['magic']
                key = i['date']
                for i in range(6):
                    for j in range(8):
                        if self.seats[key][i][j] == magic:
                            self.seats[key][i][j] = 0
                return "delete success"
        return None

    def query_rest(self, date):
        rest = 0
        table = self.get_table_key(date.strftime('%Y-%m-%d'))
        for i in table:
            for j in i:
                if j == 0:
                    rest += 1
        return rest
