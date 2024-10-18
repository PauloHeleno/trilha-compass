SELECT pro.cdpro, venda.nmcanalvendas,  venda.nmpro, SUM(venda.qtd) AS quantidade_vendas
FROM tbestoqueproduto pro
LEFT JOIN tbvendas venda ON venda.cdpro = pro.cdpro
WHERE venda.status = 'Concluído'
GROUP BY pro.cdpro, venda.nmcanalvendas, venda.nmpro
ORDER by  quantidade_vendas 
LIMIT 10