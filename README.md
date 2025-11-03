# Urban Routes - Proyecto de Pruebas Automatizadas

## Descripción del Proyecto
Urban Routes es un proyecto de automatización de pruebas para una aplicación de servicio de taxis. El proyecto implementa pruebas end-to-end que verifican el flujo completo de solicitud de un taxi, desde la selección de la ruta hasta la confirmación del pedido.

## Tecnologías y Técnicas Utilizadas

### Tecnologías
- **Python**: Lenguaje de programación principal
- **Selenium WebDriver**: Framework de automatización de pruebas web
- **pytest**: Framework de pruebas unitarias
- **Chrome WebDriver**: Driver del navegador para pruebas automatizadas

### Técnicas y Patrones de Diseño
- **Page Object Model (POM)**: Patrón de diseño para crear una representación orientada a objetos de las páginas web
- **Explicit Waits**: Técnica para manejar elementos dinámicos y asíncronos
- **Action Chains**: Para simular interacciones complejas del usuario
- **Modularización**: Separación del código en módulos lógicos para mejor mantenibilidad

## Estructura del Proyecto
```
qa-project-Urban-Routes-es/
main.py               # Archivo principal con las pruebas
urban_routes_page.py  # Implementación del Page Object Model
data.py              # Datos de prueba
README.md            # Documentación del proyecto
```

## Funcionalidades Probadas
1. Configuración de dirección de origen y destino
2. Selección de tarifa Comfort
3. Registro de número de teléfono
4. Proceso de pago con tarjeta de crédito
5. Adición de mensajes para el conductor
6. Selección de servicios adicionales (manta, pañuelos)
7. Pedido de extras (helados)
8. Verificación del proceso de búsqueda de taxi
9. Validación de la información del conductor

## Instrucciones para Ejecutar las Pruebas

### Prerrequisitos
1. Python 3.x instalado
2. Google Chrome instalado
3. Conexión a internet estable

### Configuración del Entorno
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Nicholasgl1103/qa-project-Urban-Routes-es.git
   cd qa-project-Urban-Routes-es
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Unix o MacOS:
   source .venv/bin/activate
   ```

3. Instalar las dependencias:
   ```bash
   pip install selenium pytest
   ```

### Ejecución de las Pruebas
Para ejecutar todas las pruebas:
```bash
pytest main.py -v
```

Para ejecutar una prueba específica:
```bash
pytest main.py -v -k test_complete_taxi_order
```

### Resultados de las Pruebas
Las pruebas generarán un informe detallado en la consola, mostrando:
- Número total de pruebas ejecutadas
- Número de pruebas exitosas y fallidas
- Tiempo de ejecución
- Detalles de cualquier error encontrado

## Notas Adicionales
- Las pruebas están diseñadas para ejecutarse en Chrome
- Se utilizan esperas explícitas para manejar elementos dinámicos
- El código incluye manejo de casos especiales como la confirmación del número de teléfono
- Se implementan verificaciones (assertions) en puntos clave del flujo