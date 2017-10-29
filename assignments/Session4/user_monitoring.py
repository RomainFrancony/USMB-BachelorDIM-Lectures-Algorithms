##
# @author : Romain Francony, IT Student
# brief : monitor user signing in to the exchange

import pika
import os

# setup AMQP connection
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')

subscribers = []


def callback(ch, method, properties, body):
    global subscribers

    # subscriber already exists
    if body in subscribers:
        print "[x] {login} is already registered".format(login=body)
        return

    # new subscriber
    subscribers.append(body)
    print "[x] New subscriber {message}\nTotal of {count} subscriber(s)".format(message=body, count=len(subscribers))
    for user in subscribers:
        print "\t - {user}".format(user=user)


channel.basic_consume(callback,
                      queue='presentation',
                      no_ack=True)

print "[x] Waiting for new subscriber. To exit press Ctrl+C"
channel.start_consuming()
