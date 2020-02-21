from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Alessandro', idade=44)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Alessandro').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alessandro').first()
    pessoa.idade = 45
    pessoa.save

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alessandro').first()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('bandi', '666')
    insere_usuario('leporoni', '999')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()