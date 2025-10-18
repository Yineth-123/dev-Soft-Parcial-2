# dev-Soft-Parcial-2
**Nombre:** Karen Yineth Ibarra Guzman 
**Código:** 408965
# Decisiones de Diseño:
Este proyecto consiste en el desarrollo de una API REST para la gestión de tareas (Tasks) utilizando el framework FastAPI. La API permite crear, listar, actualizar el estado, eliminar y obtener tareas vencidas, todo mediante almacenamiento en memoria (InMemory), ideal para pruebas y desarrollo académico.
* 2. Arquitectura del Proyecto

El sistema fue diseñado bajo principios de arquitectura limpia y separación de capas para garantizar claridad, escalabilidad y mantenibilidad.

| Capa                            | Función Principal                                    |
| ------------------------------- | ---------------------------------------------------- |
| **Controller (Router)**         | Recibe las peticiones HTTP y devuelve las respuestas |
| **Service**                     | Contiene la lógica del negocio y las validaciones    |
| **Repository (InMemory)**       | Almacena los datos temporalmente en una lista        |
| **DTO (Data Transfer Objects)** | Estandariza y valida los datos de entrada y salida   |
| **Model**                       | Define la entidad principal (Task)                   |

* 3. Entidad Principal: Task
Representa una actividad pendiente a realizar.

| Atributo      | Tipo de Dato | Descripción                             |
| ------------- | ------------ | --------------------------------------- |
| `id`          | Entero       | Identificador único                     |
| `title`       | String       | Título de la tarea                      |
| `description` | String       | Detalle de la tarea                     |
| `due_date`    | DateTime     | Fecha y hora límite                     |
| `status`      | Enum         | Estado de la tarea (PENDING, COMPLETED) |
| `created_at`  | DateTime     | Fecha automática de creación            |

* 4. Endpoints Implementados
     
| Método     | Ruta                      | Descripción                    |
| ---------- | ------------------------- | ------------------------------ |
| **POST**   | `/tasks`                  | Crear una nueva tarea          |
| **GET**    | `/tasks`                  | Listar todas las tareas        |
| **GET**    | `/tasks/overdue`          | Listar tareas vencidas         |
| **PATCH**  | `/tasks/{task_id}/status` | Cambiar el estado de una tarea |
| **DELETE** | `/tasks/{task_id}`        | Eliminar una tarea             |
| **GET**    | `/`                       | Ruta raíz de bienvenida        |

* 5. Justificación del Diseño
Opté por utilizar FastAPI debido a su velocidad, facilidad de estructuración por capas y compatibilidad con documentación automática Swagger.
El uso de almacenamiento InMemory permite hacer pruebas sin depender de bases de datos reales, manteniendo el sistema simple pero funcional.

✅ Beneficios del diseño:

   * Separación clara de responsabilidades.
   * Código mantenible y escalable.
   * Fácil de convertir a base de datos real en el futuro.
   * Ideal para evaluar lógica de negocio.


* Enlace de video:
     *  Cómo correr el proyecto. 
     *  Explicación decisiones de diseño. 
     *  Pruebe cada endpoint y evidencie su funcionamiento
     

## a. Cómo correr el proyecto

* Clonar el repositorio desde GitHub.

* Activar el entorno virtual:
.\venv\Scripts\activate

* Instalar dependencias (si aplica):
pip install -r requirements.txt

* Ejecutar el servidor:
uvicorn main:app --reload

* Abrir el navegador en:
http://127.0.0.1:8000/docs

