import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Cargar los archivos
df=pd.read_csv("C:/Users/sebas/Inteligencia Artificial/Country.csv")
lexp=pd.read_csv("C:/Users/sebas/Inteligencia Artificial/life_expectancy.csv")
df = df.rename(columns={'TableName': 'Country Name'})

df = df[['Country Name', 'IncomeGroup']]
lexp = lexp[['Country Name', '2016']]

# Convertir incomeGroup a valores numéricos
df['IncomeGroup'] = df['IncomeGroup'].replace({
    "Low income": 1,
    "Lower middle income": 2,
    "Upper middle income": 3,
    "High income: nonOECD":4,
    "High income: OECD":5
})

# Limpieza de datos: eliminar filas con NaN
merged_df = pd.merge(df, lexp, on="Country Name", how="inner")
merged_df = merged_df.dropna() 

# Escalamiento de datos
scaler = StandardScaler()
scaled_features = scaler.fit_transform(merged_df[['IncomeGroup', '2016']])

# Aplicar K-Means
kmeans = KMeans(n_clusters=4, random_state=42)  # Cambia el número de clusters según lo necesites
merged_df['Cluster'] = kmeans.fit_predict(scaled_features)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['IncomeGroup'], merged_df['2016'], c=merged_df['Cluster'], cmap='viridis')
plt.colorbar(label='Cluster')
plt.title('Clustering de Países por Grupo de Ingresos y Esperanza de Vida')
plt.xlabel('Grupo de Ingresos (Escalado)')
plt.ylabel('Esperanza de Vida en 2016 (Escalada)')
plt.show()

