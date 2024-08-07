from django.db import models

class Paciente(models.Model):
    SEXOS = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Intersexo', 'Intersexo')
    )
    RACES = (
        ('Branca', 'Branca'),
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
        ('Sem Informação', 'Sem Informação')
    )
    
    nome = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=20, null=True, choices=SEXOS)
    genero = models.CharField(max_length=50, null=True)
    data_nascimento = models.DateField(null=True)
    raca = models.CharField(max_length=20, null=True, choices=RACES)
    email = models.EmailField(max_length=200, null=True)
    ddd = models.CharField(max_length=3, null=True)
    telefone = models.CharField(max_length=200, null=True)
    cep = models.CharField(max_length=10, null=True)
    cpf = models.CharField(max_length=11, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    descricao = models.TextField(null=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    ESPECIALIDADES = (
        ('Cardiologista', 'Cardiologista'),
        ('Psiquiatra', 'Psiquiatra'),
        ('Ortopedista', 'Ortopedista'),
        ('Dermatologista', 'Dermatologista'),
        ('Oftalmologista', 'Oftalmologista'),
        ('Ginecologista', 'Ginecologista'),
        ('Pediatra', 'Pediatra'),
        ('Urologista', 'Urologista'),
        ('Neurologista', 'Neurologista'),
        ('Fisioterapeuta', 'Fisioterapeuta'),
        ('Psicólogo', 'Psicólogo'),
        ('Terapeuta', 'Terapeuta'),
        ('Cirurgião', 'Cirurgião'),
        ('Anestesista', 'Anestesista'),
        ('Radiologista', 'Radiologista'),
        ('Oncologista', 'Oncologista'),
        ('Infectologista', 'Infectologista'),
        ('Outro', 'Outro')
    )
    
    SEXOS = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Intersexo', 'Intersexo')
    )
    
    RACAS = (
        ('Branca', 'Branca'),
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
        ('Sem Informação', 'Sem Informação')
    )

    nome = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=20, null=True, choices=SEXOS)
    genero = models.CharField(max_length=50, null=True, blank=True)
    data_nascimento = models.DateField(null=True)
    raca = models.CharField(max_length=50, null=True, choices=RACAS, blank=True)
    email = models.CharField(max_length=50, null=True)
    ddd = models.CharField(max_length=3, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    especialidade = models.CharField(max_length=50, null=True, choices=ESPECIALIDADES)
    pacientes = models.ManyToManyField(Paciente)

    def __str__(self):
        return f"{self.nome.capitalize()} - {self.especialidade.capitalize()}"

class Consulta(models.Model):
    STATUS = (
        ('Agendada', 'Agendada'),
        ('Realizada', 'Realizada'),
        ('Cancelada', 'Cancelada')
    )

    paciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    medico = models.ForeignKey(Medico, null=True, on_delete=models.SET_NULL)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    descricao = models.TextField(null=True)
    duracao_estimada = models.DurationField(null=True)

    def get_especialidade(self):
        return 'Consulta com um ' + self.medico.especialidade
    
    def format_duracao(self):
        if self.duracao_estimada:
            total_seconds = self.duracao_estimada.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            return f"{hours} horas e {minutes} minutos"
        return "Duração não especificada"
        
    def __str__(self):
        try:
            return f"Paciente: {self.paciente.nome.capitalize()} - Médico: {self.medico.nome.capitalize()} - Status: {self.status.capitalize()}"
        except:
            return "Consulta com Nome errado"
    
