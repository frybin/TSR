from math import *

def equation(a,b,c):
    nlog=log((a/b),e)
    print(nlog)
    deltav=c*9.8*nlog
    deltav=str(deltav)
    print("The maximum change of velocity is " + deltav)

mi_b=False
mf_b=False
isp_b=False

while(mi_b==False):
    try:
        mi= float (input("Input the inital total mass: "))
        mi_b= True
    except ValueError:
        print("you must enter an number")
        mi_b= False

while(mf_b==False):
    try:
        mf= float (input("Input the dry mass: "))
        mf_b= True
    except ValueError:
        print("you must enter an number")
        mf_b= False

while(isp_b==False):
    try:
        Isp= float (input("Input the specific impulse: "))
        isp_b= True
    except ValueError:
        print("you must enter an number")
        isp_b = False


equation(mi,mf,Isp)
