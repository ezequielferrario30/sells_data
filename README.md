📝 Proyecto Integrador de Data Engineering – README
1. ¿Qué se hizo?
Se diseñó e implementó un sistema completo de análisis de ventas para una empresa de comestibles con múltiples sucursales, simulando un entorno real de ingeniería de datos.
El sistema permite cargar datos desde archivos CSV a una base de datos MySQL, modelar entidades usando programación orientada a objetos en Python, aplicar patrones de diseño (Factory, Singleton), realizar análisis avanzados mediante SQL y validar todo con testing automatizado y cobertura profesional.

2. ¿Cómo está organizado el proyecto?

ventas_data_engineering/
├── venv/                   # Entorno virtual (EXCLUIDO del repositorio)
├── data/                   # CSVs originales (input)
│   ├── categories.csv
│   ├── cities.csv
│   ├── countries.csv
│   ├── customers.csv
│   ├── employees.csv
│   ├── products.csv
│   └── sales.csv
│
├── src/                    # Código fuente principal del proyecto
│   ├── __init__.py
│   ├── main.py             # Punto de entrada del sistema
│   ├── database.py         # Conexión a MySQL (Singleton clásico)
│   ├── database_sqlalchemy.py # Conexión a MySQL usando SQLAlchemy (Singleton)
│   ├── load_data.py        # Carga los CSV a la base de datos
│   └── models/             # Clases del dominio (POO)
│       ├── __init__.py
│       ├── category.py
│       ├── city.py
│       ├── country.py
│       ├── customer.py
│       ├── employee.py
│       ├── product.py
│       ├── sale.py
│       └── factory.py      # Factory Method centralizado
│
├── sql/                    # Scripts SQL (carga, objetos SQL, consultas)
│   ├── load_data.sql
│   ├── create_views.sql
│   ├── create_procedures.sql
│   ├── create_triggers.sql
│   └── analysis_queries.sql
│
├── tests/                  # Pruebas unitarias (pytest, un archivo por clase/lógica)
│   ├── __init__.py
│   ├── test_customer.py
│   ├── test_product.py
│   ├── test_sale.py
│   ├── test_factory.py
│   ├── test_database_sqlalchemy.py
│   └── ...
│
├── integracion_final.ipynb # Notebook integrador (conexión, queries, patrones, tests)
├── .env                    # Variables de entorno (NO versionado)
├── .gitignore              # Ignorar venv/, .env, etc.
├── requirements.txt        # Librerías necesarias
└── README.md               # Documentación del proyecto


3. Justificación técnica y decisiones clave
Carga de datos automatizada
Se implementó el script load_data.sql con LOAD DATA LOCAL INFILE para importar eficientemente los datos desde los CSV a MySQL.

Permite recargar grandes volúmenes, es reproducible y portable entre entornos.

Se eligió este enfoque sobre la carga manual o scripts por filas porque minimiza errores humanos y maximiza la trazabilidad.

Modelado orientado a objetos (POO)
Cada entidad de negocio (producto, cliente, venta, etc.) se modeló como una clase Python independiente, aplicando encapsulamiento, constructores claros y métodos de negocio relevantes (ejemplo: is_perishable en Product).

Esto permite centralizar reglas y validaciones, facilitando cambios futuros si evolucionan los requisitos del negocio.

Patrones de diseño: comparación y justificación
Factory Method
Implementado en src/models/factory.py para centralizar y estandarizar la creación de instancias de modelos.

Se prefirió sobre Builder o Abstract Factory por ser más simple y flexible para modelos independientes.

Si el modelo de datos cambia, basta ajustar la Factory, manteniendo el resto del código limpio.

Singleton
Usado en la conexión a la base (database.py y database_sqlalchemy.py), asegura una única instancia viva en todo el ciclo del sistema, evitando fugas de recursos y mejorando la eficiencia.

Más simple y directo que Object Pool para ETLs, scripts y aplicaciones no concurrentes.

Centraliza la configuración y facilita el testing.

Reflexión sobre patrones
“Las elecciones de patrones priorizaron la escalabilidad, mantenibilidad y claridad. Se compararon alternativas y se eligió lo óptimo para la escala y el dominio, siempre alineados a mejores prácticas profesionales.”

----

Testing y calidad
Se desarrolló una suite de tests unitarios con pytest, separando un archivo por clase y lógica, alcanzando una cobertura >80%.

Los tests validan tanto getters/setters como lógica de negocio y la correcta aplicación de los patrones de diseño (ejemplo: Singleton siempre retorna la misma instancia, Factory genera el tipo correcto).

Esto asegura robustez, permite detectar errores rápidamente y respalda futuras refactorizaciones.

-----

Seguridad y buenas prácticas
Las credenciales de la base se almacenan únicamente en el archivo .env, que está en el .gitignore y nunca se sube al repositorio.

El código jamás expone credenciales; usa os.getenv() y carga variables seguras con python-dotenv.

El proyecto es seguro, portable y fácil de configurar en cualquier entorno.

Organización y reproducibilidad
El proyecto está ordenado por responsabilidad, siguiendo prácticas reales de ingeniería de datos.

Los scripts, notebooks, pruebas y SQL están versionados y documentados, haciendo el sistema profesional y defendible ante auditorías o equipos nuevos.

El notebook integracion_final.ipynb demuestra la integración real, con outputs visibles.


-----

Tabla resumen – Patrones de diseño aplicados
Patrón	Ubicación / Aplicación	¿Para qué se usa?	Ventajas principales	¿Por qué se eligió sobre otros?
Factory Method	src/models/factory.py	Centralizar y estandarizar la creación de entidades del sistema (modelos)	- Modularidad
- Escalabilidad
- Facilidad de mantenimiento
- Permite nuevas fuentes de datos fácilmente	Más simple y flexible que Abstract Factory o Builder
Singleton	src/database.py,
src/database_sqlalchemy.py	Garantizar que solo exista una única conexión a la base de datos	- Eficiencia
- Seguridad
- Evita fugas de recursos
- Punto de acceso único	Más simple y directo que Object Pool o Service Locator



4. ¿Cómo ejecutar el proyecto?
Clonar el repositorio y crear un entorno virtual:

```

git clone [URL_DEL_REPO]
cd ventas_data_engineering
python -m venv venv
source venv/bin/activate  # O .\venv\Scripts\activate en Windows
pip install -r requirements.txt


```

Configurar el archivo .env con las credenciales de la base de datos.

Ejecutar el script SQL sql/load_data.sql en MySQL Workbench para cargar los datos.

Correr los tests con:

```
pytest

```

Ejecutar el notebook integrador integracion_final.ipynb para ver la integración completa (conexión, queries, patrones, pruebas, outputs).

Explorar o ejecutar scripts adicionales desde src/.


5. Repositorio y versionado
Todo el código, scripts, tests, SQL y documentación están versionados y justificados.

No se suben datos sensibles ni archivos de entorno, cumpliendo estándares de seguridad y profesionalismo.

Cada cambio está registrado para trazabilidad y auditoría.


6. Reflexión final
“Cada decisión de diseño se fundamentó en maximizar la mantenibilidad, eficiencia, escalabilidad y claridad del sistema, usando patrones y prácticas seleccionados por sus ventajas reales frente a otras alternativas. La solución refleja tanto la aplicación del conocimiento técnico como la capacidad de razonar y justificar decisiones, características clave para un ingeniero de datos profesional.”