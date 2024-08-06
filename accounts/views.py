from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Medico, Consulta
from .forms import PacienteForm, ConsultaForm
import google.generativeai as genai
import textwrap
from .utils import calcular_idade_paciente

def home(request):
    consultas = Consulta.objects.all()
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()

    total_pacientes = pacientes.count()
    total_medicos = medicos.count()
    total_consultas = consultas.count()

    consultas_agendadas = consultas.filter(status='Agendada').count()
    consultas_realizadas = consultas.filter(status='Realizada').count()
    consultas_canceladas = consultas.filter(status='Cancelada').count()
 
    consultas_agendadas_ordenadas = consultas.filter(status='Agendada').order_by('data')
    # imprimir a data da consulta
    context = {
        'consultas': consultas,
        'pacientes': pacientes,
        'medicos': medicos,
        'total_pacientes': total_pacientes,
        'total_medicos': total_medicos,
        'total_consultas': total_consultas,
        'consultas_agendadas': consultas_agendadas,
        'consultas_realizadas': consultas_realizadas,
        'consultas_canceladas': consultas_canceladas,
        'consultas_agendadas_ordenadas': consultas_agendadas_ordenadas,
    }

    return render(request, 'accounts/dashboard.html', context)

def pacientes(request, pk_test):
    paciente = get_object_or_404(Paciente, id=pk_test)
    idade_paciente = calcular_idade_paciente(paciente)
    context = {'paciente': paciente, 'idade':idade_paciente}
    return render(request, 'accounts/pacientes.html', context)

def medicos(request, pk_test):
    medico = get_object_or_404(Medico, id=pk_test)
    medicos = Medico.objects.all()
    consultas_obj = Consulta.objects.filter(medico=medico)
    consultas_realizadas = [str(consulta) for consulta in consultas_obj.filter(status='Realizada') if consulta.paciente]
    consultas_agendadas = Consulta.objects.filter(medico=medico, status='Agendada')
    consultas_ordenadas = consultas_obj.order_by('data')
    context = {
        'medico': medico,
        'medicos': medicos,
        'consultas_realizadas': consultas_realizadas,
        'consultas_agendadas': consultas_agendadas,
        'consultas_ordenadas': consultas_ordenadas,
    }
    return render(request, 'accounts/medicos.html', context)

def consultas(request):
    return render(request, 'accounts/consultas.html')


def adicionar_consulta(request, medico_id):
    medicos = Medico.objects.all()
    medico = get_object_or_404(Medico, id=medico_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.medico = medico
            consulta.save()
            return redirect('medicos', pk_test=medico_id)
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = ConsultaForm()
    return render(request, 'accounts/adicionar_consulta.html', {'form': form, 'medico_id': medico_id, 'medico': medico, 'medicos': medicos})


def atualizar_consulta(request, medico_id, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('medicos', pk_test=medico_id)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'accounts/atualizar_consulta.html', {'form': form, 'medico_id': medico_id})


# Configurar a chave de API
GOOGLE_API_KEY = 'AIzaSyClxm_magrxuFMro8zeUR-xVmL2ObQpND8'
genai.configure(api_key=GOOGLE_API_KEY)

# Selecionar o modelo
model = genai.GenerativeModel('gemini-1.5-flash')

def processar_input(request):

    medicos = Medico.objects.all()

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if user_input:
            prompt_context = "Faça um resumo dessa consulta médica, em formato de um relatório médico."
            prompt = model.generate_content(user_input+'\n'+prompt_context)
            output = textwrap.dedent(prompt.text)
            request.session['output'] = output
            return redirect('processar_input')
    else:
        output = request.session.pop('output', None)

    return render(request, 'accounts/processar_input.html', {'output': output, 'medicos': medicos})