---
author: alerios
date: "2006-10-25T00:14:00"
tags:
  - software libre
title: Probando AIGLX + Compiz
---

Normalmente yo no ando probando cosas nuevas que tengan que ver con multimedia
o del tipo de vainas que le encantan a los amantes de la tecnología, pero esta
vez no pude resistirme a probar [AIGLX](http://en.wikipedia.org/wiki/AIGLX)
con [Compiz](http://en.wikipedia.org/wiki/Compiz). Me dije a mi mismo: "mi
mismo, ya que acabas de pasar el etch recién instalado a sid, pues probemos de
una vez esa vaina de [XGL](http://en.wikipedia.org/wiki/Xgl) y Compiz".

Empecé a buscar acerca de XGL y Compiz, y en un wiki de Gentoo,
[leí](http://gentoo-wiki.com/HARDWARE_Video_Card_Support_Under_XGL#Intel_Cards) que para mi
tarjeta (una Intel 855GM), era mejor utilizar AIGLX, en lugar de XGL. Así que
bajé los paquetes necesarios:

`apt-get install compiz mesa-utils`

Y edité el archivo /etc/X11/xorg.conf [como se indica](http://gentoo-wiki.com/HOWTO_AIGLX#XOrg.conf_Configuration) en el mismo wiki de Gentoo. Sin
embargo, al reiniciar el GDM, el servidor sacaba unos pequeños errores que me
obligaron a modificar el archivo de nuevo y dejar lo que había agregado así:

Section "DRI"  
Group 0  
Mode 0666  
EndSection

Section "ServerLayout"  
Option "AIGLX" "true"  
Identifier "Aiglx Layout"  
EndSection

Section "Extensions"  
Option "Composite" "Enable"  
EndSection

Section "Device"  
Identifier "Aiglx device"  
Option "XAANoOffscreenPixmaps" "true"  
Option "DRI" "true"  
Driver "i810"  
EndSection

Reinicié el X de nuevo, y finalmente, corrí el compiz [como también se
menciona](http://gentoo-wiki.com/HOWTO_AIGLX#Running_compiz) en el wiki de
Gentoo.

Hasta ahora me ha parecido muy bacano, y sobre todo me ha sorprendido la forma
como se agregaron todos los efectos bonitos de Compiz sin afectar el desempeño
del procesador ni de la memoria. Incluso a veces tengo la sensación de que
quedó más rápido ;P
