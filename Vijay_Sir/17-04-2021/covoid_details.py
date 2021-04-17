class Covid:
    total_india = 0
    total_male_attacks = 0
    total_female_attacks = 0

    def __init__(self, male_attacks, female_attacks):
        self.male_attacks = male_attacks
        self.female_attacks = female_attacks
        Covid.total_india = self.male_attacks + self.female_attacks
        Covid.total_male_attacks = Covid.total_male_attacks + self.male_attacks
        Covid.total_female_attacks = Covid.total_female_attacks + self.female_attacks

    def ap_covid(self, ap_male_attacks, ap_female_attacks):
        total_ap_attack = 0
        total_ap_attack = total_ap_attack + ap_male_attacks + ap_female_attacks
        Covid.total_india = total_ap_attack + Covid.total_india
        Covid.total_male_attacks = ap_male_attacks + Covid.total_male_attacks
        Covid.total_female_attacks = ap_female_attacks + Covid.total_female_attacks

        print(f'''AP males persons covid attack: {ap_male_attacks}
AP females persons covid attack: {ap_female_attacks}
Total ap covid attack: {total_ap_attack}''')
        print("")

    def ka_covid(self, ka_male_attacks, ka_female_attacks):
        total_ka_attack = 0
        total_ka_attack = total_ka_attack + ka_male_attacks + ka_female_attacks
        Covid.total_india = total_ka_attack + Covid.total_india
        Covid.total_male_attacks = ka_male_attacks + Covid.total_male_attacks
        Covid.total_female_attacks = ka_female_attacks + Covid.total_female_attacks

        print(f'''AP males persons covid attack: {ka_male_attacks}
KA females persons covid attack: {ka_female_attacks}
Total KA covid attack: {total_ka_attack}''')
        print("")

    def tn_covid(self, tn_male_attacks, tn_female_attacks):
        total_tn_attack = 0
        total_tn_attack = total_tn_attack + tn_male_attacks + tn_female_attacks
        Covid.total_india = total_tn_attack + Covid.total_india
        Covid.total_male_attacks = tn_male_attacks + Covid.total_male_attacks
        Covid.total_female_attacks = tn_female_attacks + Covid.total_female_attacks

        print(f'''TN males persons covid attack: {tn_male_attacks}
TN females persons covid attack: {tn_female_attacks}
Total TN covid attack: {total_tn_attack}''')
        print("")


c = Covid(10, 20)
c.ap_covid(50, 50)
c.ka_covid(150, 100)
c.tn_covid(500, 300)

print("total in india female covid attacks:", c.total_female_attacks)
print("total in india male covid attacks", c.total_male_attacks)
print("over all india covid attacks", c.total_india)
