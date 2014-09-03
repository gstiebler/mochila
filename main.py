import excel_reader
import knapsack

global_var = []
def main():
    [values, maxValue] = excel_reader.readExcel()

    print len(values)
	
    for value in values:
        print value.name
        print value.value
		
        print maxValue
	
    [pop, stats, hof] = knapsack.execute(values, maxValue)
    print "pop\n"
    print pop
    print "stats\n"
    print stats
    print "hof\n"
    print str(hof.items[0])
    
    print dir(hof.items[0])
    
    sum = 0.0
    for item in hof.items[0]:
        sum += values[item].value;
    print sum
    
main()