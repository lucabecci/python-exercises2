#search the low number in the list
list = [3, 5, 2, 0, 22, -233, 233, -212]

low_number = 'init'

for number in list:
    if low_number == 'init':
        low_number = number
    else:
        low_number = number if number < low_number else low_number

print(low_number)