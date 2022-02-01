#!/usr/bin/env python
"""


"""

from api import State, util
from api import State
from api import Deck
from api import _state
import random

class Bot:

    __max_depth = -1
    __randomize = True

    def __init__(self, randomize=True, depth=8):
        self.__randomize = randomize
        self.__max_depth = depth

    def get_move(self: Deck, state: State):
        moves = state.moves()
        prev_trick= state.get_prev_trick()    
        for move in moves:
            if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "S"):
                if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "S") in moves:
                    return Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "S")
            if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "H"):
                if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "H") in moves:
                    return Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "H")
            if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "D"):
                if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "D") in moves:
                    return Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "D")
            if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "C"):
                if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "C") in moves:
                    return Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "C")                                   
            if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "S"):
                if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "S") in moves:
                    return Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "S")
            if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "H"):
                if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "H") in moves:
                    return Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "H")
            if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "D"):
                if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "D") in moves:
                    return Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "D")
            if Deck.get_rank(move[0]) == "Q" and Deck.get_suit(move[1] == "C"):
                if Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "C") in moves:
                    return Deck.get_rank(move[0]) == "K" and Deck.get_suit(move[1] == "C")     
            if Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1] == "S"):
                return move
            if prev_trick!= Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1]) == "S":
                if Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1] == "H"):
                    return move
            if (prev_trick!= Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1]) == "S") or (prev_trick!= Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1]) == "H"):
                if Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1] == "D"):
                    return move
            if (prev_trick!= Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1]) == "S") or (prev_trick!= Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1]) == "H") or (prev_trick!= Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1]) == "D"):        
                if Deck.get_rank(move[0]) == "A" and Deck.get_suit(move[1] == "C"):
                    return move            
            # elif Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1] == "S"):
            #         return move
            # if prev_trick!= Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1]) == "S":
            #     if Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1] == "H"):
            #         return move
            # if (prev_trick!= Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1]) == "S") or (prev_trick!= Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1]) == "H"):            
            #     if Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1] == "D"):
            #         return move
            # if (prev_trick!= Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1]) == "S") or (prev_trick!= Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1]) == "H") or (prev_trick!= Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1]) == "D"):
            #     if Deck.get_rank(move[0]) == "10" and Deck.get_suit(move[1] == "C"):
            #         return move        
        else:    
            val, move = self.value(state)

            return move
    

    def value(self, state, alpha=float('-inf'), beta=float('inf'), depth = 0):

        
        if state.finished():
            winner, points = state.winner()
            return (points, None) if winner == 1 else (-points, None)
            t = d.__trick

        if depth == self.__max_depth:
            return heuristic(state)

        best_value = float('-inf') if maximizing(state) else float('inf')
        best_move = None

        moves = state.moves()

        



        for move in moves:
            next_state = state.next(move)
            value, _ = self.value(next_state)
            

            if maximizing(state):
                if value > best_value:
                    best_value = value
                    best_move = move
                    alpha = best_value
            else:
                if value < best_value:
                    best_value = value
                    best_move = move
                    beta = best_value

            # Prune the search tree
            # We know this state will never be chosen, so we stop evaluating its children
            if beta <= alpha:
                break

        return best_value, best_move

def maximizing(state):
    # type: (State) -> bool
    """
    Whether we're the maximizing player (1) or the minimizing player (2).

    :param state:
    :return:
    """
    return state.whose_turn() == 1

def heuristic(state):
    # type: (State) -> float
    """
    Estimate the value of this state: -1.0 is a certain win for player 2, 1.0 is a certain win for player 1

    :param state:
    :return: A heuristic evaluation for the given state (between -1.0 and 1.0)
    """
    return util.ratio_points(state, 1) * 2.0 - 1.0, None