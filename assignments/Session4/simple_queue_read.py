##
# @author : Romain Francony, IT Student
# brief : read new messages from the RabbitMQ instance

import pika
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-concurrency", action='store_true', help='Activate persistence')
concurrency = parser.parse_args().concurrency

amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')

counter = 0


def callback(ch, method, properties, body):
    global counter
    global concurrency
    counter = counter + 1
    print "[x] Received message : {message}\nTotal of {count} message(s)".format(message=body, count=counter)
    if concurrency:
        ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='presentation',
                      no_ack=not concurrency)

print "[x] Waiting for messages. To exit press Ctrl+C"
channel.start_consuming()
