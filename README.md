# ImGui RGB Normalizer RGB-Calc (RGB.py)

## Index / Índice

* [English 🇬🇧](#english-)
* [Español 🇪🇸](#español-)

## English 🇬🇧

This is a small **Python** script designed to quickly fix the color workflow headache in **Dear ImGui**.

Traditional graphic design tools output RGB channels as integers ranging from `0 to 255`. However, ImGui structures (`ImVec4`) require normalized float values between `0.0f and 1.0f`. This script automates that exact conversion directly via the terminal.

---

#### Key Features:
* **Range Validation:** Ensures input numbers stay strictly within the standard hexadecimal boundary (0-255).
* **Error Handling:** Prevents unexpected crashes if the user inputs alphabetical characters or invalid symbols.
* **C++ Ready Precision:** Outputs floating-point values ready to be copied and pasted directly into your ImGui styling configurations.

---

### 🚀 How to Run

Make sure you have Python installed on your system and run the script from your terminal:

```bash
python RGB.py
```

#### Usage Example:
```bash
1. English
2. Español
Choose your language/Elije Tu Idioma: 1

ImGui Color Calculator
Give me the quantity of red: 50
Give me the quantity of green: 83
Give me the quantity of blue: 57

The red color quantity is:  0.1953125
The green color quantity is:  0.32421875
The blue color quantity is: 0.22265625
```
*(Those decimal values can be placed directly into your C++ codebase as `ImVec4(0.195f, 0.324f, 0.222f, 1.0f)`)*

## Español 🇪🇸

Este es un pequeño script de **Python** diseñado para solucionar de forma rápida el dolor de cabeza de los colores en **Dear ImGui**.

Dado que las herramientas de diseño gráfico tradicionales entregan los canales RGB en un rango entero de `0 a 255`, pero las estructuras de ImGui (`ImVec4`) requieren valores flotantes normalizados entre `0.0f y 1.0f`, este script automatiza la conversión exacta desde la consola.

---

#### Características principales:
* **Validación de rango:** Controla que los números introducidos estén estrictamente dentro del rango hexadecimal estándar (0-255).
* **Manejo de errores:** Evita el cierre inesperado del programa si el usuario introduce letras o caracteres no válidos.
* **Precisión para C++:** Entrega los floats (Numeros decimales) listos para copiar y pegar directamente en los parámetros de tus estilos de ImGui.

---

### 🚀 Cómo usarlo

Asegúrate de tener instalado Python en tu sistema y ejecuta el script desde tu terminal:

```bash
python RGB.py
```

#### Ejemplo de uso:
```bash
1. English
2. Español
Choose your language/Elije Tu Idioma: 2

Calculador de colores ImGui
Dame el color rojo: 50
Dame el color verde: 83
Dame el color azul: 57

El color rojo es:  0.1953125
El color verde es:  0.32421875
El color azul es: 0.22265625
```
*(Esos valores decimales son los que se meten directamente en tu código de C++ como `ImVec4(0.195f, 0.324f, 0.222f, 1.0f)`)*
