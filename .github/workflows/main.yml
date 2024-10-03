# Question 1: Who Am I
def WhoAmI():
    return 'hz2870'


# Question 2: getBondPrice
# Version 1
def getBondPrice_v1(y, face, couponRate, m, ppy=1):
    cf = couponRate * face / ppy
    n = m * ppy
    y1 = y / ppy

    pvcf = 0
    for t in range(1, n+1):
        pvcf += cf / ((1 + y1) ** t)

    pv_f = face / ((1 + y1) ** n)

    bondPrice = pvcf + pv_f
    return bondPrice


# Version 2
def getBondPrice_v2(y, face, couponRate, m, ppy=1):
    bondPrice = 0
    coupon = face * couponRate / ppy
    for i in range(1, m*ppy+1):
        if i < m*ppy:
            cashflow = coupon
        else:
            cashflow = coupon + face
        dcf = 1 / (1 + y / ppy) ** i
        bondPrice += dcf * cashflow
    return bondPrice


# Question 3: getBondDuration
# Version 1
def getBondDuration_v1(y, face, couponRate, m, ppy=1):
    couponPayment = face * couponRate
    pvcf = 0
    w_pvcf = 0
    for t in range(1, 1 + m):
        pv = 1 / (1 + y)**t
        cashFlow = couponPayment if t < m else couponPayment + face
        pvCashFlow = pv * cashFlow
        pvcf += pvCashFlow
        w_pvcf += pvCashFlow * t

    duration = w_pvcf / pvcf
    return duration


# Version 2
def getBondDuration_v2(y, face, couponRate, m, ppy=1):
    bondDuration = 0
    coupon = face * couponRate / ppy
    pvcf = 0
    pvcf_t = 0
    
    for i in range(1, m * ppy + 1):
        dcf = 1 / (1 + y / ppy) ** i
        cashflow = coupon if i < m * ppy else coupon + face
        pvcf += dcf * cashflow
        pvcf_t += i * dcf * cashflow

    bondDuration = pvcf_t / pvcf
    return bondDuration


# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 2

# Testing the bond price functions
bondPrice_v1 = getBondPrice_v1(y, face, couponRate, m, ppy)
bondPrice_v2 = getBondPrice_v2(y, face, couponRate, m, ppy)

# Testing the bond duration functions
duration_v1 = getBondDuration_v1(y, face, couponRate, m, ppy)
duration_v2 = getBondDuration_v2(y, face, couponRate, m, ppy)


# Question 6: FizzBuzz
# Version 1
def FizzBuzz_v1(start, finish):
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


# Version 2
def FizzBuzz_v2(start, finish):
    out = []
    for i in range(start, finish + 1):
        if i % 15 == 0:
            out.append('FizzBuzz')
        elif i % 3 == 0:
            out.append('Fizz')
        elif i % 5 == 0:
            out.append('Buzz')
        else:
            out.append(i)
    return out


# Test FizzBuzz
fizzbuzz_v1 = FizzBuzz_v1(1, 15)
fizzbuzz_v2 = FizzBuzz_v2(1, 15)

# Outputs
(bondPrice_v1, bondPrice_v2, duration_v1, duration_v2, fizzbuzz_v1, fizzbuzz_v2)


