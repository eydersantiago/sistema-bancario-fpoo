# Historias de usuario – Sistema bancario

El PDF original está en esta misma carpeta: [Historias de Usuario - Sistema Bancario.pdf](Historias%20de%20Usuario%20-%20Sistema%20Bancario.pdf).

## HU-1 Registro de clientes

Como funcionario del banco, quiero registrar los clientes con su identificación, nombre y teléfono para mantener actualizada la base de datos de los usuarios del banco.

**Criterios de aceptación**
- El sistema debe permitir crear clientes con los campos: identificación, nombre y teléfono.

## HU-2 Creación de cuentas bancarias

Como funcionario del banco, quiero crear cuentas bancarias con un número único y un saldo inicial para que los clientes puedan realizar operaciones financieras.

**Criterios de aceptación**
- El sistema debe permitir crear cuentas con número de cuenta e importe inicial.
- Cada cuenta debe tener un identificador único.

## HU-3 Operaciones de retiro y consignación

Como cliente del banco, quiero retirar o consignar dinero en mi cuenta para administrar los fondos personales.

**Criterios de aceptación**
- El sistema debe permitir realizar retiros si hay saldo suficiente.
- El sistema debe permitir consignar dinero incrementando el saldo.
- El sistema debe mostrar el saldo actualizado después de cada operación.

## HU-4 Cuentas: ahorros y corriente

Como diseñador del sistema bancario, quiero implementar una relación de herencia en la clase Cuenta para crear tipos específicos de cuentas de Ahorros y Corriente, de modo que cada tipo maneje sus propias reglas de operación.

**Criterios de aceptación**
- La clase CuentaAhorros debe heredar de Cuenta y aplicar una tasa de interés periódica.
- La clase CuentaCorriente debe heredar de Cuenta y permitir un límite de sobregiro configurado.
- Las operaciones de retiro deben respetar las reglas específicas de cada tipo de cuenta.

## HU-5 Administración de banco

Como gerente del banco, quiero registrar clientes y cuentas dentro del sistema para tener organizada toda la información institucional.

**Criterios de aceptación**
- El sistema debe permitir adicionar clientes y cuentas al banco.
- El sistema debe almacenar las listas de clientes y cuentas en el objeto Banco.

## Diagrama de clases

Está en [diagrama-clases.puml](diagrama-clases.puml) (PlantUML). Para verlo dibujado, copia su contenido en <https://www.plantuml.com/plantuml/uml/>.
