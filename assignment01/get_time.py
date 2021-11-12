import datetime

def dong() -> str:
    now = datetime.datetime.now()
    
    return now.strftime("%H:%M:%S")