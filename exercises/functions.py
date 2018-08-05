# Write your solution for 1.4 here!

def is_prime(numm):
    if( numm == 2):
        return False
    if( numm == 1):
        return True
    prime = True
    for x in range(2,numm):
        if(numm%x == 0):
            return False
        elif(numm%x >=1): 
            return True
            break



print(is_prime(14))