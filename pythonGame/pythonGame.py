## Herein lies the basic Hunter class. My goal is for this class to handle most everything. 
class Hunter:
    def __init__(self, name, ratings = {}, description = '', attack = 2, armor = 0, harm = 0): # Harm counts up to 7; more harm is worse.
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
        trueDamage = damage - self.armor
        if trueDamage > 0:
            self.harm = self.harm + trueDamage 
        if self.harm >= 7:
            print(f"""Your Hunter, {self.name} has been knocked out. You'll bleed out soon,
but if the monster's dead, you'll be healed up and sent back to base.
""")
        else:
            print(f"That's gonna leave a mark, but you'll be fine. You're at {self.harm} Harm.")

# At the end of a Mystery, I'm going to need one to reset Harm. 
    def resetHarm(self):
        self.harm = 0

# I also want to give rewards. You can choose one rating to increase at the end of each mystery. 
# I'll make the max for a rating 4, even though it's three in-game. 
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

    # gear check. Will print all the important stuff. 
    def gearCheck(self):
        print(f"""
Alright {self.name}, your Ratings looks like this: {self.ratings}
and you're at {self.harm} Harm. You die at 7. 
You have the capacity to deal {self.attack} Harm, 
and your armor subtracts {self.armor} Harm from any hit you take. 
Remember, you're playing {self.description} 
""")

# subclasses for 5 select Playbooks. The only thing that's different is the rating array. 
# I'll increase armor/attacks as rewards for investigating during the game. Harm will be healed at the end of each Mystery. 
class Flake(Hunter):
    def __init__(self, name, ratings = 0 , description = 0, attack=2, armor=0, harm=0):
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
    def __init__(self, name, ratings = 0 , description = 0 , attack=2, armor=0, harm=0):
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
    def __init__(self, name, ratings = 0, description = 0, attack=2, armor=0, harm=0):
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
    def __init__(self, name, ratings = 0, description = 0, attack=2, armor=0, harm=0):
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
    def __init__(self, name, ratings = 0, description = 0, attack=2, armor=0, harm=0):
        super().__init__(name, ratings, description, attack, armor, harm)
        self.ratings = {
            'Charm':0,
            'Cool':0,
            'Sharp':1,
            'Tough':-1,
            'Weird':3
        }
        self.description = "The Spooky: A purveyor of strange powers which aren't entirely under their control. The weirdest of the bunch."

# This is the Mysteries section. We'll have an overall Mystery class and then subclasses with more detailed stuff. 

import random # have to use this to get random rolls 

