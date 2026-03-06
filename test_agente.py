# test_agente.py
from ai.agente_portafolio import preguntar_portafolio

# Probar pregunta de juegos
respuesta = preguntar_portafolio("¿Qué juegos tienes?")
print("Respuesta:", respuesta)

print("\n" + "="*50 + "\n")

# Probar pregunta de ERP
respuesta = preguntar_portafolio("Cuéntame sobre el proyecto ERP")
print("Respuesta:", respuesta)