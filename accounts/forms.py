from django import forms
from .models import Paciente, Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'nome_social': 'Nome Social',
            'nome_mae': 'Nome da Mãe',
            'sexo': 'Sexo',
            'genero': 'Gênero',
            'data_nascimento': 'Data de Nascimento',
            'raca': 'Raça',
            'nacionalidade': 'Nacionalidade',
            'cidade_nascimento': 'Cidade de Nascimento',
            'uf_nascimento': 'UF de Nascimento',
            #Estrangeiros
            'data_naturalizacao': 'Data de Naturalização',
            'pais_nascimento': 'País de Nascimento',
            'numero_passaporte': 'Número do Passaporte',
            'pais_emissao': 'País de Emissão do Passaporte',
            'data_emissao': 'Data de Emissão do Passaporte',
            'data_validade': 'Data de Validade do Passaporte',
             # Contato
            'email': 'Email',
            'tipo_telefone': 'Tipo de Telefone',
            'ddd': 'DDD',
            'telefone': 'Telefone',
              # Endereço
            'tipo_logradouro': 'Tipo de Logradouro',
            'nome_logradouro': 'Nome do Logradouro',
            'numero_logradouro': 'Número do Logradouro',
            'complemento_logradouro': 'Complemento do Logradouro',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'uf': 'UF',
            'pais': 'País',
            'cep': 'CEP',
             # Identificação
            'cpf': 'CPF',
            'numero_identidade': 'Número da Identidade',
            'uf_identidade': 'UF da Identidade',
            'orgao_emissor_identidade': 'Órgão Emissor da Identidade',
            'data_emissao_identidade': 'Data de Emissão da Identidade',
            'numero_cns': 'Número do CNS',
                # Dados dos representantes legais
            'nome_representante_legal': 'Nome do Representante Legal',
            'relacionamento_representante_legal': 'Relacionamento com o Representante Legal',
            'cpf_representante_legal': 'CPF do Representante Legal',
            'descricao': 'Descrição',
        }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        exclude = ['medico']  # Exclui o campo medico do formulário
        widgets = {
            'duracao_estimada': forms.TextInput(attrs={'placeholder': 'hh:mm:ss'}),
        }