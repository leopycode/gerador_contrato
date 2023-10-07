# gerador_contrato

<img src="Geração de Contrato.png">

Aplicação em Python para gerar contrato de prestação de serviços em um arquivo do Microsoft Word (.docx) a partir de um modelo pré-definido.

<img src="Contrato gerado.png">

A aplicação faz uso de várias bibliotecas Python para funcionar: 
    - A biblioteca docx, que faz a edição  do modelo do arquivo e gera o arquivo final;
    - A biblioteca num2words, que converte valores numéricos e valores por extenso, inclusive moedas;
    - A bibliote locale, que converte o valor do contrato para o formado da moeda brasileira (Real R$);

Na construçao da aplicação foram agregados códigos já utilizados, e presentes nos repositórios:
    - consulta_cep, aplicação em Python, com uso de API para consulta CEP (código postal brasileiro);
    - valida_documento, código, também em Python, para consultar se um número de CPF/CNPJ é válido.

Foi importado, ainda, código utilizado para converter uma data qualquer e o dia atual para o formato por extenso utilizado no Brasil.
