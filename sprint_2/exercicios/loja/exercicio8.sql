SELECT vende.cdvdd, vende.nmvdd
FROM tbvendedor vende
LEFT JOIN tbvendas venda ON venda.cdvdd = vende.cdvdd
WHERE venda.status = 'Concluído'
GROUP BY vende.cdvdd, vende.nmvdd
ORDER BY COUNT(venda.cdven) DESC
LIMIT 1 