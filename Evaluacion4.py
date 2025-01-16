import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

productos=np.array([[15, 7.0],[30, 8.5],[25, 6.5],[40, 10.0],[20, 5.5]])

encabezados= ["Cantidad", "Precio"]
producto=["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]
df=pd.DataFrame(productos, index=producto, columns=encabezados)

df.to_csv('proyecto_ventas.csv', index=False)
