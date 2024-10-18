SELECT venda.estado, ROUND(AVG(venda.qtd * venda.vrunt), 2) as gastomedio
from tbvendas venda
WHERE venda.status = 'Concluído'
GROUP BY venda.estado
order by gastomedio DESC