class Mystery:
    def __init__(self,PC,enteringTown,investigationPrompt,goodInv,badInv,lesserHarm,confrontationPrompt,monsterHarm,monsterHealth,victory):
        self.PC = PC # this will be the object that represents the player character. 
        self.enteringTown = enteringTown
        self.investigationPrompt = investigationPrompt
        self.goodInv = goodInv
        self.badInv = badInv
        self.lesserHarm = lesserHarm
        self.confrontationPrompt = confrontationPrompt
        self.monsterHarm = monsterHarm
        self.monsterHealth = monsterHealth
        self.victory = victory

    def startingMessage(self): # this kicks off the Mystery and handles any investigation
        print(self.enteringTown)
        startingChoice = input("""
What would you like to do? 
        1. Investigate further by rolling Sharp. 
        2. Ask around by rolling Charm. 
        3. Charge right into danger. 
        9. Check your gear. 
""")

        if startingChoice == "1":
            print(self.investigationPrompt)
            firstDie = random.randint(1,6)
            secondDie = random.randint(1,6)
            sharpResult = firstDie + secondDie + self.PC.ratings["Sharp"] 

            print(f"""
            You rolled {firstDie} + {secondDie} + your Sharp rating, {self.PC.ratings["Sharp"]}.
            That's a total of {sharpResult}. 
            """)
            if sharpResult < 7:
                print("Your investigation has been a failure.")
                print(self.badInv)
                self.PC.takeDamage(self.lesserHarm)
            else:
                print("Your investigation has been a success.")
                print(self.goodInv)
                self.monsterHealth = int(self.monsterHealth/2)
            self.bigBattle()

        if startingChoice == "2":
            print(self.investigationPrompt)
            firstDie = random.randint(1,6)
            secondDie = random.randint(1,6)
            charmResult = firstDie + secondDie + self.PC.ratings["Charm"] 

            print(f"""
            You rolled {firstDie} + {secondDie} + your Charm rating, {self.PC.ratings["Charm"]}.
            That's a total of {charmResult}. 
            """)
            if charmResult < 7:
                print("Your investigation has been a failure.")
                print(self.badInv)
                self.PC.harm -= self.lesserHarm
            else:
                print("Your investigation has been a success.")
                print(self.goodInv)
                self.monsterHealth = int(self.monsterHealth/2) # rounds down. I'm fine with that. 
            self.bigBattle()
        
        if startingChoice == '3':
            self.bigBattle()
        if startingChoice == '9':
            self.PC.gearCheck()
    
    def bigBattle(self): # This handles the big battle between the player's Hunter and the titular Monster of the Week
        print(self.confrontationPrompt)
        battleMenu = """The battle continues! What's next?
            1. Pull out your weapon and Kick Some Ass by rolling Tough.
            2. Focus your energy into harming the monster by rolling Weird. 
            3. Get out of here by rolling Cool. 
            9. Quickly check your gear. \n"""
        runningAway = False 
        while (self.PC.harm < 7) and (self.monsterHealth > 0) and (runningAway == False):
            battleChoice = input(battleMenu)
            firstDie = random.randint(1,6)
            secondDie = random.randint(1,6)
            if battleChoice == '3':
                fleeResult = firstDie + secondDie + self.PC.ratings["Cool"] 
                print(f"""You rolled {firstDie} + {secondDie} + your Cool rating, {self.PC.ratings["Cool"]}.
That's a total of {fleeResult}.""")
                if fleeResult >= 7:
                    print("""You've survived another day, but left others to deal with the monster. 
Get back to base and take some time to rest. Your Harm has been reset to 0.
""")
                    self.PC.resetHarm() 
                    runningAway = True 
                else:
                    print(f"The monster drags you back! You take {self.monsterHarm - 1} Harm.")
                    self.PC.takeDamage(self.monsterHarm - 1) 
            elif battleChoice == '9': # This needs to be an else-if. Otherwise, I go into the battle area when 9 is selected.
                self.PC.gearCheck()
            else: # this is all the battle stuff. 1 and 2 both share the same results. 
                if battleChoice == '1':
                    battleResult = firstDie + secondDie + self.PC.ratings["Tough"] 
                    print(f"""You rolled {firstDie} + {secondDie} + your Tough rating, {self.PC.ratings["Tough"]}. 
That's a total of {battleResult}.""")
                if battleChoice == '2':
                    battleResult = firstDie + secondDie + self.PC.ratings["Weird"] 
                    print(f"""You rolled {firstDie} + {secondDie} + your Weird rating, {self.PC.ratings["Weird"]}. 
That's a total of {battleResult}.""")
                if battleResult < 7:
                    print(f"Failure. The monster catches you off guard. You take {self.monsterHarm} Harm.")
                    self.PC.takeDamage(self.monsterHarm)
                elif battleResult < 10:
                    print(f"Mixed success. You and the monster clash. You deal {self.PC.attack} Harm, but take {self.monsterHarm} Harm.")
                    self.monsterHealth -= self.PC.attack 
                    self.PC.takeDamage(self.monsterHarm)
                elif battleResult < 12:
                    print(f"""Good success. You take the advantage. You deal one extra Harm to the monster 
for a total of {self.PC.attack + 1}, but still suffer the monster's normal {self.monsterHarm} Harm.""")
                    self.monsterHealth -= (self.PC.attack + 1) 
                    self.PC.takeDamage(self.monsterHarm)
                else:
                    print(f"Advanced success. You deal {self.PC.attack} to the monster and suffer no Harm at all!")
                    self.monsterHealth -= self.PC.attack 
        
        # victory stuff 
        if self.monsterHealth < 1: 
            print(f"{self.victory}")
            lootChoice = input("What would you like to take?")
            if lootChoice == '1': # 1 will always be armor, 2 will be attack 
                self.PC.armorUpgrade()
                print(f"You now have {self.PC.armor} armor. All Harm taken will be reduced by {self.PC.armor}.")
            if lootChoice == '2':
                self.PC.attackUpgrade() 
                print(f"You can now deal {self.PC.attack} Harm.")
            
            print("""
Good work. You've survived another week.
Get back to base and take some time to rest. Your Harm has been reset to 0.
You've also leveled up! You can increase one of your Ratings by 1.""")
            self.PC.resetHarm()
            self.PC.ratingIncrease()

