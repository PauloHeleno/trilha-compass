SELECT depen.cddep, depen.nmdep, depen.dtnasc, SUM(venda.qtd * venda.vrunt) as valor_total_vendas
FROM tbdependente depen
left JOIN tbvendedor vende ON depen.cdvdd = vende.cdvdd
LEFT JOIN tbvendas venda ON vende.cdvdd = venda.cdvdd
WHERE venda.status = 'Concluído'
GROUP BY depen.cddep, depen.nmdep, depen.dtnasc
HAVING valor_total_vendas != 0
ORDER by valor_total_vendas 
LIMIT 1