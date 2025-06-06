#!/usr/bin/env bash
# executar com permissão de root
# deve existir o usuario solr em seu SO 
# o id 8983 é o ID do user SOLR no container/docker
set -x

mkdir -p ./data
chmod -R 750 data
chown -R 8983:solr data

mkdir -p ./logs
chmod -R 750 logs
chown -R 8983:solr logs
