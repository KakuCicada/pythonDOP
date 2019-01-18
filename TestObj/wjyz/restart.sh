#!/usr/bin/env bash
#

objdir=`dirname $(dirname $(readlink -f "$0"))`
configfile="${objdir}/config/wjyz.ini"
serverdir="${objdir}/server"
battledir="${objdir}/battle"

battle_start() {
  binfile=$1
  objname=$2
  cd ${battledir}
  nohup ./${binfile} -n=${objname} -ini=${configfile} > /dev/null 2> ${objdir}/log/${objname}.err.log &

  sleep 5
  battle_objpid=`ps aux | grep -w ${objname} | grep -v grep | awk '{print $2}'`
  if [ ${battle_objpid} == '' ];then
    echo "${objname} start faild"
    exit 2
  else
    echo "${objname} start success"
  fi
}

stop() {
  objname=$1
  objpid=`ps aux | grep -w ${objname} | grep -v grep | awk '{print $2}'`
  kill ${objpid}
  while [ ${objpid} != '' ]; do
    echo "${objname} is stopping ..."
    sleep 3
  done
}

