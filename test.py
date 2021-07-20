#!/usr/bin/python3
import schedule
import sys
import zphs01b
import time


import time
import sys
import schedule
import json
import datetime
import os, time
import schedule
import sys
import requests
import csv
import socket    
import os
import smtplib
from datetime import datetime
import logging
import logging.config
import datetime


##############################Time delay ####################
EVERY_SECONDS1 = 2;


# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs_1_2.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter(' %(message)s')
f_format = logging.Formatter(' %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)



def sendemail():


    readout = zphs01b.read_all()
    print('temp:'  + str(readout['temperature']))
    print("voc:" + str(readout['voc']))
    print("rh:"  + str(readout['rh']))
    print("ch2o:" +  str(readout['ch2o']))
    print("co:" + str(readout['co']))
    print("o3:" + str(readout['o3']))
    print("no2:"  + str(readout['no2']))
    print("co2:" + str(readout['co2']))
    print("pm10:"  + str(readout['pm10']))
    print("pm2.5:"  +  str(readout['pm2.5']))
    print("pm1.0:"    + str(readout['pm1.0']))

    logger.error([ readout ])




#define timming  function
def main(argv):

   # print("====================== Starting Poulta  Process ======================");
    schedule.every(EVERY_SECONDS1).seconds.do(sendemail);  
    



    while True:

         schedule.run_pending()

         time.sleep(5)
         print("====================== Shutting down Poulta Process ======================");
 
   
if __name__ == "__main__":
    main(sys.argv)