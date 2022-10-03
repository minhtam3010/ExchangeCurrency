from datetime import datetime

today = datetime.today()
day = today.strftime("%d/%m/%Y")
print(day)
current_time = day + " " + today.strftime("%H:%M:%S")
print("Current Time =", current_time)