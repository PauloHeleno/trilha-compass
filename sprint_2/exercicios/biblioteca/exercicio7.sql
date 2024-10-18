SELECT aut.nome
FROM autor aut
LEFT JOIN livro li ON li.autor = aut.codautor
GROUP by aut.nome
HAVING COUNT(li.cod) = 0
ORDER BY aut.nome