import pypyodbc
import random as rand


### TODO: Break generating bits into discrete static functions

class Character():

    def __init__(self): 
        connection  = pypyodbc.connect("Driver={SQL Server};Server=localhost;Database=MazeRats;Trusted_Connection=Yes;")
        self.cursor = connection.cursor()

        self.gender = rand.randint(0,1)
        self.firstname = ""
        self.surname = ""

        if self.gender == 0:
            self.cursor.execute("SELECT Name from FemaleNames WHERE NameID =" + str(rand.randint(1,36)))
        else:
            self.cursor.execute("SELECT Name from MaleNames WHERE NameID =" + str(rand.randint(1,36)))
        self.firstname = self.cursor.fetchone()[0]

        coin = rand.randint(0,1)
        if coin == 0:
            self.cursor.execute("SELECT Name FROM UpperSurnames WHERE NameID =" + str(rand.randint(1,36)))
        else: 
            self.cursor.execute("SELECT Name FROM LowerSurnames WHERE NameID =" + str(rand.randint(1,36)))
        self.surname = self.cursor.fetchone()[0]

        self.abilities = {
            1 : ("+2", "+1", "+0"), 
            2 : ("+2", "+0", "+1"),
            3 : ("+1", "+2", "+0"),
            4 : ("+0", "+2", "+1"),
            5 : ("+1", "+0", "+2"),
            6 : ("+0", "+1", "+2")
            }[rand.randint(1,6)]

        self.startfeature = {
            1 : "+1 attack bonus",
            2 : "One spell slot",
            3 : "Path - "
        }[rand.randint(1,3)]

        if self.startfeature == "Path - ":
            self.startfeature = {
                1 : "Briarborn - Tracking, foraging, survival.",
                2 : "Fingersmith - Tinkering, picking locks or pockets",
                3 : "Roofrunner - Climbing, leaping, balancing.",
                4 : "Shadowjack - Moving silently, hiding in shadows."
            }[rand.randint(1,4)]

        if self.startfeature == "One spell slot":
            self.spell = self.randomSpell()
            self.startfeature += " - " + self.spell

        self.items = []
        for i in range(0, 6):
            while True:
                choice = rand.randint(1,36)
                query = "SELECT GearName FROM StartingGear WHERE GearID =" + str(choice)
                self.cursor.execute(query)
                result = self.cursor.fetchone()[0]
                if result not in self.items:
                    self.items.append(result)
                    break

        self.weapons = []
        for i in range(0, 2):
            while True:
                choice = rand.randint(1, 18)
                query = "SELECT WeaponName, WeaponType FROM Weapons WHERE WeaponID =" + str(choice)
                self.cursor.execute(query)
                res = self.cursor.fetchone()
                weap = res[0]
                wtype = res[1]
                if weap not in self.weapons:
                    self.weapons.append(str(weap + " (" + wtype + ")"))
                    break

        self.cursor.execute("SELECT AppearanceName FROM Appearance WHERE AppearanceID =" + str(rand.randint(1,36)))
        self.appearance = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT DetailName FROM PhysicalDetail WHERE DetailID =" + str(rand.randint(1,36)))
        self.physdetail = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT BackgroundName FROM Background WHERE BackgroundID =" + str(rand.randint(1,36)))
        self.bg = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT ClothingName FROM Clothing WHERE ClothingID =" + str(rand.randint(1,36)))
        self.clothing = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT PersonalityName FROM Personality WHERE PersonalityID =" + str(rand.randint(1,36)))
        self.person = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT MannerismName FROM Mannerism WHERE MannerismID =" + str(rand.randint(1,36)))
        self.manner = self.cursor.fetchone()[0]

    def returnChar(self):
        self.thechar = self.firstname + " " + self.surname \
        + "\nAbilities: Strength " + self.abilities[0] + ", Dexterity " + self.abilities[1] \
            + ", Will " + self.abilities[2] \
        + "\nStarting feature: " + self.startfeature \
        + "\nItems: " + ", ".join(self.items) \
        + "\nWeapons: " + ", ".join(self.weapons) \
        + "\nAppearance: " + self.appearance \
        + "\nPhysical detail: " + self.physdetail \
        + "\nBackground: " + self.bg \
        + "\nClothing: " + self.clothing \
        + "\nPersonality: " + self.person \
        + "\nMannerism: " + self.manner
        return self.thechar



    def randomSpell(self):
        spelltype = rand.randint(1,12)

        if spelltype == 1:
            self.cursor.execute("SELECT SName FROM SpellPhysicalEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellPhysicalForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 2:
            self.cursor.execute("SELECT SName FROM SpellPhysicalEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellEtherealForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 3:
            self.cursor.execute("SELECT SName FROM SpellEtherealEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellPhysicalForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 4:
            self.cursor.execute("SELECT SName FROM SpellEtherealEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellEtherealForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 5:
            self.cursor.execute("SELECT SName FROM SpellPhysicalElements WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellPhysicalForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 6:
            self.cursor.execute("SELECT SName FROM SpellPhysicalElements WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellEtherealForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 7:
            self.cursor.execute("SELECT SName FROM SpellEtherealElements WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellPhysicalForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 8:
            self.cursor.execute("SELECT SName FROM SpellEtherealElements WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellEtherealForms WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 9:
            self.cursor.execute("SELECT SName FROM SpellPhysicalEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellPhysicalElements WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 10:
            self.cursor.execute("SELECT SName FROM SpellPhysicalEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellEtherealElements WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 11:
            self.cursor.execute("SELECT SName FROM SpellEtherealEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellPhysicalElements WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]
        elif spelltype == 12:
            self.cursor.execute("SELECT SName FROM SpellEtherealEffects WHERE SID =" + str(rand.randint(1,36)))
            spell = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SName FROM SpellEtherealElements WHERE SID =" + str(rand.randint(1,36)))
            spell += " " + self.cursor.fetchone()[0]

        return spell