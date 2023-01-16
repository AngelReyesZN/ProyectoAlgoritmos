# -*- coding: utf-8 -*-



# # Importamos los módulos necesarios
# import math
# import numpy as np
# from matplotlib import pyplot as plt
# 
# # Generamos los datos para el gráfico
# x = np.array(range(500))*0.1
# y = np.zeros(len(x))
# for i in range(len(x)):
#     y[i] = math.sin(x[i])
# 
# # Creamos el gráfico
# plt.ion()
# plt.plot(x,y)
import matplotlib.pyplot as plt
import numpy as np
import math
######
x=np.linspace(0.001,100)
y1=(2.65*math.pi*x**3)/6
y2=6/(2.65*math.pi*x**3)
y3=6/(math.pi*x)
fuente={'fontname':'Tahoma'}
######
plt.plot(x,y1,label='Masa')
plt.plot(x,y2,label='Num. de Part.')
plt.plot(x,y3,label='Superf. Especif.')
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel('Diametros',**fuente)
plt.ylabel('Masa,Num de Part, Superf. Especif.',**fuente)
plt.title('Titulo')
plt.show()
# plt.savefig('img1.png',dpi=300)





# grafica1 = plt.figure(figsize=(13,10), dpi= 80)
# plt.plot([1,2,3,4,10], color="blue", linewidth=2, alpha=.7)
# plt.ylabel("Datos mostrados")
# 
# grafica1.savefig("grafica1.png")
# 
# plt.show()
# # 


# plt.figure(figsize=(16,10), dpi= 80)
# sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", label="Cyl=4", alpha=.7)
# sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color="deeppink", label="Cyl=5", alpha=.7)
# sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)
# sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", label="Cyl=8", alpha=.7)
# 
# # Decoration
# plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
# plt.legend()
# plt.show()





# # Data for plotting
# t = np.arange(1, 2, 4)
# s = np.arange(5,12,26)
# 
# fig, ax = plt.subplots()
# ax.plot(t, s)
# 
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
# 
# fig.savefig("test.png")
# plt.show()

