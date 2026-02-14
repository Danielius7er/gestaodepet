"""
Sistema de Controle de Máquina de Banho para PetShop
Descrição: Interface de terminal interativa com menu
"""

from maquina_banho import MaquinaBanho
import os
import sys

class ControladorPetshop:
    """
    Classe que gerencia a interface de terminal do sistema.
    Attributes:
        maquina: Instância de MaquinaBanho
        executando: Flag para controlar o loop principal
    """
    
    def __init__(self):
        self.maquina = MaquinaBanho()
        self.executando = True
    
    def iniciar(self):
        self.exibir_boas_vindas()
        
        while self.executando:
            self.exibir_menu()
            self.processar_opcao()
        
        self.encerrar()
    
    def exibir_boas_vindas(self):
        self.limpar_tela()
        print("\n")
        print("=" * 74)
        print("|" + " " * 72 + "|")
        print("|" + "BEM-VINDO AO SISTEMA DE CONTROLE DE BANHO".center(72) + "|")
        print("|" + " " * 72 + "|")
        print("|" + "PETSHOP - MÁQUINA DE BANHO".center(72) + "|")
        print("|" + " " * 72 + "|")
        print("=" * 74)
        print("\nPressione ENTER para continuar...")
        input()
        self.limpar_tela()
    
    def exibir_menu(self):
        print("\n")
        print("=" * 74)
        print("|" + "MENU PRINCIPAL".center(72) + "|")
        print("=" * 74)
        print("|" + " " * 72 + "|")
        print("|  1. Dar banho no pet                                                   |")
        print("|  2. Abastecer com água                                                 |")
        print("|  3. Abastecer com shampoo                                              |")
        print("|  4. Verificar nível de água                                            |")
        print("|  5. Verificar nível de shampoo                                         |")
        print("|  6. Verificar pet no banho                                             |")
        print("|  7. Colocar pet na máquina                                             |")
        print("|  8. Retirar pet da máquina                                             |")
        print("|  9. Limpar máquina                                                     |")
        print("|  10. Ver status geral                                                  |")
        print("|  0. Sair                                                               |")
        print("|" + " " * 72 + "|")
        print("=" * 74)
        print("\nEscolha uma opção (0-10): ", end="")
    
    def processar_opcao(self):
        """Processa a opção escolhida pelo usuário."""
        try:
            opcao = input().strip()
            
            if not opcao:
                print("Entrada inválida! Tente novamente.")
                self.aguardar_enter()
                return
            
            try:
                opcao = int(opcao)
            except ValueError:
                print("Erro: Digite um número válido!")
                self.aguardar_enter()
                return
            
            self.limpar_tela()
            
            opcoes = {
                1: self.executar_dar_banho,
                2: self.executar_abastecer_agua,
                3: self.executar_abastecer_shampoo,
                4: self.executar_verificar_agua,
                5: self.executar_verificar_shampoo,
                6: self.executar_verificar_pet,
                7: self.executar_colocar_pet,
                8: self.executar_retirar_pet,
                9: self.executar_limpar_maquina,
                10: self.executar_status_geral,
                0: self.executar_sair
            }
            
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                print("Opção inválida! Digite um número entre 0 e 10.")
                self.aguardar_enter()
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            self.executando = False
    
    def executar_dar_banho(self):
        """Executa a operação de dar banho."""
        print("\nDAR BANHO NO PET\n")
        resultado = self.maquina.dar_banho()
        print(resultado)
        self.aguardar_enter()
    
    def executar_abastecer_agua(self):
        """Executa a operação de abastecer água."""
        print("\nABASTECER COM ÁGUA\n")
        resultado = self.maquina.abastecer_agua()
        print(resultado)
        self.aguardar_enter()
    
    def executar_abastecer_shampoo(self):
        """Executa a operação de abastecer shampoo."""
        print("\nABASTECER COM SHAMPOO\n")
        resultado = self.maquina.abastecer_shampoo()
        print(resultado)
        self.aguardar_enter()
    
    def executar_verificar_agua(self):
        """Executa a operação de verificar água."""
        print("\nVERIFICAR NÍVEL DE ÁGUA\n")
        resultado = self.maquina.verificar_nivel_agua()
        print(resultado)
        self.aguardar_enter()
    
    def executar_verificar_shampoo(self):
        """Executa a operação de verificar shampoo."""
        print("\nVERIFICAR NÍVEL DE SHAMPOO\n")
        resultado = self.maquina.verificar_nivel_shampoo()
        print(resultado)
        self.aguardar_enter()
    
    def executar_verificar_pet(self):
        """Executa a operação de verificar pet."""
        print("\nVERIFICAR PET NO BANHO\n")
        resultado = self.maquina.verificar_pet_no_banho()
        print(resultado)
        self.aguardar_enter()
    
    def executar_colocar_pet(self):
        """Executa a operação de colocar pet."""
        print("\nCOLOCAR PET NA MÁQUINA\n")
        nome_pet = input("Digite o nome do pet: ")
        resultado = self.maquina.colocar_pet_na_maquina(nome_pet)
        print(resultado)
        self.aguardar_enter()
    
    def executar_retirar_pet(self):
        """Executa a operação de retirar pet."""
        print("\nRETIRAR PET DA MÁQUINA\n")
        resultado = self.maquina.retirar_pet_da_maquina()
        print(resultado)
        self.aguardar_enter()
    
    def executar_limpar_maquina(self):
        """Executa a operação de limpar máquina."""
        print("\nLIMPAR MÁQUINA\n")
        resultado = self.maquina.limpar_maquina()
        print(resultado)
        self.aguardar_enter()
    
    def executar_status_geral(self):
        """Executa a operação de ver status geral."""
        print("\nSTATUS GERAL\n")
        resultado = self.maquina.obter_status_geral()
        print(resultado)
        self.aguardar_enter()
    
    def executar_sair(self):
        """Encerra o programa."""
        self.executando = False
    
    def aguardar_enter(self):
        """Aguarda o usuário pressionar ENTER."""
        input("\nPressione ENTER para continuar...")
        self.limpar_tela()
    
    def encerrar(self):
        """Exibe mensagem de encerramento."""
        self.limpar_tela()
        print("\n")
        print("=" * 74)
        print("|" + " " * 72 + "|")
        print("|" + "Obrigado por usar o Sistema de Controle de Banho!".center(72) + "|")
        print("|" + " " * 72 + "|")
        print("|" + "Até logo no PetShop!".center(72) + "|")
        print("|" + " " * 72 + "|")
        print("=" * 74)
        print("\n")
    
    @staticmethod
    def limpar_tela():
        """Limpa a tela do terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """Função principal que inicia o programa."""
    try:
        controlador = ControladorPetshop()
        controlador.iniciar()
    except Exception as e:
        print(f"Erro ao executar o programa: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
