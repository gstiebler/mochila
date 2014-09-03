import xlrd
import math

class Value:

	def __init__(self, name, value):
		self.name = name
		self.value = value

def readExcel():
	book = xlrd.open_workbook("entrada.xls")
	print "The number of worksheets is", book.nsheets
	print "Worksheet name(s):", book.sheet_names()
	sh = book.sheet_by_index(0)
	print sh.name, sh.nrows, sh.ncols

	values = []

	for rx in range(sh.nrows):
		values.append(Value(sh.cell_value(rowx=rx, colx=0), sh.cell_value(rowx=rx, colx=1)))
		
	return values, sh.cell_value(rowx=0, colx=3)
