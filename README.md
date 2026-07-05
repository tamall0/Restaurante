Mi nombre es Tayana Maldonado, en este apartado muestro una breve descripción de las mejoras en el programa de Restaurante

## Descripción de la Versión Mejorada: Jerarquía y Pilares POO

Esta nueva versión evoluciona el sistema modular `restaurante_app` enfocándose en la administración especializada de los productos del restaurante.
Se diseñó e implementó una estructura jerárquica que permite aplicar de forma estricta los tres pilares fundamentales de la Programación Orientada
a Objetos (POO):

1. **Herencia:** Se estableció una clase padre general llamada `Producto` que centraliza los atributos compartidos (nombre, precio y disponibilidad).
2. De ella se derivan dos clases hijas altamente especializadas: `Platillo` (que añade control sobre el tiempo de preparación) y `Bebida` (que
3. gestiona el volumen en mililitros), reutilizando el constructor base mediante `super()`.
4. **Encapsulamiento y Validación:** Se protegió el acceso directo al atributo crítico del precio (`__precio`) usando visibilidad privada. Su lectura
5. y modificación se restringen a los métodos de interfaz `obtener_precio()` y `cambiar_precio()`, incluyendo en este último una lógica de validación
6. interna que bloquea e informa en consola si se intentan registrar valores negativos o iguales a cero.
7. **Polimorfismo:** Se sobrescribió el método `mostrar_informacion()` en ambas clases hijas. Esto permite que la clase de servicio `Restaurante`
8. procese una única lista unificada de productos y descubra de manera dinámica en tiempo de ejecución qué formato de impresión aplicar (si el de un
9. plato o el de una bebida) con solo recorrer la colección.

El flujo principal en `main.py` actúa como el entorno de prueba, simulando la creación de los objetos, la verificación de las reglas de negocio de los
precios y la impresión organizada del menú en consola.
