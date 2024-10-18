SELECT 
    vende.nmvdd AS vendedor,
    SUM(venda.qtd * venda.vrunt) AS valor_total_vendas,
    ROUND(SUM(venda.qtd * venda.vrunt) * vende.perccomissao / 100, 2) AS comissao
FROM tbvendedor vende
LEFT JOIN tbvendas venda ON vende.cdvdd = venda.cdvdd
WHERE venda.status = 'Concluído'
GROUP BY vende.nmvdd
ORDER BY comissao DESC;
