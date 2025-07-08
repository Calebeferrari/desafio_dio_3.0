from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, nome, cpf, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.contas = []
    
    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nNascimento: {self.nascimento}\nIdade: {self.idade}\nContas: {self.visualizacao_contas_vinculadas}'
    
    # Calculando idade - criar uo atributo idade a partir de nascimento
    @property
    def idade(self):
        # Converter data em objeto tipo date
        data_objeto = datetime.strptime(self.nascimento, "%d/%m/%Y").date()

        # Calculo de idade
        idade = datetime.today().year - data_objeto.year

        # Verificando se já fez aniversário
        if (datetime.today().month, datetime.today().day) < (data_objeto.month, data_objeto.day):
            idade -= 1
        return idade
    
    # Formatação de cpf
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf_informado):
        cpf_convertion = str(cpf_informado)[:3] + '.' + str(cpf_informado)[3:6] + '.' + str(cpf_informado)[6:9] + '-' + str(cpf_informado)[9:11]
        self._cpf = cpf_convertion

    
    # Vinculação de conta a cliente
    def vincular_conta(self, conta_unica):
        self.contas.append(conta_unica)

    
    # Visualização de informações de contas vinculadas
    @property
    def visualizacao_contas_vinculadas(self):
        if self.contas != []:
            contas_ = ''
            for conta_vis in self.contas:
                contas_ += str(f'\n{conta_vis}')

            return contas_
        else:
            return f'Não há constas vinculadas.'


# Classe Conta
class Conta:

    # Declaração de variável de classe que será usada para criar número de contas
    contador_contas = 1

    def __init__(self):
        self.agencia = f'{1:03}'
        self.conta = Conta.contador_contas
        Conta.contador_contas += 1 # Adiciona mais 1 toda vez que cria uma conta nova
        self.saldo = 0
        self.extrato = []
    
    def __str__(self):
        return f'Agência: {self.agencia} - N° Conta: {self.conta:04}'
    
    
    def deposito(self, valor):
        # Atualização de saldo
        self.saldo += valor
        # Armazenando informações de transação p/ extrato
        self.extrato.append(self.transacao_formatada(valor, 'deposito'))

        return self.saldo
    

    def saque(self, valor):
        # Condição p/ saque.
        if self.saldo <= 0 or self.saldo < valor:
            return False
        else:
            # Atualização de saldo
            self.saldo -= valor
            # Armazenando informações de transação p/ extrato
            self.extrato.append(self.transacao_formatada(valor, 'saque'))

            return self.saldo
    
    
    def extrato_bancario(self):
        # Variável que conterá informação de extrato
        info_extrato = ''
        # Ciclo que organiza informações de extrato
        for pos, valor in enumerate(self.extrato):
            for key, value in valor.items():
                info_extrato +=  f'{key}: {value}\n'
            info_extrato += '\n'
        
        # Retorno de informações de extrato - Caso não haja nenhum
        if info_extrato == '':
            return f'Nenhuma transação efetuada.'
        # Retorno de informações de extrato - Caso haja informações
        else:
            return info_extrato


    #@staticmethod
    def transacao_formatada(self, valor_transacao, tipo_transacao):
        '''
        valor_transacao: Recebe o valor da transação
        tipo_transacao: Receb o tipo da transação, que pode ser 'deposito' ou 'saque'.
        '''

        # Criando data da transação bancária
        data_transacao = datetime.today()
        data_formatada = data_transacao.strftime("%d/%m/%Y - %H:%M:%S")

        # Formatar saída de valores monetários.
        valor_formatado = str(f'{valor_transacao:.2f}').replace('.', ',')
        saldo_formatado = str(f'{self.saldo:.2f}').replace('.', ',')

        # Dicionário que armazena as informações da transação bancária
        info_transacao = {}
        if tipo_transacao == 'deposito':
            info_transacao['Depósito'] = f'R${valor_formatado}'

        elif tipo_transacao == 'saque':
            info_transacao['Saque'] = f'R${valor_formatado}'

        info_transacao['Data'] = data_formatada
        info_transacao['Saldo'] = f'R${saldo_formatado}'

        return info_transacao



# Classe Lista geral de cadastros
class Lista_Geral:
    def __init__(self):
        self.lista_clientes = []

    
    def adicionar_cadastros(self, cadastro_cliente):
        self.lista_clientes.append(cadastro_cliente)
    
    
    def excluir_cadastro(self, posicao_cadastro):
        del self.lista_clientes[posicao_cadastro]
    

    def organizar_lista(self, lista_cadastros):
        lista_ordenada = sorted(lista_cadastros, key=lambda cliente:cliente.nome)
        self.lista_clientes = lista_ordenada

    
    def visualizar_cadastros(self):
        # Informa o cabeçalho da lista
        print_visualizacao = f'{'Pos.':03} {'Cliente':^31} {'CPF':^11}\n'+'-'*50+'\n'

        for pos, cadastro in enumerate(self.lista_clientes, 1):
            # Mostra resultados da lista formatados
            print_visualizacao += f'{pos:03} {cadastro.nome[:31]:31} {cadastro.cpf}\n'
        
        return print_visualizacao
    
    
    def validacao_cpf(self, cpf_informado):
        # Validador de cpf
        validador_cpf = True

        # Ciclo p/ verificar se cpf já existe
        for pos, cpf in enumerate(self.lista_clientes):
            if cpf_informado == cpf.cpf:
                validador_cpf = False

        return validador_cpf

#------------------------------------------------------------
if __name__ == "__main__":

    p1 = Cliente('Tay',12312312310, '01/11/1990')
    p2 = Cliente('Fer',12312312311, '06/04/1989')
    p3 = Cliente('Jan',12312312312, '20/01/1997')
    p4 = Cliente('Anf',12312312313, '15/11/1992')

    lista_teste = Lista_Geral()
    lista_teste.adicionar_cadastros(p1)
    lista_teste.adicionar_cadastros(p2)
    lista_teste.adicionar_cadastros(p3)
    lista_teste.adicionar_cadastros(p4)

    lista_teste.organizar_lista(lista_teste.lista_clientes)

    c1 = Conta()
    c2 = Conta()

    p1.vincular_conta(c1)
    #p1.vincular_conta(c2)

    c1.deposito(200)
    c1.saque(50)
    
    #print(c1.saldo)
    print(c1.extrato_bancario())




