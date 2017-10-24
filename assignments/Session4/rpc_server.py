##
# @author : Romain Francony, IT Student
# brief : Receive and respond to rpc message

import pika
import os

# Setup connection
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)


def on_request(ch, method, props, body):
    ##
    # Response to the client
    # @param ch
    # @params method
    # @params props
    # @params body
    request = str(body)
    print 'Receiving request : {request}'.format(request=request)
    response = 'Fine and you ?'
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print 'Sending response : {response}'.format(response=response)


# setup channel
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

# wait for requests
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
print('Starting to wait for the client request')
channel.start_consuming()
