class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    Aplica encapsulamiento protegiendo el atributo precio.
    """
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre: str = nombre
        # Atributo encapsulado (privado) solicitado
        self.__precio: float = precio
        self.disponible: bool = disponible

    # Métodos de acceso y modificación (Getter y Setter)
    def obtener_precio(self) -> float:
        """Devuelve el valor del precio protegido."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        """Modifica el precio aplicando la validación obligatoria."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"[Error]: El precio de '{self.nombre}' debe ser estrictamente mayor a cero y no negativo.")

    def mostrar_informacion(self) -> str:
        """Método base para ser sobrescrito por las clases hijas."""
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Nombre: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"