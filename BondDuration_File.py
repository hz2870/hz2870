

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
