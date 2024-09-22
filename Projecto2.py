import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

## Part A
class WOFPlayer:
    
    def __init__(self, initName):
        self.name = initName
        self.prizeMoney = 0
        self.prizes = []
  
    def addMoney(self, atm):
        self.prizeMoney += atm
      
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        prize = self.prizes.append(prize)
        
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


## Part B       
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):    
        base_prompt ="""
        {} has ${}

        Category: {}
        Phrase: {}
        Guessed: {}
        
        Guess a letter, phrase, or type 'exit' or 'pass':
        """.format(self.name, self.prizeMoney ,category, obscuredPhrase, guessed)
        get_move = input(base_prompt)
        return get_move
    
## Part C
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, init_difficulty):
        import pdb;pdb.set_trace()
        super().__init__(name)
        self.difficulty = init_difficulty
        
    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        print('Random number between 1 and 10: {}'.format(rand_number))
        if(rand_number > self.difficulty):
            return False
        elif rand_number <= self.difficulty:
            return True
        
    def getPossibleLetters(self, guessed):
        accu = []
        for x in LETTERS:
            if x not in guessed:
                accu.append(x)

        if self.prizeMoney < VOWEL_COST:
            for vowel in VOWELS:
                if vowel in accu:
                    accu.remove(vowel)

        return accu  
              
    def getMove(self, category, obscuredPhrase, guessed):
        possible_letters = self.getPossibleLetters(guessed)
        if not possible_letters:
            return "pass"
        
        if self.smartCoinFlip():
            for letter in reversed(self.SORTED_FREQUENCIES):
                if letter in possible_letters:
                    return letter
        else:
            return random.choice(possible_letters)



#player = WOFPlayer("Jose")
#player.addMoney(200)
if __name__ == "__main__":
    # Crear instancia de WOFComputerPlayer
    player = WOFComputerPlayer("ComputerPlayer", 300)  # Ejemplo de nombre y dificultad
    
    # Simular algunos movimientos y cambios en prizeMoney
    player.addMoney(500)  # Agregar dinero para simular un cambio en prizeMoney
    
    # Supongamos que ya se han adivinado algunas letras
    guessed_letters = ['A', 'E', 'I']
    
    # Llamar al método getPossibleLetters
    possible_letters = player.getPossibleLetters(guessed_letters)
    
    # Imprimir o verificar la salida
    print("Letras posibles:", possible_letters)
#computer_player.getPossibleLetters("HIGADO")   
#player.addPrize("Vacaciones")
#human_player = WOFHumanPlayer("Jose")
#category = "Animal"
#obscuredPhrase = "_ _ _ _ _ _"
#guessed = "A, E, I, O, U"
#Llamar al metodo get move y capturar el resultado
#move = human_player.getMove(category, obscuredPhrase, guessed)
#print(human_player)

# Imprimir el resultado
#print("El movimiento ingresado fue:", move)

#print(a)
#print(test.name)
#print(test)