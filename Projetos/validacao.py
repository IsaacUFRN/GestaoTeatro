from datetime import datetime

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        valor = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True


def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, '%d/%m/%Y')
        return True
    except:
        return False

def validar_preco(preco):
    try:
        preco = float(preco.replace(',', '.'))
        return f"R$ {preco:.2f}".replace('.', ',')
    except:
        return None