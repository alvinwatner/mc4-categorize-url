from subprocess import call

from random import randint
from time import sleep

with open('mc4-domain.txt') as f:
    lines = [line.rstrip().split()[0] for line in f]

start = 31000 # CHANGE THIS start_row_no
end = 32000 # CHANGE THIS end_row_no
output_file_name = "result.txt" # CHANGE THIS IF NEEDED

for line in lines[start:end]:
    call("python3 chameleon.py --proxy m --check --output '"+ output_file_name + "' --domain " + line, shell=True)
    sleep(randint(0,2))
