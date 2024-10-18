SELECT aut.codautor, aut.nome, COUNT(li.cod)  as quantidade_publicacoes
FROM autor aut
LEFT JOIN livro li ON li.autor = aut.codautor
GROUP by aut.codautor, aut.nome
ORDER BY quantidade_publicacoes  DESC
LIMIT 1