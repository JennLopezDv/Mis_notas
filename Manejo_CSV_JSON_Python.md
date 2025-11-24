# Manejo de archivos CSV y JSON en Python

### De nivel novato a avanzado

Este documento te guía paso a paso desde lo más básico hasta técnicas
avanzadas para leer, escribir y transformar archivos **CSV** y **JSON**
en Python utilizando las herramientas estándar (`open`, `csv`, `json`) y
buenas prácticas como:

-   Uso correcto de `with`
-   Manejo de `encoding`
-   Lectura eficiente
-   Escritura atómica
-   Prevención de corrupción de archivos

------------------------------------------------------------------------

## Índice

1.  Conceptos básicos sobre archivos y `with open`
2.  Parámetros importantes de `open()`
3.  Manejo de CSV con el módulo `csv`
4.  Manejo de JSON con el módulo `json`
5.  Operaciones prácticas
6.  Manejo de errores y buenas prácticas
7.  Resumen rápido: ejemplos listos para copiar

------------------------------------------------------------------------

## 1. Conceptos básicos sobre archivos y `with open`

En Python, para trabajar con archivos se utiliza la función `open()`. La
forma más recomendada es:

``` python
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
# aquí el archivo ya está cerrado
```

### ¿Por qué usar `with`?

-   Garantiza el cierre del archivo automáticamente.
-   Evita fugas de recursos.
-   Hace el código más claro y seguro.

------------------------------------------------------------------------

## 2. Parámetros importantes de `open()`

``` python
open(path, mode='r', encoding=None, newline=None)
```

  Parámetro   Descripción
  ----------- ------------------------------------------------
  path        Ruta del archivo
  mode        Modo de apertura
  encoding    Codificación del texto
  newline     Control de saltos de línea (importante en CSV)

### Modos comunes:

-   `'r'` → lectura\
-   `'w'` → escritura (sobrescribe)\
-   `'a'` → añadir al final\
-   `'x'` → crear exclusivamente\
-   `'b'` → binario (`rb`, `wb`)\
-   `'+'` → lectura/escritura

> ✅ Para CSV en Windows: usar siempre `newline=''`

------------------------------------------------------------------------

## 3. Manejo de CSV con el módulo `csv`

``` python
import csv
```

### 3.1 Leer CSV como listas

``` python
with open("datos.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
```

### 3.2 Leer CSV como diccionarios

``` python
with open("productos.csv", "r", encoding="utf-8", newline="") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["nombre"], fila["precio"])
```

✅ Más legible y práctico.

------------------------------------------------------------------------

### 3.3 Escribir CSV con writer

``` python
with open("salida.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["id", "nombre", "precio"])
    escritor.writerow([1, "Lápiz", 1200])
```

------------------------------------------------------------------------

### 3.4 Escribir CSV con DictWriter

``` python
campos = ["id", "nombre", "precio"]

with open("productos_out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerow({"id": 1, "nombre": "Lápiz", "precio": 1200})
```

------------------------------------------------------------------------

## 4. Manejo de JSON con el módulo `json`

``` python
import json
```

### 4.1 Leer JSON

``` python
with open("datos.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

### 4.2 Escribir JSON legible

``` python
with open("salida.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

Parámetros útiles: - `indent=2` → Formateo legible -
`ensure_ascii=False` → Soporte para tildes - `sort_keys=True` → Ordenar
claves

------------------------------------------------------------------------

## 5. Operaciones prácticas

### CSV → JSON

``` python
def csv_a_json(ruta_csv, ruta_json):
    with open(ruta_csv, "r", encoding="utf-8", newline="") as f_csv:
        lector = csv.DictReader(f_csv)
        datos = list(lector)

    with open(ruta_json, "w", encoding="utf-8") as f_json:
        json.dump(datos, f_json, indent=2, ensure_ascii=False)
```

### JSON → CSV

``` python
def json_a_csv(ruta_json, ruta_csv):
    with open(ruta_json, "r", encoding="utf-8") as f:
        datos = json.load(f)

    if not datos:
        return

    campos = datos[0].keys()

    with open(ruta_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)
```

------------------------------------------------------------------------

## 6. Archivos grandes (optimización)

Procesamiento fila a fila:

``` python
with open("grande.csv", "r", encoding="utf-8", newline="") as f:
    for fila in csv.DictReader(f):
        procesar(fila)
```

JSON por líneas (NDJSON):

``` python
with open("datos.ndjson", "r") as f:
    for linea in f:
        obj = json.loads(linea)
        procesar(obj)
```

------------------------------------------------------------------------

## 7. Buenas prácticas

✅ Siempre usa `with open`\
✅ Especifica `encoding="utf-8"`\
✅ Usa `newline=''` en CSV\
✅ Maneja errores con try/except\
✅ Valida estructuras antes de procesarlas

Ejemplo:

``` python
try:
    with open("archivo.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Archivo no encontrado")
except json.JSONDecodeError:
    print("JSON inválido")
```

------------------------------------------------------------------------

## Resumen express

### Leer CSV

``` python
productos = list(csv.DictReader(open("productos.csv", encoding="utf-8")))
```

### Escribir CSV

``` python
writer.writerows(productos)
```

### Leer JSON

``` python
datos = json.load(open("datos.json", encoding="utf-8"))
```

### Escribir JSON

``` python
json.dump(datos, open("salida.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
```

------------------------------------------------------------------------

📌 Documento limpio, didáctico y listo para estudio o referencia rápida.
