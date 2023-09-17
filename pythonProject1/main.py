#user inputs name and age
user_name = input('What is your name?')
user_age = int(input('How old are you?'))

#finding current year
from datetime import date
today_date = date.today()
year = today_date.year

#calculates year user is born
year_born = year - user_age
print('Hello,',user_name,'! You were born in', year_born)