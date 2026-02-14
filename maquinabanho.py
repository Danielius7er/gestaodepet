"""
Sistema de Controle de Máquina de Banho para PetShop
Arquivo: maquina_banho.py
Descrição: Classe com toda a lógica da máquina de banho
"""

class MaquinaBanho:
    """
    Classe que gerencia o funcionamento de uma máquina de banho automática para petshop.
    
    Atributos:
        CAPACIDADE_AGUA: Capacidade máxima de água (30L)
        CAPACIDADE_SHAMPOO: Capacidade máxima de shampoo (10L)
        CONSUMO_AGUA_BANHO: Água consumida em cada banho (10L)
        CONSUMO_SHAMPOO_BANHO: Shampoo consumido em cada banho (2L)
        CONSUMO_AGUA_LIMPEZA: Água consumida na limpeza (3L)
        CONSUMO_SHAMPOO_LIMPEZA: Shampoo consumido na limpeza (1L)
        ABASTECIMENTO_PADRAO: Quantidade de abastecimento por operação (2L)
    """
    
    # Constantes da máquina
    CAPACIDADE_AGUA = 30
    CAPACIDADE_SHAMPOO = 10
    CONSUMO_AGUA_BANHO = 10
    CONSUMO_SHAMPOO_BANHO = 2
    CONSUMO_AGUA_LIMPEZA = 3
    CONSUMO_SHAMPOO_LIMPEZA = 1
    ABASTECIMENTO_PADRAO = 2
    
    def __init__(self):
        """Inicializa a máquina com valores padrão."""
        self.nivel_agua = 0.0
        self.nivel_shampoo = 0.0
        self.pet_atual = None
        self.pet_limpo = False
        self.maquina_limpa = True
    
    def dar_banho(self):
        """
        Realiza o banho do pet atual.
        
        Returns:
            str: Mensagem de sucesso ou erro
        """
        if self.pet_atual is None:
            return "Erro: Nenhum pet na máquina!"
        
        if self.nivel_agua < self.CONSUMO_AGUA_BANHO:
            return (f"Erro: Água insuficiente! Necessário: {self.CONSUMO_AGUA_BANHO}L, "
                    f"Disponível: {self.nivel_agua}L")
        
        if self.nivel_shampoo < self.CONSUMO_SHAMPOO_BANHO:
            return (f"Erro: Shampoo insuficiente! Necessário: {self.CONSUMO_SHAMPOO_BANHO}L, "
                    f"Disponível: {self.nivel_shampoo}L")
        
        self.nivel_agua -= self.CONSUMO_AGUA_BANHO
        self.nivel_shampoo -= self.CONSUMO_SHAMPOO_BANHO
        self.pet_limpo = True
        
        return (f"[OK] Banho do {self.pet_atual} realizado com sucesso!\n"
                f"     Água consumida: {self.CONSUMO_AGUA_BANHO}L | "
                f"Shampoo consumido: {self.CONSUMO_SHAMPOO_BANHO}L")
    
    def abastecer_agua(self):
        """
        Adiciona 2L de água ao tanque.
        
        Returns:
            str: Mensagem de sucesso ou aviso
        """
        nova_quantidade = self.nivel_agua + self.ABASTECIMENTO_PADRAO
        
        if nova_quantidade > self.CAPACIDADE_AGUA:
            diferenca = self.CAPACIDADE_AGUA - self.nivel_agua
            self.nivel_agua = self.CAPACIDADE_AGUA
            return (f"Aviso: Tanque cheio! Abastecida apenas {diferenca}L de água.\n"
                    f"       Nível de água: {self.nivel_agua}L / {self.CAPACIDADE_AGUA}L")
        
        self.nivel_agua = nova_quantidade
        return (f"[OK] Abastecimento de água realizado!\n"
                f"     {self.ABASTECIMENTO_PADRAO}L adicionados.\n"
                f"     Nível de água: {self.nivel_agua}L / {self.CAPACIDADE_AGUA}L")
    
    def abastecer_shampoo(self):
        """
        Adiciona 2L de shampoo ao tanque.
        
        Returns:
            str: Mensagem de sucesso ou aviso
        """
        nova_quantidade = self.nivel_shampoo + self.ABASTECIMENTO_PADRAO
        
        if nova_quantidade > self.CAPACIDADE_SHAMPOO:
            diferenca = self.CAPACIDADE_SHAMPOO - self.nivel_shampoo
            self.nivel_shampoo = self.CAPACIDADE_SHAMPOO
            return (f"Aviso: Tanque cheio! Abastecida apenas {diferenca}L de shampoo.\n"
                    f"       Nível de shampoo: {self.nivel_shampoo}L / {self.CAPACIDADE_SHAMPOO}L")
        
        self.nivel_shampoo = nova_quantidade
        return (f"[OK] Abastecimento de shampoo realizado!\n"
                f"     {self.ABASTECIMENTO_PADRAO}L adicionados.\n"
                f"     Nível de shampoo: {self.nivel_shampoo}L / {self.CAPACIDADE_SHAMPOO}L")
    
    def verificar_nivel_agua(self):
        """
        Verifica e exibe o nível de água.
        
        Returns:
            str: Informações formatadas do nível de água
        """
        percentual = (self.nivel_agua / self.CAPACIDADE_AGUA) * 100
        status = self._obter_status_nivel(percentual)
        
        return (f"===== NÍVEL DE ÁGUA =====\n"
                f"  {self.nivel_agua}L / {self.CAPACIDADE_AGUA}L\n"
                f"  Percentual: {percentual:.1f}%\n"
                f"  Status: {status}\n"
                f"=========================")
    
    def verificar_nivel_shampoo(self):
        """
        Verifica e exibe o nível de shampoo.
        
        Returns:
            str: Informações formatadas do nível de shampoo
        """
        percentual = (self.nivel_shampoo / self.CAPACIDADE_SHAMPOO) * 100
        status = self._obter_status_nivel(percentual)
        
        return (f"===== NÍVEL DE SHAMPOO =====\n"
                f"  {self.nivel_shampoo}L / {self.CAPACIDADE_SHAMPOO}L\n"
                f"  Percentual: {percentual:.1f}%\n"
                f"  Status: {status}\n"
                f"=============================")
    
    def _obter_status_nivel(self, percentual):
        """
        Obtém o status textual baseado no percentual.
        
        Args:
            percentual: Percentual do tanque cheio
            
        Returns:
            str: Status descritivo
        """
        if percentual == 0:
            return "VAZIO"
        elif percentual <= 25:
            return "CRÍTICO"
        elif percentual <= 50:
            return "BAIXO"
        elif percentual < 100:
            return "BOM"
        else:
            return "CHEIO"
    
    def verificar_pet_no_banho(self):
        """
        Verifica se há pet na máquina e seu status.
        
        Returns:
            str: Informações do pet ou mensagem de vazio
        """
        if self.pet_atual is None:
            return "* Nenhum pet na máquina."
        
        status_limpeza = "LIMPO" if self.pet_limpo else "SUJO (Necessário limpar)"
        
        return (f"===== PET NA MÁQUINA =====\n"
                f"  Nome: {self.pet_atual}\n"
                f"  Status: {status_limpeza}\n"
                f"==========================")
    
    def colocar_pet_na_maquina(self, nome_pet):
        """
        Coloca um pet na máquina.
        
        Args:
            nome_pet: Nome do pet
            
        Returns:
            str: Mensagem de sucesso ou erro
        """
        if not self.maquina_limpa:
            return "Erro: A máquina está suja! Limpe antes de colocar outro pet."
        
        if self.pet_atual is not None:
            return f"Erro: Já existe um pet na máquina ({self.pet_atual})!"
        
        if not nome_pet or not nome_pet.strip():
            return "Erro: Nome do pet inválido!"
        
        self.pet_atual = nome_pet.strip()
        self.pet_limpo = False
        self.maquina_limpa = True
        
        return f"[OK] {self.pet_atual} colocado na máquina com sucesso!"
    
    def retirar_pet_da_maquina(self):
        """
        Retira o pet da máquina.
        
        Returns:
            str: Mensagem com o status da operação
        """
        if self.pet_atual is None:
            return "Erro: Nenhum pet na máquina!"
        
        if not self.pet_limpo:
            self.maquina_limpa = False
            resultado = (f"[AVISO] {self.pet_atual} foi retirado da máquina sem estar limpo.\n"
                        f"        A máquina agora está suja e precisa ser limpa!")
        else:
            resultado = f"[OK] {self.pet_atual} retirado com sucesso da máquina!"
        
        self.pet_atual = None
        self.pet_limpo = False
        
        return resultado
    
    def limpar_maquina(self):
        """
        Limpa a máquina.
        
        Returns:
            str: Mensagem de sucesso ou erro
        """
        if self.pet_atual is not None:
            return "Erro: Retire o pet da máquina antes de fazer limpeza!"
        
        if self.maquina_limpa:
            return "Informação: A máquina já está limpa!"
        
        if self.nivel_agua < self.CONSUMO_AGUA_LIMPEZA:
            return (f"Erro: Água insuficiente para limpeza! Necessário: "
                    f"{self.CONSUMO_AGUA_LIMPEZA}L, Disponível: {self.nivel_agua}L")
        
        if self.nivel_shampoo < self.CONSUMO_SHAMPOO_LIMPEZA:
            return (f"Erro: Shampoo insuficiente para limpeza! Necessário: "
                    f"{self.CONSUMO_SHAMPOO_LIMPEZA}L, Disponível: {self.nivel_shampoo}L")
        
        self.nivel_agua -= self.CONSUMO_AGUA_LIMPEZA
        self.nivel_shampoo -= self.CONSUMO_SHAMPOO_LIMPEZA
        self.maquina_limpa = True
        
        return (f"[OK] Máquina limpa com sucesso!\n"
                f"     Água consumida: {self.CONSUMO_AGUA_LIMPEZA}L | "
                f"Shampoo consumido: {self.CONSUMO_SHAMPOO_LIMPEZA}L")
    
    def obter_status_geral(self):
        """
        Obtém o status geral da máquina.
        
        Returns:
            str: Resumo formatado de todos os status
        """
        status_pet = "Vazia" if self.pet_atual is None else f"{self.pet_atual} ({('Limpo' if self.pet_limpo else 'Sujo')})"
        status_maquina = "Limpa" if self.maquina_limpa else "Suja"
        
        return (f"========== STATUS GERAL DA MÁQUINA DE BANHO ==========\n"
                f"|  Pet na máquina: {status_pet:<25} |\n"
                f"|  Água: {self.nivel_agua:<3.0f}L / {self.CAPACIDADE_AGUA}L                          |\n"
                f"|  Shampoo: {self.nivel_shampoo:<3.0f}L / {self.CAPACIDADE_SHAMPOO}L                        |\n"
                f"|  Estado da máquina: {status_maquina:<20} |\n"
                f"=====================================================")
