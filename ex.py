"""
EXEMPLOS DE USO - Sistema de Máquina de Banho
Arquivo: exemplos_uso.py
"""

from maquina_banho import MaquinaBanho

# ============================================================================
# EXEMPLO 1: Uso Básico - Sequência simples
# ============================================================================

def exemplo_1_basico():
    """Exemplo 1: Uso básico com sequência simples."""
    print("\n" + "="*70)
    print("EXEMPLO 1: USO BÁSICO")
    print("="*70)
    
    # Criar instância
    maquina = MaquinaBanho()
    
    # Abastecer água
    print("\n1. Abastecendo água...")
    print(maquina.abastecer_agua())
    print(maquina.abastecer_agua())
    
    # Abastecer shampoo
    print("\n2. Abastecendo shampoo...")
    print(maquina.abastecer_shampoo())
    
    # Verificar níveis
    print("\n3. Verificando níveis...")
    print(maquina.verificar_nivel_agua())
    print("\n" + maquina.verificar_nivel_shampoo())
    
    # Colocar pet
    print("\n4. Colocando pet...")
    print(maquina.colocar_pet_na_maquina("Rex"))
    
    # Dar banho
    print("\n5. Dando banho...")
    print(maquina.dar_banho())
    
    # Retirar pet
    print("\n6. Retirando pet...")
    print(maquina.retirar_pet_da_maquina())
    
    # Status final
    print("\n7. Status final...")
    print(maquina.obter_status_geral())


# ============================================================================
# EXEMPLO 2: Tratamento de Erros
# ============================================================================

def exemplo_2_erros():
    """Exemplo 2: Como o sistema trata erros."""
    print("\n" + "="*70)
    print("EXEMPLO 2: TRATAMENTO DE ERROS")
    print("="*70)
    
    maquina = MaquinaBanho()
    
    # Erro 1: Tentar dar banho sem pet
    print("\nTentando dar banho SEM pet...")
    print(maquina.dar_banho())
    
    # Erro 2: Água insuficiente
    print("\nAbastecendo pouca água e tentando banho...")
    maquina.abastecer_agua()  # Só 2L
    maquina.colocar_pet_na_maquina("Fluffy")
    print(maquina.dar_banho())  # Precisa 10L
    
    # Erro 3: Tentar colocar pet em máquina suja
    print("\nTentando colocar segundo pet sem limpar...")
    maquina2 = MaquinaBanho()
    maquina2.colocar_pet_na_maquina("Dog1")
    maquina2.retirar_pet_da_maquina()  # Sai sujo, máquina fica suja
    print(maquina2.colocar_pet_na_maquina("Dog2"))  # Erro!


# ============================================================================
# EXEMPLO 3: Simulação Completa
# ============================================================================

def exemplo_3_simulacao_completa():
    """Exemplo 3: Simulação completa com dois pets."""
    print("\n" + "="*70)
    print("EXEMPLO 3: SIMULAÇÃO COMPLETA - DOIS PETS")
    print("="*70)
    
    maquina = MaquinaBanho()
    
    print("\n>>> PREPARANDO A MÁQUINA")
    for i in range(5):
        print(f"Abastecendo água {i+1}/5...")
        maquina.abastecer_agua()
    
    for i in range(2):
        print(f"Abastecendo shampoo {i+1}/2...")
        maquina.abastecer_shampoo()
    
    print("\n>>> PET 1: REX")
    print(maquina.colocar_pet_na_maquina("Rex"))
    print(maquina.verificar_pet_no_banho())
    print(maquina.dar_banho())
    print(maquina.retirar_pet_da_maquina())
    
    print("\n>>> PREPARANDO PARA PET 2")
    print(maquina.verificar_nivel_agua())
    print(maquina.verificar_nivel_shampoo())
    
    print("\n>>> PET 2: BELLA")
    print(maquina.colocar_pet_na_maquina("Bella"))
    print(maquina.dar_banho())
    print(maquina.retirar_pet_da_maquina())
    
    print("\n>>> STATUS FINAL")
    print(maquina.obter_status_geral())


# ============================================================================
# EXEMPLO 4: Validações de Capacidade
# ============================================================================

def exemplo_4_capacidade():
    """Exemplo 4: Validações de capacidade máxima."""
    print("\n" + "="*70)
    print("EXEMPLO 4: VALIDAÇÕES DE CAPACIDADE")
    print("="*70)
    
    maquina = MaquinaBanho()
    
    # Abastecer até o limite
    print("\nAbastecendo água até o máximo...")
    for i in range(20):
        resultado = maquina.abastecer_agua()
        if "Aviso" in resultado or "cheio" in resultado.lower():
            print(f"Tentativa {i+1}: {resultado}")
            break
        if i == 19:
            print(f"Tentativa {i+1}: Tanque está cheio! {resultado}")
    
    print("\nAbastecendo shampoo até o máximo...")
    for i in range(10):
        resultado = maquina.abastecer_shampoo()
        if "Aviso" in resultado or "cheio" in resultado.lower():
            print(f"Tentativa {i+1}: {resultado}")
            break


