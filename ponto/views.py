from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from .forms import PontoForm
from .models import Ponto


def index(request):
    if str(request.method) == "POST":
        form = PontoForm(request.POST, request.FILES)
        if form.is_valid():
            data = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
            nome = request.user
            foto = form.cleaned_data['foto']
            
            ponto = Ponto(data=data, nome=nome, foto=foto)
            ponto.save()

            messages.success(request, "Foto salva com sucesso.")
            form = PontoForm()
        else:
            messages.error(request, "Falha ao salvar foto.")
    else:
        form = PontoForm()

    context = {'form': form}

    return render(request, 'index.html', context)


def historico(request):
    pontos = Ponto.objects.all()[:7]
    context = {'pontos': pontos}
    return render(request, 'historico.html', context)