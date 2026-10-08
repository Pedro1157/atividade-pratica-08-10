from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    if session.query(Autor).count() > 0:
        return

    autores = [
        Autor(nome="Machado de Assis", pais="Brasil"),
        Autor(nome="George Orwell", pais="Reino Unido"),
        Autor(nome="J.K. Rowling", pais="Reino Unido"),
    ]

    session.add(autores[0])
    session.add_all([autores[1], autores[2]])
    session.commit()

    livros = [
        Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=autores[0], disponivel=True),
        Livro(titulo="Dom Casmurro", ano=1899, autor=autores[0], disponivel=False),
        Livro(titulo="1984", ano=1949, autor=autores[1], disponivel=True),
        Livro(titulo="A Revolução dos Bichos", ano=1945, autor=autores[1], disponivel=False),
        Livro(titulo="Harry Potter e a Pedra Filosofal", ano=1997, autor=autores[2], disponivel=True),
        Livro(titulo="Harry Potter e a Câmara Secreta", ano=1998, autor=autores[2], disponivel=True),
    ]

    for livro in livros[:3]:
        session.add(livro)
    session.add_all(livros[3:])
    session.commit()
