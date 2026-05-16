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

## Observação

O `README.md` dentro de `lambda-pipeline/` não foi alterado. Ele já contém detalhes sobre o pipeline e como usar o projeto.

