list = []
print('Insert numbers and if you need exit input the word "stop"')

while True:
    value = input('insert your value: ')
    if value == 'stop':
        break
    else:
        try:
            value = int(value)
            list.append(value)
        except:
            print('invalid input')
            exit()
result = 0 
for n in list:
    result += n

print(result)