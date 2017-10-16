##
# @author : Romain Francony, IT Student
# brief : publish new message on the RabbitMQ instance

import pika
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-concurrency", action='store_true', help='Activate persistence')
parser.add_argument("-n", "--sendmany", type=int, default=1)
concurrency = parser.parse_args().concurrency
nb_message = parser.parse_args().sendmany

properties = None
if concurrency:
    properties = pika.BasicProperties(
        delivery_mode=2
    )

amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()

message = "Romain Francony"

channel.queue_declare(queue='presentation')

for i in xrange(nb_message):
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=message,
                          properties=properties)

    print "[x] Sent {message}".format(message=message)
connection.close()
