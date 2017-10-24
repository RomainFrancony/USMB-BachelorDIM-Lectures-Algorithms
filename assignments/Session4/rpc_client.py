##
# @author : Romain Francony, IT Student
# brief : Send rpc message and wait for the server's response

import os
import pika
import uuid
import msgpack
import msgpack_numpy as m

# Setup connection
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

# Declare channel
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

# Generate uid and message to send
corr_id = str(uuid.uuid4())

request_msg = {'type': 0, 'value': 'hi, how fine?'}
encoded_message = msgpack.packb(request_msg, default=m.encode)

# Send message
channel.basic_publish(exchange='',
                      routing_key='rpc_queue',
                      properties=pika.BasicProperties(
                          reply_to=callback_queue,
                          correlation_id=corr_id, ),
                      body=encoded_message)

print 'Question : {question}'.format(question=request_msg['value'])
response = None


def on_response(ch, method, props, body):
    ##
    # Callback for the response
    # @param ch
    # @params method
    # @params props
    # @params body

    # Check if the client ID is the same
    if corr_id == props.correlation_id:
        global response

        response = msgpack.unpackb(str(body), object_hook=m.decode)
        print 'Response : {rep}'.format(rep=response['value'])
    else:
        raise ValueError('Correlation ID is not the same')


print('Starting to wait on the response queue')
channel.basic_consume(on_response, no_ack=True, queue=callback_queue)

# wait for an answer from the server
while response is None:
    connection.process_data_events()
connection.close()