# the else-if statement here means that if you tie -- kill the monster but also die -- it counts as a win.         
        elif self.PC.harm >= 7: 
            print(f"Sorry, {self.PC.name}. Other Hunters may arise in your stead...")

# Mystery subclasses! These contain the flavortext and monster stats for different Mysteries. 

class DreamAwayTheTime(Mystery):
    def __init__(self, PC, enteringTown = '', investigationPrompt = '', goodInv = '', badInv = '', lesserHarm = 0, confrontationPrompt = '', monsterHarm = 0, monsterHealth = 0, victory = ''):
        super().__init__(PC, enteringTown, investigationPrompt, goodInv, badInv, lesserHarm, confrontationPrompt, monsterHarm, monsterHealth, victory)
        
        self.enteringTown = """
A long road leads into the small town of Handfast. After a short talk with the sheriff, 
you've reviewed security footage and found that whatever is responsible for the nighttime attacks 
only shows up as a dark blob on the tapes. Even more worrying, his records indicate a child goes 
missing from the town every 40 years, to the date. This cycles's date was three days ago, 
when the attacks began, but no child has yet gone missing."""
        
        self.investigationPrompt = """
At the town playground, you spy a girl watching from afar. She idles at the treeline, watching the other kids play.
The sunset glints off a short dagger as her hands twirl it. A cloak over her dress is interwoven with violets."""
        
        self.goodInv = """
You have a pleasant chat with the girl, Violet. She tells you that she has enjoyed the last 40 years with Oberon,
the king of faeries, in his timeless realm. He's brought a brutish creature, a Redcap named Bonecruncher,
to steal away the town's favorite child per a centuries-old fey pact. 
She tells you where Bonecruncher will next attack.

You make preparations for the redcap's rage. His Harm capacity has been halved for the final showdown. Get ready."""

        self.badInv = """
You try to look into the dagger-clutching girl. She ducks into the woods as you follow. 
A dagger slashes across your side. You take 1 Harm. You awake hours later,
your memory still foggy, and stumble into town under a dark sky."""

        self.lesserHarm = 1 
        self.confrontationPrompt = """
A massive fey creature beneath a woolen cap dripping with blood charges into the town street!"""

        self.monsterHarm = 2
        self.monsterHealth = 9
        self.victory = """
Bonecruncher is defeated! You renegotiate the terms of Oberon's old bargain with the town. 
Violet returns to the fey realm, which is now more her home than Handfast. She leaves you with a gift.

1. Take Violet's fairy cloak (gain +1 armor). 
2. Take the enchantment of Violet's dagger (deal +1 Harm)."""

