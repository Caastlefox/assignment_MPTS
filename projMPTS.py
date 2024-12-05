import numpy as np

def Ruv(kb,kg,rb,di):
    #important assumption buv = 2*di, they are simmetrical to each other
    res = 0
    buv = 2*di
    sigma = (kb-kg)/(kb+kg)
    res  -= 1/(2*np.pi*kb)*(np.log(buv)+sigma*np.sqrt(np.log(((rb**2-di**2)/rb**2)**2-buv**2)**2))
    return res
#important Ruv not divided
def Ruu(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf):
    res = 0
    Prf = 0.35
    sigma = (kb-kg)/(kb+kg)
    res  += 1/(2*np.pi*kb)*(np.log(rb/rpo)+sigma*np.log(rb**2/(rb**2-di**2)))
    Ref = 2*M/(np.pi*mif*rpi)
    hf = 0.023*Ref**0.8*Prf*kf/(2*rpi)
    res += np.log(rpo/rpi)/(2*np.pi*kp)+1/(2*np.pi*hf*kp)
    return res
#important Ruu not divided
def temp_profile_in(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf,cf):

    varRuu = Ruu(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf)
    varRuv = Ruv(kb,kg,rb,di)
    A = np.array(((M*cf-varRuv-varRuu),(varRuv)),
                 ((M*cf-varRuv-varRuu),(varRuv)))
    B = np.array(((varRuu)),
                 ((varRuv)))
    np.linalg.solve(A,B)
def temp_profile_around():
    pass
def calc(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf):
    
    temp_profile_in(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf)
    temp_profile_around()

def plot():
    pass

d    = 5
H    = 110
rb   = 0.055
rpo  = 0.016
rpi  = 0.013
di   = 0.03
seg  = 20
N    = 2
M    = 0.2
kg   = 3.5
ag   = 1.62*10**-6
cf   = 4190
rhof = 1000
kf   = 0.614
mif  = 0.00086
kp   = 0.4
kb   = 1.3
Q    = 4000
calc(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf)
plot()
