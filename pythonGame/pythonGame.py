## Herein lies the basic Hunter class. My goal is for this class to handle most everything. 
class Hunter:
    def __init__(self, name, ratings, description, attack = 2, armor = 0, harm = 0): # Harm counts up to 7; more harm is worse.
        self.name = name
        self.ratings = {
            'Charm':0,
            'Cool':0,
            'Sharp':0,
            'Tough':0,
            'Weird':0
        }
        self.attack = attack
        self.armor = armor
        self.harm = harm

# Now for methods. During the Mysteries, I'm going to need one to take damage.
    def takeDamage(self,damage):
        self.harm = self.harm + damage 
        if self.harm >= 7:
            print("Your Hunter has died. Better luck next time.")
            # implement some way to end the loop. 
# At the end of a Mystery, I'm going to need one to reset Harm. 
    def resetHarm(self):
        self.harm = 0

# I also want to give rewards. You can choose one rating to increase at the end of each mystery. I'll make the max for a rating 4, even though it's three in-game. 
    def ratingIncrease(self):
        print("Here are your current Ratings: \n",self.ratings)
        ratingChoice = input("Enter the name of the Rating you'd like to increase.")

        if ratingChoice.lower() == 'charm': 
            self.ratings['Charm'] += 1
        elif ratingChoice.lower() == 'cool':
            self.ratings['Cool'] += 1
        elif ratingChoice.lower() == 'sharp':
            self.ratings['Sharp'] += 1
        elif ratingChoice.lower() == 'tough':
            self.ratings['Tough'] += 1
        elif ratingChoice.lower() == 'weird':
            self.ratings['Weird'] += 1
        else: 
            print("Sorry, that's not a valid rating. Enter the name of the rating you'd like to increse, not any number. Case insensitive.")
            self.ratingIncrease() # re-runs the function if there's an error. 
    

# Investigating during a mystery should also have a reward. One will upgrade armor, another will upgrade your attack.
# Later, I can do a reward that halves the monster's health. 
    def armorUpgrade(self):
        self.armor += 1
    def attackUpgrade(self):
        self.attack += 1

# Now we'll have a simple endMystery function for when the mystery ends. Still need to implement deleting the completed Mystery from the mystery list. 
# Maybe put this in the mysteries section??? 

    def endMystery(self):
        print("""
        Good work. You've survived another week.
        You can take some time to rest. Your Harm has been reset to 0.
        You've also leveled up! You can increase one of your Ratings by 1.
        The maximum value for each Rating is 4. 
        """)
        self.resetHarm()
        self.ratingIncrease()


# subclasses for 5 select Playbooks. The only thing that's different is the rating array. 
# I'll increase armor/attacks as rewards for investigating during the game. Harm will be healed at the end of each Mystery. 
class Flake(Hunter):
    def __init__(self, name, ratings, description, attack=2, armor=0, harm=0):
        super().__init__(name, ratings, description, attack, armor, harm)
        self.ratings = {
            'Charm':1,
            'Cool':1,
            'Sharp':2,
            'Tough':-1,
            'Weird':0
        }
        self.description = "The Flake: A conspiracy theorist following real conspiracies. The sharpest of the bunch." 

class Monstrous(Hunter):
    def __init__(self, name, ratings, description, attack=2, armor=0, harm=0):
        super().__init__(name, ratings, description, attack, armor, harm)
        self.ratings = {
            'Charm':-1,
            'Cool':-1,
            'Sharp':0,
            'Tough':3,
            'Weird':1
        }
        self.description = 'The Monstrous: A monster fighting for the good guys. The toughest of the bunch.'

class Mundane(Hunter):
    def __init__(self, name, ratings, description, attack=2, armor=0, harm=0):
        super().__init__(name, ratings, description, attack, armor, harm)
        self.ratings = {
            'Charm':2,
            'Cool':1,
            'Sharp':0,
            'Tough':1,
            'Weird':-1
        }
        self.description = 'The Mundane: Just a normal regular person. The most charming of the bunch.'

