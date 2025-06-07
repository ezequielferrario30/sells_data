# 📝 Proyecto Integrador de Data Engineering – README

---

## 1. ¿Qué se hizo?

Se diseñó e implementó un sistema completo de análisis de ventas para una empresa de comestibles con múltiples sucursales, simulando un entorno real de ingeniería de datos.  
El sistema abarca desde la carga de datos desde archivos CSV a una base de datos MySQL, el modelado orientado a objetos en Python, la aplicación de patrones de diseño (Factory, Singleton), la construcción de objetos SQL avanzados (función, trigger, procedimiento almacenado, vista, índice), la ejecución de consultas SQL avanzadas (CTEs y funciones de ventana), la integración total desde Python, la visualización analítica, y la validación con testing automatizado y cobertura profesional.

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
│   └── ...
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
- **Decisión**: Es preferible a carga manual, minimiza errores y maximiza performance y auditabilidad.

### Modelado orientado a objetos (POO)

- **Clases**: Cada entidad de negocio (producto, cliente, venta, etc.) es una clase Python con encapsulamiento, constructores y métodos de negocio.
- **Ventajas**: Centraliza reglas, facilita validaciones y cambios futuros del modelo.
- **Decisión**: Refleja prácticas reales de desarrollo profesional y escalable.

### Patrones de diseño: comparación y justificación

| Patrón         | Ubicación / Aplicación                 | ¿Para qué se usa?                                        | Ventajas principales                                                                      | ¿Por qué se eligió sobre otros?                          |
| -------------- | -------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Factory Method | src/models/factory.py                  | Centralizar y estandarizar creación de entidades         | Modularidad, escalabilidad, mantenimiento, nuevas fuentes de datos fáciles                | Más simple/flexible que Abstract Factory o Builder        |
| Singleton      | src/database.py, src/database_sqlalchemy.py | Garantizar instancia única de conexión a la base de datos | Eficiencia, seguridad, evita fugas de recursos, punto de acceso único                     | Más simple/directo que Object Pool o Service Locator      |

**Reflexión:**  
Se priorizó escalabilidad, mantenibilidad y claridad. Las alternativas fueron evaluadas y se eligió lo óptimo para la escala y el dominio, siempre alineado a buenas prácticas.

---

### Objetos SQL y consultas avanzadas

- **Función**: `calcular_descuento` centraliza la lógica de descuentos por tipo de cliente.
- **Vista**: `ventas_mensuales_ciudad_categoria` para reportes segmentados y dashboards rápidos.
- **Procedimiento almacenado**: `registrar_venta` estandariza la carga de ventas, permite validar y auditar.
- **Trigger**: registra logs de ventas en tiempo real y aplica reglas automáticas, asegurando trazabilidad.
- **Índice**: mejora la performance en consultas frecuentes sobre ventas.
- **Consultas avanzadas**: uso intensivo de CTEs y funciones de ventana (`RANK`, `ROW_NUMBER`, `DENSE_RANK`, `SUM() OVER`), mostrando dominio de SQL avanzado y analítica real.

**Decisión**:  
El diseño de estos objetos responde a necesidades analíticas y de negocio reales, y demuestra cómo el modelo puede evolucionar con nuevas reglas.

---

### Integración total desde Python

- Todo el pipeline (creación y consulta de objetos SQL, ejecución de funciones/procedimientos, visualizaciones, logs) se realiza desde Python usando SQLAlchemy y pandas.
- Demuestra automatización, reproducibilidad, y capacidad para construir pipelines robustos en ingeniería de datos.

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
- Notebooks integradores (`integracion_final.ipynb`, `integracion_objetos_sql.ipynb`) muestran outputs, explicaciones y justificaciones, cumpliendo con los criterios de evaluación y prácticas profesionales.

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

- No se suben datos sensibles ni entorno virtual, cumpliendo estándares de seguridad y profesionalismo.

- Cada cambio está registrado para trazabilidad y auditoría.

---

## Lecciones aprendidas

- La importancia de la **modularidad y el versionado**: Organizar el código y los SQL en carpetas bien definidas acelera el desarrollo y el debugging.
- **Automatizar la carga y modelado** desde el inicio reduce errores y permite iterar más rápido sobre los datos.
- La **integración entre Python y SQL** permite construir pipelines reproducibles y profesionales, facilitando el análisis y la visualización de los resultados.
- El uso de **patrones de diseño** no es solo teórico: hacen el sistema mucho más mantenible, especialmente cuando los requerimientos cambian.
- Los **tests de integración** ayudan a detectar rápidamente cualquier ruptura en la lógica entre objetos SQL y código Python, ahorrando tiempo en debugging.
- Documentar **decisiones y supuestos** en README y notebooks hace que el trabajo sea entendible y defendible ante cualquier auditoría.



---

## FAQ / Troubleshooting

**¿Qué hago si el script SQL da error de permisos o ruta?**  
Verifica que el usuario de MySQL tenga permisos de `FILE`, y que la ruta de los CSV sea correcta para el sistema operativo.

**¿Por qué me sale “Access denied for user” al correr desde Python?**  
Chequea que las credenciales y el nombre de la base estén bien configurados en `.env` y que ese usuario tenga permisos suficientes.

**¿Cómo sé si los triggers y funciones están activos?**  
Puedes consultar `SHOW TRIGGERS;` y `SHOW FUNCTION STATUS WHERE Db = 'ventas';` en MySQL Workbench.  
Además, el notebook muestra los logs generados por triggers.

**¿Puedo cambiar o ampliar el modelo de datos?**  
Sí. Si agregas una nueva lógica de negocio (por ejemplo, tipos de productos), puedes agregar columnas y adaptar los modelos y scripts siguiendo el mismo enfoque modular.

**¿Cómo veo los outputs si corro los notebooks en otro entorno?**  
Asegúrate de ejecutar cada celda. Si el entorno no tiene las librerías, instala con `pip install -r requirements.txt` y verifica la conexión a la base.




---

# 6. Reflexión final

Cada decisión de diseño se fundamentó en maximizar mantenibilidad, eficiencia, escalabilidad y claridad, usando patrones y técnicas seleccionadas por sus ventajas reales y justificadas en cada punto.
La solución refleja tanto la aplicación del conocimiento técnico como la capacidad de razonar y justificar decisiones, habilidades clave para un ingeniero de datos profesional.

El resultado es un sistema reproducible, robusto, seguro y defendible, alineado con las mejores prácticas del sector y las expectativas del negocio.