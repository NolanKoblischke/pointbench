import numpy as np
import matplotlib.pyplot as plt
N = 100
csv_name = 'points.csv'
with open(csv_name,'w') as f:
    f.write('x,y\n')
for i in range(N):
    pt = np.random.rand(2)*8+1
    pt = np.round(pt,3)
    plt.plot(pt[0],pt[1],'o')
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.minorticks_on()
    plt.grid(which='both',linestyle='--')
    with open(csv_name,'a') as f:
        f.write(str(pt[0])+','+str(pt[1])+'\n')
    plt.savefig('plots/'+str(i)+'.png')
    plt.close()
