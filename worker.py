from serial import *
from datetime import datetime
import re
import time
import logging as log
from models import Entry
import config

log.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=log.ERROR,
    filename='worker.log'
)

try:
    ser = Serial(config.workerCOMport, 19200, timeout=0, writeTimeout=0)
except ValueError:
    log.critical('Wrong argument passed')
    sys.exit(1)
except SerialException:
    log.critical('Cannot found or configure COM port')
    sys.exit(1)

find_nums = re.compile(r'([\+\-]?[0-9]+)')

while True:
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    try:
        ser.write('ATC.\r\n'.encode())
    except SerialTimeoutException:
        log.error('Write timed out')
        continue

    ans = st = ''
    read_success = True
    start = datetime.now()
    while st != 'OK\r\n':
        try:
            st = ser.readline().decode()
        except UnicodeDecodeError:
            log.error('Cannot decode output of device')
            read_success = False
            break

        if (datetime.now() - start).seconds > config.workerReadTimeout:
            log.error('Read timed out')
            read_success = False
            break

        if st != '':
            ans += st

    if read_success:
        ans = ans.replace('\n', '').replace('\r', '')
        match = [int(float(i)) for i in find_nums.findall(ans)[4:]]

        Entry.create(
            time=time.time(),
            inner_temperature=match[0],
            outer_temperature=match[1],
            pressure=match[2],
            humidity=match[3],
            wind_speed=match[4],
            wind_direction=match[5]
        )

        time.sleep(config.workerPeriod)
