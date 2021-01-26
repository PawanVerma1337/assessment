from datetime import datetime

# dict_trasnform function takes dict as parameter 
# transforms it and returns a dict as a result.

def dict_transform(d):
    result = ['','','','','','','']
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    for k,v in d.items():
        date =  datetime.strptime(k, '%Y-%m-%d')
        if result[date.weekday()] == '': 
            result[date.weekday()] =  v
        else:
            result[date.weekday()] +=  v

    for i in range(len(result)):
        if result[i] == '':
            result[i] = (result[i-1] + result[i+1])/2

    return dict(zip(days,result))
