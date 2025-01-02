# Função para calcular a quantidade de unidades de cada tipo
def calcular_unidades(taxa_aproveitamento_lua_percent, proporcao_mineral1, proporcao_mineral2, proporcao_mineral3, proporcao_mineral4):
    # Tamanho total com base na Taxa de Aproveitamento da Lua em m³
    volume_total = (taxa_aproveitamento_lua_percent / 100) * 30000

    # Calcula o volume de cada tipo de mineral
    volume_mineral1 = (proporcao_mineral1 / 100) * volume_total
    volume_mineral2 = (proporcao_mineral2 / 100) * volume_total
    volume_mineral3 = (proporcao_mineral3 / 100) * volume_total
    volume_mineral4 = (proporcao_mineral4 / 100) * volume_total

    # Calcula a quantidade de unidades de cada tipo
    unidades_mineral1 = volume_mineral1 / 10
    unidades_mineral2 = volume_mineral2 / 10
    unidades_mineral3 = volume_mineral3 / 10
    unidades_mineral4 = volume_mineral4 / 10

    # Retorna os resultados como um dicionário
    return {
        "Mineral #1": int(unidades_mineral1),
        "Mineral #2": int(unidades_mineral2),
        "Mineral #3": int(unidades_mineral3),
        "Mineral #4": int(unidades_mineral4)
    }

# Função para calcular a quantidade de unidades em um mês
def calcular_unidades_mensal(taxa_aproveitamento_lua_percent, proporcao_mineral1, proporcao_mineral2, proporcao_mineral3, proporcao_mineral4):
    # Calcula as unidades para uma taxa de aproveitamento
    unidades_por_taxa = calcular_unidades(taxa_aproveitamento_lua_percent, proporcao_mineral1, proporcao_mineral2, proporcao_mineral3, proporcao_mineral4)

    # Considerando 1 taxa de aproveitamento por hora, 24 horas por dia, durante 30 dias
    horas_por_mes = 24 * 30

    # Multiplica a quantidade de unidades por horas no mês
    unidades_mensal = {tipo: quantidade * horas_por_mes for tipo, quantidade in unidades_por_taxa.items()}

    return unidades_mensal

# Função para validar as entradas do usuário
def validar_entrada(valor, permitir_zero=False):
    try:
        valor_float = round(float(valor), 2)
        if valor_float < 0 or (valor_float == 0 and not permitir_zero):
            raise ValueError
        return valor_float
    except ValueError:
        raise ValueError("Entrada inválida. Por favor, insira um número positivo com até 2 casas decimais.")

# Interação via prompt
if __name__ == "__main__":
    # Solicita ao usuário os nomes e valores necessários
    mineral1_nome = input("Informe o nome do Mineral #1: ") or "Mineral #1"
    mineral2_nome = input("Informe o nome do Mineral #2: ") or "Mineral #2"
    mineral3_nome = input("Informe o nome do Mineral #3: ") or "Mineral #3"
    mineral4_nome = input("Informe o nome do Mineral #4: ") or "Mineral #4"

    try:
        taxa_aproveitamento_lua_percent = validar_entrada(input("Informe a Taxa de Aproveitamento da Lua em porcentagem (100% = 30000 m³, não pode ser 0%): "))
        proporcao_mineral1 = validar_entrada(input(f"Informe a proporção do {mineral1_nome} em %: "))
        proporcao_mineral2 = validar_entrada(input(f"Informe a proporção do {mineral2_nome} em %: "))
        proporcao_mineral3 = validar_entrada(input(f"Informe a proporção do {mineral3_nome} em %: "))
        proporcao_mineral4 = validar_entrada(input(f"Informe a proporção do {mineral4_nome} em % (pode ser 0%): "), permitir_zero=True)

        # Chamada da função para unidades por taxa de aproveitamento
        resultado = calcular_unidades(taxa_aproveitamento_lua_percent, proporcao_mineral1, proporcao_mineral2, proporcao_mineral3, proporcao_mineral4)

        # Exibindo o resultado por taxa de aproveitamento
        print("\nQuantidade de unidades por tipo (por Taxa de Aproveitamento da Lua):")
        for tipo, quantidade in resultado.items():
            nome = locals().get(f"{tipo.lower().replace(' ', '_')}_nome", tipo)
            print(f"{nome}: {quantidade} unidades")

        # Chamada da função para unidades mensais
        resultado_mensal = calcular_unidades_mensal(taxa_aproveitamento_lua_percent, proporcao_mineral1, proporcao_mineral2, proporcao_mineral3, proporcao_mineral4)

        # Exibindo o resultado mensal
        print("\nQuantidade de unidades por tipo (em um mês de 30 dias):")
        for tipo, quantidade in resultado_mensal.items():
            nome = locals().get(f"{tipo.lower().replace(' ', '_')}_nome", tipo)
            print(f"{nome}: {quantidade} unidades")

    except ValueError as e:
        print(e)