# ============================================================================
# EXEMPLO 5: Máquina Suja
# ============================================================================

def exemplo_5_maquina_suja():
    """Exemplo 5: Demonstração de máquina suja."""
    print("\n" + "="*70)
    print("EXEMPLO 5: MÁQUINA SUJA")
    print("="*70)
    
    maquina = MaquinaBanho()
    
    print("\n>>> Colocando pet na máquina...")
    maquina.colocar_pet_na_maquina("Spot")
    print("Pet colocado: Spot (SUJO)")
    
    print("\n>>> Retirando pet SEM dar banho...")
    print(maquina.retirar_pet_da_maquina())
    
    print("\n>>> Tentando colocar novo pet...")
    print(maquina.colocar_pet_na_maquina("Luna"))
    
    print("\n>>> Limpando a máquina...")
    # Primeiro abastecer recursos
    maquina.abastecer_agua()
    maquina.abastecer_shampoo()
    print(maquina.limpar_maquina())
    
    print("\n>>> Agora conseguimos colocar novo pet!")
    print(maquina.colocar_pet_na_maquina("Luna"))


# ============================================================================
# EXEMPLO 6: Acesso direto aos atributos
# ============================================================================

def exemplo_6_atributos():
    """Exemplo 6: Acessando atributos da máquina."""
    print("\n" + "="*70)
    print("EXEMPLO 6: ATRIBUTOS DA MÁQUINA")
    print("="*70)
    
    maquina = MaquinaBanho()
    
    print(f"\nEstado inicial:")
    print(f"  Nível de água: {maquina.nivel_agua}L")
    print(f"  Nível de shampoo: {maquina.nivel_shampoo}L")
    print(f"  Pet atual: {maquina.pet_atual}")
    print(f"  Pet limpo: {maquina.pet_limpo}")
    print(f"  Máquina limpa: {maquina.maquina_limpa}")
    
    # Fazer operações
    maquina.abastecer_agua()
    maquina.abastecer_shampoo()
    maquina.colocar_pet_na_maquina("Test")
    
    print(f"\nApós operações:")
    print(f"  Nível de água: {maquina.nivel_agua}L")
    print(f"  Nível de shampoo: {maquina.nivel_shampoo}L")
    print(f"  Pet atual: {maquina.pet_atual}")
    print(f"  Pet limpo: {maquina.pet_limpo}")
    print(f"  Máquina limpa: {maquina.maquina_limpa}")


# ============================================================================
# EXEMPLO 7: Constantes
# ============================================================================

def exemplo_7_constantes():
    """Exemplo 7: Exibindo as constantes do sistema."""
    print("\n" + "="*70)
    print("EXEMPLO 7: CONSTANTES DO SISTEMA")
    print("="*70)
    
    print(f"\nCapacidades:")
    print(f"  Água máxima: {MaquinaBanho.CAPACIDADE_AGUA}L")
    print(f"  Shampoo máximo: {MaquinaBanho.CAPACIDADE_SHAMPOO}L")
    
    print(f"\nConsumo por banho:")
    print(f"  Água: {MaquinaBanho.CONSUMO_AGUA_BANHO}L")
    print(f"  Shampoo: {MaquinaBanho.CONSUMO_SHAMPOO_BANHO}L")
    
    print(f"\nConsumo na limpeza:")
    print(f"  Água: {MaquinaBanho.CONSUMO_AGUA_LIMPEZA}L")
    print(f"  Shampoo: {MaquinaBanho.CONSUMO_SHAMPOO_LIMPEZA}L")
    
    print(f"\nAbastecimento padrão:")
    print(f"  Por operação: {MaquinaBanho.ABASTECIMENTO_PADRAO}L")


# ============================================================================
# EXEMPLO 8: Usando com try/except
# ============================================================================

def exemplo_8_excecoes():
    """Exemplo 8: Tratamento de exceções."""
    print("\n" + "="*70)
    print("EXEMPLO 8: TRATAMENTO DE EXCEÇÕES")
    print("="*70)
    
    maquina = MaquinaBanho()
    
    # Exemplo 1: Try/except
    print("\nExemplo 1: Tratando possíveis erros")
    try:
        if maquina.pet_atual is None:
            print("Nenhum pet na máquina, operação inválida")
        else:
            print(maquina.dar_banho())
    except Exception as e:
        print(f"Erro: {e}")
    
    # Exemplo 2: Verificação antes de operação
    print("\nExemplo 2: Verificação preventiva")
    try:
        # Verificar se pode colocar pet
        if maquina.maquina_limpa and maquina.pet_atual is None:
            maquina.colocar_pet_na_maquina("Safe Pet")
            print("Pet colocado com sucesso!")
    except Exception as e:
        print(f"Erro ao colocar pet: {e}")


