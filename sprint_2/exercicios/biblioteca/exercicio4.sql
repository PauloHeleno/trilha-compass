SELECT aut.nome, aut.codautor, aut.nascimento, COUNT(li.cod) AS quantidade
FROM autor aut
LEFT JOIN livro li ON li.autor = aut.codautor
GROUP BY aut.codautor, aut.nome, aut.nascimento
ORDER BY aut.nome ASC