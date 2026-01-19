# Gerador de Certificados em PDF

Este projeto tem como objetivo gerar certificados em PDF de forma automatizada a partir de uma planilha CSV contendo os dados dos participantes.

O script utiliza um arquivo PDF base (template) e insere dinamicamente informações como nome e matrícula em posições específicas do documento, gerando um certificado individual para cada participante.

---

## Tecnologias utilizadas

- Python 3
- Pandas
- ReportLab
- PyPDF

---

## Estrutura do projeto

```text
gerador-certificados-pdf/
├── src/
│   └── main.py
├── data/
│   └── alunos.csv
├── templates/
│   └── template.pdf
├── output/
│   └── certificados_gerados/
├── requirements.txt
├── README.md
├── LICENSE.txt
└── .gitignore
````
---

## Como funciona

1. Os dados dos participantes são lidos a partir de um arquivo CSV.
2. Um PDF de sobreposição (overlay) é criado com os textos dinâmicos.
3. O overlay é mesclado com o PDF base (template).
4. Um certificado em PDF é gerado para cada participante.

---

## Formato do arquivo CSV

O arquivo CSV deve conter as seguintes colunas:
- `Aluno`: nome completo do participante
- `Matricula`: identificador do participante (tratado como texto para preservar zeros à esquerda)

```csv
Aluno,Matricula
Exemplo de Aluno Um,000123
Exemplo de Aluno Dois,987654
```
---

## Como executar o projeto
1. Clone este repositório

```bash
git clone <url-do-repositorio>
```
2. (opcional, mas recomendado) Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
Os certificados gerados serão salvos automaticamente na pasta output/.

---

## Observações

O posicionamento dos textos no certificado pode ser ajustado diretamente no código, alterando as coordenadas utilizadas no overlay.

O template do certificado pode ser substituído por qualquer outro arquivo PDF, desde que o layout seja compatível com as posições definidas.

O arquivo CSV deve conter as colunas Aluno e Matricula, conforme descrito neste repositório.

Este projeto foi desenvolvido com fins educacionais e de aprendizado em automação de documentos com Python.

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE.txt) para mais detalhes.