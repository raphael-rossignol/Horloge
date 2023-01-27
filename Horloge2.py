import time
status = True


def change_time(new_hour):
    list_new_hour = list(new_hour)
    while status is True:
        list_new_hour[2] += 1
        alarm()
        print("\r", list_new_hour[0], ":", list_new_hour[1], ":", list_new_hour[2], end="")
        if list_new_hour[2] >= 60:
            list_new_hour[1] += 1
            list_new_hour[2] = 0
        if list_new_hour[1] >= 60:
            list_new_hour[0] += 1
            list_new_hour[1] = 0
        if list_new_hour[0] >= 24:
            list_new_hour[0] = 0
        time.sleep(1)
        return list_new_hour


change_time((23, 59, 30))


def alarm(time_alarm):
    list_time_alarm = list(time_alarm)
    if list_time_alarm == list_new_hour:
        print("It is time")


alarm((0, 0, 5))


def display_time():
    while status is True:
        time_live = time.strftime("%H:%M:%S")
        print("\r", time_live, end="")
        time.sleep(1)


display_time()