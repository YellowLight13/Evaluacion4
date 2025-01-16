import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

productos=np.array([[15, 7.0],[30, 8.5],[25, 6.5],[40, 10.0],[20, 5.5]])

encabezados= ["Cantidad", "Precio"]
producto=["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]
df=pd.DataFrame(productos, index=producto, columns=encabezados)

df.to_csv('proyecto_ventas.csv', index=False)



PT_P1= df["Cantidad"].iloc[0]* df["Precio"].iloc[0]
PT_P2= df["Cantidad"].iloc[1]* df["Precio"].iloc[1]
PT_P3= df["Cantidad"].iloc[2]* df["Precio"].iloc[2]
PT_P4= df["Cantidad"].iloc[3]* df["Precio"].iloc[3]
PT_P5= df["Cantidad"].iloc[4]* df["Precio"].iloc[4]

df["Precio total"]= (PT_P1, PT_P2, PT_P3, PT_P4, PT_P5)




fig, ax=plt.subplots(nrows=1, ncols=1, figsize=(10,6))
ax.bar(x= df.index, height =df["Precio total"])
ax.set_title("Precio Total Por Producto")
ax.set_ylabel("Precio Total")
ax.set_xlabel("Productos")
plt.savefig("Precio_total.png")