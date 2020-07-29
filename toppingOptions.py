import datetime
today = datetime.date.today()
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
days_til_friday = (friday - today)
print(days_til_friday.days)

# df = datetime.date.today()
# while df.weekday() != 4:
#     df += datetime.timedelta(1)
# dt = 
# print(df - dt)