class Card(object):
    '''Represents a standard playing card.'''
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                     Card.suit_names[self.suit])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        return 0

    def __cmp1__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        print(t1)
        print(t2)
        return cmp(t1, t2)


queen_of_diamonds = Card(1, 12)
print(queen_of_diamonds)
jack_of_hearts = Card(2, 11)
print(jack_of_hearts)
queen_of_diamonds.__cmp1__(jack_of_hearts)
