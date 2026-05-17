
# AWS Lambda Python + GitHub Actions

Exemplo de projeto com:
- AWS Lambda em Python
- Pipeline CI/CD com GitHub Actions
- Deploy automático usando AWS CLI
- Estrutura pronta para estudos

## Estrutura

```

lambdas/

├── api-estados-mysql/
│   ├── app.py
│   ├── requirements.txt
│   └── template.yaml
│
├── api-externa/
│   ├── app.py
│   ├── requirements.txt
│   └── template.yaml
│
├── api-externa-com-fastapi/
│   ├── app.py
│   ├── requirements.txt
│   └── template.yaml
│
├── processador-sqs/
│   ├── app.py
│   └── requirements.txt
│
├── processador-imagens/
│   ├── app.py
│   └── requirements.txt
│
└── scheduler-notificacoes/
    ├── app.py
    └── requirements.txt

Visual Studio Code
Python 3.11+
AWS Toolkit
AWS SAM CLI
Docker Desktop

```

## API externa com FastAPI

A pasta `api-externa-com-fastapi/` agora contém uma Lambda que usa FastAPI e `Mangum` para integrar com o SAM.

Como testar localmente:

```bash
cd api-externa-com-fastapi
sam build --template template.yaml
sam local start-api --template template.yaml --port 3000
curl http://127.0.0.1:3000/cep/01310100
```

O endpoint retorna os dados de CEP usando a API pública ViaCEP.

## Como funciona a esteira

1. Você faz push no GitHub
2. O GitHub Actions dispara automaticamente
3. O pipeline:
   - Instala dependências
   - Executa testes
   - Gera pacote ZIP
   - Faz deploy da Lambda

## Secrets necessários no GitHub

Vá em:
Settings -> Secrets and variables -> Actions

Crie:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION

## Criar Lambda

Exemplo:

```bash
aws lambda create-function           --function-name minha-lambda-python           --runtime python3.11           --role arn:aws:iam::123456789:role/lambda-role           --handler app.lambda_handler           --zip-file fileb://lambda.zip
```
