#
#  Ten-Year_Minimum_Errors.ipynb
#  Student Loans
#
#  Created by Ed Silkworth on 7/29/19.
#  Copyright © 2019-2020 Ed Silkworth. All rights reserved.
#

# for computing ten-year minimum payment errors

import multiprocessing as mp # for accelerating computations
import math # for certain mathematic functions
import time # for timing computations
# for acceleration and timing, ``computations'' mean all processes involved in computing errors

# given
p_max = 10000 # default: 10000
p_min = 2000 # default: 2000
N = 40 # default: 40
# p will vary, see BO() and T() for more information
APR = 4.53 # default: 4.53
compound = 0 # 1 (yes) or 0 (no), default: 0
alpha = 1 # default: 1
# a = a_min, see BO() regarding a_min
# length of repayment in years and months, total payments, savings and change in savings are ignored

def open():
    print("\nChecking for errors...\n(p, error)\n") # prints first

def close():
    end = time.time()
    print("\nCompleted in %.2fs" %(end-start))

# set
delta_N = (p_max-p_min)/N

if compound == 0:
    i = APR/100/12
elif compound == 1: 
    i = pow( 1+APR/100/365.25 , 365.25/12 )-1
else: None
    
# test within $0.02 of a_min
test = 2 # see BO() regarding a_min, and see T() for running the test  

# check and round quantities to the nearest cent with a function
def CR(x): 
    
    if x*100-math.floor(x*100) > 0.499999 and x*100-math.floor(x*100) < 0.5:
        return round(x*100+1)/100
    else: 
        return round(x*100)/100

# compute the monthly principal balance and, consequently, monthly outstanding interest with a function
def BO(i, alpha, p, c): # see apply_async() and T() regarding p and c
    
    # set
    B = [p] # meaning B[0] = p
    O = [0] # meaning O[0] = 0
    m = 1
    
    if i > 0 and alpha == 0:
        a_min = math.ceil( B[0]/120 *100)/100
    elif i == 0:
        a_min = math.ceil( B[0]/120 *100)/100
    elif i > 0 and 0 < alpha <= 1:
        a_min = math.ceil( alpha*(B[0]*i)*pow(1+alpha*i,120) / (pow(1+alpha*i,120)-1) *100)/100 # case in which the numerical solution may deviate
    else: None
        
    # testing minimum
    a_min += 0.01*c
    
    while B[m-1] - (a_min - CR(alpha*B[m-1]*i)) > 0 and CR(a_min) != CR(alpha*B[0]*i): # do, except if B[1]=B[0]
        B.append(CR(B[m-1] - (a_min - CR(alpha*B[m-1]*i)))) # check whenever round, and check and round at end
        O.append(CR(O[m-1] + CR(B[m-1]*i) - CR(alpha*B[m-1]*i)))
        m += 1
    
    # if B[1]=B[0], remove potential error from consideration  
    if CR(a_min) == CR(alpha*B[0]*i):
        return # exit function and return nothing
    else: None
    
    # set
    n = m
    
    # set
    af = B[n-1] + CR(B[n-1]*i) + O[n-1]
    B.append(B[n-1] - (af - CR(B[n-1]*i) - O[n-1])) # = 0
    # O[n] = 0
    
    return B

# for running the test
def T(j, r, loop):
    
    # just for ones' information
    if loop == 1:
        open()

    # log potential errors in L
    if len( BO(i, alpha, p_min+delta_N*j, 0) )-1 <= 120: 
        L = [0/100] # meaning potentially no error exists
    else: L = []

    for c in r:
        if len( BO(i, alpha, p_min+delta_N*j, -(c+1)) )-1 <= 120:
            L.append(-(c+1)/100)
        else: None
        if len( BO(i, alpha, p_min+delta_N*j, c+1) )-1 <= 120:
            L.append((c+1)/100)            
        else: None    
        
    # compute any errors, and output them
    if float(min(L)) != 0:
        if float(min(L)) > 0:
            print("%s, +%.2f" %(p_min+delta_N*j, min(L)))
        else: 
            print("%s, %.2f" %(p_min+delta_N*j, min(L)))
    else: None
    
    # show progress periodically for large numbers of computations
    # without doing so and if errors are few, output may appear to stall

    factor = math.floor((p_min+delta_N*j)/1000)
    if (p_min+delta_N*j) >= 1000*factor and (p_min+delta_N*(j-1)) < 1000*factor:
        print("\n(at p = %s)\n" %(1000*factor))
    else: None
    
    # just for ones' information
    if loop == N+1:
        print("\n--\nOut of %s computation(s)" %(N+1))
        close()
    else: None
         
# for implementing multiprocessing
def apply_async():
    
    pool = mp.Pool()
    
    loop = 1
    for j in range(N+1):
        pool.apply_async(T, args=(j, range(test), loop, )) # empty slot at end is required
        loop += 1

    pool.close()
    pool.join()

start = time.time()

if __name__ == "__main__":
    apply_async()                           
else: None

# end = time.time() placed in close()