import random


def main():
    first_player_key = int(input("Enter encrypt key of first player: "))
    second_player_key = int(input("Enter encrypt key of second player: "))
    throw_value = random.randint(1, 6)

    first_player_throw = throw_value ^ first_player_key
    second_player_throw = throw_value ^ second_player_key

    print("First player want throw: " + str(first_player_throw))
    print("Second player want throw: " + str(second_player_throw))
    print("Players exchanged keys...")
    print("first player " + str(first_player_throw ^ first_player_key))
    print("second player " + str(second_player_throw ^ second_player_key))


if __name__ == '__main__':
    main()
