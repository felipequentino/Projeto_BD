from datetime import date

def calcular_idade_paciente(paciente):
  """
  Calcula a idade do paciente em anos, meses e dias.

  Args:
    paciente: Objeto do paciente que contém a data de nascimento.

  Returns:
    Idade do paciente formatada como string.
  """

  data_nascimento = paciente.data_nascimento
  data_atual = date.today()
  diferenca_tempo = data_atual - data_nascimento
  anos = diferenca_tempo.days // 365
  meses = (diferenca_tempo.days % 365) // 30
  dias = (diferenca_tempo.days % 365) % 30
  idade_em_anos_meses_dias = f"{anos} anos, {meses} meses e {dias} dias"
  return idade_em_anos_meses_dias