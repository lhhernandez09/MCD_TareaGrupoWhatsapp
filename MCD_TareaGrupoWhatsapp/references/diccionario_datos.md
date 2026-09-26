# Diccionario de datos — chat de WhatsApp

## Fuente

- Archivo: `data/raw/chat.txt`
- Origen: exportación de un grupo de WhatsApp.
- Unidad de análisis: un mensaje enviado al grupo.
- Formato de origen: texto plano UTF-8. Cada mensaje nuevo inicia con fecha, hora, remitente y contenido; las líneas posteriores sin ese encabezado se consideran continuación del mensaje anterior.

> Nota de privacidad: el archivo contiene mensajes y nombres personales. No debe publicarse ni compartirse fuera del equipo sin anonimizar los datos.

## Estructura del archivo crudo

Cada mensaje se representa, de forma general, así:

```text
[dd/mm/aa, h:mm:ss a.m.|p.m.] Remitente: Mensaje
```

| Campo | Descripción | Tipo | Ejemplo |
| --- | --- | --- | --- |
| `fecha` | Fecha original del envío. | Texto (`dd/mm/aa`) | `13/07/25` |
| `hora` | Hora original del envío. | Texto (`h:mm:ss`) | `7:57:26` |
| `ampm` | Indicador de horario de 12 horas. | Texto (`a.m.` / `p.m.`) | `a.m.` |
| `remitente` | Nombre mostrado de quien envió el mensaje. | Texto | `Juan Pérez` |
| `mensaje` | Contenido textual del mensaje. Puede incluir emojis, enlaces o saltos de línea. | Texto | `Buenos días familia` |

## Variables derivadas en la libreta

La libreta `notebooks/main.ipynb` transforma los campos anteriores en las siguientes variables:

| Variable | Descripción | Tipo | Regla de creación |
| --- | --- | --- | --- |
| `fecha_hora` | Marca de tiempo completa del mensaje. | Fecha y hora (`datetime`) | Combina `fecha`, `hora` y `ampm`. |
| `fecha` | Fecha calendario del mensaje. | Fecha | Se extrae de `fecha_hora`. |
| `hora` | Hora del día en formato de 24 horas. | Entero (`0`–`23`) | Se extrae de `fecha_hora`. |
| `dia_semana` | Día de la semana del mensaje. | Texto | Se obtiene de `fecha_hora`; está en inglés por la configuración predeterminada de pandas. |
| `longitud_mensaje` | Número de caracteres del contenido del mensaje. | Entero | Longitud de `mensaje`. |
| `es_multimedia` | Indica si el mensaje corresponde a contenido multimedia omitido en la exportación. | Booleano | Busca `image`, `video`, `audio`, `sticker` o `GIF` seguido de `omitted`, sin distinguir mayúsculas. |
| `remitente` | Identificador anonimizado del remitente para el análisis. | Texto | Sustituye el nombre original por un personaje de *Star Wars*, mediante una asignación aleatoria con semilla 42. |

## Consideraciones de calidad

- Los mensajes multilínea se unen al mensaje inmediatamente anterior.
- Los avisos del sistema o las líneas que no cumplen el patrón de fecha, hora y remitente no se convierten en registros independientes.
- La anonimización se realiza durante el análisis; el archivo crudo conserva los nombres originales.
- El formato de fecha, hora y los textos que representan multimedia dependen de la configuración de exportación de WhatsApp y podrían requerir ajustes si se usa otra exportación.
