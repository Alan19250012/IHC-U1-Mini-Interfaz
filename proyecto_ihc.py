def saludar(perfil):
    if perfil["nivel"] == "nuevo":
        return "Bienvenido, " + perfil["nombre"] + ". Te explico paso a paso."
    elif perfil["nivel"] == "intermedio":
        return "Hola de nuevo, " + perfil["nombre"] + ". Continuemos."
    return "Hola " + perfil["nombre"] + ". Dime y voy directo."

def reconocer(texto):
    texto = texto.lower()
    if "horario" in texto:
        return "Tu horario está en la plataforma: LUN y MIE de 10:00 a 11:30."
    if "calificacion" in texto or "calificación" in texto:
        return "Las calificaciones se publican los viernes."
    if "tarea" in texto:
        return "Las tareas se entregan en el portafolio de evidencias."
    return None

def ayuda_inteligente(perfil):
    if perfil["nivel"] == "nuevo":
        return "Puedes preguntar por: horario, calificación o tarea."
    return "Temas disponibles: horario, calificación, tarea."

usuario = {"nombre": "Luis", "nivel": "nuevo"}
print(saludar(usuario))
for i in range(3):
    entrada = input("¿En qué te ayudo? ")
    respuesta = reconocer(entrada)
    print(respuesta if respuesta else ayuda_inteligente(usuario))
