
from multiprocessing import Pool

def aggregateodds(filename):
    try:
        sumofodds = 0
        exclude = [0,1]
        with open(filename,'r') as file:
            element = int(file.next()) # Gets the first element in the file. A for-loop works just as well.
            while True:
                if element not in exclude:
                    if element%2!=0:
                        sumofodds = sumofodds + element
                        element = int(file.next())
                    else:
                        element = int(file.next())
                else:
                    element = int(file.next())
    except Exception as e:
        return sumofodds

      
if __name__ == '__main__':
    p = Pool(3)
    multi_result = (p.map(aggregateodds,['two.txt','eleven.txt','five.txt']))
    Result = reduce(lambda x,y: x+y,[x*2 for x in multi_result])
    print Result



