import time, sys, re, os, random

sleep_until = sys.argv[1]
real_time = re.compile(r"(\d{1,2})[:]?(\d{1,2})?")
# supports formats like 12:00, or 12:58 or 12: or 12 only .....
time_list = real_time.search(sleep_until)
if not time_list[2]: # if no time list 2 then only hour is assigned.
	sleep_until = "%s:0" % (time_list[1])
a = True
while a:
	time.sleep(10)
	time_now = time.localtime()
	time_now_string = str(time_now[3]) + ":" + str(time_now[4])
	if time_now_string == sleep_until: a = False
my_list = os.listdir(r"D:\Downloads\SHAREit\SHV-E250S\music")
music = random.choice(my_list)
os.startfile(r"D:\Downloads\SHAREit\SHV-E250S\music\\" + music)
