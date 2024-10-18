SELECT COUNT(li.cod) AS quantidade, edi.nome, end.estado, end.cidade
FROM editora edi
JOIN livro li ON edi.codeditora = li.editora
JOIN endereco end ON edi.endereco = end.codEndereco
GROUP BY edi.codeditora, edi.nome, end.estado, end.cidade
ORDER BY quantidade DESC
LIMIT 5