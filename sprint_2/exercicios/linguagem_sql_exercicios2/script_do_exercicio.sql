SELECT edi.codeditora, edi.nome, COUNT(li.cod) as QuantidadeLivros
FROM editora edi
LEFT JOIN livro li on edi.codeditora = li.editora
GROUP by edi.codeditora, edi.nome
HAVING COUNT(li.cod) != 0
ORDER BY QuantidadeLivros DESC
LIMIT 5


SELECT li.cod, li.titulo, aut.codautor, aut.nome, li.valor, edi.codeditora, edi.nome
FROM livro li
left JOIN autor aut on li.autor = aut.codautor
LEFT join editora edi on li.editora = edi.codeditora
ORDER by valor DESC
LIMIT 10


