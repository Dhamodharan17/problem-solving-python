# AP 1
def biscuitGenerator():
    
    #Get input
    a,b,t = input().split()
    a = float(a)
    b = float(b)
    t = float(t)
    totalBiscuits = 0
    i =1
    limit = a
    
    # Generate biscuit until given time t
    while limit <= t+0.5:
        totalBiscuits = totalBiscuits + b
        i = i+1 #subsequent
        # next time where machine will generate b biscuits
        limit = a*i
        
    print(int(totalBiscuits))
    
biscuitGenerator()

# AP2 - previous approach we went to each slot and added biscuits but same biscuits at each slot so we can find slots * #biscuits

def biscuitGenerator():
    
    a,b,t = map(float, input().split())
    
    totalSlots = (t+0.5) // a
    
    total_biscuits =totalSlots*b
    
    print(int(total_biscuits))
    
biscuitGenerator()

