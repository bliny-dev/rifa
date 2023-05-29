from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sorteio, Premios, Promocaos


def gerir_sorteio(request):
    if request.method == 'GET':
        sorteios = Sorteio.objects.filter(status=True)
        return render(request, "gere_rifa.html", {'sorteios': sorteios})

    elif request.method == 'POST':
        
        # Lógica para salvar os dados do formulário
        # Após salvar os dados, redirecionar para outra página
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        qtd_bilhetes = request.POST.get('qtd_bilhetes')
        data_sorteio = request.POST.get('data_sorteio')
        status = request.POST.get('status', False) == 'True'
        image_sorteio = request.POST.get('image_sorteio')
        user=request.user  

        sorteio = Sorteio(
            nome=nome,
            descricao=descricao,
            preco=preco,
            qtd_bilhetes=qtd_bilhetes,
            data_sorteio=data_sorteio,
            status=status,
            image_sorteio=image_sorteio,
            user=request.user  
        )
        sorteio.save()

        
        # # Lide com o envio da imagem
        # imagens = request.FILES.getlist('imagem_sorteio')  # Obtenha a lista de imagens enviadas
        # for imagem in imagens:
        #     images_sorteio = Images_sorteio(arquivo=imagem)
        #     images_sorteio.save()
        #     sorteio.images_sorteio.add(images_sorteio)  # Associe a imagem ao objeto Sorteio

        return redirect("gerir_sorteio")


def adiciona_premio(request):
    
    sorteio_id = request.POST.get('sorteio_id')
    descricao_premio = request.POST.get('descricao_premio')
    numero_premio = request.POST.get('numero_premio')

    # Verificando se o ID do sorteio é válido
    try:
        sorteio = Sorteio.objects.get(id=sorteio_id)
    except Sorteio.DoesNotExist:
        # Lidar com o caso em que o sorteio não existe
        return redirect("gerir_sorteio")


    if request.method == 'POST':
        # Obtendo o ID do sorteio a partir da requisição
        sorteio_id = request.POST.get('sorteio_id')
        numero_premio = request.POST.get('numero_premio')
        descricao_premio = request.POST.get('descricao_premio')

        # Criando um novo objeto de prêmio associado ao sorteio
        premio = Premios(
            numero_premio=numero_premio,
            descricao_premio=descricao_premio,
            sorteio=sorteio
        )
        premio.save()

        sorteio.premio.add(premio)

    
        # Redirecionando para a página de gerenciamento de sorteios
        return redirect("gerir_sorteio")

    # Lidar com o caso em que a requisição não é do tipo POST
    return redirect("gerir_sorteio")