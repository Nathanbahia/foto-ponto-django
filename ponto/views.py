from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from core import settings
from .forms import PontoForm
from .models import Ponto
from datetime import datetime


def index(request):
    if str(request.method) == "POST":
        form = PontoForm(request.POST, request.FILES)
        if form.is_valid():
            data = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
            matricula = form.cleaned_data['matricula']
            aves = form.cleaned_data['aves']
            foto = form.cleaned_data['foto']
            ponto = Ponto(data=data, matricula=matricula, aves=aves, foto=foto)
            ponto.save()

            title = str(data)
            html_content = """
            <h1>Sulgipe</h1>
            <h2>Registro de Ponto</h2>
            <hr>
            <p>Data|Hora: {}</p>
            <p>Matrícula: {}</p>
            <hr>            
            <a href="https://pontosulconta.pythonanywhere.com/visualizacao/{}">
                Visualize a foto clicando aqui!
            </a>
            """.format(data, matricula, ponto.pk)

            text_content = title
            from_mail = settings.EMAIL_HOST_USER
            msg = EmailMultiAlternatives(
                title, 
                text_content, 
                from_mail, 
                ['nathanbabahia@gmail.com', 'junioroliveiraeng@icloud.com', ]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Foto salva com sucesso.")
            form = PontoForm()
        else:
            messages.error(request, "Falha ao salvar foto.")
    else:
        form = PontoForm()

    context = {'form': form}

    return render(request, 'index.html', context)


def historico(request):
    pontos = Ponto.objects.all().order_by("-pk")[:7]
    context = {'pontos': pontos}
    return render(request, 'historico.html', context)


def visualizar_foto(request, pk):
    foto = Ponto.objects.get(pk=pk)
    return render(request, 'visualizacao.html', {'foto': foto})