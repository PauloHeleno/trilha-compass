SELECT venda.cdcli, venda.nmcli, SUM(venda.qtd * venda.vrunt) AS gasto
FROM tbvendas venda
WHERE venda.status = 'Concluído'
GROUP BY venda.cdcli, venda.nmcli
ORDER BY gasto DESC
LIMIT 1