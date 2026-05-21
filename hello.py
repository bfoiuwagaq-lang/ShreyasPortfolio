moves = ["rock", "paper", "scissors"]

player_history = []
my_history = []

while True:
    opponent = input("opponent move: ").lower()

    if opponent not in moves:
        print("invalid")
        continue

    player_history.append(opponent)

    computer = "rock"

    if len(player_history) >= 2:

        if player_history[-1] == player_history[-2]:
            if opponent == "rock":
                computer = "paper"
            elif opponent == "paper":
                computer = "scissors"
            else:
                computer = "rock"

        
        elif (
            player_history[-2] == "rock" and opponent == "paper"
        ) or (
            player_history[-2] == "paper" and opponent == "scissors"
        ) or (
            player_history[-2] == "scissors" and opponent == "rock"
        ):

            if opponent == "rock":
                predicted = "paper"
            elif opponent == "paper":
                predicted = "scissors"
            else:
                predicted = "rock"

            if predicted == "rock":
                computer = "paper"
            elif predicted == "paper":
                computer = "scissors"
            else:
                computer = "rock"

        else:
            if opponent == "rock":
                computer = "paper"
            elif opponent == "paper":
                computer = "scissors"
            else:
                computer = "rock"

    print("my move:", computer)

    my_history.append(computer)