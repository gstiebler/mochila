import excel_reader
import knapsack

global_var = []
def main():
    [values, maxValue] = excel_reader.readExcel()

    print len(values)

    knapsack.initializeToolbs(len(values))

    file = open("output.txt", "w")

    file.write("hello world in the new file\n")


	
    while len(values) > 0:
        [pop, stats, hof] = knapsack.execute(values, maxValue)
        
        sum = 0.0
        hof_items = []
        for item in hof.items[0]:
            sum += values[item].value;
            file.write(values[item].name + "\n")
            hof_items.append(item)
        file.write(str(sum) + "\n")
        hof_items.sort(reverse=True)
        for item in hof_items:
            values.pop(item)
        
    file.close()
    
main()