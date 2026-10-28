# Sistema bancario – FPOO

Parte práctica del parcial de **Fundamentos de Programación Orientada a Objetos (FPOO-01)**, 28 de octubre de 2026.

Implementa en C++, **desde cero**, el sistema bancario descrito en las historias de usuario y en el diagrama de clases. ADACEEN te acompaña mientras programas: pídele ayuda en VS Code o en el panel del navegador cuando tengas una duda.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| [docs/historias-de-usuario.md](docs/historias-de-usuario.md) | HU-1 a HU-5 con sus criterios de aceptación |
| [docs/diagrama-clases.puml](docs/diagrama-clases.puml) | Diagrama de clases en PlantUML (Cliente, Cuenta, CuentaAhorros, CuentaCorriente, Titularidad, Banco) |
| [docs/Historias de Usuario - Sistema Bancario.pdf](docs/Historias%20de%20Usuario%20-%20Sistema%20Bancario.pdf) | El enunciado original en PDF |
| `src/main.cpp` | Programa principal (está casi vacío: lo armas tú) |
| `src/modelo/` | Aquí van tus clases, cada una en su `.h` y su `.cpp` |
| `Makefile` | Compila todo lo que haya en `src/` y `src/modelo/` |

## Compilar y ejecutar

En la terminal de VS Code (Ctrl + ñ, o menú *Terminal → New Terminal*):

```bash
make        # compila; el ejecutable se llama banco
make run    # compila y ejecuta
make clean  # borra lo compilado
```

También puedes usar *Terminal → Run Build Task* (Ctrl + Shift + B).

## Sugerencia de orden

1. `Cliente` (HU-1)
2. `Cuenta` con retiro y consignación (HU-2 y HU-3)
3. `CuentaAhorros` y `CuentaCorriente` heredando de `Cuenta` (HU-4)
4. `Titularidad`, que une un cliente con una cuenta
5. `Banco` con su lista de titularidades (HU-5)
6. `main.cpp`: crea un banco, clientes y cuentas, y muestra el saldo después de cada operación

## Entrega (para subir al Campus)

1. Arma el zip: *Terminal → Run Task… → **Preparar entrega (.zip)*** (o escribe `make entrega` en la terminal). Aparece `entrega-<tu-usuario>-sistema-bancario.zip` en el Explorador.
2. Descárgalo: clic derecho sobre ese archivo en el Explorador → **Download**.
3. Súbelo al Campus donde indique el profesor.

Tu trabajo también queda guardado en el editor: si cierras la pestaña y vuelves a abrirlo desde ADACEEN, sigue ahí.
