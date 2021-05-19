---
author: alerios
date: "2006-11-03T23:19:00"
tags:
  - software libre
title: Usando el lector de memorias SD del HP Pavilion dv1000
---

Tengo este portátil desde hace más de un año y nunca me había puesto a
cacharrear con el lector de memorias SD que trae incorporado, así que ¿qué
mejor plan para un viernes en la tarde antes de ir a rumbear?

En realidad resultó ser más fácil de lo que creía. Google me mandó a un
[enlace buenísimo de gentoo](http://forums.gentoo.org/viewtopic-t-432605.html)
y a [otro de ubuntu](http://ubuntuforums.org/showthread.php?t=276932) que
también está muy bien.

En últimas, y para no aburrirlos, solo tuve que hacer lo que aparece en el
siguiente script del init, y ¡¡magia magia!!, cuando inserto una memoria, se
monta solita y de una vez se me pregunta lo que quiero hacer con las fotos que
almacena.

Por cierto, `lspci` dice que mi tarjeta es una:  
`02:09.3 Mass storage controller: Texas Instruments PCIxx21 Integrated FlashMedia Controller`

Este es el archivo `/etc/init.d/sdhci` que creé y seguro le puede servir a
muchos usando este portátil en debian:

#! /bin/sh

### BEGIN INIT INFO

# Provides: sdhci

# Required-Start: $local_fs $remote_fs

# Required-Stop: $local_fs $remote_fs

# Default-Start: 2 3 4 5

# Default-Stop: 0 1 6

# Short-Description: SDHCI initscript

# Description: Used to mount Texas Instruments

# PCIxx21 Integrated FlashMedia Controller

### END INIT INFO

# Author: Alejandro Rios P.

# PATH should only include /usr/\* if it runs after the mountnfs.sh script

PATH=/sbin:/usr/sbin:/bin:/usr/bin  
DESC="SDHCI module mounting"  
NAME=sdhci  
SCRIPTNAME=/etc/init.d/$NAME

# Define LSB log\_\* functions.

# Depend on lsb-base (>= 3.0-6) to ensure that this file is present.

. /lib/lsb/init-functions

#

# Function that starts the daemon/service

#

do_start()  
{

# change 02:09.3 for your device identifier shown by

# 'lspci' command

# cambia 02:09.3 por el identificador del dispositivo

# mostrado por el comando 'lspci'

setpci -s 02:09.3 4c=0x22  
modprobe sdhci || return 1  
modprobe mmc_block || return 1  
}

#

# Function that stops the daemon/service

#

do_stop()  
{  
rmmod mmc_block || return 1  
rmmod sdhci || return 1  
rmmod mmc_core || return 1  
}

case "$1" in  
start)  
do_start  
;;  
stop)  
do_stop  
;;  
restart|force-reload)  
log_daemon_msg "Restarting $DESC" "$NAME"  
do_stop  
case "$?" in  
0|1)  
do_start  
case "$?" in  
0) log_end_msg 0 ;;

1. log*end_msg 1 ;; # Old process is still running  
   *) log*end_msg 1 ;; # Failed to start  
   esac  
   ;;  
   *)  
   ( Failed to stop  
   log_end_msg 1  
   ;;  
   esac  
   ;;  
   \*)  
   echo "Usage: $SCRIPTNAME {start|stop|restart|force-reload}" >&2  
   exit 3  
   ;;  
   esac

:
