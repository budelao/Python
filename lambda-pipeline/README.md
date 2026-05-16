
# AWS Lambda Python + GitHub Actions

Exemplo de projeto com:
- AWS Lambda em Python
- Pipeline CI/CD com GitHub Actions
- Deploy automático usando AWS CLI
- Estrutura pronta para estudos

## Estrutura

```
lambda-github-pipeline-example/
├── app.py
├── requirements.txt
├── template.yaml
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md

Fazer:

lambdas/

├── api-clientes/
│   ├── app.py
│   ├── requirements.txt
│   └── template.yaml
│
├── api-pedidos/
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
