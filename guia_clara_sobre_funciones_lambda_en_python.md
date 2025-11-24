# 📘 Funciones Lambda en Python

## Guía clara y sencilla para principiantes

Este documento está pensado para personas que están aprendiendo Python por primera vez y quieren entender qué son las **funciones lambda**, para qué sirven y cómo usarlas en situaciones reales, paso a paso y sin tecnicismos innecesarios.

---

## 1. ¿Qué es una función lambda?

Una función lambda es una **función pequeña y anónima** (sin nombre) que se escribe en una sola línea y se usa para tareas simples.

En lugar de escribir una función completa con `def`, puedes usar lambda cuando la función es muy corta y directa.

### ✅ Idea clave:
> Lambda sirve para crear funciones rápidas, cortas y temporales.

---

## 2. Comparación: función normal vs lambda

### Función normal:
```python
def sumar(a, b):
    return a + b

print(sumar(3, 5))
```

### La misma función con lambda:
```python
sumar = lambda a, b: a + b
print(sumar(3, 5))
```

📌 Diferencias principales:
- No usa `def`
- No tiene nombre propio (aunque se puede asignar a una variable)
- Todo va en una sola línea

Estructura general:
```python
lambda argumentos: resultado
```

---

## 3. Ejemplos básicos para entender mejor

### ✅ Ejemplo 1: Duplicar un número
```python
duplicar = lambda x: x * 2
print(duplicar(5))  # Resultado: 10
```

### ✅ Ejemplo 2: Saber si un número es par
```python
es_par = lambda x: x % 2 == 0
print(es_par(4))  # True
print(es_par(7))  # False
```

### ✅ Ejemplo 3: Convertir grados Celsius a Fahrenheit
```python
celsius_a_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_a_fahrenheit(25))  # 77.0
```

---

## 4. ¿Cuándo se usan normalmente las funciones lambda?

Se usan principalmente junto con funciones como:

- `map()` → transformar datos
- `filter()` → filtrar datos
- `sorted()` → ordenar datos

### Ejemplo con lista:
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)
```
Resultado:
```
[1, 4, 9, 16, 25]
```

---

# 📊 Aplicación práctica: Top 3 productos más vendidos con porcentajes

Imaginemos que tenemos una lista de productos con sus ventas:

```python
productos = [
    {"nombre": "Arroz", "ventas": 150},
    {"nombre": "Azúcar", "ventas": 120},
    {"nombre": "Aceite", "ventas": 200},
    {"nombre": "Café", "ventas": 90},
    {"nombre": "Leche", "ventas": 170}
]
```

### 1️⃣ Calcular total de ventas
```python
total_ventas = sum(p["ventas"] for p in productos)
```

### 2️⃣ Ordenar usando lambda (de mayor a menor)
```python
productos_ordenados = sorted(productos, key=lambda p: p["ventas"], reverse=True)
```

### 3️⃣ Obtener el Top 3
```python
top_3 = productos_ordenados[:3]
```

### 4️⃣ Calcular porcentajes con lambda

```python
resultado = list(map(
    lambda p: {
        "producto": p["nombre"],
        "ventas": p["ventas"],
        "porcentaje": round((p["ventas"] / total_ventas) * 100, 2)
    },
    top_3
))

for item in resultado:
    print(item)
```

### 📌 Resultado final esperado:
```
{'producto': 'Aceite', 'ventas': 200, 'porcentaje': 27.03}
{'producto': 'Leche', 'ventas': 170, 'porcentaje': 22.97}
{'producto': 'Arroz', 'ventas': 150, 'porcentaje': 20.27}
```

---

## 🧠 ¿Qué aprendimos aquí?

- Lambda simplifica funciones pequeñas
- Permite ordenar y transformar estructuras complejas
- Es ideal para análisis rápidos de datos
- Se usa mucho en automatización y procesamiento de información

---

## ✅ Resumen rápido

| Característica | Función normal | Lambda |
|--------------|----------------|--------|
| Usa def | Sí | No |
| Tiene nombre | Sí | No |
| Varias líneas | Sí | No |
| Para lógica compleja | Sí | No recomendado |
| Para tareas rápidas | No ideal | Perfecto |

---

## 🎯 Conclusión

Las funciones lambda son una herramienta poderosa cuando entiendes su simplicidad. No reemplazan a las funciones normales, pero son perfectas cuando necesitas operaciones rápidas, claras y compactas.

Si estás comenzando con Python, no te preocupes si al inicio parecen confusas: con la práctica se vuelven una gran aliada.

---

📎 Este archivo está listo para guardarse como:

```
funciones_lambda_python.md
```

Si deseas que lo exporte listo para descargar, dímelo y te lo genero en archivo.

