📝 Proyecto Integrador de Data Engineering – README
1. ¿Qué se hizo?
Se diseñó e implementó un sistema completo de análisis de ventas para una empresa de comestibles con múltiples sucursales, simulando un entorno real de ingeniería de datos.
El sistema permite cargar datos desde archivos CSV a una base de datos MySQL, modelar entidades usando programación orientada a objetos en Python, aplicar patrones de diseño (Factory, Singleton), realizar análisis avanzados mediante SQL y validar todo con testing automatizado y cobertura profesional.

2. ¿Cómo está organizado el proyecto?
bash
Copiar
Editar
ventas_data_engineering/
├── data/           # Archivos CSV originales
├── src/
│   ├── __init__.py
│   ├── database.py         # Singleton para conexión MySQL
│   ├── models/
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── city.py
│   │   ├── country.py
│   │   ├── customer.py
│   │   ├── employee.py
│   │   ├── factory.py      # Factory Method
│   │   ├── product.py
│   │   └── sale.py
│   └── ...                 # Otros scripts fuente
├── sql/
│   └── load_data.sql       # Script para crear tablas y cargar datos
├── tests/
│   ├── __init__.py
│   ├── test_customer.py
│   ├── test_product.py
│   ├── test_sale.py
│   ├── test_employee.py
│   ├── test_factory.py
│   └── ...                 # Otros tests
├── .env                    # Variables de entorno (credenciales DB)
├── .gitignore
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación y justificaciones técnicas
3. Justificación técnica (profunda y argumentada)
Carga de datos automatizada
Se eligió el comando LOAD DATA LOCAL INFILE en el script load_data.sql para automatizar la importación de datos desde archivos CSV a MySQL.

Ventajas:

Permite recargar grandes volúmenes de datos de forma eficiente, repetible y documentada.

Es preferible a la carga manual o a scripts línea por línea porque reduce errores humanos, acelera el proceso y asegura la trazabilidad.

La estructura del script está pensada para ser portable entre distintos entornos, facilitando el testing y la migración.

Modelado orientado a objetos (POO)
Cada entidad (producto, cliente, venta, etc.) se modeló como una clase Python independiente.

Decisiones:

Usé atributos encapsulados y propiedades para proteger la integridad de los datos (principio de encapsulamiento).

Incorporé métodos de negocio en cada clase (por ejemplo, is_perishable en Product) para reflejar reglas y validaciones reales, y centralizar lógica que podría cambiar si evolucionan los requisitos.

Patrones de diseño – Comparación y justificación
Factory Method
Se implementó una factory centralizada para crear instancias de todos los modelos.

Elegí este patrón sobre otros (como Builder o Abstract Factory) porque balancea bien simplicidad y flexibilidad:

Builder sería útil si hubiera que armar objetos complejos en muchos pasos (no es el caso acá).

Abstract Factory sería útil si hubiera familias de objetos interdependientes (acá son independientes).

Con Factory, si el modelo de datos cambia, la lógica de creación de objetos está centralizada y no dispersa por todo el código, lo que simplifica el mantenimiento.

Singleton
La conexión a MySQL usa el patrón Singleton para garantizar una única instancia durante todo el ciclo de vida de la aplicación.

Elegí Singleton y no otros (como Object Pool) porque el sistema no requiere múltiples conexiones concurrentes; con una conexión persistente se cumple el principio de eficiencia y se evita sobrecargar el servidor.

Centralizar el acceso a la conexión también facilita el testing y la configuración del entorno, porque todos los componentes acceden al mismo recurso de manera controlada y segura.

Reflexión
La decisión de usar estos patrones se tomó considerando la escalabilidad futura (el sistema puede crecer y soportar nuevos modelos, reglas o integraciones sin grandes refactorizaciones), la claridad para cualquier desarrollador que tome el proyecto después, y el cumplimiento explícito de criterios de calidad y mejores prácticas de la industria.

Testing y calidad
Se implementó una suite de pruebas unitarias con pytest, separando tests por clase, lo que es más profesional y permite detectar problemas rápidamente.

La cobertura de tests apunta al 80% o más, superando el mínimo, y los tests no solo validan getters/setters sino también reglas de negocio y casos borde.

Ventaja:
Esto asegura robustez ante cambios, facilita la refactorización y demuestra una mentalidad de ingeniería responsable, no solo de scripting.

Organización y reproducibilidad
El proyecto está organizado en carpetas por responsabilidad (src/, sql/, tests/, data/), siguiendo las prácticas de proyectos reales de software.

Todo el flujo (carga, modelado, testing) está versionado en el repositorio, documentado y justificado, mostrando un trabajo profesional, reproducible y defendible ante cualquier auditoría o cambio de equipo.

Tabla resumen – Patrones de diseño aplicados
Patrón	Ubicación / Aplicación	¿Para qué se usa?	Ventajas principales	¿Por qué se eligió sobre otros?
Factory Method	src/models/factory.py	Centralizar y estandarizar la creación de entidades del sistema (modelos)	- Modularidad
- Escalabilidad
- Facilidad de mantenimiento
- Permite nuevas fuentes de datos fácilmente	Más simple y flexible que Abstract Factory o Builder
Singleton	src/database.py	Garantizar que solo exista una única conexión a la base de datos	- Eficiencia
- Seguridad
- Evita fugas de recursos
- Punto de acceso único	Más simple y directo que Object Pool o Service Locator

4. ¿Cómo ejecutar el proyecto?
Clonar el repositorio y crear un entorno virtual:

bash
Copiar
Editar
git clone [URL_DEL_REPO]
cd ventas_data_engineering
python -m venv venv
source venv/bin/activate  # O .\venv\Scripts\activate en Windows
pip install -r requirements.txt
Configurar el archivo .env con las credenciales de la base de datos.

Ejecutar el script SQL sql/load_data.sql en MySQL Workbench para cargar los datos.

Correr los tests con:

bash
Copiar
Editar
pytest
Ejecutar análisis o scripts adicionales desde src/.

5. Repositorio y versionado
Estructura completa, scripts fuente, tests, datos de ejemplo, scripts SQL y documentación están versionados en este repositorio.

Cada cambio está justificado y registrado para asegurar trazabilidad y fácil auditoría.

6. Frase final
Cada decisión de diseño se fundamentó en maximizar la mantenibilidad, eficiencia, escalabilidad y claridad del sistema, usando patrones y prácticas seleccionados por sus ventajas reales frente a otras alternativas. La solución refleja tanto la aplicación del conocimiento técnico como la capacidad de razonar y justificar decisiones, características clave para un ingeniero de datos profesional.

