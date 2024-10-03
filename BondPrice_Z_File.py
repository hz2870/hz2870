

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
