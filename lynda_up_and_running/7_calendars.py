#
# CALENDARS
#

import calendar

def main():

	START_DAY = calendar.MONDAY

	c = calendar.TextCalendar(START_DAY)
	text = c.formatmonth(2013, 1, 0, 0)
	# print(text)

	hc = calendar.HTMLCalendar(START_DAY)
	html = hc.formatmonth(2013, 1)
	# print(html)

	# for i in c.itermonthdays(2013, 8):
		# print(i)

	# for name in calendar.month_name:
		# print(name)

	# for day in calendar.day_name:
		# print(day)

	# First friday of every month
	for m in range(1, 13):
		cal = calendar.monthcalendar(2017, m)
		weekone = cal[0]
		weektwo = cal[1]

		if weekone[calendar.FRIDAY] != 0:
			meetday = weekone[calendar.FRIDAY]
		else:
			meetday = weektwo[calendar.FRIDAY]

		print(calendar.month_name[m],meetday)


if __name__ == '__main__':
	main()