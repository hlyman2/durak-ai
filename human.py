# it is up to these functions to make sure all actions done are legal

def defend(hand, field):
    
def attack(hand, field):
    print("current field:")
    for allegation, beating in field.cards:
        print(f"{allegation}: {beating}")

    print("choose cards to attack with:")
    for i, card in enumerate(hand):
        print(f"{i}: {card}")

    inp = input("choose numbers, space separated")

    for i in inp.split(" "):
        j = int(i)
        if field.add_allegation(self.hand[i]):
            self.hand[i] = None
        

