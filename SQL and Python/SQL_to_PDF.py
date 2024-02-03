#pip install fpdf
#pip install fpdf
import pyodbc
from fpdf import FPDF
SERVER = input("Please Enter the Server name or ip and port number in the form (IP:PORT): ")
DATABASE = input("Please Enter the database name: ")

connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes')

cursor = connection.cursor()
cursor.execute('select * from sales.order_items;')

result = cursor.fetchall()

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 12)
for column in cursor.description:
    pdf.cell(30,10,column[0],border=1)
pdf.ln()

pdf.set_font('Arial','',10)
for row in result:
    for string in row:
        pdf.cell(30,10,str(string),border=1)
    pdf.ln()

pdf.output('result.pdf','F')
