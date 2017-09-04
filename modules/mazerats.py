import pypyodbc
import random as rand

class Character():

    def __init__(self): 
        connection  = pypyodbc.connect("Driver={SQL Server};Server=localhost;Database=MazeRats;Trusted_Connection=Yes;")
        cursor = connection.cursor()

        self.gender = rand.randint(0,1)

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
            self.path = {
                1 : "Briarborn: Tracking, foraging, survival.",
                2 : "Fingersmith: Tinkering, picking locks or pockets",
                3 : "Roofrunner: Climbing, leaping, balancing.",
                4 : "Shadowjack: Moving silently, hiding in shadows."
            }[rand.randint(1,4)]
            self.startfeature += self.path

        self.items = []
        for i in range(0, 6):
            while True:
                choice = rand.randint(1,36)
                query = "SELECT GearName FROM StartingGear WHERE GearID =" + str(choice)
                cursor.execute(query)
                result = cursor.fetchone()[0]
                if result not in self.items:
                    self.items.append(result)
                    break

        cursor.execute("SELECT AppearanceName FROM Appearance WHERE AppearanceID =" + str(rand.randint(1,36)))
        self.appearance = cursor.fetchone()[0]

        cursor.execute("SELECT DetailName FROM PhysicalDetail WHERE DetailID =" + str(rand.randint(1,36)))
        self.physdetail = cursor.fetchone()[0]

        cursor.execute("SELECT BackgroundName FROM Background WHERE BackgroundID =" + str(rand.randint(1,36)))
        self.bg = cursor.fetchone()[0]

        cursor.execute("SELECT ClothingName FROM Clothing WHERE ClothingID =" + str(rand.randint(1,36)))
        self.clothing = cursor.fetchone()[0]

        cursor.execute("SELECT PersonalityName FROM Personality WHERE PersonalityID =" + str(rand.randint(1,36)))
        self.person = cursor.fetchone()[0]

        cursor.execute("SELECT MannerismName FROM Mannerism WHERE MannerismID =" + str(rand.randint(1,36)))
        self.manner = cursor.fetchone()[0]

    def returnChar(self):
        self.thechar = "Abilities: Strength = " + self.abilities[0] + ", Dexterity = " + self.abilities[1] \
            + ", Will = " + self.abilities[2] \
        + "\nStarting feature: " + self.startfeature \
        + "\nItems: " + ", ".join(self.items) \
        + "\nAppearance: " + self.appearance \
        + "\nPhysical detail: " + self.physdetail \
        + "\nBackground: " + self.bg \
        + "\nClothing: " + self.clothing \
        + "\nPersonality: " + self.person \
        + "\nMannerism: " + self.manner
        return self.thechar