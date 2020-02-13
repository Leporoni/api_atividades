from models import Pessoas

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

if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()