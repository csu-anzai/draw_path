# encoding='utf-8'
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.2)
y=np.sin(x)

fig,ax=plt.subplots()
ax.plot(x,y)
plt.savefig("C:\Users\octopus\Desktop\html")
plt.show()