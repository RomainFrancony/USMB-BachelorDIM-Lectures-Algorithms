##
# @author : Romain Francony, IT Student
# brief : send message to subscriber and sent sign in to the monitoring service

import pika
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-signin", "--signin", type=str, default=False)
parser.add_argument("-message", "--message", type=str, default=False)
login = parser.parse_args().signin
message = parser.parse_args().message

# setup connection to AMQP
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)

# user wants to sign in
if login is not False:
    # Check user entered a login
    if login == '':
        raise ValueError('Invalid login')

    channel = connection.channel()

    channel.queue_declare(queue='presentation')

    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=login)

    print "[x] Signing in with login : {message}".format(message=login)

# user wants to send a message
if message is not False:
    # Check user entered a login
    if message == '':
        raise ValueError('Invalid message')

    channel = connection.channel()

    # create exchange channel
    channel.exchange_declare(exchange='posts',
                             exchange_type='fanout')
    # publish the message
    channel.basic_publish(exchange='posts',
                          routing_key='',
                          body=message)

    print "[x] Send message : {message}".format(message=message)

# read all the message on the post channel
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
