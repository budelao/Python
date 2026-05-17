import json
import pika
from pika.exceptions import (
    AMQPConnectionError,
    ChannelClosedByBroker,
    AMQPChannelError
)

def callback(ch, method, properties, body):

    try:

        print("Mensagem recebida do RabbitMQ")

        mensagem = json.loads(body)

        print(f"Conteúdo: {mensagem}")

        print("Processando mensagem...")

        # regra de negócio aqui

        print("Mensagem processada com sucesso")

        ch.basic_ack(
            delivery_tag=method.delivery_tag
        )

        print("ACK enviado")

    except Exception as e:

        print(f"Erro ao processar mensagem: {str(e)}")

def consumir_mensagens():

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
                    host='localhost',
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

        print("Registrando consumer...")

        try:

            channel.basic_consume(
                queue='fila_pedidos',
                on_message_callback=callback
            )

            print("Consumer registrado com sucesso")

        except Exception as e:

            print(f"Erro ao registrar consumer: {str(e)}")
            raise

        print("Aguardando mensagens...")

        try:

            channel.start_consuming()

        except KeyboardInterrupt:

            print("Consumer interrompido manualmente")

        except Exception as e:

            print(f"Erro durante consumo: {str(e)}")
            raise

    except Exception as e:

        print(f"Erro geral RabbitMQ Consumer: {str(e)}")
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