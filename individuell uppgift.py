#blackjack spel
import random 

class Kortlek:
    def __init__(self):
        # Skapa en lista med kort (52 kort)
        self.kort = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 
                     '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                     '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
                     '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',]
                    
        self.blanda()

    # funktion med metoden som blandar korten.
    def blanda(self):
        random.shuffle(self.kort)

    # funtkion med metoden som drar ett kort från kortleken
    def dra_kort(self):
        if len(self.kort) > 0:
            return self.kort.pop()  # Ta bort och returnera det översta kortet
        else:
            return None  # Om det inte finns några kort kvar, returnera None

def beräkna_poäng(hand):
    poäng = 0
    ess = 0  # Hålla reda på antalet ess i handen

    for kort in hand:
        if kort in ['J', 'Q', 'K']:
            poäng += 10
        elif kort == 'A':
            ess += 1  # Räkna antalet ess
        else:
            poäng += int(kort)
    
    # Hantera värdet av ess
    for _ in range(ess):
        if poäng + 11 <= 21:
            poäng += 11  # Räkna ess som 11 om det inte överstiger 21
        else:
            poäng += 1   # Annars räkna ess som 1
    
    return poäng


def blackjack():
    kortlek = Kortlek()
    spelare_hand = []
    dealer_hand = []

    # Dela ut två kort var till spelaren och dealern
    for _ in range(2):
        spelare_hand.append(kortlek.dra_kort())
        dealer_hand.append(kortlek.dra_kort())

    # Spelarens tur
    while True:
        print(f"Din hand: {spelare_hand}")
        print(f"Dealerns första kort: {dealer_hand[0]}")

        spelare_poäng = beräkna_poäng(spelare_hand)
        print(f"Din poäng: {spelare_poäng}")

        if spelare_poäng > 21:
            print("Du har förlorat!")
            return

        val = input("Vill du ha ett kort till? (ja/nej): ")
        if val.lower() != "ja":
            break
        
        nytt_kort = kortlek.dra_kort()
        if nytt_kort is not None:
            spelare_hand.append(nytt_kort)
        else:
            print("Inga fler kort kvar i kortleken!")
            break

    # Dealerns tur
    dealer_poäng = beräkna_poäng(dealer_hand)
    while dealer_poäng < 17:
        dealer_hand.append(kortlek.dra_kort())
        dealer_poäng = beräkna_poäng(dealer_hand)
    
    # Visa slutresultat
    print(f"Din slutliga hand: {spelare_hand} (Poäng: {spelare_poäng})")
    print(f"Dealerns slutliga hand: {dealer_hand} (Poäng: {dealer_poäng})")

    # Avgör vinnare
    if dealer_poäng > 21:
        print("Du vinner!")
    elif spelare_poäng > dealer_poäng:
        print("Du vinner!")
    elif spelare_poäng < dealer_poäng:
        print("Dealer vinner!")
    else:
        print("Det blev oavgjort!")

# Kör spelet
blackjack()






