# Medical Prescription Management System

Este proyecto tiene como objetivo gestionar las prescripciones médicas, permitiendo registrar, buscar, actualizar, eliminar prescripciones y generar informes sobre las prescripciones más frecuentes y la duración promedio de las mismas. Es una herramienta útil para clínicas o consultorios médicos.

## Funcionalidades

El sistema ofrece las siguientes funcionalidades clave:

1. **Registrar una prescripción**: Permite registrar una nueva prescripción médica con detalles como el nombre del paciente, medicamento, dosis, frecuencia, duración y fecha.

2. **Buscar una prescripción**: Permite buscar prescripciones por el nombre del paciente.

3. **Actualizar una prescripción**: Permite actualizar la dosis o la duración de una prescripción existente.

4. **Eliminar prescripciones vencidas**: Permite eliminar prescripciones cuyo período de duración haya expirado.

5. **Generar informes**:
    - Medicamentos más recetados: Muestra los medicamentos que más se han recetado.
    - Duración promedio de las prescripciones: Muestra el promedio de duración de las prescripciones registradas.

6. **Menú interactivo**: Ofrece una interfaz de usuario interactiva en la consola para realizar diversas operaciones con las prescripciones.

## Cómo funciona

El sistema mantiene una lista de diccionarios (`prescriptions`), donde cada diccionario contiene los detalles de una prescripción médica. Cada prescripción tiene los siguientes atributos:

- **patient**: Nombre del paciente.
- **medicine**: Nombre del medicamento recetado.
- **dose**: Dosis del medicamento (por ejemplo, 500mg).
- **frequency**: Frecuencia de toma (por ejemplo, cada 6 horas).
- **duration**: Duración del tratamiento en días.
- **date**: Fecha de la prescripción (en formato YYYY-MM-DD).

Las funciones principales del sistema permiten:

- **preload_prescriptions**: Inicializa la lista de prescripciones con algunos datos predeterminados.

- **register_prescription**: Permite registrar una nueva prescripción, validando que la duración sea un número positivo y que la fecha esté en el formato correcto.

- **search_prescription**: Permite buscar prescripciones por el nombre del paciente.

- **update_prescription**: Permite actualizar la dosis o la duración de una prescripción específica.

- **delete_expired_prescriptions**: Permite eliminar las prescripciones que hayan expirado, preguntando al usuario por confirmación antes de proceder.

- **generate_reports**: Genera un informe con los medicamentos más recetados y la duración promedio de las prescripciones.

- **menu**: Muestra un menú interactivo donde el usuario puede seleccionar qué operación realizar.

## Uso

### Requisitos

Este proyecto requiere Python 3.x para ejecutarse correctamente.

### Ejecución

1. Clona o descarga este repositorio.
2. Ejecuta el archivo `medical_prescription_manager.py` en tu terminal o entorno de desarrollo Python.
3. El sistema mostrará un menú interactivo en la consola donde podrás elegir entre las diferentes opciones para gestionar las prescripciones.

### Ejemplo de flujo

1. **Registrar una prescripción**:
   - El usuario ingresa los detalles de la prescripción (nombre del paciente, medicamento, dosis, frecuencia, duración y fecha), y la prescripción se registra en el sistema.

2. **Buscar una prescripción**:
   - El usuario puede buscar prescripciones por el nombre del paciente y se mostrarán los resultados coincidentes.

3. **Actualizar una prescripción**:
   - El usuario puede actualizar la dosis o la duración de una prescripción específica.

4. **Eliminar prescripciones vencidas**:
   - El sistema detecta prescripciones vencidas y permite eliminarlas después de confirmar la acción.

5. **Generar informes**:
   - El sistema muestra los medicamentos más recetados y la duración promedio de las prescripciones.

## Objetivo

El objetivo de este proyecto es proporcionar una solución para gestionar las prescripciones médicas, ayudando a los profesionales de la salud a llevar un registro adecuado de los tratamientos recetados, sus duraciones y la frecuencia de los medicamentos utilizados.

## Contribuciones

Si deseas contribuir al proyecto, puedes hacer un fork y enviar un pull request. Las mejoras y sugerencias son siempre bienvenidas.
