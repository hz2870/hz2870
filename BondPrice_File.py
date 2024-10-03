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
