# Glenn Grant-Richards
# 10.1 - Create your own class
# For this assignment, I chose to describe the "sigma".  This is a personality type of a person.  In the following code, the user gets to choose the name and wealth of their sigma, but other attributes are randomly selected.  Then, they fight their enemy in a lethal battle of rock, paper, scissors.
import random
# Need random for random.randint(), which is used for the "fight" method
class Sigma():
    # Call constuctor
    def __init__ ( self, strength, weakness ):
        # All sigmas value the same things, money and power
        global value
        value = "money and power"
        self.strength = strength
        self.weakness = weakness
    def set_name ( self, name ):
        # Set the sigma's name
        self.name = name
    def get_name ( self ):
        # Print out the sigma's name that was just set
        print(f"Your name is {self.name}")
        return self.name
    def set_wealth( self, wealth ):
        # Set the sigma's wealth
        self.wealth = wealth
    def get_wealth( self ):
        # Print out the sigma's wealth that was just set
        print(f"Your wealth is ${self.wealth}")
        return self.wealth
    # This method randomly selects a hobby for the sigma from nine prewritten hobbies
    def gain_hobby ( self ):
        whichHobby = random.randint( 0, 8 )
        if whichHobby == 0:
            hobby = "drinking tap water"
        elif whichHobby == 1:
            hobby = "smelling people"
        elif whichHobby == 2:
            hobby = "writing in a diary, then eating the diary so no one else can read it"
        elif whichHobby == 3:
            hobby = "brushing your teeth"
        elif whichHobby == 4:
            hobby = "searching for Pokémon in real life"
        elif whichHobby == 5:
            hobby = "stealing ducks from local parks"
        elif whichHobby == 6:
            hobby = "drinking milk through a curly straw"
        elif whichHobby == 7:
            hobby = "peeling an orange, then eating only the peel"
        else:
            hobby = "eating books in libraries with no-food policies"
        # Print out the hobby
        print(f"Your hobby is {hobby}")
        return None
    # This method randomly selects a fear for the sigma from seven prewritten fears
    def gain_fear ( self ):
        whichFear = random.randint( 0, 6 )
        if whichFear == 0:
            fear = "nightlights"
        elif whichFear == 1:
            fear = "lobsters"
        elif whichFear == 2:
            fear = "not getting enough money"
        elif whichFear == 3:
            fear = "cereal"
        elif whichFear == 4:
            fear = "Mount Everest"
        elif whichFear == 5:
            fear = "red velvet"
        else:
            fear = "inexpensive clothing"
        # Print out the fear
        print(f"Your fear is {fear}")
        return None
    # This method randomly selects a hustle for the sigma from seven prewritten hustles
    def gain_hustle ( self ):
        whichHustle = random.randint( 0, 6 )
        if whichHustle == 0:
            global hustle
            hustle = "negotiating good"
        elif whichHustle == 1:
            hustle = "fractional milkman"
        elif whichHustle == 2:
            hustle = "NFL runningback"
        elif whichHustle == 3:
            hustle = "3D printing 3D printers, then coming to terms with the fact they broke the Second Law of Thermodynamics"
        elif whichHustle == 4:
            hustle = "selling exotic koi fish"
        elif whichHustle == 5:
            hustle = "filling suitcases with Olive Garden breadsticks, then selling them on Ebay"
        else:
            hustle = "screenshotting then reselling NFT's"
        # Print out the hustle
        print(f"Your hustle is {hustle}")
        return None
    def gain_enemy( self ):
    # This method randomly selects a formidable foe for the sigma to attempt to vanquish from five prewritten and dangerous enemies
        whichEnemy = random.randint( 0, 4 )
        if whichEnemy == 0:
            global enemy
            enemy = "laundry detergent"
        elif whichEnemy == 1:
            enemy = "tricicles"
        elif whichEnemy == 2:
            enemy = "Gilbert"
        elif whichEnemy == 3:
            enemy = "green vegetables"
        else:
            enemy = "pajamas"
        # Print out the enemy the sigma will face in mortal combat
        print(f"Your enemy is {enemy}")
        return None
    def fight ( self ):
        while True:
            attack = input( f"Fight your enemy, {enemy}, in a game of rock, paper, scissors.  Choose only 'rock', 'paper', or 'scissors'. ")
            enemyAttack = random.randint( 0, 2 )
            if enemyAttack == 0:
                # Enemy plays 'rock'
                enemyWin = "scissors"
                # Enemy wins if you play scissors, since rock beats scissors
                enemyTie = "rock"
                # Enemy ties if you play 'rock', since both played rock
                enemyLoss = "paper"
                # Enemy loses if you play 'paper', since paper beats rock
            elif enemyAttack == 1:
                # Enemy plays 'paper'
                enemyWin = "rock"
                # Enemy wins if you play rock, since paper beats rock
                enemyTie = "paper"
                # Enemy ties if you play 'paper', since both played paper
                enemyLoss = "scissors"
                # Enemy loses if you play 'scissors', since scissors beats paper
            elif enemyAttack == 2:
                # Enemy plays 'scissors'
                enemyWin = "paper"
                # Enemy wins if you play paper, since scissors beats paper
                enemyTie = "scissors"
                # Enemy ties if you play 'scissors', since both played scissors
                enemyLoss = "rock"
                # Enemy loses if you play 'rock', since rock beats scissors
            # If the sigma loses, they lose some money and are unfortunately slain
            if attack == enemyWin:
                self.wealth -= 100
                print(f"Your enemy, {enemy}, has defeated you, {self.name}, and you do not obtain your values, {value}!  In the encounter, you lose some wealth.  Your net worth is now only ${self.wealth}.  Also, since you have been defeated in mortal combat....")
                return None
            # If the sigma wins, they gain some money and return victorious
            elif attack == enemyLoss:
                self.wealth *= 1.2
                print(f"You, {self.name}, have defeated your enemy, {enemy}, and obtained your values, {value}!  In the encounter, you gain some wealth.  Your net worth is now ${self.wealth}.  Your strength, {self.strength}, has proved more important that your weakness, {self.weakness}.")
                return None
            # If the sigma and their enemy tie, the fight continues
            elif attack == enemyTie:
                print(f"You, {self.name}, have tied your enemy, {enemy}.  Try again.")
            else: print("You did not input a correct attack.  Choose either 'rock', 'paper', or 'scissors'.")
def main():
    # Create the sigma
    mySigma = Sigma( "mindset", "peanut allergy" )
    mySigma.set_name( "Humphrey" )
    mySigma.get_name()
    mySigma.set_wealth( 100 )
    mySigma.get_wealth()
    mySigma.gain_hobby()
    mySigma.gain_fear()
    mySigma.gain_hustle()
    mySigma.gain_enemy()
    mySigma.fight()
if __name__ == "__main__":
    # Call the main function
    main()