# ============================================================================
# EXEMPLO 9: Simulação Diária
# ============================================================================

def exemplo_9_dia_de_trabalho():
    """Exemplo 9: Simulando um dia de trabalho."""
    print("\n" + "="*70)
    print("EXEMPLO 9: UM DIA DE TRABALHO NO PETSHOP")
    print("="*70)
    
    maquina = MaquinaBanho()
    pets = ["Rex", "Luna", "Buddy", "Max"]
    
    print("\n>>> ABERTURA DO PETSHOP")
    print("Abastecendo máquina...")
    for i in range(8):
        maquina.abastecer_agua()
    for i in range(3):
        maquina.abastecer_shampoo()
    print(maquina.obter_status_geral())
    
    print("\n>>> DURANTE O DIA")
    for pet in pets:
        print(f"\n--- Banho de {pet} ---")
        if maquina.nivel_agua < 10 or maquina.nivel_shampoo < 2:
            print(f"Precisamos abastecer!")
            maquina.abastecer_agua()
            maquina.abastecer_shampoo()
        
        maquina.colocar_pet_na_maquina(pet)
        print(f"Pet {pet} na máquina")
        print(maquina.dar_banho())
        print(maquina.retirar_pet_da_maquina())
    
    print("\n>>> FECHAMENTO")
    print(maquina.obter_status_geral())


# ============================================================================
# EXEMPLO 10: Cálculo de Eficiência
# ============================================================================

def exemplo_10_eficiencia():
    """Exemplo 10: Calculando eficiência."""
    print("\n" + "="*70)
    print("EXEMPLO 10: ANÁLISE DE EFICIÊNCIA")
    print("="*70)
    
    maquina = MaquinaBanho()
   
    for i in range(15):
        maquina.abastecer_agua()
    for i in range(5):
        maquina.abastecer_shampoo()
    
    agua_inicial = maquina.nivel_agua
    shampoo_inicial = maquina.nivel_shampoo
    
    print(f"\nRecursos iniciais:")
    print(f"  Água: {agua_inicial}L")
    print(f"  Shampoo: {shampoo_inicial}L")
    
    # Simular 2 banhos
    pets = ["Teste1", "Teste2"]
    banhos = 0
    
    for pet in pets:
        if maquina.nivel_agua >= 10 and maquina.nivel_shampoo >= 2:
            maquina.colocar_pet_na_maquina(pet)
            maquina.dar_banho()
            maquina.retirar_pet_da_maquina()
            banhos += 1
    
    agua_final = maquina.nivel_agua
    shampoo_final = maquina.nivel_shampoo
    
    print(f"\nRecursos finais (após {banhos} banhos):")
    print(f"  Água: {agua_final}L (consumida: {agua_inicial - agua_final}L)")
    print(f"  Shampoo: {shampoo_final}L (consumido: {shampoo_inicial - shampoo_final}L)")
    
    print(f"\nEficiência:")
    print(f"  Banhos possíveis com tanque cheio: {int(30 / 10)} com água")
    print(f"  Banhos possíveis com tanque cheio: {int(10 / 2)} com shampoo")
    print(f"  Recurso limitante: Shampoo!")


# ============================================================================
# EXECUÇÃO DOS EXEMPLOS
# ============================================================================

def menu_exemplos():
    """Menu para escolher qual exemplo executar."""
    while True:
        print("\n" + "="*70)
        print("MENU DE EXEMPLOS - SISTEMA MÁQUINA DE BANHO")
        print("="*70)
        print("\n1. Uso Básico")
        print("2. Tratamento de Erros")
        print("3. Simulação Completa")
        print("4. Validações de Capacidade")
        print("5. Máquina Suja")
        print("6. Atributos")
        print("7. Constantes")
        print("8. Exceções")
        print("9. Dia de Trabalho")
        print("10. Análise de Eficiência")
        print("0. Sair")
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            exemplos = {
                "1": exemplo_1_basico,
                "2": exemplo_2_erros,
                "3": exemplo_3_simulacao_completa,
                "4": exemplo_4_capacidade,
                "5": exemplo_5_maquina_suja,
                "6": exemplo_6_atributos,
                "7": exemplo_7_constantes,
                "8": exemplo_8_excecoes,
                "9": exemplo_9_dia_de_trabalho,
                "10": exemplo_10_eficiencia
            }
            
            if opcao == "0":
                print("\nEncerrando exemplos. Até logo!")
                break
            elif opcao in exemplos:
                exemplos[opcao]()
            else:
                print("Opção inválida!")
        
        except KeyboardInterrupt:
            print("\n\nExemplos interrompidos.")
            break
        except Exception as e:
            print(f"Erro ao executar exemplo: {e}")


if __name__ == "__main__":
    menu_exemplos()
