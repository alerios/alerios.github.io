---
author: alerios
date: "2010-10-15T17:53:00"
tags:
  - asterisk
  - mashup
  - postea.me
  - twitter
title: Mashup Howto o de cómo nació Postea.me
---

[Postea.me](http://postea.me/) (mi primer
[Mashup](http://es.wikipedia.org/wiki/Mashup_%28aplicaci%C3%B3n_web_h%C3%ADbrida%29))
es un servicio con el cuál puedes actualizar tu estado en twitter con una
llamada telefónica, gratis. Como buen programador linuxero, dejo aquí
documentados los pasos que seguí para su construcción:

1\. Investigar un servicio que sea relativamente fácil de armar a partir de
cosas ya existentes. En este caso, quería hacer algo que fuera la combinación
entre un IVR de [Asterisk](http://www.asterisk.org/applications/ivr) y
[Twitter](http://twitter.com/). Encontré que en inglés hay servicios como
calltweet.com, tweetcall.com, guagee.com y trottr.com, pero ninguno en
español, y menos con números de Hispanoamérica.

2\. Elegir el nombre. A algo simple, llamativo y de preferencia un
[cognado](http://es.wikipedia.org/wiki/Cognado) en varios idiomas. También hay
que tener en cuenta que el nombre de dominio sea corto y esté disponible.

3\. No reinventar la rueda. Todo el sitio web de Postea.me está basado en
Joomla y en un conjunto de extensiones que considero esenciales:

- JoomSEF, para gestionar las URLs.
- Joomfish, para internacionalización
- MiniJomTweet, para la integración con Twitter

- XMap, para generar el sitemap.xml
- GAuthordetails, para mostrar otros artículos del mismo autor
- com_content-extended, para listar los artículos de un mismo autor
- Y suficiencia en PHP para combinarlo todo y hacer ajustes

4\. Usar el poder de Python y Perl. Para hacer el IVR de Asterisk, utilicé
módulos como:

- Agilib, para el AGI

- Simplejson, urllib y oauth2 para twitter
- MySQLdb, Suds y Soaplib para joomla
- Un algoritmo para generar URLs cortas.
- Y una tarea en cron con Lame para convertir los audios que graba Asterisk a .mp3

5\. Algo de embellecimiento para el sitio web:

- El logo usando el GIMP.
- Reproductor mp3: http://flash-mp3-player.net
- Un botoncito javascript para compartir los posts como bookmarks

- Google Analytics y http://social.bidsystem.com/
- Página en facebook

Y bueno, mucho café ... con la emoción me tomó menos de una semana tener el
primer piloto andando. Espero lo disfruten :)
