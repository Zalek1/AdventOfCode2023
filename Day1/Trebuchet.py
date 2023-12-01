def spelledToInt(spelled):
    match spelled:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9
        case _:
            return 0
        
input = open("input.txt","r")
sum = 0
for line in input:
    digit = []
    index = 0
    for char in line:
        if(char.isdigit()):
            digit.append(char)
        else:
            for count in range(6):
                if(count > 2):
                    if(index+count <= len(line)):
                        if(spelledToInt(line[index:index+count]) != 0):
                            digit.append(spelledToInt(line[index:index+count]))
        index += 1
            

    if(digit):
        number = str(digit[0]) + str(digit[len(digit)-1])
        print(number)
        sum += int(number)
print(sum)