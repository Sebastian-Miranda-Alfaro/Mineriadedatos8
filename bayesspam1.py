import pandas as pd

datos = {
    'correo': ["correoN", "correoN", "correoN", "correoN", "correoN", "correoN", "correoN", "correoS", "correoS", "correoS"],
    'oferta': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    'archivo': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  
    'link': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]     
}


df = pd.DataFrame(datos)
print(df)

# Probabilidades previas
prob_spam = 0.30   
prob_no_spam = 0.70 
# Probabilidades condicionales para spam
p_oferta_spam = 0.90   
p_archivo_spam = 0.80  
p_link_spam = 0.85     

# Probabilidades condicionales para no spam
p_oferta_no_spam = 0.20  
p_archivo_no_spam = 0.40  
p_link_no_spam = 0.10     

# Calcular la probabilidad total de cada característica (normalización)
p_oferta = p_oferta_spam * prob_spam + p_oferta_no_spam * prob_no_spam
p_archivo = p_archivo_spam * prob_spam + p_archivo_no_spam * prob_no_spam
p_link = p_link_spam * prob_spam + p_link_no_spam * prob_no_spam

# Calcular la probabilidad de que el correo sea spam que tiene oferta, archivo y link
p_spam_oferta_archivo_link = (p_oferta_spam * p_archivo_spam * p_link_spam * prob_spam) / (p_oferta * p_archivo * p_link)


print(f"La probabilidad de que el correo sea spam que tiene oferta, archivo adjunto y link sospechoso es: {p_spam_oferta_archivo_link:.2f}")
