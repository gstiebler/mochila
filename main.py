import excel_reader
import knapsack

global_var = []
def main():
    [values, maxValue] = excel_reader.readExcel()

    print len(values)

    knapsack.initializeToolbs(len(values))
	
    #while len(values) > 0:
    [pop, stats, hof] = knapsack.execute(values, maxValue)
    print "hof\n"
	
    sum = 0.0
    for item in hof.items[0]:
        sum += values[item].value;
        print values[item].name
    print sum
    
main()