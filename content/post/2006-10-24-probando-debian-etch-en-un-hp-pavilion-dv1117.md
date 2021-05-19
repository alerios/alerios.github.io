---
author: alerios
date: "2006-10-24T22:36:00"
tags:
  - software libre
title: Probando Debian Etch en un HP Pavilion dv1117
---

Mientras llega el reporte de instalación que envié al BTS y no se ha
procesado, quiero comentar como me fué con la imagen diaria del instalador de
etch que probé ayer.

Primero, me bajé la [`debian-testing-i386-netinst.iso`](http://ftp.acc.umu.se/cdimage/daily-builds/daily/arch-latest/) creada el 20061021, la quemé en un CD y la puse a
andar con el método de instalación gráfico (installgui).

Me gusta mucho como se ve el instalador gráfico, lástima que no me haya
reconocido el touchpad Synaptics con el que viene el portátil. Tampoco pude
usar la tecla TAB para saltar hasta la opción de "Captura de Pantalla", pero
de todas formas el resto de la instalación la pude realizar sin ningún
problema utilizando solamente el teclado.

El instalador me reconoció la tarjeta de red Ethernet, pero la inalámbrica no,
como era de esperarse, pues es una `Intel PRO/Wireless 2200BG` cuyos drivers
son libres, pero para funcionar requiren unos archivos de firmware cerrado que
tuve que bajar de [por ahí](http://www.damr.net/llpfiles/ipw2200-fw-3.0.tgz) y
copiar a `/usr/lib/hotplug/firmware/.`

La otra cosa que no me funcionó automáticamente luego de la instalación fue el
escalado de frecuencia del procesador. Me tocó usar modconf para cargar el
módulo `speedstep_centrino` a mano.

Por lo demás, estoy contento con el nuevo instalador, incluyendo la traducción
a Español. Ah, por cierto, también sucedió algo maravilloso: luego de elegir
el idioma, el teclado, la codificación y el país en el instalador, no tuve que
volver a hacer ninguna geekada para tener el sistema en Español.

Está quedando muy bien. Felicitaciones a todos los que han contribuido, espero
poder ayudar en esta parte del proyecto en el futuro cercano.

Actualización: Ya se procesó el reporte de fallo, es el
[#395118](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=395118).
