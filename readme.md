# Projeto banco Dio 3.0
***
Esse programa é uma melhoria da versão anterior, que foi feito utilizando orientação a obejto.
É um programa simples que simula o sistema de acesso de um funcionário de Banco. Que tem como função fazer cadastro de cliente, cadastro de conta e a movimentação financeira da mesma.
## Principais funções
1. Criar cadastro de cliente.
2. Cadastrar uma conta, ou mais, a um cliente específico.
3. Visualização de cadastro realizados.
   1. Visualização completa de dados cadastrados.
   2. Possibilidade de correção de dados cadastrados.
4. Área para movimentação de conta.
   1. Deposito
   2. Saque
   3. Extrato bancário
5. Área de exclusiva do programador.
   1. Visualização de listas e dicionários.
   2.  Possíveis atualizações de estruturas de lista e dicionários.
 ## Funcionamento detalhado
Programa presou em ser o mais intuitivo possível, dispondo as suas opções na ordem mais conveniente aos processos de cadastramentos, visualizações e movimentações bancárias.
Até então, o presente programa foi testado em todas as suas funcionalidades e não apresenta erros de travamentos ou lógicos. Todas as funcionalidades foram criadas com seus devidos tratamentos de erros.
### 1. Cadastrar cliente
Campo responsável pelo cadastramento de um cliente. Nele, por enquanto, foi criado apenas 4 campos cadastrais: Nome, CPF, data de nascimento e endereço. Podendo ser acrescentado outros como telefone, e-mail, etc.
Em todos eles se obedecem regras específicas de tratamento de erros de maneira a receber apenas o que foi indicado.
E em cada um deles é oferecido no final de cada cadastro a opção de confirmação junto com a de correção.
Em todo o processo, o usuário tem a opção de encerrar quando bem entender, com a devida entrada indicada.
1. Nome:
Recebe uma String.
Retorna o valor da entrada com as iniciais de cada nome em maiúsculo.
2. CPF:
Recebe apenas uma entrada numérica de 11 caracteres sem pontuação.
Retorna o valor da entrada com as devidas pontuações.
E não aceita CPFs já cadastrados
3. Nascimento:
Recebe apenas uma entrada no formato de data no padrão Pt-Br.
E retorna ao cadastro, junto com a data de nascimento a idade do cliente cadastrado.

### 2. Cadastrar conta
* Abre duas opções de pesquisa de cadastro. Uma através do CPF e outra numa lista disposta em ordem alfabética.
* Uma vez selecionado o cadastro, abre a opção de cadastrar uma conta nova ou de voltar.
* Optando pela opção de cadastramento, uma conta é gerada e vinculada ao cadastro do cliente selecionado.
* O valor das contas são criados em ordem decrescente, de forma que se um cliente for excluído, o valor da conta não se repete.
* Um cliente pode ter mais de uma conta cadastrada. E nunca uma conta ter mais de um cliente.
* O valor da agência, por enquanto é fixo.

### 3. Movimentar conta
* Abre duas opções de pesquisa de cadastro. Uma através do CPF e outra numa lista disposta em ordem alfabética.
* Selecionando um cadastro, abre uma área com os dados do cliente e suas contas cadastradas.
* Ao se escolher uma conta, abre-se as opções de depósito, saque e extrato.
* A entrada do **depósito e do **saque, recebem apenas um valor numérico, do tipo Float. 
* Apesar da entrada do tipo Float, ela deve obedecer o padrão Pt-Br com o uso de virgula.
* E os valores retornados para confirmação tem o padrão Pt-Br, com virgula depois da casa decimal e com o sinal de cifrão moeda nacional corrente.
* O saque não pode ser feito sem saldo em conta.
* A opção do **extrato é apenas para visualização. Contém os valores de depósito e saque exibidos no padrão Pt-Br, cada um a data da transação e finaliza com o dado do saldo atual.
### 4. Verificar cadastro
* Mostra uma lista geral com nome e cpf de cadastros já realizados.
### 5. Lista geral
* Abre duas opções de pesquisa de cadastro. Uma através do CPF e outra numa lista disposta em ordem alfabética.
* Se selecionado o número do cliente, abre uma área com todos os dados do cliente com as opções de correção dos dados cadastrais, de exclusão do cadastro ou de encerramento da consulta.
### 6. Área do programador
* Área usada para testes. Principalmente para verificar os valores e estruturas das listas, dicionários e classes.
* Área dinâmica, que pode ser alterada para o uso demandado. 