from pdfreader import PDFDocument, SimplePDFViewer
from tabula import read_pdf
import camelot
import pandas
def readPDF(name):
    file_name = 'fernanda.pdf'
    tables = camelot.read_pdf(file_name)
    columns = {'0':'Dt Liq', '1':'Código ID', '2':'Par', '3':'Nº Doc Liq', '4':'Conta', '5':'Entradas', '6':'Saídas', '7':'Saldo'}
    tables[0].df.rename(columns=columns)
    tables[0].df.to_csv('fernanda.csv', encoding='utf-8', index=False)
if __name__ == "__main__":

    readPDF('ITAU - CARLOS GOMES')