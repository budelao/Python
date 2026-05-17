import httpx
from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()


@app.get("/cep/{cep}")
async def buscar_cep(cep: str):
    cep = cep.replace("-", "").strip()
    if len(cep) != 8:
        raise HTTPException(status_code=400, detail="CEP inválido")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
    except httpx.RequestError:
        raise HTTPException(status_code=500, detail="Erro ao consultar CEP")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao consultar CEP")

    dados = response.json()
    if dados.get("erro"):
        raise HTTPException(status_code=404, detail="CEP não encontrado")

    return {
        "cep": dados.get("cep"),
        "logradouro": dados.get("logradouro"),
        "bairro": dados.get("bairro"),
        "cidade": dados.get("localidade"),
        "estado": dados.get("uf")
    }


lambda_handler = Mangum(app)
