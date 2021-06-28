import numpy as np

class Simulation:

    def __init__(self, cards, num_of_sims):
        self.cards = cards
        self.num_of_sims = num_of_sims

    def run_for_cards(self, cards):
        cards=self.cards
        num_of_sims=self.num_of_sims
        deck, losses = np.arange(1,cards), 0

        for _ in range(num_of_sims):
            draw = np.random.choice(a=deck, size=len(deck), replace=False)
            if any(draw == list(deck)):
                losses+=1

        return 1-(losses/num_of_sims)

    def run(self):
        return self.run_for_cards(self.cards)

if __name__ == "__main__":
    sim = Simulation(cards=13, num_of_sims=1300)
    print(f"The probability of winning is {sim.run()}")
    for n in range(20):
        print(Simulation(cards=n, num_of_sims=1200).run())