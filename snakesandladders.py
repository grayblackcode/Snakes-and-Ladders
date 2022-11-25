import random


class Player:
    def __init__(self, name):
        self.position = 0
        self.name = name

    # find the position of the player and place on the relevant snake and ladder combinations.
    def get_position(self):
        return self.position

    # returning the final position after roll
    def after_roll(self):
        roll = input('Press enter to roll')
        if roll == '':
            roll = random.randint(1, 6)
        print(f"{self.name}'s dice roll is {roll}")
        self.position += int(roll)
        return self.position

    # depending on the player's position moves them up and down with a message
    @staticmethod
    def snake_and_ladder(position):
        results = {1: 38, 4: 14, 9: 31, 17: 7, 21: 42, 28: 84, 51: 67, 54: 34,
                   62: 19, 64: 60, 72: 91, 80: 99, 87: 36, 93: 73, 95: 75, 98: 79}
        if position in results:
            return 'You have moved from position {} to position {}'.format(position, results[position])


# input different player's names
def register():
    new = Player(input('Player name: '))
    players.append(new)


players = []
for x in range(0, 4):
    register()

for player in players:
    print(player.name, player.position)


def play():
    player_index = 0
    while True:
        if player_index < len(players):  # if no winner player index resets to 0
            curr_player = players[player_index]
            print(f"\n{curr_player.name}'s turn")  # this person's turn
            print(f"{curr_player.name}'s initial position: {curr_player.position}")
            curr_player.after_roll()
            print(f"{curr_player.name}'s position after roll: {curr_player.position}")

            if curr_player.position in [1, 4, 9, 17, 21, 28, 51, 54, 62, 64, 72, 80, 87, 93, 95, 98]:
                print(curr_player.snake_and_ladder(curr_player.position))

                final = curr_player.snake_and_ladder(curr_player.position)
                curr_player.position = int(final.split(' ')[8])
                print(f"{curr_player.name}'s position after roll: {curr_player.position}")

            if curr_player.position > 100:
                curr_player.position -= 100
            if curr_player.position == 100:
                print(f"{curr_player.name} Wins!!")
                break

            player_index += 1

        else:
            player_index = 0
    return 'GAME OVER'


play()
