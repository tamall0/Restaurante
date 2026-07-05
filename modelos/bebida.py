from modelos.producto import Producto

class Bebida(Producto):
    """
    Clase hija que representa una bebida. Hereda de Producto 
    y añade un atributo específico.
    """
    def __init__(self, nombre: str, precio: float, disponible: bool, volumen_mililitros: int):
        # Uso de super() para reutilizar los atributos de la clase padre
        super().__init__(nombre, precio, disponible)
        # Atributo propio específico
        self.volumen_mililitros: int = volumen_mililitros

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método del padre para demostrar polimorfismo."""
        info_base = super().mostrar_informacion()
        return f"[BEBIDA]   {info_base} | Volumen: {self.volumen_mililitros} ml."