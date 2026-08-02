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
3.78541,                    #### US Gallon to Liter:       1 US Gallon =        3.78541 Liter
#### Temperature        
1                           #### Keep it 1, the forumla is too complicated
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



#### Check to see if the measure arrays are the same length
lengthCheck = len(imperial) + len(metric) + len(deltas)

if lengthCheck / 3 != len(deltas):
    print(f'Arrays needs to be equally filled (same length)')
    exit()



################################################################################################

def getInputType() -> int:
    while True:
        converterType = 0
        try:
            
            converterType = int(input('1. Imperial to metric\t 2. Metric to imperial: '))
            
            if converterType not in (1 , 2):
                converterType = int(input('Not a valid choice\n1. Imperial to metric\t 2. Metric to imperial: '))
            else:
                break

        except Exception as e:
            converterType = 0
            print(f' getInput ERROR: {e}')
        
    return converterType



def getInputNumber( converterType ):
    while True:
        try:
            inputNumber = str(input("Number to convert: ")).strip().replace(',','.')
            
            try:
                TestInputNumber = float( inputNumber )
                break

            except Exception as e:
                print(f'inputNumber conversion ERROR: {e}')

        except Exception as e:
            inputNumber = 0
            print(f'getInputNumber ERROR: {e}')
    
    return inputNumber


def extraConversions( converterType, inputNumber ):
    try:

        #### Imperial to metric multiplies
        if converterType == 1 and '.' in ( str(inputNumber) ):
            feetN           = int(inputNumber[ : inputNumber.find('.')])
            meters_feet     = feetN  * 0.3048
            inchesN         = int(inputNumber[ inputNumber.find('.')+1 :])
            centim_inches   = (inchesN / 2.54) / 10        
            exConv          = f'{feetN}ft {inchesN}in  \t to  Mt-Cm   =\t{meters_feet + centim_inches:.2f}'

            addedExtraConversion = True

        else:
            exConv = ""
            addedExtraConversion = False

    except Exception as e:
        print(f'extraConversions ERROR: {e}')

    return exConv, addedExtraConversion


################################################################################################

def main():
    try:

        arrayToPrint  = []

        converterType = getInputType()
        inputNumber = getInputNumber( converterType )
        exConv, addedExtraConversion = extraConversions( converterType, inputNumber )


        inputNumber = float( inputNumber )

        #### Imperial to metric multiplies
        if converterType == 1:

            for i in range(0, len(metric)):

                result = f'{inputNumber} {imperial[i]}\t to  {metric[i]}  =  {inputNumber * deltas[i]:.2f}'

                if imperial[i] in ("Inches","Feet","Yards","Miles"):
                    length.append(result)
                    
                elif imperial[i] in ("Pounds","Ounce"):
                    weight.append(result)

                elif imperial[i] in ("US Gallon"):
                    volume.append(result)

                elif imperial[i] in ("Fahrenheit"):
                    formulaResult = f"{float( (inputNumber -32 ) / (9/5)):.2f}"     #### °F = °C * 1.8 + 32
                    result = f'{inputNumber} {imperial[i]}\t to  {metric[i]}  =  {formulaResult}'
                    temp.append(result)
                
                else:
                    print(f'Measure error')
            
            #### Combined conversions for better usability
            if addedExtraConversion:
                length.insert(3 , exConv)



        #### Metric to imperial divides
        elif converterType == 2:
            for i in range(0, len(imperial)):

                result = f'{inputNumber} {metric[i]}\t to  {imperial[i]}  =  {inputNumber / deltas[i]:.2f}'

                if metric[i] in ("Centimeters","Meters","Meters","Kilometers"):
                    length.append(result)

                elif metric[i] in ("Kilograms","Kilograms"):
                    weight.append(result)

                elif metric[i] in ("Liter"):
                    volume.append(result)

                elif metric[i] in ("Celsius"):
                    formulaResult = f" {float(  (inputNumber * (9/5) +32 ) ):.2f}"  #### °C = (°F - 32) ÷ (9/5)    
                    result = f'{inputNumber} {metric[i]}\t to  {imperial[i]}  =  {formulaResult}'
                    temp.append(result)
                
                else:
                    print(f'Measure error')


        arrayToPrint = length + weight + volume + temp   

        for j in range(0, len(arrayToPrint)):
        
            print(f'{arrayToPrint[j]}')



    except Exception as e:
        print(f'main ERROR: {e}')



if __name__ == "__main__":
    main()