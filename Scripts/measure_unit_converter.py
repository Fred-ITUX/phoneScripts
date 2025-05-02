



imperial = [
#### Length
"Inches",
"Feet",
"Yards",
"Miles",
#### Weight
"Pounds",
"Ounce",
#### Volume
"US Gallon",
#### Temperature
"Fahrenheit"
]

deltas = [
#### Length             
2.54,                       #### Inches to Centimeters:    1 inch =             2.54 centimeters
0.3048,                     #### Feet to Meters:           1 foot =             0.3048 meters
0.9144,                     #### Yards to Meters:          1 yard =             0.9144 meters
1.60934,                    #### Miles to Kilometers:      1 mile =             1.60934 kilometers
#### Weight                         
0.453592,                   #### Pounds to Kilograms:      1 pound =            0.453592 kilograms
0.0283495,                  #### Ounce to Kilograms:       1 ounce =            0.0283495 
#### Volume                     
3.78541,                     #### US Gallon to Liter:       1 US Gallon =        3.78541 Liter
#### Temperature        
-17.22                      #### Fahrenheit to Celsius:    1 Fahrenheit =       -17.22
]


metric = [
#### Length
"Centimeters",
"Meters",
"Meters",
"Kilometers",
#### Weight
"Kilograms",
"Kilograms",
#### Volume
"Liter",
#### Temperature
"Celsius"
]



length = ["\n📏  Length"]
weight = ["\n⚖️  Weight"]
volume = ["\n💧  Volume"]
temp   = ["\n🌡️  Temperature"]

arrayToPrint  = []



#### Check to see if the measure arrays are the same length
lentghCheck = len(imperial) + len(metric) + len(deltas)

if lentghCheck / 3 != len(deltas):
    print(f'Arrays needs to be equally filled (same length)')
    exit()



################################################################################################

converterType = str(input('1. Imperial to metric\t 2. Metric to imperial: ')).strip()
        
while True:
    try:

        if converterType not in ("1" , "2"):
            converterType = str(input('Not valid choice\n1. Imperial to metric\t 2. Metric to imperial: ')).strip()
        
        else:
            break

    except Exception as e:
        print(f'Error: {e}')






while True:
    try:

        inputNumber   = str(input("Number to convert: ")).strip().replace(',','.')

        valueCheck = float(inputNumber)

        if float(inputNumber) != valueCheck  :
            print(f'{inputNumber} != {float(inputNumber)}')

        else:
            inputNumber = float(inputNumber)
            break

    except Exception as e:
        print(f'Error: {e}')



################################################################################################


#### Imperial to metric multiplies
if converterType == "1":
    for i in range(0, len(metric)):

        result = f'{inputNumber} {imperial[i]}\t to  {metric[i]}  =  {inputNumber * deltas[i]}'

        if imperial[i] in ("Inches","Feet","Yards","Miles"):
            length.append(result)
            
        elif imperial[i] in ("Pounds","Ounce"):
            weight.append(result)

        elif imperial[i] in ("US Gallon"):
            volume.append(result)

        elif imperial[i] in ("Fahrenheit"):
            temp.append(result)

        else:
            print(f'Measure error')


#### Metric to imperial divides
elif converterType == "2":
    for i in range(0, len(imperial)):

        result = f'{inputNumber} {imperial[i]}\t to  {metric[i]}  =  {inputNumber * deltas[i]}'

        if metric[i] in ("Centimeters","Meters","Meters","Kilometers"):
            length.append(result)


        elif metric[i] in ("Kilograms","Kilograms"):
            weight.append(result)


        elif metric[i] in ("Liter"):
            volume.append(result)


        elif metric[i] in ("Celsius"):
            temp.append(result)

        else:
            print(f'Measure error')

else:
    print(f'Type error')
    exit() 


################################################################################################


arrayToPrint = length + weight + volume + temp   

for j in range(0, len(arrayToPrint)):
   
    print(f'{arrayToPrint[j]}')



