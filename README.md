markdown
# pyFuzz - Web Directory Fuzzing Tool 🔍

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

`pyFuzz` es una herramienta para descubrir directorios y archivos ocultos en servidores web mediante **fuzzing**. Combina una URL base con entradas de una wordlist y verifica los códigos de estado HTTP, resaltando los resultados con colores para una interpretación rápida.

---

## Requisitos 
- **Python 3.x**
- Instalar dependencias:
  ```bash
  pip install requests colorama
  ```

---

## Uso 

### Sintaxis Básica
```bash
./pyFuzz.py <URL> <WORDLIST> [EXTENSIONES]
```

### Parámetros
| Parámetro      | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `URL`          | URL objetivo (ej: `http://ejemplo.com` o `http://127.0.0.1:8080`).          |
| `WORDLIST`     | Ruta a la wordlist (ej: `/usr/share/wordlists/dirb/common.txt`).            |
| `EXTENSIONES`  | Extensiones opcionales para probar (ej: `.php`, `.bak`, `.git`).            |

### Ejemplos 
1. **Fuzzing básico (sin extensiones)**:
   ```bash
   ./pyFuzz.py http://127.0.0.1 /usr/share/wordlists/rockyou.txt
   ```

2. **Fuzzing con múltiples extensiones**:
   ```bash
   ./pyFuzz.py http://ejemplo.com /ruta/wordlist.txt .php .html .env
   ```

3. **Ignorar códigos 404**:
   ```bash
   ./pyFuzz.py http://ejemplo.com/secret/ wordlist.txt .txt
   ```

---

## Características 
- **Detección de rutas**: Combina la URL con entradas de la wordlist.
- **Soporte para extensiones**: Añade extensiones personalizadas a las rutas.
- **Resultados coloreados**:
  - **Verde**: Códigos `200`, `403`, etc. (éxito o acceso denegado).
  - **Amarillo**: Redirecciones (`301`, `302`, `303`).
  - **Ignorado**: Respuestas `404` (no se muestran).
- **Manejo de errores**: Detecta problemas de conexión, permisos o archivos inválidos.

---

## Notas 
-  Asegúrate de que la URL termine con `/` si buscas subdirectorios (ej: `http://sitio.com/admin/`).
-  Utiliza wordlists adecuadas para el contexto:
  - `common.txt` para directorios.
  - `raft-small-words.txt` para archivos.
-  Agrega extensiones comunes (ej: `.php`, `.json`) para aumentar la efectividad.

---

## Contribución 
¿Quieres mejorar `pyFuzz`? ¡Abre un *issue* para reportar errores o envía un *pull request* con nuevas funcionalidades!

---


**Creado por [SkullB0yG](https://github.com/SkullB0yG)** - ¡Feliz Hacking! 🚀
``` 
