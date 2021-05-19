---
author: alerios
date: "2006-08-10T17:47:00"
tags:
  - software libre
title: Fallos críticos 2 - Alerios 1
---

Desde ayer estoy calentando motores para la [Mini-DebConf-CO](http://wiki.debian.org/DebianColombia/MiniDebconf2006) y la
[BSP](http://wiki.debian.org/BSP) contínua que se ha declarado en todas las
fronteras del proyecto. Estuve ayudando por los laditos a
[Santiago](http://afrodita.unicauca.edu.co/~santiago/blog/) y Stuart a probar
los [paquetes](http://www4.netsweng.com/~anderson/ming-unstable/) que éste
último hizo para las fuentes de ming, que necesitamos para por fin sacar a la
luz mi paquete de [op-panel en pkg-voip](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=323689).  
 También gracias a charlas con Santiago, pude enviar un parche al BTS para
corregir [un fallo crítico de ssmtp](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=374327), el primero que en verdad se puede decir que
corrijo, pues antes había intentado cerrar otros dos, pero sin suerte.

Estoy animado con Debian, y hasta se me vino a la cabeza una primera versión
en español de una [canción para Etch al estilo
Julien](http://julien.danjou.info/blog/index.php/2006/08/01/312-etch-song):

(8)  
Porque yo  
no quiero trabajar,  
no quiero ir a estudiar,  
no me quiero casaar.  
Quiero cerrar un fallo crítico al día,  
y que en diciembre salga Debian Etch al fin...(bis)  
(8)

Actualización: [Anibal](http://users.monash.edu.au/~anibal/) me contó por IRC
que ya había probado el mismo parche antes, pero que estaba incompleto pues su
siempre oportuno pbuilder, que a tantos nos ha dado la mano, fallaba al
compilar sin libssl-dev instalado. Esta misma noche Anibal completó el parche,
dejando el paquete ya compilado y listo para probar
[aquí](http://debianrules.v7w.com/~pbuilder/debian/pool/ssmtp/).
