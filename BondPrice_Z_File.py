

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
