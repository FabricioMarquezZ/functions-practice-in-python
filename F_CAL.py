# Function that allows calculating discounts depending on the amount of money spent
# 20-30- dls=20%
# 31-50 dls=30%
# 51- dls=40%

def desc(V):
    if V == 30 and V >= 20:
        DESCP = ((V/100)*20)
        print("Total: ", int(DESCP))
    elif V >= 31 and V == 50:
        DESCP = ((V/100)*30)
        print("Total: ", int(DESCP))
    elif V >= 51:
        DESCP = ((V/100)*40)
        print("Total: ", int(DESCP))


desc(55)
