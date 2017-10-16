##
# @author : Romain Francony, IT Student
# brief : publish or send message from RabbitMQ instance

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-read", action='store_true', help='Read the queues')
read = parser.parse_args().read

if read:
    execfile('simple_queue_read.py')
else:
    execfile('simple_queue_publish.py')
