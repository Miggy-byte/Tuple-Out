import random

class DiceGame:
    def __init__(self, target_score=50, num_players=2):
        # Set up the game with the target score and number of players
        self.target_score = target_score
        self.num_players = num_players
        self.scores = [0] * num_players  # Initialize scores for all players
        self.current_player = 0  # Start with player 1

    def roll_dice(self):
        """Simulate rolling three six-sided dice."""
        return [random.randint(1, 6) for _ in range(3)]

    def check_tupled_out(self, dice):
        """Check if the player tupled out (all three dice are the same)."""
        return len(set(dice)) == 1

    def get_fixed_dice(self, dice):
        """Return indices of fixed dice (those that appear twice)."""
        counts = {x: dice.count(x) for x in set(dice)}
        fixed = [i for i, value in enumerate(dice) if counts[value] == 2]
        return fixed

    def player_turn(self):
        """Simulate a player's turn."""
        print(f"Player {self.current_player + 1}'s turn!")
        dice = self.roll_dice()
        print(f"Initial roll: {dice}")

        # Check if the player tupled out (three identical dice)
        if self.check_tupled_out(dice):
            print("Tupled out! You score 0 points for this turn.")
            return 0  # Tupled out means 0 points

        total_score = sum(dice)  # Start with the total of the initial roll
        fixed = self.get_fixed_dice(dice)  # Find which dice are fixed
        rerollable = [i for i in range(3) if i not in fixed]  # Dice that can be re-rolled

        # While the player has dice to re-roll
        while rerollable:
            rerolled_dice = [
                dice[i] if i in fixed else random.randint(1, 6) for i in range(3)
            ]
            print(f"Re-rolled dice: {rerolled_dice}")
            dice = rerolled_dice  # Update the dice with the re-rolled values

            # Check if the player tupled out after the re-roll
            if self.check_tupled_out(dice):
                print("Tupled out! You score 0 points for this turn.")
                return 0  # Tupled out means 0 points

            # Update fixed dice
            fixed = self.get_fixed_dice(dice)
            rerollable = [i for i in range(3) if i not in fixed]  # Update re-rollable dice

            # Ask the player whether they want to stop or continue
            stop = input("Do you want to stop? (y/n): ").lower()
            if stop == 'y':
                total_score = sum(dice)  # Player stops, so they score the total of the dice
                print(f"You scored {total_score} points this turn.")
                return total_score

        return total_score

    def play(self):
        """Play the game until one player reaches the target score."""
        while max(self.scores) < self.target_score:
            print(f"Current scores: {self.scores}")
            score = self.player_turn()  # The current player takes their turn
            self.scores[self.current_player] += score  # Add score to the player's total
            print(f"Player {self.current_player + 1}'s total score: {self.scores[self.current_player]}")

            # Check if any player has won
            if self.scores[self.current_player] >= self.target_score:
                break

            # Move to the next player
            self.current_player = (self.current_player + 1) % self.num_players

        # Game over, announce the winner
        winner = self.scores.index(max(self.scores)) + 1
        print(f"Game Over! Player {winner} wins with {max(self.scores)} points!")

# Set up the game
num_players = int(input("Enter the number of players: "))
target_score = 50  # Default target score
game = DiceGame(target_score=target_score, num_players=num_players)
game.play()
