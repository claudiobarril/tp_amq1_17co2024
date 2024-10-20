# tp_amq1_17co2024

# Evaluación del Curso

La evaluación de los conocimientos impartidos durante las clases será a modo de entrega de trabajo práctico final. La entrega de trabajo final de la cursada comprende una investigación, desarrollo y resultados finales basados en un set de datos a elección por el grupo (máximo 6 personas).

## Criterios de Aprobación

Los criterios de aprobación son los siguientes:

1. **Trabajo en Grupo:** 
   - Obligación de trabajar en grupo mínimo de 2 y máximo de 6 personas.
   - Excepciones se pueden hacer mediante un correcto justificativo.

2. **Fuentes de Información:**
   - Cada TP debe citar la fuente de información de evaluación.
   - Se debe especificar de dónde se obtuvieron los datos.

3. **Formato de Entrega:**
   - Preferentemente en notebook de iPython (formato `.ipynb`).
   - También se acepta entrega mediante un documento en Google Colab.

4. **Propuesta de Investigación:**
   - Contendrá la propuesta de investigación en los datos.
   - Citar el porqué de la evaluación.
   - Explicar qué se pretende encontrar o descubrir con dicha investigación.

5. **Selección del Algoritmo:**
   - Explicar el porqué de la elección del algoritmo empleado.
   - Justificar cómo se llegó a esa elección por sobre otras opciones.

6. **Resultados y Métricas:**
   - Expresar de manera clara el resultado de la investigación.
   - Aportar las métricas necesarias para comprender el desempeño del algoritmo elegido.

7. **Reproducibilidad:**
   - El entregable debe incluir el código acompañado para su reproducibilidad.

8. **Reflexión y Propuestas Futuras:**
   - En su cierre, debe dar una reflexión de la investigación.
   - Proponer nuevos caminos de resolución en caso de ser necesario.

## Instrucciones para Ejecutar el Proyecto
### Ejecución con Poetry

1. **Instalar Poetry**: Si no tienes Poetry instalado, sigue las instrucciones [aquí](https://python-poetry.org/docs/#installation).

2. **Clonar el repositorio**:
    ```bash
    git clone git@github.com:claudiobarril/tp_amq1_17co2024.git
    cd tp_amq1_17co2024
    ```

3. **Instalar las dependencias**:
    ```bash
    poetry install
    ```

4. **Iniciar el entorno virtual**:
    ```bash
    poetry shell
    ```

5. **Ejecutar Jupyter Notebook**:
    ```bash
    jupyter lab
    ```
   Abre la notebook deseada en la interfaz de Jupyter.

### Ejecución en Docker
1. **Instalar Docker**: Si no tienes Docker instalado, sigue las instrucciones [aquí](https://docs.docker.com/get-docker/).

2. **Construir la imagen de Docker**:
    ```bash
    docker build -t amq1 .
    ```

3. **Ejecutar el contenedor de Docker**:
    ```bash
    docker run -p 8895:8895 amq1
    ```
   Abre tu navegador y ve a `http://localhost:8895` para acceder a Jupyter Notebook.
