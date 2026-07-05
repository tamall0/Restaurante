from servicios.restaurante import Restaurante
from modelos.platillo import Platillo
from modelos.bebida import Bebida

def ejecutar_sistema() -> None:
    # 1. Instanciar el servicio principal
    mi_restaurante = Restaurante("Rincón Gourmet")

    # 2. Crear al menos dos objetos de tipo Platillo
    platillo_uno = Platillo("Lomo Saltado", 12.50, True, 20)
    platillo_dos = Platillo("Ceviche Clásico", 14.00, True, 15)

    # 3. Crear al menos dos objetos de tipo Bebida
    bebida_uno = Bebida("Chicha Morada Grande", 3.50, True, 1000)
    bebida_dos = Bebida("Jugo de Maracuyá", 2.50, False, 400)

    # 4. Agregar los objetos creados a la lista administrada por el restaurante
    mi_restaurante.agregar_producto(platillo_uno)
    mi_restaurante.agregar_producto(platillo_dos)
    mi_restaurante.agregar_producto(bebida_uno)
    mi_restaurante.agregar_producto(bebida_dos)

    # 5. Demostración de validación del encapsulamiento (intentos de cambiar precios)
    print("--- Demostración de Modificación y Validación de Precios ---")
    platillo_uno.cambiar_precio(13.25)   # Cambio válido
    bebida_uno.cambiar_precio(-1.50)    # Intento inválido (Disparará el mensaje de error)

    # 6. Mostrar la información registrada de forma organizada en consola
    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    ejecutar_sistema()