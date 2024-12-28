import re


def cpf_validate(cpf: str) -> str:
    def calculate_digit(digits, weight):
        sum_digit = sum(a * b for a, b in zip(digits, range(weight, 1, -1)))
        return (sum_digit * 10 % 11) % 10
    
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        raise ValueError("O CPF deve conter 11 dígitos.")

    if all(d == cpf[0] for d in cpf):
        raise ValueError("CPF inválido. Todos os dígitos são iguais.")

    numbers = [int(digit) for digit in cpf]

    if numbers[9] != calculate_digit(numbers[:9], 10):
        raise ValueError("Primeiro dígito verificador inválido.")

    if numbers[10] != calculate_digit(numbers[:10], 11):
        raise ValueError("Segundo dígito verificador inválido.")

    return str(cpf)

def phone_number_validate(phone_number: str) -> str:
    phone_number = re.sub(r'\D', '', phone_number)

    if len(phone_number) not in {10, 11}:
        raise ValueError("O telefone deve ter 10 (fixo) ou 11 (celular) dígitos.")
    
    ddd = int(phone_number[:2])
    if not 11 <= ddd <= 99:
        raise ValueError("DDD inválido. Deve estar entre 11 e 99.")
    
    return str(phone_number)

def cep_validate(cep: str) -> str:
    cep = re.sub(r'\D', '', cep)
    if len(cep) != 8:
        raise ValueError('O formato do CEP informado é inválido.')
    
    return str(cep)