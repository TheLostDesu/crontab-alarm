from crontab import CronTab
import os


cron = CronTab(user=True)

SET_ERROR = 1
SET_OK = 0



def set_alarm():
    print("let's set a smart alarm")
    print("input days of the week")
    days = [day[:3:] for day in input().split()]
    for day in range(len(days)):
        if days[day] not in ['MON', 'TUE', 'WEN', 'THU', 'FRI', 'SAT', 'SUN']:
            if days[day] not in ['1', '2', '3', '4', '5', '6', '7']:
                print('wrong day format')
                return SET_ERROR
            else:
                days[day] = int(days[day])

    time = input("input time in format of HH:MM\n").split(':')
    if len(time) != 2:
        print('wrong time format')
        return SET_ERROR
    
    if not time[0].isdigit() or int(time[1]) < 0 or int(time[1]) > 60:
        print('wrong time format')
        return SET_ERROR
    if not time[1].isdigit() or int(time[0]) < 0 or int(time[0]) > 24:
        print('wrong time format')
        return SET_ERROR
    
    job = cron.new(os.getcwd() + 'alarm.py')
    job.dow.on(*days)
    job.hour.on(time[0])
    job.minute.on(time[1])
    job.enable()
    cron.write()
    return SET_OK


print(set_alarm())