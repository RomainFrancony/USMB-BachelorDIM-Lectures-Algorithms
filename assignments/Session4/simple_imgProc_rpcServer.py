##
# @author : Romain Francony, IT Student
# brief : Receive and respond process image with rpc

import pika
import os
import msgpack
import msgpack_numpy as m
import sys

sys.path.insert(0, '../Session3')
import S3_imgproc_tools as image_process
import numpy as np

# Setup connection
amqp_url = "amqp://taumfzlk:P1gefgPdpz3UKtJ7aivorzL8tzpMALuX@lark.rmq.cloudamqp.com/taumfzlk"
url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

# Available filters list
filters_dictionary = {'invert': image_process.invert_colors_opencv, 'threshold': image_process.threshold_colors_opencv}


def process_image(img, filter):
    ##
    # Apply a filter on an image
    # @param img to filter
    # @filter filter to apply on the image

    # check if the input is a numpy array
    if not isinstance(img, (np.ndarray, np.generic)):
        return {'error': 'Image is not a numpy array'}

    # check if filter exist
    if not filter in filters_dictionary:
        return {'error': 'Unknown filter'}

    return filters_dictionary[filter](img)


def on_request(ch, method, props, body):
    ##
    # Response to the client
    # @param ch
    # @params method
    # @params props
    # @params body
    request = str(body)
    decoded_message = msgpack.unpackb(request, object_hook=m.decode)

    print 'Request received'
    # check if request if properly formated
    if ('filter_type' in decoded_message) and ('image' in decoded_message):
        # Process the image and encode it for response
        response = process_image(decoded_message['image'], decoded_message['filter_type'])
    else:
        response = {'error': 'Request not properly formated'}

    encoded_response = msgpack.packb(response, default=m.encode)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=str(encoded_response))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print 'Sending response'


# setup channel
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

# wait for requests
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
print('Starting to wait for the client request')
channel.start_consuming()
