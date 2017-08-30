#! coding: utf-8

# Ask the user to input the day of the week
day = input('Enter the day of the week')
print('You entered:', day)


day = raw_awinput('Enter the day of the week2')
print('You entered:', day)

# Ask the user to input the number of knights
num_knights = int(input('Enter the number of knights'))

#User enters , but it comes in as text
print('You entered:', num_knights) 
if num_knights < 3 or day == 'Monday':
    print('Retreat!')


# Battle Rules
num_knights = int(input('How many knights?')) 
day = input('What day is it?'))
if num_knights < 3 or day == 'Monday': 
    print('Retreat!')
elif num_knights >= 10 and day == 'Wednesday': 
    print('Trojan Rabbit!')
else: 
    print('Truce?')


# Battle Rules
num_knights = int(input('Enter number of knights') 
day = input('Enter day of the week')
enemy = input('Enter type of enemy')
if enemy == 'killer bunny': 
    print('Holy Hand Grenade!')
else:
# Original Battle Rules
if num_knights < 3 or day == 'Monday': 
    print('Retreat!')
if num_knights >= 10 and day == 'Wednesday': 
    print('Trojan Rabbit!')
else: print('Truce?')