from django.contrib import admin
from django.contrib.sites.models import Site
from bot.models import Bot

class BotAdmin(admin.ModelAdmin):
    list_display=('users_resposnd','bot_response')

admin.site.register(Bot,BotAdmin)