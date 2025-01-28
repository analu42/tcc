from django.shortcuts import render

def homepage(request):
    # return HttpResponse('O Jogo da Imitação')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("My About Page.")
    return render(request, 'about.html')

def story1(request):
    return render(request, 'story1.html')

def story2(request):
    return render(request, 'story2.html')

def story3(request):
    return render(request, 'story3.html')

def story4(request):
    return render(request, 'story4.html')

def choose(request):
    return render(request, 'choose.html')

def chat(request):
    return render(request, 'chat.html')

def chat_view(request):
    if request.method == "POST":
        # Recebe a mensagem do usuário
        user_message = request.POST.get('message', '')
        if user_message:
            # Salva a mensagem do usuário no banco
            Message.objects.create(sender="user", text=user_message)

            # Simula uma resposta do bot (pode ser integrado ao Gemini depois)
            bot_response = f"Você disse: {user_message}"
            Message.objects.create(sender="bot", text=bot_response)

        # Retorna as mensagens atualizadas
        messages = Message.objects.all().order_by('timestamp')
        return JsonResponse({'messages': [{'sender': msg.sender, 'text': msg.text} for msg in messages]})

    # Para GET, carrega o template inicial
    return render(request, 'chat.html')