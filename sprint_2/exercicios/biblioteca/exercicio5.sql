SELECT DISTINCT aut.nome
FROM autor aut
JOIN livro li ON li.autor = aut.codautor
JOIN editora edi ON edi.codeditora = li.editora
JOIN endereco end on end.codendereco = edi.endereco 
WHERE end.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')
ORDER BY aut.nome 