from django.contrib import admin
from bpl_app.models import TeamsInfo,PlayersInfo,Umpires,Matches,CriketScores
# Register your models here.

admin.site.register(TeamsInfo)
admin.site.register(PlayersInfo)
admin.site.register(Umpires)
admin.site.register(Matches)
admin.site.register(CriketScores)