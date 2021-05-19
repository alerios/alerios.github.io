---
author: alerios
date: "2006-09-06T05:10:00"
tags:
  - software libre
title: Sobre Open Conference Systems
---

OCS ([Open Conference Systems](http://pkp.sfu.ca/ocs)) fue el sistema de
conferencias que utilizamos en las pasadas
[JSL-2006](http://jsl.unicauca.edu.co/) y tengo algunas cuantas cosas que
decir sobre esta aplicación.

[Ceronman](http://wiki.freaks-unidos.net/weblogs/ceronman/) realizó una
exploración de varios sistemas similares que nos pudieran servir, obviamente
libres, y creo que antes de OCS probó también [Comas](http://www.comas-code.org/), el que se utiliza en las [DebConfs](http://www.debconf.org/). Aún
no me ha explicado bien por qué lo escogió, pero el caso es que finalmente OCS
fue el que utilizamos.

En su versión actual, esta aplicación [no tiene soporte para
i18n](http://pkp.sfu.ca/support/forum/viewtopic.php?t=1148), de modo que me
tocó editar los archivos PHP a mano para traducir los mensajes a Español, y en
el proceso también me dí cuenta de que el código deja mucho qué desear.

Para completar, por ahi nonroot le pilló una vulnerabilidad que aún no ha
reportado y con la que tuvimos que convivir durante todo el evento a merced de
cualquier juáker.

De todas formas la aplicación se comportó bien y sirve para lo que uno
necesita, con ella hicimos la convocatoria, revisión y publicación de
ponencias, se gestionaron los jurados, se hizo el registro de asistentes y
hasta se gestionó y se publicó el horario de todas las actividades.

Como muchas aplicaciones libres, la primera versión es regularsita, pero poco
a poco va mejorando, así que los invito a que le hechen un ojo y la tengan en
cuenta a la hora de querer gestionar la organización de un evento.

Por cierto, las modificaciones que hice para traducirlo a español están
disponibles en [este enlace](http://jsl.unicauca.edu.co/ocs-es.tgz).
