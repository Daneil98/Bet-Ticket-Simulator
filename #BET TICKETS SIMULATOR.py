#BET TICKETS SIMULATOR
import random
import csv
import pandas as pd

team_bet = ['home win', 'draw', 'away win']
player_bet = ['To score', 'Not score']
corner = ['home win', 'draw', 'away win']

N = int(input("Please input the total number of matches to be played: "))
n = int(input("Enter the total number of possible event outcomes for each match: "))
bets = input("what type of bet do you want to place?:")

def combinations(n, N):
    #This function calculates the total number of possible tickets that can be played within the constraints N & n
    total_tickets = pow(n, N)
    print (f"The total number of tickets needed to cover all possible outcomes are: {total_tickets}")     


def bet():
    #This fuction tells users about their bets and gets the kind of bet they want
    print (f"Team bets are:  {team_bet}")
    print (f"Player bets are:  {player_bet}")
    print (f"Corner bets are:  {corner}")
    
    
    
    
def teams():
    specific_rows = [0,1,2,3] 
    df = pd.read_csv('epl-2022-UTC.csv', usecols=["Home_Team", "Away_Team"], skiprows = lambda x: x not in specific_rows)
    home_team = []
    away_team = []
    for Home_Team in df['Home_Team']:
        home_team.append(Home_Team)
    for Away_Team in df['Away_Team']:
        away_team.append(Away_Team)
    home_str = "\n".join(home_team)
    away_str = "\n".join(away_team)
    #print(f"HOME TEAMS are: {home_str}")
    #print(f"AWAY TEAMS are: {away_str}")    
    matches = [f"{home} Vs {away}" for home, away in zip(home_team, away_team)]
    if bets == "player_bet":
        for match in matches:
            for bet in player_bet:
                print(f"{match} - {bet}")        
        
    elif bets == "team_bet":
        for match in matches:
            for bet in team_bet:
                print(f"{match} - {bet}")
                
    elif bets == "corner":
        for match in matches:
            for bet in corner:
                print(f"{match} - {bet}")
    
        

if __name__ == "__main__": 
    combinations(n, N)
    bets()
    teams() 
    
