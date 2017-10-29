##
# @author : Romain Francony, IT Student
# brief : publish message to subscribers with fanout exchange

import pika
import os

# setup AMQP connection
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()


message = "Hello subscribers"

# create exchange channel
channel.exchange_declare(exchange='posts',
                         exchange_type='fanout')
# publish the message
channel.basic_publish(exchange='posts',
                      routing_key='',
                      body=message)

print "[x] Sent {message}".format(message=message)
connection.close()
