# Alice and Bob take turns playing a game with Alice starting first.

# In this game, there are n piles of stones. On each player's turn,
# the player should remove any positive number of stones from a non-empty pile of his or her choice.
# The first player who cannot make a move loses, and the other player wins.

 # Given an integer array piles, where piles[i] is the number of stones in the ith pile, return true if Alice wins,
# or false if Bob wins.

# Both Alice and Bob play optimally.

class Solution:
     def nimGame(self, piles: list[int]) -> bool:
          n = len(piles)

           def apply(move, state):
                arr = state.copy()
                i, dx = move
                arr[i] += dx
                return arr

            def getMoves(state):
                arr = state
                moves = []
                for i, v in enumerate(arr):
                    moves.extend([(i, -x) for x in range(1, v + 1)])
                return moves

            def isWin(state):
                for move in getMoves(state):
                    nxt_state = apply(move, state)
                    if not isWin(nxt_state):
                        return True
                return False

            return isWin(piles)
