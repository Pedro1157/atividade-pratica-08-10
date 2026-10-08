1: para que serve o campo 'disponivel' em 'livro?
ele controla se o livro está disponível para empréstimo. quando 'true', o livro pode ser emprestado quando 'false', ele está indisponível

2: por que é necessário chamar 'session.commit()' após emprestar ou devolver?
porque 'commit()' salva as alterações no banco de dados, Sem isso, a mudança no objeto em memória não fica persistida no SQLite

3: em qual consulta você usa o relacionamento entre 'livro' e 'autor'?
na consulta 'listar_livros', onde acessamos 'livro.autor.nome' para mostrar o nome do autor do livro, e também na consulta 'listar_livros_por_autor', ao percorrer 'autor.livros'.
