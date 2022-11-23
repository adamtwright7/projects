## Double hash comments are by me, adamTwright. Single hashes are instructions.

firstWelcomeMessage = "Welcome, hunter. Each week, you'll embark on a new mystery. \n" \
"Lots of forks in the road lie ahead of you. When you come to one, enter the number assocated with your choice when prompted. \n" \
"Moves will have their associated stat next to them, in parentheses. \n" \
"It's a cold, hard world out there. I hope you're ready. \nGood hunting. \n"

print(firstWelcomeMessage)

class Hunter:
    def __init__(self, name, harm = 7):
        self.name = name
        self.harm = harm


def main():
# As a user, I should be able to choose a Hero and give it a name
## I'm also going to do Playbooks. 



# As a user, I should be able to choose a Hero and see my stats (health,attack, etc)
# As a user, I should be able to immediately fight a villain
# As a user, I should be able to choose an action from a menu that is printed
# As a user, I should be able to view this menu by calling a function
# As a user, I should be able to have the game quit if I reach 0 health or the enemy reaches 0 health

    mysteriesList = ["Enter the number associated with the Mystery you'd like to investigate."]

# Extra Challenge
# As a user, I should be able to run away and avoid the monster
# As a user, I should be able to find coins or earn coins either fighting the monster or running away
# As a user, I should be able to purchase an item from a store using coins
# As a user, I should be able to change my stats when I purchase an item
# As a user, I should be able to view my items that I currently have

    basicMovesList = ["Which move would you like to use? \n 1. Kick Some Ass! (Tough) \n 2. Run away with Act Under Pressure (Cool) \n"] 

main()