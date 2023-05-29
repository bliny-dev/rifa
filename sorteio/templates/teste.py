def adiciona_premio(request):
    if request.method == 'POST':
        # Obtendo o ID do sorteio e o nome do prêmio a partir da requisição
        sorteio_id = request.POST.get('sorteio_id')
        nome_premio = request.POST.get('nome_premio')


        # Verificando se o prêmio já existe no banco de dados
        try:
            premio = Premios.objects.get(nome=nome_premio)
        except Premios.DoesNotExist:
            # Criando um novo objeto de prêmio se ele não existir
            premio = Premios(nome=nome_premio)
            premio.save()

        # Adicionando o prêmio ao sorteio
        sorteio.premios.add(premio)

        # Redirecionando para a página de gerenciamento de sorteios
        return redirect("gerir_sorteio")

    # Lidar com o caso em que a requisição não é do tipo POST
    return redirect("gerir_sorteio")
