from django.db import models

# Create your models here.

class TeamsInfo(models.Model):
    team_id = models.CharField(max_length=128,unique=True,primary_key=True)
    team_name = models.CharField(max_length=128,unique=True)
    branch = models.CharField(max_length=128)
    captain_phoneno = models.CharField(max_length=12)
    sport = models.CharField(max_length=12,default="null")

    def __str__(self):
        return self.team_id

class PlayersInfo(models.Model):
    player_team_id = models.ForeignKey(TeamsInfo,on_delete=models.CASCADE)
    player_id = models.CharField(max_length=12,unique=True,primary_key=True)
    player_role = models.CharField(max_length=128,null=True)
    phone_no = models.CharField(max_length=12,unique=True)
    branch = models.CharField(max_length=128)
    player_name = models.CharField(max_length=128,null=True)
    sport = models.CharField(max_length=12,default="null")

    def __str__(self):
        return self.player_id

class Umpires(models.Model):
    umpire_id = models.CharField(max_length=12,unique=True,primary_key=True)
    umpire_name = models.CharField(max_length=128)
    phone_no = models.CharField(max_length=12,unique=True)
    
    def __str__(self):
        return self.umpire_id

class Matches(models.Model):
    team1_id = models.CharField(max_length=128,unique=True)
    team2_id = models.CharField(max_length=128,unique=True)
    umpire_id = models.ForeignKey(Umpires,on_delete=models.CASCADE)
    status = models.CharField(max_length=128)
    match_no = models.CharField(max_length=12,unique=True,primary_key=True)

    def __str__(self):
        return self.match_no

class CriketScores(models.Model):
    cmatch_no = models.ForeignKey(Matches,on_delete=models.CASCADE)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    status = models.CharField(max_length=128)
    overs = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.cmatch_no)
   
