import pickle

def recupera_pecas():
    try:
        pecas = {}
        arq_pecas = open("pecas.dat", "rb")
        pecas = pickle.load(arq_pecas)
        arq_pecas.close()
    except:
        pecas = {
            'P01' : ["Romeu e Julieta", "Drama", "2h30m", "01/07/2026", "R$ 25,00", True],
            'P02' : ["Hamlet", "Tragédia", "3h", "05/02/2026", "R$ 30,00", True],
            'P03' : ["O Fantasma da Ópera", "Musical", "2h45m", "10/07/2026", "R$ 35,00", True],
            'P04' : ["O Auto da Compadecida", "Comédia", "2h15m", "20/07/2026", "R$ 40,00", True],
            'P05' : ["As Bruxas de Salem", "Suspense", "2h", "28/07/2026", "R$ 45,00", True]
        }
        arq_pecas = open("pecas.dat", "wb")
        pickle.dump(pecas, arq_pecas)
        arq_pecas.close()
    return pecas


def recupera_ingressos():
    try:
        ingressos = {}
        arq_ingressos = open("ingressos.dat", "rb")
        ingressos = pickle.load(arq_ingressos)
        arq_ingressos.close()
    except:
        ingressos = {
            'ING01' : ["Flavius Gorgonio", "12222222222", "P01", True],
            'ING02' : ["João Victor", "13333333333", "P02", True],
            'ING03' : ["Ana Beatriz", "14444444444", "P03", True],
            'ING04' : ["Carlos Henrique", "15555555555", "P04", True],
            'ING05' : ["Fernanda Costa", "16666666666", "P05", True]
        }
        arq_ingressos = open("ingressos.dat", "wb")
        pickle.dump(ingressos, arq_ingressos)
        arq_ingressos.close()
    return ingressos


def recupera_atores():
    try:
        atores = {}
        arq_atores = open("atores.dat", "rb")
        atores = pickle.load(arq_atores)
        arq_atores.close()
    except:
        atores = {
            '11111111111' : ["Matheus Augusto", "19 anos", "Masculino", "P01", True],
            '22222222222' : ["Aline Silva", "18 anos", "Feminino", "P01", True],
            '33333333333' : ["Davi Lucas", "22 anos", "Masculino", "P03", True],
            '44444444444' : ["Natalia Costa", "32 anos", "Feminino", "P04", True],
            '55555555555' : ["Lucas Mendes", "25 anos", "Masculino", "P02", True]
        }
        arq_atores = open("atores.dat", "wb")
        pickle.dump(atores, arq_atores)
        arq_atores.close()
    return atores


def grava_pecas(pecas):
    arq_pecas = open("pecas.dat", "wb")
    pickle.dump(pecas, arq_pecas)
    arq_pecas.close()


def grava_ingressos(ingressos):
    arq_ingressos = open("ingressos.dat", "wb")
    pickle.dump(ingressos, arq_ingressos)
    arq_ingressos.close()


def grava_atores(atores):
    arq_atores = open("atores.dat", "wb")
    pickle.dump(atores, arq_atores)
    arq_atores.close()