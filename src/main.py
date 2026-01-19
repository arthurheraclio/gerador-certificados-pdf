import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, landscape
from pypdf import PdfReader, PdfWriter
import os

OUTPUT_DIR = "../output/certificados_gerados"
os.makedirs(OUTPUT_DIR, exist_ok=True)

tabela = pd.read_csv("../data/alunos.csv")
print(tabela)

#posicoes
pos_nome_x = 370
pos_nome_y = 353
pos_matricula_x = 260
pos_matricula_y = 326

def gerar_certificado(nome, matricula):

    overlay_pdf = canvas.Canvas("overlay.pdf", pagesize=landscape(A4))
    overlay_pdf.setFillColorRGB(0, 0, 0)
    overlay_pdf.setFont("Times-Roman", 16)
    overlay_pdf.drawString(pos_nome_x, pos_nome_y, f"{nome}")
    overlay_pdf.drawString(pos_matricula_x, pos_matricula_y, f"{matricula}")

    overlay_pdf.save()
    base = PdfReader("../templates/template.pdf")

    overlay = PdfReader("overlay.pdf")

    writer = PdfWriter()

    pagina_base = base.pages[0]
    pagina_overlay = overlay.pages[0]

    pagina_base.merge_page(pagina_overlay)

    writer.add_page(pagina_base)

    with open(f"{OUTPUT_DIR}/Certificado {nome}.pdf", "wb") as f:
        writer.write(f)

for row in tabela.itertuples():
    nome = row.Aluno
    matricula = row.Matricula
    gerar_certificado(nome, matricula)


