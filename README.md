# Proyecto #2 de Organización del Computador

Escriba un Programa que permita el manejo del inventario para una tienda de venta de historietas (Como las de DC y Marvel Comics). Su programa debe contar con las siguientes funcionalidades:

## I Registro de Nuevas Historietas:

El sistema debe permitir el registro de nuevas historietas de las cuales se almacenará la siguiente información:

* Serial (8 Dígitos)

* Título (40 Caracteres máximo)

* Precio de Venta (3 Dígitos máximo)

* Stock Actual (2 Dígitos máximo)

## II Consulta:

Se debe poder buscar una historieta por:

* Serial utilizando el índice respectivo.

* Consulta por 1 o 2 palabras del título. (Para ello debe haber un índice que contenga todas las palabras que hay en los títulos de todas las historietas)

* Una vez encontrada una historieta se debe mostrar toda la información correspondiente a la misma (Serial, Título, Precio y Stock)

## III Compra:

Se debe poder comprar una cantidad indicada por el usuario de cualquier historieta registrada en el sistema (Siempre y cuando haya suficiente Stock de esta). Se debe mostrar el costo total de la compra en caso de que esta pueda realizarse.

## IV Reabastecimiento:

Se debe poder incrementar el Stock de una historieta por concepto de reabastecimiento.

## V Eliminación:

Se debe poder eliminar una historieta del sistema (Debe ser eliminación lógica).

## VI Compactador:

Debe existir una funcionalidad que elimine físicamente las historietas que ya se han eliminado lógicamente y que actualice los índices correspondientemente.

* * *

**Plataforma**: Python utilizando vectores en memoria. No obstante, los datos deben poder grabarse en disco duro al finalizar la ejecución del programa, adicionalmente se deben leer desde disco los últimos datos guardados cuando el programa inicie. Para la defensa debe haber al menos 10 historietas cargadas en el sistema.Todas las búsquedas deben funcionar apoyándose en índices. El uso de una búsqueda secuencial será penalizado.

**Fecha de Entrega**: Lunes 29 de noviembre de 2021, enviando la aplicación por e-mail al preparador. La defensa se realizará el martes 30 de noviembre.