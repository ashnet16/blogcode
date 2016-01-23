def write_five():
    x = 0
    while x < 500000000:
        x = x + 11
        yield x

	
    
number = write_five()
with open('eleven.txt','w') as five:
    for num in number:
        five.write(str(num)+'\n')
        
    


