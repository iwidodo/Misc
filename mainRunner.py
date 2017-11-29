temperatures=[10,-20,-289,100]
convertedTemps=[]
finalValues = open("storedValues.txt" , 'w')

def tempConverter(temperatures):
    for value in temperatures:
        if value > -273.25:
            value = value*1.8 + 32
            convertedTemps.append(value)
            finalValues.write(str(value)+"\n") 
    
    print(convertedTemps)
    finalValues.close()

tempConverter(temperatures) #Call Method