#Project 100 ---- Atm
class Atm():
    def __init__(self,card,pin,amount):
        self.card = card
        self.pin = pin
        self.amount = amount
    
    def insert_card(self):
        card = input("Press E to insert your Atm Card :")
    def enter_pin(self):
        pin = input("Enter ypur pin :")
    def enter_amount(self):
        amount = input("Enter amount :")
        print("Amount withdrew   Balance -> 1985555")

card1 = Atm('card','pin','amount')

print(card1.insert_card())
print(card1.enter_pin())
print(card1.enter_amount())
    
