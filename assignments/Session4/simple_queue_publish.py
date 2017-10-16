##
# @author : Romain Francony, IT Student
# brief : publish new message on the RabbitMQ instance

import pika
import os

amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()

message = "Romain Francony"

channel.queue_declare(queue='presentation')
channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body=message)

print "[x] Sent {message}".format(message=message)
connection.close()
