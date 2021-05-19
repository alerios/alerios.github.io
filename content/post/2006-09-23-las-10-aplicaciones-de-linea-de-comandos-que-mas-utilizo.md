---
author: alerios
date: "2006-09-23T16:29:00"
tags:
  - software libre
title: las 10 aplicaciones de línea de comandos que más utilizo
---

Continuando con la moda en [planet.d.n](http://planet.debian.net/), aquí están
mis resultados:

[alerios@arriero ~]$ history|awk '{print $2}'|awk 'BEGIN {FS="|"} {print
$1}'|sort|uniq -c|sort -g -r|head -10

87 ls  
61 cd  
55 vi  
38 svn  
30 ssh  
19 sudo  
19 more  
19 man  
14 ping  
11 wget

A ver si también aplico el resto de cosas de los [tips de
IBM](http://www-128.ibm.com/developerworks/aix/library/au-productivitytips.html?ca=dgr-lnxw07UNIX-Office-Tips) que dieron origen a esto.
