# dev-Soft-Parcial-2
**Nombre:** Karen Yineth Ibarra Guzman 
**Código:** 408965
* Decisiones de Diseño:
  * Tecnología elegida y razón:
     * Elegí desarrollar el proyecto utilizando Python con el framework FastAPI, por ser una tecnología moderna, ligera y con soporte para documentación automática mediante OpenAPI/Swagger. Además, FastAPI permite implementar validaciones automáticas con Pydantic, lo que facilita garantizar la integridad de los datos que ingresan al sistema. También permite una arquitectura escalable y buenas prácticas sin complejidad adicional.

  * Arquitectura utilizada:
     * Se implementó una arquitectura en capas siguiendo el patrón Controller → Service → Repository. Los controllers únicamente reciben las solicitudes HTTP y delegan la lógica. El service contiene las reglas de negocio, como validación de estados y fechas. El repository es responsable del acceso a datos mediante SQLAlchemy, encapsulando completamente la interacción con la base de datos. Esta arquitectura garantiza alta cohesión, bajo acoplamiento y cumplimiento con los requisitos del parcial.
* Enlace de video:
     *  Cómo correr el proyecto. 
     *  Explicación decisiones de diseño. 
     *  Pruebe cada endpoint y evidencie su funcionamiento
     # Parcial FastAPI - Gestión de Tareas


## 🧠 Decisiones de diseño
Elegí **Python + FastAPI** porque permite crear APIs rápidas y bien estructuradas con validación automática.  
Usé arquitectura **Controller → Service → Repository**, para mantener responsabilidades separadas:
- **Controller:** maneja rutas y peticiones.
- **Service:** contiene reglas de negocio (validaciones, estados permitidos, etc.).
- **Repository:** maneja la base de datos (SQLite) usando SQLAlchemy.

## ⚙️ Cómo correr el proyecto
1. Crear entorno virtual y activar:
   ```bash
   python -m venv venv
   venv\Scripts\activatevenv
   venv\Scripts\activate

