import excel_reader

def main():
	values = excel_reader.readExcel()

	print len(values)
	
	for value in values:
		print value.name
		print value.value
		
main()