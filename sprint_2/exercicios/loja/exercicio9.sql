SELECT  venda.cdpro, venda.nmpro
FROM tbvendas venda
WHERE venda.status = 'Concluído' and venda.dtven BETWEEN '2014-02-03' and '2018-02-02'
GROUP BY venda.cdpro, venda.nmpro
HAVING COUNT(venda.cdpro)
ORDER BY COUNT(venda.cdpro) DESC
LIMIT 1 