from docx import Document
from num2words import num2words
from datas_extenso import hoje, data_formatada
import locale
from documento import DocCpf
import requests

hoje = hoje()
contrato = Document("modelo_contrato_2.docx")

print("\n\033[1m{:=^60} \033[m".format(" Sistema de Geração de Contrato "))
print("\n\033[1m{:=^60} \033[m".format(" Insira os dados do Cliente "))


nome_cliente = str(input("\nNome do Cliente: ")).strip().upper()
data = str(input("Data de Nascimento: "))
data_nasc = data_formatada(data)

doc = str(input("CPF do cliente: "))
cpf = DocCpf(doc)
cpf_cliente = str(cpf)

cep = str(input("CEP do cliente: "))
consulta_cep = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
consulta_cep = consulta_cep.json()
cep_consultado = consulta_cep["cep"]
cep_formatado = f"{cep_consultado[0:2]}.{cep_consultado[2:5]}-{cep_consultado[5:8]}"
endereco = consulta_cep["address"]
print(f"Logradouro: {endereco}")
num = str(input("Número: "))
complemento = str(input("Complemento: "))
bairro = consulta_cep["district"]
cidade = consulta_cep["city"]
estado = consulta_cep["state"]
print(f"Bairro: {bairro}")
print(f"Cidade: {cidade} - UF: {estado}")

valor = float(input("Valor do Contrato: R$ "))
locale.setlocale(locale.LC_MONETARY, "pt_BR")
valor_contrato = locale.currency(valor, grouping=True)
valor_ext = num2words(valor, lang="pt_BR", to="currency")

dados_contrato = {
    "nome_cliente" : nome_cliente,
    "cpf_cliente" : cpf_cliente,
    "data_nasc" : data_nasc,
    "cep" : cep_formatado,
    "endereco" : endereco,
    "numero" : num,
    "complemento" : complemento,
    "bairro" : bairro,
    "cidade" : cidade,
    "uf" : estado,
    "valor_contrato" : valor_contrato,
    "valor_ext" : valor_ext,
    "data_hoje" : hoje
}

for p in contrato.paragraphs:
    for c in dados_contrato:
        p.text = p.text.replace(c, dados_contrato[c])

contrato.save(f"Contrato {nome_cliente}.docx")
print("\n\033[1m{:=^60} \033[m".format(" Contrato gerado com sucesso "))
