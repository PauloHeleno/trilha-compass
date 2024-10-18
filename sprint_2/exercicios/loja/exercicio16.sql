SELECT venda.estado, venda.nmpro,  ROUND(AVG(venda.qtd), 4) as quantidade_media
from tbvendas venda
WHERE venda.status = 'Concluído'
GROUP BY venda.estado, venda.nmpro