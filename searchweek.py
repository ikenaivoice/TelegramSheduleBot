import datetime

def week():
    this_week = datetime.datetime.today().strftime("%W")
    if int(this_week) % 2 == 0:
        return 1
    else:
        return 0



