import datetime

def ding() -> str:
    now = datetime.datetime.now()
    
    return now.strftime("%Y-%m-%d")