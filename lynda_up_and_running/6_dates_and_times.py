#
# DATES AND TIMES
#

# Import modules
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
	# === DATE, DATETIME, TIME ===

	# --- Date ---
	today = date.today()
	print('Date:', today)

	# date components
	print('Date components:', today.day, today.month, today.year)

	# Weekday (0 is monday, 6 is sunday)
	print('Date weekday:', today.weekday())

	# --- Datetime ---
	today = datetime.now()
	print('Datetime:', today)

	# current time
	ct = datetime.time(datetime.now())
	print('Datetime current time:', ct)

	# weekday
	wd = date.weekday(today)
	days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
	print('Datetime weekday:', wd, days[wd])

	# --- Time ---
	t = time(23, 59, 59)
	print('Time:',t)

	# === FORMATTING ===
	now = datetime.now()

	# date formatting

	# %y/%Y - year, %a/%A - weekday, %b/%B - month, %d - day of month
	print('Formatting:', now.strftime('%Y'))
	print('Formatting:', now.strftime('%a, %d %B, %y '))

	# %c - local date and time, %x - local date, %X - local time
	print('Formatting:', now.strftime('%c'))
	print('Formatting:', now.strftime('%x'))
	print('Formatting:', now.strftime('%X'))

	# time formatting

	# %I/%H - 12/24 hour, %M - minute, %S - second, %p - local am/pm
	print('Time formatting:', now.strftime('%I:%M:%S %p'))
	print('Time formatting:', now.strftime('%H:%M'))


	# === TIMEDELTAS ===

	delta = timedelta(days=365, hours=5, minutes=1)
	print('Timedelta:', delta)

	nowPlusYear = now + timedelta(days=365)
	print('Timedelta:', nowPlusYear)

	nowPlusDays = now + timedelta(weeks=2, days=3)
	print('Timedelta:', nowPlusDays)

	nowMinusWeek = now - timedelta(weeks=1)
	print('Timedelta:', nowMinusWeek.strftime('%A %B %d, %y'))

	# Find how many days till 1 april?
	today = date.today()
	afd = date(today.year, 4, 1) # April Fool's day
	print('Timedelta(afd):', (today - afd).days)

	# find when 1 april will be in next year
	if(afd < today): afd = afd.replace(year = today.year + 1)

	time_to_afd = afd - today
	print('Timedelta(afd):', time_to_afd.days, 'days till afd')


if __name__ == "__main__":
	main()