class Professional(Hunter):
    def __init__(self, name, ratings, description, attack=2, armor=0, harm=0):
        super().__init__(name, ratings, description, attack, armor, harm)
        self.ratings = {
            'Charm':0,
            'Cool':2,
            'Sharp':-1,
            'Tough':2,
            'Weird':-1
        }
        self.description = "The Professional: A 9-5, agency-employed monster hunter. The coolest of the bunch."

class Spooky(Hunter):
    def __init__(self, name, ratings, description, attack=2, armor=0, harm=0):
        super().__init__(name, ratings, description, attack, armor, harm)
        self.ratings = {
            'Charm':0,
            'Cool':0,
            'Sharp':1,
            'Tough':-1,
            'Weird':3
        }
        self.description = "The Spooky: A purveyor of strange powers which aren't entirely under their control. The weirdest of the bunch."

def playMotW():
    print("""
    Welcome, hunter. Each week, you'll embark on a new mystery.
    If you've never played MotW before, don't worry. You'll catch on quick. 
    You play a Hunter with Ratings that describe them and that you use for Moves. 
    Play your cards right, and you might just bag the monster without dying. 
    About that... try not to take a total of 7 Harm. If you do, you die. 

    Lots of forks in the road lie ahead of you. 
    When you come to one, enter the number assocated with your choice when prompted.
    Moves will have their associated rating next to them in parentheses.  
    It's a strange world out there. I hope you're ready.
                        Good hunting.
    """)

# This is the character creation section. It covers the following two instructions: 
# "As a user, I should be able to choose a Hero and give it a name" and "As a user, I should be able to choose a Hero and see my ratings (health,attack, etc)"
    readyToHunt = False
    while readyToHunt != True: # Keeps looping until the player is ready. 
        playerName = input("Enter your Hunter's name: \n")
        playbook = input("""
        What kind of Hunter would you like to be?
        1. The Flake: A conspiracy theorist following real conspiracies. The sharpest of the bunch.
        2. The Monstrous: A monster fighting for the good guys. The toughest of the bunch.
        3. The Mundane: Just a normal regular person. The most charming of the bunch.
        4. The Professional: A 9-5, agency-employed monster hunter. The coolest of the bunch.
        5. The Spooky: A purveyor of strange powers which aren't entirely under their control. The weirdest of the bunch.
        """)
        if playbook == '1':
            playerHunter = Flake(playerName)
        if playbook == '2':
            playerHunter = Monstrous(playerName)
        if playbook == '3':
            playerHunter = Mundane(playerName)
        if playbook == '4':
            playerHunter = Professional(playerName)
        if playbook == '5':
            playerHunter = Spooky(playerName)
        
        try: # doing a try statment so that I can write an error code
            print(f"""You've chosen {playerHunter.name}, who plays the role of {playerHunter.description}.
                Your ratings are {playerHunter.ratings}. 
                You'll start with offensive capabilities that do {playerHunter.attack} Harm, whether by magic or weapon.
                You'll start with armor which reduces all Harm you take by {playerHunter.armor}. Don't worry, we'll get you a flak vest later.""")
            if input("If you're ready to hunt, press (y). Hit any other key to respec your Hunter.") == 'y':
                readyToHunt = True
        except:
            print("Choice not found. Try entering your Hunter's information again.")

# OK, now we can finally actually play! This is the Mysteries section. 
    hunting = True
    while hunting == True: # we gotta stop it somehow
        mysteriesList = ["Enter the number associated with the Mystery you'd like to investigate."]

# As a user, I should be able to immediately fight a villain
# As a user, I should be able to choose an action from a menu that is printed
# As a user, I should be able to view this menu by calling a function
# As a user, I should be able to have the game quit if I reach 0 health or the enemy reaches 0 health

    

# Extra Challenge
# As a user, I should be able to run away and avoid the monster
# As a user, I should be able to find coins or earn coins either fighting the monster or running away
# As a user, I should be able to purchase an item from a store using coins
# As a user, I should be able to change my stats when I purchase an item
# As a user, I should be able to view my items that I currently have

    basicMovesList = ["Which move would you like to use? \n 1. Kick Some Ass! (Tough) \n 2. Run away with Act Under Pressure (Cool) \n"] 

playMotW()