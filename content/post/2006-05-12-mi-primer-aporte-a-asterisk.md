---
author: alerios
date: "2006-05-12T20:59:00"
tags:
  - software libre
  - telefonía IP
title: Mi primer aporte a asterisk :)
---

Luego de casi 24 horas de programar como loco, terminé el nuevo driver de cdr
para asterisk, [cdr_sqlite3_custom](http://bugs.digium.com/view.php?id=7149),
con el cual ya se pueden agregar campos variables al cdr desde el dialplan
para que se almacenen en una base de datos de sqlite3, y por lo tanto, se
puedan mejorar las estadísticas en
[DeS](http://destar.berlios.de/)[tar](http://destar.berlios.de/), agregando
por ejemplo los dialouts, las troncales, pbx_virtuales, etc.

Me costó mucho trabajo pues hace como 7 años que no programaba en C, pero
bueno, al final este Frankenstein ¡está vivo! VIVO!

Espero que varias personas lo puedan probar para corregirle los errores que
tenga y que pronto sea integrado a la rama principal de desarrollo de
asterisk, sino, pues de todas formas le seguiré trabajando porque lo necesito
para DeStar.` `
