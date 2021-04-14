class Cricket:
    def __init__(self,
                 name,
                 jersey,
                 roll,
                 batting_style,
                 no_ipl,
                 odi,
                 no_world,
                 s_100,
                 s_50,
                 straight_rate,
                 wickets,
                 bowling):
        self.name = name
        self.jersey = jersey
        self.roll = roll
        self.batting_style = batting_style
        self.no_ipl = no_ipl
        self.odi = odi
        self.no_world = no_world
        self.s_100 = s_100
        self.s_50 = s_50
        self.straight_rate = straight_rate
        self.wickets = wickets
        self.bowling = bowling

    def profile_Batsman(self):
        print(f'''{self.name} profile
    jersey Number: {self.jersey}
    Type of roll: {self.roll}
    Batting Style: {self.batting_style}
    Bowling style: {self.bowling}
    Number Of Ipl Matches played: {self.no_ipl}
    Number Of one days Matches played: {self.odi}
    Number of world cup Matches played: {self.no_world}
    Number 100 score: {self.s_100}
    Number 100 score: {self.s_50}
    Number Of wickets: {self.straight_rate} 
    Straight Rate: {self.straight_rate}
''')


c1 = Cricket('Ms Dhoni', 7, 'Batting', 'Right_Hand_Batsman', 'Not Bowld', 5, 10, 3, 100, 500, 150, 450)
c1.profile_Batsman()
c2 = Cricket('Kohli', 18, 'Batting', 'Right_Hand_Batsman', "Not Bowld", 5, 5, 3, 80, 500, 145, 340)
c2.profile_Batsman()
c3 = Cricket('Raina', 5, 'Batting', 'Right_Hand_Batsman', 'Not Bowld', 4, 3, 7, 60, 500, 243, 45)
c3.profile_Batsman()
c4 = Cricket('Boomra', 5, 'Bowling', 'Right_Hand_Bowler', 'Right hand Bowler', 4, 3, 7, 60, 500, 120, 20)
c4.profile_Batsman()
