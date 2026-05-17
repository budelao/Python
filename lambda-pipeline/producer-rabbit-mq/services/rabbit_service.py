import json
import pika
from pika.exceptions import (
    AMQPConnectionError,
    ChannelClosedByBroker,
    AMQPChannelError
)

def enviar_mensagem(mensagem):

    connection = None
    channel = None

    try:

        print("Criando credenciais...")

        credentials = pika.PlainCredentials(
            'guest',
            'guest'
        )

        print("Criando conexão RabbitMQ...")

        try:

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='rabbitmq',
                    port=5672,
                    virtual_host='/',
                    credentials=credentials
                )
            )

            print("Conexão criada com sucesso")

        except AMQPConnectionError as e:

            print(f"Erro de conexão RabbitMQ: {str(e)}")
            raise

        print("Criando channel...")

        try:

            channel = connection.channel()

            print("Channel criado com sucesso")

        except AMQPChannelError as e:

            print(f"Erro ao criar channel: {str(e)}")
            raise

        print("Declarando queue...")

        try:

            channel.queue_declare(
                queue='fila_pedidos'
            )

            print("Queue declarada com sucesso")

        except ChannelClosedByBroker as e:

            print(f"Erro ao declarar queue: {str(e)}")
            raise

        print("Publicando mensagem...")

        try:

            channel.basic_publish(
                exchange='',
                routing_key='fila_pedidos',
                body=json.dumps(mensagem)
            )

            print("Mensagem enviada com sucesso")

        except Exception as e:

            print(f"Erro ao publicar mensagem: {str(e)}")
            raise

    except Exception as e:

        print(f"Erro geral RabbitMQ: {str(e)}")
        raise

    finally:

        print("Fechando recursos...")

        try:

            if channel and channel.is_open:
                channel.close()
                print("Channel fechado")

        except Exception as e:

            print(f"Erro ao fechar channel: {str(e)}")

        try:

            if connection and connection.is_open:
                connection.close()
                print("Conexão fechada")

        except Exception as e:

            print(f"Erro ao fechar conexão: {str(e)}")