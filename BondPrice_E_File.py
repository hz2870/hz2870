

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
