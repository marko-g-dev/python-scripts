import sys
from datetime import datetime, timedelta

arguments = sys.argv
if(len(arguments) < 3):
    print("Not enough arguments!")
    exit()

try:
    N = int(arguments[2])
except ValueError:
    print("Wrong time input!")
    exit()

try:
    file =  open(arguments[1], "r")
    data = file.read()
    file.close()
except FileNotFoundError:
    print("Could not open file:", arguments[1])
    exit()

lista = data.split("\n\n")

new_data = ''
for part in data.split("\n\n"):
    num, time, text = part.split("\n", 2)
    start_time, end_time = time.split(" --> ")

    new_start_time = datetime.strptime(start_time, '%H:%M:%S,%f')
    new_start_time = new_start_time + timedelta(milliseconds=N)
    new_start_time = new_start_time.strftime("%H:%M:%S,%f")[:-3]

    new_end_time = datetime.strptime(end_time, '%H:%M:%S,%f')
    new_end_time = new_end_time + timedelta(milliseconds=N)
    new_end_time = new_end_time.strftime("%H:%M:%S,%f")[:-3]

    print([num, new_start_time, new_end_time, start_time, end_time , text])

    new_data += num + "\n" + new_start_time + " --> " + new_end_time + "\n" + text + "\n\n"


print(new_data)

file = open(arguments[1].replace(".srt", "(2).srt"), "w")
file.write(new_data)
file.close()
