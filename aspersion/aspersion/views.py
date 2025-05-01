from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bot.models import Bot


def botwork(request):
    users_message = ""
    reply = ""


    if request.method == 'POST':
        try:
            users_message = request.POST.get('users_resposnd')
            bot_response = Bot.objects.filter(users_resposnd__icontains=users_message).first()

            if bot_response:
                reply = bot_response.bot_response
            else:
                reply = "Say Something Else🥺"

        except:
            pass
    return render(request,"bot.html",{'users_message':users_message,'reply':reply})