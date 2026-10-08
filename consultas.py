from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    stmt = select(Livro).join(Livro.autor).order_by(Livro.titulo)
    livros = session.execute(stmt).scalars().all()

    if not livros:
        print("Nenhum livro cadastrado.")
        return []

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} | {livro.autor.nome} | {status}")

    return livros


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    stmt = select(Livro).join(Livro.autor).where(Livro.disponivel.is_(True)).order_by(Livro.titulo)
    livros = session.execute(stmt).scalars().all()

    if not livros:
        print("Nenhum livro disponível.")
        return []

    for livro in livros:
        print(f"- {livro.titulo} | {livro.autor.nome} | Disponível")

    return livros


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    stmt = select(Livro).join(Livro.autor).where(Livro.titulo.ilike(f"%{trecho}%")).order_by(Livro.titulo)
    livros = session.execute(stmt).scalars().all()

    if not livros:
        print(f"Nenhum livro encontrado com o trecho: '{trecho}'")
        return []

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} | {livro.autor.nome} | {status}")

    return livros


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    stmt = select(Autor).where(Autor.nome.ilike(f"%{nome_autor}%"))
    autor = session.execute(stmt).scalar_one_or_none()

    if autor is None:
        print(f"Autor '{nome_autor}' não encontrado.")
        return []

    livros = autor.livros
    if not livros:
        print(f"Nenhum livro encontrado para o autor '{autor.nome}'.")
        return []

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"- {livro.titulo} | {status}")

    return livros
