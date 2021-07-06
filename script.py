from subprocess import call
from random import randint
from time import sleep
from collections import namedtuple

import datetime
import pytz

time_zone = pytz.timezone('Asia/Jakarta')

def delta_time(start_time, stop_time):
  delta_time = stop_time - start_time
  minute, second = divmod(delta_time.total_seconds(), 60)
  hour, minute   = divmod(minute, 60)

  return int(hour), int(minute), int(second)

lines = namedtuple('lines', ['url', 'num_pages'])

with open('mc4-domain.txt') as f:
    lines = [lines(line.rstrip().split()[0], line.rstrip().split()[1]) for line in f]

start = 100_000 # CHANGE THIS start_row_no
end = 102_000 # CHANGE THIS end_row_no

output_file_name = "./result.txt" # CHANGE THIS IF NEEDED


start_time = datetime.datetime.now(time_zone)
for i, line in enumerate(lines[start:end]):
    call("python3 chameleon.py --proxy m --check --output '"+ output_file_name + "' --domain " + line.url, shell=True)
    print(f"line : {i + start}/{end} | url: {line.url} | num_pages : {line.num_pages}")
    if i+start == end - 1:
        stop_time = datetime.datetime.now(time_zone)
        hour, minute, second = delta_time(start_time, stop_time)
        print("")
        print(f" **************  Process Finished : {end - start} samples  ************")
        print(f" **********  {hour} Hours, {minute} Minutes, {second} Seconds  ********")




