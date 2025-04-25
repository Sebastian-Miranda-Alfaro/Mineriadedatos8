#Importar las librerías necesarias
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
#Importar la clase DecisionTreeClassifier para crear el árbol de decisión 
from sklearn.model_selection import train_test_split  #Importar la función train test_split para dividir los datos
from sklearn.metrics import accuracy_score
#Importar la función accuracy_score para la precisión del modelo
import matplotlib.pyplot as plt
# Cargar el conjunto de datos
# Dato de ejemplo: ¿Jugar tenis? (14 dias)
data = {
   'Cielo': ['Soleado', 'Soleado','Nublado', 'Lluvioso', 'Lluvioso','Lluvioso', 'Nublado','Soleado', 'Soleado','Lluvioso', 'Soleado','Nublado', 'Nublado','Lluvioso'],
   'Humedad': ['Alta', 'Alta', 'Alta','Normal', 'Normal', 'Alta', 'Normal','Alta', 'Hormal', 'Normal','Normal', 'Alta', 'Normal', 'Alta', ],
   'Viento': ['Débil', 'Fuerte', 'Débil',"Débil", 'Fuerte', 'Débil', 'Fuerte',"Débil", "Débil", 'Débil','Fuerte', 'Fuerte', 'Débil','Fuerte'],
   'Jugar': ['No', 'No', 'Si', 'Si', 'No', 'Si', 'Si','No', 'Si','Si', 'Si', 'Si', 'Si', 'No']}
df=pd.DataFrame(data)

#Preprocesar los datos
#Los algoritmos requieren valores numéricos, no strings. Usamos codificación de etiquetas:
# Convertir variables categóricas a numéricas
from sklearn.preprocessing import LabelEncoder
# Crear un codificador para cada columna
label_encoders = {}
df_encoded = df.copy ()
# Copia del DataFrame original
for column in df.columns:
   le = LabelEncoder() # Crear un codificador de etiquetas
   df_encoded[column] = le.fit_transform(df[column]) # Aplicar el codificador a la columna
   label_encoders[column] = le # Guardar los codificadores para interpretar después


print(df_encoded)
print ("\nDataset codificado:")

#Dividir Datos en Entrenamiento y Prueba 
#Separar características (X) y variable objetivo (y)
# X son las características (Cielo, Humedad, Viento) y y es la variable objetivo (Jugar) (drop es para eliminar la columna 'Jugar')
X = df_encoded.drop('Jugar', axis=1) #Todas las columnas excepto 'Jugar' axis se refiere a las columnas
# Y se refiere a la variable objetivo, que es 'Jugar'
y = df_encoded['Jugar'] # Solo la columna 'Jugar'

# Dividir en 70% entrenamiento, 30% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print ("\nDatos de entrenamiento:")
print(X_train.head())
print ("\nDatos de prueba:")
print (X_test.head())
#Entrenar el Árbol de Decisión
# Crear y entrenar el modelo
model = DecisionTreeClassifier(criterion='gini', # Métrica para dividir nodos (Gini o Entropía) 
                               max_depth=3, # Profundidad máxima del árbol (evita overfitting) 3 por que es un árbol pequeño
                               random_state=42)
model.fit(X_train, y_train)

#Predecir en lod atos de prueba
y_pred = model.predict(X_test)

#Calcular precision
accuracy = accuracy_score(y_test, y_pred) #accuracy_score calcula la precision 
#del modelo comparando las predicciones con los valores reales 
print(f"\nPrecision del modelo: {accuracy:.2f}")

#Visualizar el arbol de decision 
#Configurar figura 
plt.figure(figsize=(10,6))

#Dibujar el arbol
#plot_tree es una funcion de sklearn que dibuja el árbol de decision 
#model es el arbol de decision entrenado 
#feature_name son los nombres de las caracteristicas (Cielo,Humedad,Viento)
#Class_names son los nombres de las clases (Jugar=0 -> 'No', Jugar=1 -> 'Si')
plot_tree(
    model,
    feature_names=X.columns, #Nombre de las caracteristicas
    class_names=['No', 'Si'], #Nombre de las clases (Jugar=0 -> 'No')
    filled = True, #Colorear por clase
    rounded = True, #Formar los nodos
    impurity = True #Mostrar impureza (Gini)
)

plt.title("Arbol de decision - ¿Jugar tenis?")
plt.show()

print("Importancia de caracteristicas:",model.feature_importances_)
print("Nombres de caracteristicas:", X.columns)

#Predecir undia nuevo: Cielo = "lluvioso (1)", Humedad = "Normal (1)", Viento = "Debil (0)"
nuevo_dia = pd.DataFrame([[1,1,0]], columns= X.columns)
prediccion = model.predict(nuevo_dia) #Predecir si se puede jugar o no
if prediccion[0] ==1:
   print("Prediccion: Si se puede jugar")
else:
   print("Prediccion: No, no se puede jugar")

#Mostrar la prediccion (1=Si, 0=No)
#Guardar el modelo entrenado y los codificadores 