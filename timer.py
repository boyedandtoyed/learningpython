import time, sys, re, os, random
sleep_until = "0:0:10"
real_time = re.compile(r"(\d{1,2})[:]?(\d{1,2})?[:]?(\d{1,2})?")
time_list = real_time.search(sleep_until)
a = 0
if time_list[3]:
	time_in_seconds = int(time_list[1]) * 3600 + int(time_list[2]) * 60 + int(time_list[3])
elif time_list[2]:
	time_in_seconds = int(time_list[1]) * 3600 + int(time_list[2]) * 60
else:
	time_in_seconds = int(time_list[1]) * 3600
for i in range(time_in_seconds):
	time.sleep(1)
my_list = os.listdir("D:\\Downloads\\SHAREit\\SHV-E250S\\music")
music = random.choice(my_list)
os.startfile("D:\\Downloads\\SHAREit\\SHV-E250S\\music\\" + music)
