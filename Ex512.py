count = 0
average = 0
total = 0
minimal = None
maximal = None
while True:
    num = input('Please enter a digital number: ')
    if num == 'done':
        break
    else:
        try:
            total += int(num)
            count += 1
            average = total / count
            if minimal is None:
                minimal = num
            elif num < minimal:
                minimal = num
            if maximal is None:
                maximal = num
            elif num > maximal:
                maximal = num
        except ValueError:
            print ('wrong data please enter digital number: ')
    print ("Number: ", num)
print ('Total : ', total)
print ('Average : ', average)  
print ('Maximum : ', maximal)
print ('Minimum : ', minimal)          
print ('Done!')
