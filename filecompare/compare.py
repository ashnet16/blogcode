
with open('two.txt','r') as num_two, open('five.txt','r') as num_five, open('common.txt','w+') as common:
    two = int(num_two.next())
    five = int(num_five.next())
    while True:
        if two == five:
            common.write(str(two) + '\n')
            two = int(num_two.next())
            five = int(num_five.next())
        elif two < five:
            two = int(num_two.next())

        elif two > five:
            five = int(num_five.next())













