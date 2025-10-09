import PyPDF2 as pyp
import os

merger = pyp.PdfFileMerger()
# merger.append('ex1.pdf')
# merger.append('ex2.pdf')
# merger.append('ex3.pdf')
listas_arquivos = os.listdir('pdf_mesclar') # nome da pasta)

for arquivo in listas_arquivos:
    if '.pdf' in arquivo:    
        merger.append(f'pdfs_mesclar/{arquivo}')

    
merger.write('pdf-final.pdf')


