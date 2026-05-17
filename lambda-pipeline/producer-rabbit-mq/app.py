from services.rabbit_service import enviar_mensagem

def lambda_handler(event, context):

    mensagem = {
        "pedido_id": 123,
        "cliente": "Ivan"
    }

    enviar_mensagem(mensagem)

    return {
        "statusCode": 200
    }