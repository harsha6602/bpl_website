from django.shortcuts import render,redirect
from .models import PlayersInfo,TeamsInfo,CriketScores
# Create your views here.

max_team_id_no = 1


def index(request):
    return render(request,"html files/index.html")

def registration(request):

    if request.method == "POST":
        global max_team_id_no
        max_team_id_no += 1
        print(max_team_id_no)
        team_id_generated = "bpl_team_" + str(max_team_id_no)
        team_names = request.POST['team_name']
        branch_name = request.POST['branch']
        cap_phno = request.POST['captain_phno']
        team_info = TeamsInfo(team_id = team_id_generated,
                                                     team_name = team_names,
                                                     branch = branch_name,
                                                     captain_phoneno = cap_phno)
        team_info.save()

        cap_name = request.POST['captain_name']
        cap_usn = request.POST['captain_usn']
        new_info = PlayersInfo(player_team_id = team_info,
                             player_id = cap_usn,
                             player_role="captain", 
                             phone_no = cap_phno,
                             branch = branch_name,
                             player_name = cap_name,
                             sport = "Cricket")
        new_info.save()
        for i in range(2,9):
            j = str(i)
            name = request.POST['name'+j]
            usn = request.POST['usn'+j]
            phno = request.POST['phno'+j]
            new_info = PlayersInfo(player_team_id = team_info,
                             player_id = usn,
                             player_role="players", 
                             phone_no = phno,
                             branch = branch_name,
                             player_name = name,
                             sport = "Cricket")
            new_info.save()

    return render(request,"html files/registration.html")

def login(request):
    return redirect('/admin')

def scores(request):
    live = CriketScores.objects.all()
    team_score = {'live_score':live}
    print(team_score['live_score'][0])
    return render(request,"html files/scores.html",context=team_score)

def badminton_reg(request):
    if request.method == "POST":
        global max_team_id_no
        max_team_id_no += 1
        print(max_team_id_no)
        team_id_generated = "bpl_team_" + str(max_team_id_no)
        team_names = request.POST['team_name']
        branch_name = request.POST['branch']
        cap_phno = request.POST['captain_phno']
        team_info = TeamsInfo(team_id = team_id_generated,
                                                     team_name = team_names,
                                                     branch = branch_name,
                                                     captain_phoneno = cap_phno)
        team_info.save()
        cap_name = request.POST['captain_name']
        cap_usn = request.POST['captain_usn']
        new_info = PlayersInfo(player_team_id = team_info,
                             player_id = cap_usn,
                             player_role="captain", 
                             phone_no = cap_phno,
                             branch = branch_name,
                             player_name = cap_name,
                             sport = "badminton")
        new_info.save()
        name = request.POST['name2']
        usn = request.POST['usn2']
        phno = request.POST['phno2']
        new_info = PlayersInfo(player_team_id = team_info,
                             player_id = usn,
                             player_role="players", 
                             phone_no = phno,
                             branch = branch_name,
                             player_name = name,
                             sport = "badminton")
        new_info.save()   

    return render(request,"html files/badminton_reg.html")


def team_details(request):
    team_list = PlayersInfo.objects.order_by('player_team_id')
    team_id_list = {'player_info':team_list}
    print(team_id_list['player_info'][1])
    return render(request,'html files/players_info.html',context=team_id_list)