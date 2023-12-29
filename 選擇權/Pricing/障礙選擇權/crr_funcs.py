import math
import numpy as np 
from scipy.stats import norm

def tree_stock(S0:float, T:float, sigma:float, n:int) -> np.array:
    
    # 設定相關變數
    
    dt = T / n  # 每期長度
    u = math.exp( sigma*math.sqrt(dt) )  # 股價上漲倍數
    d = 1 / u  # 股價下跌倍數
    
    # 建立股價二項樹
    
    S = np.zeros( (n+1,n+1) )  # 建立一個 n*n的空矩陣，後面再填入股價
    S[0,0] = S0  # t=0時股價為S0
    
        # 注意，按照下方第二個迴圈內的寫法，t跟i之關係如下  
        # t=1時i=0
        # t=2時i=0,1
        # t=3時i=0,1,2
        # t=n時i=0,1,...,n-1
        # 故，需要一個變數a控制i的變化
    
    a = 1
    for t in range(1,n+1) :  # 將數值填入空矩陣中        
        for i in range(a) :
            S[i,t] = S[i,t-1] * u
            S[i+1,t] = S[i,t-1] * d
        a +=1
        
    return S

def American_call(S0, K, r, T, sigma, n) -> np.array :
    
    # 設定相關變數
    
    dt = T / n  # 每期長度
    u = math.exp( sigma*math.sqrt(dt) )  # 股價上漲倍數
    d = 1 / u  # 股價下跌倍數
    prob = ( math.exp(r*dt) - d ) / (u - d)  # 風險中立機率
    
    # 建立買權二項樹
    
    S = tree_stock(S0, T, sigma, n)  # 引入股價二項樹
    C = np.zeros((n+1,n+1))  # 建立買權空矩陣，後面再填入數值
    
    # 先計算買權到期日價值
        
    C[:,-1] = np.maximum( S[:, -1] - K, 0 )   
                  
    # 基於二項樹向前計算    
        
    t = n   # 基於下面迴圈做法，需先給定初始值
    b = n   # 此變化規律見2-1的i變化
    while not t < 1 :  # 只要t不等於0，就一直執行下面迴圈(一直折現至t=0)
        for i in range(b) :
            hold_option_value = math.exp(-r*dt) * ( C[i,t]*prob + C[i+1,t]*(1-prob) )  # 計算第t-1期持有選擇權的期望價值(由第t期折現而來)
            strike_value = S[i,t-1] - K  # 計算第t-1期提前履約能得到的履約價值
            C[i,t-1] = max( hold_option_value, strike_value )  # 持有選擇權價值和履約價值取大作為下次計算的選擇權價值
        t = t - 1  # 因CRR是由後往前計算，故時間(期數)為遞減至t=0
        b = b - 1
        
    Call = C[0,0]
        
    return Call

def American_put(S0, K, r, T, sigma, n) -> np.array :
    
    # 設定相關變數
    
    dt = T / n  # 每期長度
    u = math.exp( sigma*math.sqrt(dt) )  # 股價上漲倍數
    d = 1 / u  # 股價下跌倍數
    prob = ( math.exp(r*dt) - d ) / (u - d)  # 風險中立機率
    
    # 建立賣權二項樹
    
    S = tree_stock(S0, T, sigma, n)  # 引入股價二項樹
    P = np.zeros((n+1,n+1))  # 建立賣權空矩陣，後面再填入數值
    
    # 先計算賣權到期日價值
    
    P[:,-1] = np.maximum( K - S[:,-1], 0 )
   
    # 基於二項樹向前計算 
        
    t = n   # 基於下面迴圈做法，需先給定初始值
    b = n   # 此變化規律見2-1
    while not t < 1 :  # 只要t不等於0，就一直執行下面迴圈(一直折現至t=0)
        for i in range(b) :
            hold_option_value = math.exp(-r*dt) * ( P[i,t]*prob + P[i+1,t]*(1-prob) )  # 計算在第t-1期持有選擇權的期望價值(由第t期折現而來)
            strike_value = K - S[i,t-1]   # 計算第t-1期提前履約能得到的履約價值
            P[i,t-1] = max( hold_option_value, strike_value )   # 持有選擇權價值和履約價值取大作為下次計算的選擇權價值
        t = t - 1  # 因CRR是由後往前計算，故時間(期數)為遞減至t=0
        b = b - 1 
        
    Put = P[0,0]
        
    return Put