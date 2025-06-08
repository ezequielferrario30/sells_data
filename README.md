# 📝 Proyecto Integrador DE – README

---

## 1. ¿Qué hice?

Se diseñó e implementó un sistema completo de análisis de ventas para una startup con varias sucursales.
El objetivo es implementar un sistema que procese archivos de ventas generados diariamente, organice la informacion en una base de daos y permita  realizar analisis.

Este sistema abarca desde la carga de datos desde archivos CSV a una base de datos MySQL, el modelado orientado a objetos en Python, la aplicación de patrones de diseño (Factory, Singleton), la construcción de objetos SQL avanzados (función, trigger, procedimiento almacenado, vista, índice), la ejecución de consultas SQL avanzadas (CTEs y funciones de ventana), la integración total desde Python, la visualización analítica, y la validación con testing automatizado y cobertura profesional.

---

## 2. ¿Cómo está organizado el proyecto?

```
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
│   ├── main.py
│   ├── database.py
│   ├── database_sqlalchemy.py
│   ├── load_data.py
│   └── models/
│       ├── __init__.py
│       ├── category.py
│       ├── city.py
│       ├── country.py
│       ├── customer.py
│       ├── employee.py
│       ├── product.py
│       ├── sale.py
│       └── factory.py
│
├── sql/
│   ├── load_data.sql
│   ├── create_functions.sql
│   ├── create_views.sql
│   ├── create_procedures.sql
│   ├── create_triggers.sql
│   ├── create_indexes.sql
│   └── analysis_queries.sql
│
├── tests/
│   ├── __init__.py
│   ├── test_customer.py
│   ├── test_product.py
│   ├── test_sale.py
│   ├── test_factory.py
│   ├── test_database_sqlalchemy.py
│   ├── test_integracion_objetos_sql.py
│   
│
├── integracion_final.ipynb         # Notebook de integración Avance 1 (base, modelos, queries, patrones, tests)
├── integracion_objetos_sql.ipynb   # Notebook de integración Avance 2 (objetos SQL, ejecución, visualizaciones)
├── .env
├── .gitignore
├── requirements.txt
└── README.md

```



---

## 3. Justificación técnica y decisiones clave

### Carga de datos automatizada

- **Script**: `load_data.sql` con `LOAD DATA LOCAL INFILE` para importar eficientemente los CSV.
- **Ventajas**: Recarga grandes volúmenes, reproducible, portable y trazable. Evita errores manuales.

### Modelado orientado a objetos (POO)

- **Clases**: Cada entidad de negocio (producto, cliente, venta, etc.) es una clase Python con encapsulamiento, constructores y métodos de negocio.
- **Ventajas**: Centraliza las reglas, facilita validaciones y cambios futuros del modelo.

### Patrones de diseño: comparación y justificación

| Patrón         | Ubicación / Aplicación                 | ¿Para qué se usa?                                        | Ventajas principales                                                                      | ¿Por qué se eligió sobre otros?                          |
| -------------- | -------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Factory Method | src/models/factory.py                  | Centralizar y estandarizar creación de entidades         | Modularidad, escalabilidad, mantenimiento, nuevas fuentes de datos fáciles                | Más simple/flexible que  Factory o Builder        |
| Singleton      | src/database.py, src/database_sqlalchemy.py | Garantizar instancia única de conexión a la base de datos | Eficiencia, seguridad, evita fugas de recursos, punto de acceso único                     | Más simple/directo que Object Pool o Service Locator      |

Factory me permite tener un solo lugar en el código donde se crean los objetos de mi negocio: productos, clientes, ventas, etc.
Si mañana cambia la forma en que se crea un cliente (por ejemplo, agrego un campo, o cambio el tipo de dato), solo modifico el método Factory, no tengo que buscar en todo el código dónde instancio clientes.

También me sirve para automatizar la creación de objetos a partir de datos (como dicts de un CSV).
Por ejemplo, puedo leer una fila del CSV y decirle a la Factory: “creame un producto con estos datos” y listo, sin repetir lógica.

Además, si algún día tengo diferentes versiones de una entidad (por ejemplo, “ClienteVIP” o “ProductoPremium”), la Factory puede decidir a quién instanciar según el contexto.

Use este metodo para tener el código centralizado, ordenado y fácil de mantener, siguiendo buenas prácticas de diseño. Me parece mucho mejor utilizar este patron porque es mucho mas simple y eficiente para lo que tenia que hacer, al no ser objetos muy complejos  me parecio mejor que Builder y tampoco tengo familia entera de objetos como para usar Abstact Factory.


La parte de las conexiones de datos creo que es una de las mas importantes:


- Si abro muchas conexiones a la vez, puedo sobrecargar la base y hacer lento el sistema.

- Si cada parte del programa crea su propia conexión, se complica la gestión y debugging.

Singleton garantiza que solo haya una única conexión  en todo el sistema.
Cuando cualquier parte del código necesita conectarse, simplemente usa esa conexión ya creada.

Esto hace el código más eficiente, seguro y fácil de testear, porque si necesito cambiar algo de la conexión (por ejemplo, la base de datos, usuario, etc.), lo hago en un solo lugar y se aplica en toda la aplicación.

Usar este metodo me permiteque la conexión sea única y controlada, evitando errores y mejorando el rendimiento del sistema. Si bien hay otros metodos, en este caso solo tenia que cargar csv, es decir, datos de un mismo tipo por lo que me parecio lo mas simple y eficiente para no elegir otro patron.


----

### Escalabilidad

El foco en la escalabilidad estuvo puesto todo el tiempo.

Es por ello que se le dio vital importancia a la modularizacion:

