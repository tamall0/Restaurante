from modelos.producto import Producto

class Platillo(Producto):
    """
    Clase hija que representa una comida. Hereda de Producto 
    y añade un atributo específico.
    """
    def __init__(self, nombre: str, precio: float, disponible: bool, tiempo_preparacion_minutos: int):
        # Uso de super() para reutilizar los atributos de la clase padre
        super().__init__(nombre, precio, disponible)
        # Atributo propio específico
        self.tiempo_preparacion_minutos: int = tiempo_preparacion_minutos

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método del padre para demostrar polimorfismo."""
        info_base = super().mostrar_informacion()
        return f"[PLATILLO] {info_base} | Tiempo de Prep: {self.tiempo_preparacion_minutos} min."