from services.rabbit_service import consumir_mensagens

def main():

    print("Iniciando consumer...")

    consumir_mensagens()

if __name__ == "__main__":
    main()