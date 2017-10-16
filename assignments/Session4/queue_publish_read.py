##
# @author : Romain Francony, IT Student
# brief : publish or send message from RabbitMQ instance

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-read", action='store_true', help='Read the queues')
parser.add_argument("-concurrency", action='store_true', help='Activate concurrency with 100 messages send')
read = parser.parse_args().read
concurrency = parser.parse_args().concurrency

if concurrency:
    # create one sender with 100 messages
    os.system("py -2 simple_queue_publish.py -concurrency -n 100")
    # create 2 readers
    os.system("py -2 simple_queue_read.py -concurrency")
    os.system("py -2 simple_queue_read.py -concurrency")
elif read:
    execfile('simple_queue_read.py')
else:
    execfile('simple_queue_publish.py')
