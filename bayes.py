probability={
    "R_T":0.2,
    "R_F":0.8,
    "R_TS_T":0.01,
    "R_TS_F":0.99,
    "R_FS_T":0.4,
    "R_FS_F":0.6,
    "S_TR_TG_T":0.99,
    "S_TR_TG_F":0.01,
    "S_TR_FG_T":0.9,
    "S_TR_FG_F":0.1,
    "S_FR_TG_T":0.8,
    "S_FR_TG_F":0.2,
    "S_FR_FG_T":0.0,
    "S_FR_FG_F":1.0
    }

def R_prob(R):
    if(R==1):
        return probability["R_T"]
    else:
        return probability["R_F"]

def S_prob(R,S):
    if(R==1 and S==1):
        return probability["R_TS_T"]
    elif(R==1 and S==0):
        return probability["R_TS_F"]
    elif(R==0 and S==0):
        return probability["R_FS_F"]
    else:
        return probability["R_FS_T"]

def G_prob(G,R,S):
    if(G==1 and R==1 and S==1):
        return probability["S_TR_TG_T"]
    elif(G==0 and R==1 and S==1):
        return probability["S_TR_TG_F"]
    elif(G==1 and R==0 and S==1):
        return probability["S_TR_FG_T"]
    elif(G==0 and R==0 and S==1):
        return probability["S_TR_FG_F"]
    elif(G==1 and R==1 and S==0):
        return probability["S_FR_TG_T"]
    elif(G==0 and R==1 and S==0):
        return probability["S_FR_TG_F"]
    elif(G==1 and R==0 and S==0):
        return probability["S_FR_FG_T"]
    else:
        return probability["S_FR_FG_F"]

def prob():
    iR=int(input("Enter if it rained(yes=1 and no=0):"))
    iS=int(input("Enter if sprinkler is on or off(on=1 and off=0):"))
    iG=int(input("Enter if grass is wet(yes=1 and no=0):"))
    PR=R_prob(iR)
    PS=S_prob(iR,iS)
    PG=G_prob(iG,iR,iS)
    print(PR)
    print(PS)
    print(PG)
    P=PR*PS*PG
    print("Probability=",P)

prob()
    
    
