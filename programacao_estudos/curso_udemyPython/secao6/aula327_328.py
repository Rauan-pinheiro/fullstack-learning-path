# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from pypdf import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAL = PASTA_RAIZ.parent / "secao6" /"pdf_original_aula327"
NOVA_PASTA = PASTA_RAIZ / "arquivos_novos"

RELATORIO_BACEN = PASTA_ORIGINAL / "R20230210.pdf"

# NOVA_PASTA.mkdir(parents=True, exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print()
    
page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
print(page0.images[0])

# with open(NOVA_PASTA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)
    
writer = PdfWriter()
writer.add_page(page0)

with open(NOVA_PASTA / "page0.pdf", 'wb') as arquivo:
    writer.write(arquivo)
    