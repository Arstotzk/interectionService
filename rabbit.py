import pika

class Rabbit:
    def __init__(self):
        self.parameters = pika.URLParameters('amqp://service:service@localhost:5672/main')
        self.parameters.socket_timeout = 5
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def PutImage(self):
        self.channel.queue_declare(queue='processing_images')
        self.channel.basic_publish(exchange='mainExchange', routing_key='processing_images', body='test_image')
        self.connection.close()
