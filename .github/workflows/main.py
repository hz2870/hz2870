#---------------------Qeustion 1: Who Am I

def WhoAmI():
    return('wx2297')


#--------------------Question 2: getBondPrice


def getBondPrice(y, face, couponRate, m, ppy=1):
    bondPrice = 0
    coupon = face * couponRate / ppy
    numberCoupon = m * ppy
    for t in range(1, numberCoupon+1):
        dcf = 1/(1+y/ppy)**t
        bondPrice += dcf * coupon
    bondPrice += face * dcf
    
    return(bondPrice)

# method 2

def getBondPrice(y, face, couponRate, m, ppy=1):
    bondPrice = 0
    coupon = face * couponRate / ppy    
    for i in range(1,m*ppy+1):
        if i < m*ppy:
            cashflow = coupon
        else:
            cashflow = coupon + face
        dcf = 1/(1+y/ppy)**i
        bondPrice += dcf * cashflow        
    return(bondPrice)

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
#ppy = 1
ppy = 2
#<no ppy value passed>
getBondPrice(y, face, couponRate, m, ppy)


#--------------------Qestion 3: getBondDuration


def getBondDuration(y, face, couponRate, m, ppy=1):

    couponPayment = face * couponRate

    pvcf = 0
    w_pvcf = 0

    for t in range(1, 1+m):
        pv = 1 / (1 + y)**t
        cashFlow = couponPayment if t < m else couponPayment + face
        pvCashFlow = pv * cashFlow
        pvcf += pvCashFlow
        w_pvcf += pvCashFlow * t

    duration = w_pvcf / pvcf
    return (duration)

# method 2
def getBondDuration(y, face, couponRate, m, ppy = 1):
    bondDuration = 0
    
    coupon = face * couponRate / ppy
    
    pvcf = 0
    pvcf_t = 0
    
    for i in range (1, m*ppy+1):
        dcf = 1/(1+y/ppy)**i
        if i < m*ppy:
            cashflow = coupon 
        else:
            cashflow = coupon + face
        pvcf += dcf * cashflow
        pvcf_t += i * dcf * cashflow

    
    bondDuration = pvcf_t/pvcf
    
    return(bondDuration)

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
getBondDuration(y, face, couponRate, m, ppy = 1)



#---------------------Question 4: getBondPrice_Enumerate



def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    coupon = face * couponRate
    m = len(yc)

    for t, y in enumerate(yc, start=1):
        pv_factor = 1 / (1 + y)**t
        if t < m:
            cashFlow = coupon
        else:
            cashFlow = coupon + face
        pv_cashFlow = cashFlow * pv_factor
        bondPrice += pv_cashFlow

    return bondPrice

# method 2

def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    coupon = face * couponRate

    for a, b in enumerate(yc):
        if a < m-1:
            cashflow = coupon
        else:
            cashflow = coupon + face
        dcf = 1 / (1 + b) ** (a + 1)  # Correcting the discount factor exponentiation
        bondPrice += dcf * cashflow

    return bondPrice

# Test values
yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04
m = 5
getBondPrice_E(face, couponRate, m, yc)



#----------------------- Question 5: getBondPrice_Zip

def getBondPrice_Z(face, couponRate, times, yc):
    cpn = couponRate * face
    bondPrice = 0
    for y, t in zip(yc, times):
        dfn = 1 / ((1+y)**t)
        bondPrice += dfn * cpn
    bondPrice += face * dfn
    return(bondPrice)

# method 2

def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    coupon = face * couponRate
    
    for a, b in zip(yc, times):
        if b != times[-1]:
            cashflow = coupon
        else:
            cashflow = coupon + face
        dcf = 1/(1+a)**b
        bondPrice += dcf * cashflow
                
        
    return(bondPrice)


# Test values
yc = [0.010, 0.015, 0.020, 0.025, 0.030]
times = [1, 1.5, 3, 4, 7]
face = 2000000
couponRate = 0.04
getBondPrice_Z(face, couponRate, times, yc)


#-------------------------- Question 6: FizzBuzz

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
