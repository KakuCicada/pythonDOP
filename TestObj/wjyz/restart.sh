#!/usr/bin/env bash
#

objdir=`dirname $(dirname $(readlink -f "$0"))`
configfile="${objdir}/config/wjyz.ini"
serverdir="${objdir}/server"
battledir="${objdir}/battle"

start() {
  binfile=$1
  objname=$2
  nohup ./${binfile} -n=${objname} -ini=${configfile} > /dev/null 2> ${objdir}/log/${objname}.err.log &
}

