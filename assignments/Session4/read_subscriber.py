##
# @author : Romain Francony, IT Student
# brief : simple fanout publish read

import pika
import os

# setup connection
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()


# function called when receiving a new message
def callback(ch, method, properties, body):
    print "[x] Received message : {message}".format(message=body)


# connect to the channel
channel.exchange_declare(exchange='posts',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='posts',
                   queue=queue_name)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print "[x] Waiting for messages. To exit press Ctrl+C"
channel.start_consuming()
