# from datetime import datetime, timedelta
# dt_string='2019/01/20'
# dt_string2='2019/02/09'
# date = datetime.strptime(dt_string, "%Y/%m/%d")
# date2= datetime.strptime(dt_string2, "%Y/%m/%d")

# print((date2-date).days)
# print(date + timedelta(days=30))

queue=[(0,1),(1,2)]
while(queue):
    node=queue.pop(0)
    print(node[1])