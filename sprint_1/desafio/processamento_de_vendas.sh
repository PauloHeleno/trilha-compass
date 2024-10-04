#!/bin/bash
mkdir -p vendas
cp ecommerce/dados_de_vendas.csv vendas/
cd vendas
mkdir -p backup
cp dados_de_vendas.csv backup/dados-$(date +"%Y%m%d").csv
cd backup
mv dados-*.csv backup-dados-$(date +"%Y%m%d").csv
touch relatorio.txt
date +"%Y-%m-%d %H:%M" >> relatorio.txt
head -n 2 backup-dados-*.csv | tail -n 1 | cut -d',' -f5 >> relatorio.txt
tail -n 1 backup-dados-*.csv | cut -d',' -f5 >> relatorio.txt
echo $(( $( wc -l < backup-dados-*.csv ) -1 )) >> relatorio.txt
head -n 10 backup-dados-*.csv
head -n 10 backup-dados-*.csv >> relatorio.txt
zip -r backup-dados-$(date +"%Y%m%d").zip backup-dados-*.csv
rm backup-dados-*.csv
rm ../dados_de_vendas.csv


