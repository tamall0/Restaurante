from modelos.producto import Producto

class Restaurante:
    """
    Clase de servicio encargada de administrar la lista de productos
    y procesarlos aplicando polimorfismo.
    """
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        # Almacena de forma dinámica cualquier variante derivada de la clase padre Producto
        self.lista_productos: list[Producto] = []

    def agregar_producto(self, nuevo_producto: Producto) -> None:
        """Registra un producto (sea Platillo o Bebida) en el sistema."""
        self.lista_productos.append(nuevo_producto)

    def mostrar_menu_completo(self) -> None:
        """
        Demuestra polimorfismo al recorrer la lista llamando a mostrar_informacion()
        independientemente de si el objeto es un Platillo o una Bebida.
        """
        print(f"\n===== MENÚ DE {self.nombre_establecimiento.upper()} =====")
        if not self.lista_productos:
            print("El menú está vacío.")
            return
            
        for producto in self.lista_productos:
            # Polimorfismo en acción: ejecuta la versión del método que corresponda al tipo de objeto
            print(producto.mostrar_informacion())