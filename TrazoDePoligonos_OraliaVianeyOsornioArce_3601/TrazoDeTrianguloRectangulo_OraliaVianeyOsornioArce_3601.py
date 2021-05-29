import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image

plt.imshow(Image.open('fondo.png'))

def DDA(x1, y1, x2, y2, a):
    x1r=x1; y1r=y1
    x2r=x2; y2r=y2
    x1t=x1; y1t=y1

    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x3=x1
    y3=a
    if(dx>dy):
        steps=dx
    else:
        steps=dy
    xinc=float(dx/steps)    
    yinc=float(dy/steps)    
    xinc=round(xinc, 1)
    yinc=round(yinc, 1)

    dx1= abs(x3-x1)
    dy1= abs(y3-y1)
    if(dx1>dy1):
        steps1=dx1
    else:
        steps1=dy1
    xinc1=float(dx1/steps1)
    yinc1=float(dy1/steps1)
    xinc1=round(xinc1, 1)
    yinc1=round(yinc1, 1)

    for i in range (0, int (steps+1)):
        plt.gca().add_patch(Rectangle((x1, y1), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))  
        plt.ylim(0, 20)
        x1=(x1+xinc); y1=(y1+yinc)
        print ("("+str(round(x1))+", "+str(round(y1))+")")
        print ("("+str(round(x3))+", "+str(round(y3))+")")
    for i in range (0, int (steps1+1)):
        plt.title('***DDA***')
        
        plt.gca().add_patch(Rectangle((x2r, y2r), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 20)
        x2r=(x2r+xinc1); y2r=(y2r+yinc1)
        print ("("+str(round(x1r))+", "+str(round(y1r))+")")
        print ("("+str(round(x2r))+", "+str(round(y2r))+")") 
    
    xt2=x1-1; yt2=y2r-1
    

     
    dxt= abs(round(xt2-x1t))
    dyt= abs(round(yt2-y1t))
    if(dxt>dyt):
        stepst=dxt
    else:
        stepst=dyt
    xinct=float(dxt/stepst)
    yinct=float(dyt/stepst)
    xinct=round(xinct, 1)
    yinct=round(yinct, 1)

    for i in range (0, int (stepst+1)):
        plt.gca().add_patch(Rectangle(((x1t),round(y1t)), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))  
        plt.ylim(0, 20)
        x1t=(x1t+xinct); y1t=(y1t+yinct)
        plt.plot(round(x1t), round(y1t),"m*")
        plt.plot(round(x1), round(yt2),"m*")
        
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

def Bresenham(x1, y1, x2, y2, a):
    x=x1; y=y1; xr=x1; yr=y1
    xt=x1; yt=y1 
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    p=2*dy-dx
    x3=x1; y3=a

    while (x<=x2):
        plt.gca().add_patch(Rectangle((x, y), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 30)
        x+=1; x3+=1
        if (p<0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            y+=1; y3+=1

        print ("("+str(round(x))+", "+str(round(y))+")")
        print ("("+str(round(x3))+", "+str(round(y3))+")")
        print ("("+str(round(xr))+", "+str(round(yr))+")")
        print ("("+str(round(x2))+", "+str(round(y2))+")")

    while (yr<=y3):
        plt.gca().add_patch(Rectangle((x2, y2), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 30)
        yr+=1; y2+=1
        if (p<0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            xr+=1; x2+=1

        print ("("+str(round(x))+", "+str(round(y))+")")
        print ("("+str(round(x3))+", "+str(round(y3))+")")
        print ("("+str(round(xr))+", "+str(round(yr))+")")
        print ("("+str(round(x2))+", "+str(round(y2))+")")
   
    

    xp = xt
    yp = yt
    dxt = abs(x2 - xt)
    dyt = abs(y3 - yt)
    pt = (2 * dy) - dxt

    for i in range(xt , x2):
        plt.gca().add_patch(Rectangle((xp, yp), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 30)
        
        xp=xp+1
        if pt<0:
            pt = pt + (2 * dyt)
        else:
            pt = pt + (2 * dyt ) - (2 * dxt)
            yp=yp+1


    plt.title('***Bresenhams***')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
if __name__=="__main__":
    #solicitar los valores que son asignados a las variables de inicalización 
    tipo=int(input("\033[1;33m"+"Ingrese el valor del algoritmo a usar:\n1. Algoritmo DDA\n2. Algoritmo Bresenham\n"+'\033[0;m')) 
    x1=int(input("\033[4;35m"+"X1="+'\033[0;m'))
    y1 = int(input("\033[4;35m"+"Y1="+'\033[0;m')) 
    a=int(input("\033[;36m"+"altura="+"\033[0;m")) 
    b = int(input("\033[;36m"+"base="+'\033[0;m'))   
    y2=y1
    if (tipo==1):
        DDA(x1, y1,((b+x1)-1), y2, ((a+y1)-1))
    elif (tipo==2):
        Bresenham(x1, y1,((b+x1)-1), y2, ((a+y1)-1))
