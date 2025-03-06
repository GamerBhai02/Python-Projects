from random import shuffle
from functools import total_ordering


@total_ordering
class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        return (self.value, self.suit) < (other.value, other.suit)

    def __gt__(self, other):
        return (self.value, self.suit) > (other.value, other.suit)

    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(2, 15) for suit in range(4)]
        shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def __repr__(self):
        return self.name


class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(input("Enter player 1 name: "))
        self.p2 = Player(input("Enter player 2 name: "))

    def display_round_result(self, p1_card, p2_card):
        print(f"{self.p1.name} drew {p1_card} | {self.p2.name} drew {p2_card}")

    def announce_winner(self, winner_name):
        print(f"{winner_name} wins this round!")

    def determine_game_winner(self):
        if self.p1.wins > self.p2.wins:
            return self.p1.name
        elif self.p1.wins < self.p2.wins:
            return self.p2.name
        else:
            return "It's a tie!"

    def play_game(self):
        print("Welcome to War! Let's play.")
        
        while len(self.deck.cards) >= 2:
            response = input("Press any key to play, or 'q' to quit: ")
            if response.lower() == 'q':
                break

            p1_card = self.deck.draw_card()
            p2_card = self.deck.draw_card()

            self.display_round_result(p1_card, p2_card)

            if p1_card > p2_card:
                self.p1.wins += 1
                self.announce_winner(self.p1.name)
            elif p2_card > p1_card:
                self.p2.wins += 1
                self.announce_winner(self.p2.name)
            else:
                print("It's a tie! War round begins...")
                self.war_round(p1_card, p2_card)

        print(f"Game Over! {self.determine_game_winner()} wins the game.")

    def war_round(self, p1_card, p2_card):
        war_p1_cards = [p1_card]
        war_p2_cards = [p2_card]

        while len(self.deck.cards) > 2:
            print("War continues!")
            war_p1_cards.append(self.deck.draw_card())
            war_p2_cards.append(self.deck.draw_card())

            p1_card = war_p1_cards[-1]
            p2_card = war_p2_cards[-1]
            print(f"{self.p1.name} drew {p1_card} | {self.p2.name} drew {p2_card}")

            if p1_card > p2_card:
                self.p1.wins += 1
                print(f"{self.p1.name} wins the war round!")
                break
            elif p2_card > p1_card:
                self.p2.wins += 1
                print(f"{self.p2.name} wins the war round!")
                break

        if len(war_p1_cards) > len(war_p2_cards):
            print(f"{self.p1.name} wins the war round!")
        elif len(war_p2_cards) > len(war_p1_cards):
            print(f"{self.p2.name} wins the war round!")
        else:
            print("It's a tie in the war!")


if __name__ == "__main__":
    game = Game()
    game.play_game()