class DamnDirtyApes(Mystery):
    def __init__(self, PC, enteringTown = '', investigationPrompt = '', goodInv = '', badInv = '', lesserHarm = 0, confrontationPrompt = '', monsterHarm = 0, monsterHealth = 0, victory = ''):
        super().__init__(PC, enteringTown, investigationPrompt, goodInv, badInv, lesserHarm, confrontationPrompt, monsterHarm, monsterHealth, victory)
        
        self.enteringTown = """
Welcome to Pittsburg State University, home of the gorillas! Around campus are strung graduation banners 
-- and webs of police tape. Tall, concrete collumns release steam into the air."""
        
        self.investigationPrompt = """
Claire Guimaras, the local police chief, commands detectives and crime scene cleaners. 
She explains that long primate hairs have been found at the scene of the murder and all of the lab break-ins. 
In all cases, the perpetrator also broke grates that cover the air vents that connect to the expansive network
of steam tunnels beneath campus. Chief Guimaras has one main suspect: Robin Harding, 
the head of the student group that calls themselves the Animal Freedom Militia."""
        
        self.goodInv = """
You find that Robin is happy about the released primates, but not responsible. 
She clues you in on her main suspect: Dr. Lawrence Beech, an infamous professor on campus
whose experiments with primates had to be stopped by his peers. Though he somehow has tenure,
he hasn't been seen in a couple days, and reportedly didn't give his finals this year.
Local legend is that he has a secret lab in the steam tunnels under campus. 

You head into the steam tunnels, ready and equipped. The professor's harm capacity has been halved."""

        self.badInv = """
As you creep about one of the trashed labs, echoing monkey calls approach through the vents.
Robo-monkeys hop into the lab! Shoulder-mounted rail guns launch refuse at you.
Grappling hooks launch from where chimp arms should be, and you're dragged into the steam tunnels. You take 2 Harm."""

        self.lesserHarm = 2 
        self.confrontationPrompt = """
Through the dark steam below campus is a cluttered lab stacked high with prosthetic limbs, primate parts,
and strange chrome weaponry. A wild-eyed, balding professor raises up a laser gun and aims it at you!
Then rants about his evil plans to take over campus for a while. Then the laser begins to charge!"""

        self.monsterHarm = 4
        self.monsterHealth = 6
        self.victory = """
Dr. Beech screams with the rage of a nerd scorned! Now he'll never complete his research or be dean! 
But the primates are released for rehabilitation with the Animal Freedom Militia, 
and Beech is hidden away from the world by whatever shadowy organization you work for. 
After a few years out of the publish-or-perish mindset, 
he comes back to his senses (and morals) and is able to replicate some of his research for you. 

1. Take some chrome armor from Dr. Beech's lab (+1 harm) 
2. Take some weird etheric-bionic lazer thing (+1 attack)
"""

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
            print(f"""
You've chosen {playerHunter.name}, 
who plays the role of {playerHunter.description}
Your ratings are {playerHunter.ratings}. 
You'll start with offensive capabilities that do {playerHunter.attack} Harm, whether by magic or weapon.
You'll start with armor which reduces all Harm you take by {playerHunter.armor}. 
Don't worry, we'll get you a flak vest later.""")
            if input("If you're ready to hunt, enter 'y'. Enter any other key to respec your Hunter. \n") == 'y':
                readyToHunt = True
        except:
            print("Choice not found. Try entering your Hunter's information again.")

# OK, now we can finally actually play! 
    hunting = True
    completedMysteries = [] # this will track which mysteries are completed so they can't be replayed. 
    while (hunting == True) and (playerHunter.harm < 7): # we gotta stop it somehow
        mainMenu = """
Welcome back to base, Hunter! 
Enter the number associated with the Mystery you'd like to investigate.
Easiest Mysteries are listed first. You can investigate a Mystery twice, but it's less fun that way. 
Enter 9 to check your gear. 
If you'd like to retire your Hunter to safety, enter any other key or 0. 

1. Investigate strange weather events, household inconveniences, 
and worrisome nighttime attacks in the small town of Handfast. 

2. A college town has been suffering from a spate of burglaries of its labs. Complex medical devices and 
primates have both been stolen. Now a security guard was torn to pieces a few days ago. 

9. Check your gear. 

0. Retire to safety. (Quit the game.)
"""
        mainMenuChoice = input(mainMenu)
        if mainMenuChoice == '1':
            mystery = DreamAwayTheTime(playerHunter)
            mystery.startingMessage()
        elif mainMenuChoice == '2':
            mystery = DamnDirtyApes(playerHunter)
            mystery.startingMessage()
        elif mainMenuChoice == '9':
            playerHunter.gearCheck()
        else:
            print(f"""
Congratulations, {playerHunter.name}. You've retired to safety. 
And who knows? One day a young Hunter may need your expertise.""")
            hunting = False 

playMotW()

