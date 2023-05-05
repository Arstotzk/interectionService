import pika
from config_read import Settings


class Rabbit:
    def __init__(self):
        settings = Settings()
        self.parameters = pika.URLParameters('amqp://' + settings.rabbitLogin + ':' + settings.rabbitPassword + '@' +
                                             settings.rabbitHost + ':' + str(settings.rabbitPort) + '/' +
                                             settings.rabbitVirtualHost)
        self.parameters.socket_timeout = 5
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def PutImage(self, uuid):
        self.channel.queue_declare(queue='processing_images')
        self.channel.basic_publish(exchange='mainExchange', routing_key='processing_images', body=uuid)
        self.connection.close()

    def FindParams(self, uuid):
        self.channel.queue_declare(queue='find_params_images')
        self.channel.basic_publish(exchange='mainExchange', routing_key='find_params_images', body=uuid)
        self.connection.close()
