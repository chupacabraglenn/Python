	GitHub link: https://github.com/chupacabraglenn/Python	

	The sigma class describes the real-world object of the sigma.  Sigmas are a type of people who strive towards excellence.  The word "sigma" derives from wolves, and originally referred to lone wolves who were still the alpha.
The same is used to describe people.  They are successfull, free-thinkers, and very independent.  Examples include Steve Jobs, John Wick, Han Solo, Eren Jaeger, and Leonardo da Vinci.  The purpose of this project was to allow users
to create their own sigma and explore their various hobbies, fears, and hustles, then hone them in a fight against their enemy.  Sigmas almost always possess the same values: money and power.  This is why I chose to create 'value' 
as the class variable.  All sigmas have a strength and a weakness, which I decided was best to leave up to the user.  

	Additionally, all sigmas need a name.  I thought it was best if users could choose their own name for their sigma
to add a personal touch.

	They get to set the name of their sigmas with the set_name() method and return it with the get_name() method.  The amount of wealth the sigma possesses is also left up for the user to decide, using set_wealth to choose their
amount of money and get_wealth to return it.
  
	Then, a random hobby, fear, hustles, and enemy are created for the specific sigma.  

	"gain_hobby" chooses a random hobby for the sigma.

	"gain_fear" chooses a random fear for the sigma.  

	"gain_hustle" chooses a random hustle for the sigma.

	"gain_enemy" chooses the enemy the sigma will face.

	In the fight() method, the sigma face their enemy in a game of rock, paper, scissors.  If the sigma proves victorious, they gain more wealth.  If the sigma and their enemy tie, the sigma must fight their enemy again.  If the 
sigma loses, they are defeated in battle and lose some of their wealth.






	To run the program, the user must call the constructor using parameters for the sigma's strength and weakness.  Then, they must call the set_name() method with a parameter for the sigma's name and return it using the get_name()
method.  They must set the wealth of their sigma using a float parameter for set_wealth() and return it using get_wealth().  Next, the user calls gain_hobby(), gain_fear(), gain_hustle(), and gain_enemy() so the sigma is randomly
assigned a hobby, fear, hustle, and enemy.  Then, the user calls the fight() method where the user inputs an attack for the sigma.  If the attack defeats the enemy, the sigma wins.  If it ties, the user must input another attack.  This
can be the same attack assigned as before.  Lastly, if the sigma loses, the fight ends.