- Separacion por carpetas de forma clara (Data para la fuente de datos, src para el codigo en python, sql para los scripts de SQL, test para los tets)

- Cada entidad de negocio tiene su propio archivo para facilitar los cambios, a s u vez toda la logica de conexion a la base de datos estan en modulos separados como tambien los funciones y procedimientos en SQL

- Se aplicaron patrones de diseño como Factory Method y Singleton

De esta manera el codigo es mucho mas facil de entender, mantener y ampliar ya que  al tener todo modulado por parte varias personas o equipos pueden trabajar al mismo tiempo.


---
### Objetos SQL y consultas avanzadas

- **Función**: `calcular_descuento` centraliza la lógica de descuentos por tipo de cliente.
- **Vista**: `ventas_mensuales_ciudad_categoria` para reportes segmentados y dashboards rápidos.
- **Procedimiento almacenado**: `registrar_venta` estandariza la carga de ventas, permite validar y auditar.
- **Trigger**: registra logs de ventas en tiempo real y aplica reglas automáticas, asegurando trazabilidad.
- **Índice**: mejora la performance en consultas frecuentes sobre ventas.
- **Consultas avanzadas**: uso intensivo de CTEs y funciones de ventana (`RANK`, `ROW_NUMBER`, `DENSE_RANK`, `SUM() OVER`).

**Decisión**:  
El diseño de estos objetos responde a necesidades analíticas y de negocio reales, y demuestra cómo el modelo puede evolucionar con nuevas reglas.

---

### Integración total desde Python

- Todo el pipeline (creación y consulta de objetos SQL, ejecución de funciones/procedimientos, visualizaciones, logs) se realiza desde Python usando SQLAlchemy y pandas en conjunto con otras librerias.


---

### Visualizaciones analíticas

- Incluye gráficos de:  
    - Evolución de ventas mensuales  
    - Top productos y clientes  
    - Distribución por ciudad y tipo de cliente  
    - Evolución por categoría  
- Las visualizaciones apoyan la interpretación de los resultados y la toma de decisiones estratégicas.

---

### Testing y calidad

- Tests unitarios y de integración con `pytest`:
    - Validan modelos, lógica de negocio, patrones y objetos SQL.
    - Chequean que los triggers y funciones trabajan en conjunto y que la integración Python-SQL es correcta.
- Asegura robustez, calidad, y fácil refactorización.

---

### Seguridad y buenas prácticas

- Credenciales sólo en `.env` (no versionado).
- Código seguro, portable y fácil de configurar.
- `.gitignore` bien configurado, sin datos sensibles ni entorno virtual.

---

### Organización y reproducibilidad

- Proyecto ordenado por responsabilidad, versión controlada y documentada.
- Notebooks integradores (`integracion_final.ipynb`, `integracion_objetos_sql.ipynb`) muestran outputs, explicaciones y justificaciones. En el primero se hizo la parte de P2 y en el segundo el de P3.

---

## 4. ¿Cómo ejecutar el proyecto?

**1. Clonar el repositorio y crear un entorno virtual:**
```bash
git clone [URL_DEL_REPO]
cd ventas_data_engineering
python -m venv venv
source venv/bin/activate  # O .\venv\Scripts\activate en Windows
pip install -r requirements.txt
```

2. Configurar el archivo .env con credenciales de la base.

3. Ejecutar el script SQL de carga:

Desde MySQL Workbench: abrir y ejecutar sql/load_data.sql y los demás scripts de sql/ para crear funciones, triggers, vistas, índices y procedimientos.

4. Correr los tests:

```

pytest


```

5. Ejecutar los notebooks:

integracion_final.ipynb (avance 1, integración base y modelos)

integracion_objetos_sql.ipynb (avance 2, objetos SQL, ejecuciones, outputs y visualizaciones)

6. Explorar o ejecutar scripts adicionales desde src/.

----- 

# 5. Repositorio y versionado

- Todo el código, SQL, tests, notebooks y documentación están versionados y justificados.

- No  hay datos sensibles ni entorno virtual subido, cumpliendo estándares de seguridad y profesionalismo.

- Cada cambio está registrado para trazabilidad y auditoría.

---

## Lecciones aprendidas

- La importancia de la **modularidad y el versionado**: Organizar el código y los .sql en carpetas bien definidas hace que sea mas comodo y por ende mas facil el desarrollo y el debugging.
- **Automatizar la carga y modelado** desde el inicio limita errores y permite iterar más rápido sobre los datos.
- La **integración entre Python y SQL** permite construir pipelines reproducibles y profesionales, facilitando el análisis y la visualización de los resultados, para luego integrar con librerias como pandas.
- El uso de **patrones de diseño**  hacen el sistema mucho más mantenible, especialmente cuando los requerimientos cambian.
- Los **tests de integración** ayudan a detectar rápidamente cualquier ruptura en la lógica entre objetos SQL y código Python, ahorrando tiempo en debugging.
- Documentar **decisiones y supuestos** en README y notebooks hace que el trabajo sea entendible y defendible ante cualquier proceso de revisado




# 6. Reflexión final

Cada decisión de diseño se fundamentó en maximizar mantenibilidad, eficiencia, escalabilidad y claridad, usando patrones y técnicas seleccionadas por sus ventajas reales y justificadas en cada punto.
La solución refleja tanto la aplicación del conocimiento técnico como la capacidad de razonar y justificar decisiones, habilidades clave para un ingeniero de datos profesional.

El resultado es un sistema reproducible, robusto, seguro y defendible, alineado con las mejores prácticas del sector y las expectativas del negocio.