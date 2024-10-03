

def FizzBuzz(start, finish):
    outlist = []
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append("fizzbuzz")
        elif i % 3 == 0:
            outlist.append("fizz")
        elif i % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(i)
    return outlist

####
def FizzBuzz(start, finish):
    out = []
    for i in range(start, finish+1):
        if i%15 == 0:
            out.append('FizzBuzz')
        elif i%3 == 0:
            out.append('Fizz')
        elif i%5 == 0:
            out.append('Buzz')
        else:
            out.append(i)
    return(out)

FizzBuzz(1, 15)
# Test the function with start = 1 and finish = 15
start = 1
finish = 15
result = FizzBuzz(start, finish)
print(result)

FizzBuzz(start, finish)
