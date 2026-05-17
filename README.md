# Repositório Python

Este repositório contém exemplos de aplicações Python para AWS Lambda organizadas em `lambda-pipeline`.

## Estrutura do projeto

- `lambda-pipeline/`
  - `api-estados-mysql/`
  - `api-externa/`

## APIs já implementadas em `lambda-pipeline`

### 1. `api-estados-mysql`

- Função AWS Lambda em Python.
- Conecta em um banco MySQL usando `pymysql`.
- Recupera registros da tabela `tb_estados`.
- Retorna lista de estados como JSON.
- Principais arquivos:
  - `app.py`
  - `requirements.txt`
  - `template.yaml`

### 2. `api-externa`

- Função AWS Lambda em Python.
- Faz chamada externa para a API WeatherAPI.
- Busca dados de clima para Paris em português.
- Usa `requests` para fazer a requisição HTTP.
- Principais arquivos:
  - `app.py`
  - `requirements.txt`
  - `template.yaml`

### 3. `api-externa-com-fastapi`

- Função AWS Lambda em Python.
- Usa `FastAPI` com `Mangum` para integração com o SAM.
- Consulta a API pública ViaCEP para buscar dados de CEP.
- Principais arquivos:
  - `app.py`
  - `requirements.txt`
  - `template.yaml`

### 4. `producer-rabbit-mq`

- Função AWS Lambda em Python.
- Faz um envio para RabbitMQ.
- Principais arquivos:
  - `app.py`
  - `requirements.txt`
  - `template.yaml`
  - `services\rabbit_service.py`

  ### 4. `consumer-rabbit-mq`

- Função AWS Lambda em Python.
- Faz leitura de mensagem RabbitMQ.
- Principais arquivos:
  - `app.py`
  - `requirements.txt`
  - `template.yaml`
  - `services\rabbit_service.py`