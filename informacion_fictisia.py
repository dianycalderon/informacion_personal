# Creando un diccionario 'informacion_personal' con datos ficticios de una persona
informacion_personal = {
    "nombre": "Carlos Pérez",  # aqui estara el nombre de la persona fictisia
    "edad": 28,  # Edad de la persona que vamos a utilizar
    "ciudad": "Guayaquil",  # Ciudad donde reside
    "profesion": "Ingeniero"  # Profesión que ejerce
}

# Accediendo y modificando el valor asociado a la clave 'ciudad'
informacion_personal["ciudad"] = "Quito"  # Cambiare la ciudad a Quito

# Agregando o modificando la clave 'profesion'
informacion_personal["profesion"] = "Docente Universitario"  # Se actualizara  la profesión de la persona

# Verificando si la clave 'telefono' existe, si no, se agrega con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"  # Agregando un número de teléfono ficticio

# Eliminando la clave 'edad' porque no es necesaria en este contexto
del informacion_personal["edad"]

# Imprimiendo el diccionario final después de todas las modificaciones
print("Diccionario final:", informacion_personal)
