class MiClase:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def obtener_propiedad(self, nombre_propiedad):
        # Usamos getattr para acceder dinámicamente a la propiedad
        return getattr(self, nombre_propiedad, None)  # Devuelve None si no encuentra la propiedad

# Crear un objeto de la clase
obj = MiClase(10, 20)

# Acceder a las propiedades 'x' y 'y' usando el método obtener_propiedad
print(obj.obtener_propiedad('x'))  # Salida: 10
print(obj.obtener_propiedad('y'))  # Salida: 20
print(obj.obtener_propiedad('z'))  # Salida: None (porque no existe 'z')