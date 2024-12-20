from _pytest.monkeypatch import V
import numpy as np
import matplotlib.pyplot as plt
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
def temp_profile_in(iter_num,kb,kg,rb,rpo,di,mif,kp,rpi,M,kf,cf):
    
    #dt = 
    Tinit = 281.
    Tu = np.full((iter_num,21),Tinit)
    Tv = np.full((iter_num,21),Tinit)
    Tbi = Tinit
    dt = 1
    dz = 1 
    varRuu = (Ruu(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf)+Ruv(kb,kg,rb,di))/2
    varRuv = -2*Ruv(kb,kg,rb,di)

    for t in range(1,iter_num):
        Tu[t][0] = Tv[t-1][0]+Q/cf/(2*M)
        for i in range(1,21):
            Tbi = (Tv[t][i-1]+Tv[t][i]+Tu[t][i]+Tu[t][i-1])/4
            """
            A = np.array((((-M*cf/dz-varRuu),0),
                         (0,(M*cf/dz-varRuu))))
            B = np.array(((-Tu[t-1][i]*M*cf/dz+varRuu*(Tu[t-1][i]-2*100)),
                          (Tv[t-1][i]*M*cf/dz+varRuu*(Tv[t-1][i]-2*100))))
            
            """
            A = np.array((((-M*cf/dz-varRuv-varRuu),(varRuv)),
                         (varRuv,(M*cf/dz-varRuv-varRuu))))
            B = np.array(((-Tu[t-1][i]*M*cf/dz+varRuu*(Tu[t-1][i]-2*Tbi)+varRuv*(Tu[t-1][i]-Tv[t-1][i])),
                          (Tv[t-1][i]*M*cf/dz+varRuu*(Tv[t-1][i]-2*Tbi)+varRuv*(Tv[t-1][i]-Tu[t-1][i]))))
            
            Tu[t][i],Tv[t][i] =np.linalg.solve(A,B)
        Tv[t][0] = Tv[t][1]
        Tv[t][20] = Tu[t][20]
    return Tu,Tv

def calc(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf,cf):
    iter_num = 20001
    Tu,Tv = temp_profile_in(iter_num,kb,kg,rb,rpo,di,mif,kp,rpi,M,kf,cf)
    #temp_profile_around()
    t = np.linspace(0,iter_num-1,iter_num)
    plt.clf()
    plt.plot(t,Tu[:,0],label='0')
    plt.plot(t,Tu[:,1],label='1')
    plt.plot(t,Tu[:,2],label='2')
    plt.plot(t,Tu[:,5],label='5')
    plt.plot(t,Tu[:,8],label='8')
    plt.plot(t,Tu[:,10],label='10')
    plt.legend()
    plt.show()
    plt.clf()
    plt.plot(t,Tv[:,0],label='0')
    plt.plot(t,Tv[:,1],label='1')
    plt.plot(t,Tv[:,2],label='2')
    plt.plot(t,Tv[:,5],label='5')
    plt.plot(t,Tv[:,8],label='8')
    plt.plot(t,Tv[:,10],label='10')
    plt.legend()
    plt.show()
  

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
calc(kb,kg,rb,rpo,di,mif,kp,rpi,M,kf,cf)
plot()
