from dndgame.character import Character, RACE_BONUSES
from dndgame.combat import Combat
from dndgame.enemy import Goblin


def get_valid_choice(min_choice: int, max_choice: int) -> int:
    """Get a valid numeric choice from the user.

    Args:
        min_choice: The smallest valid choice.
        max_choice: The largest valid choice.

    Returns:
        A valid integer within the specified range.
    """
    while True:
        choice = input(f"Enter choice ({min_choice}-{max_choice}): ")

        try:
            choice_number = int(choice)
        except ValueError:
            print(
                f"Invalid choice. Please enter a number "
                f"from {min_choice} to {max_choice}."
            )
            continue

        if min_choice <= choice_number <= max_choice:
            return choice_number

        print(
            f"Invalid choice. Please enter a number "
            f"from {min_choice} to {max_choice}."
        )


def create_character() -> Character:
    """Create a character from user input.

    Returns:
        The newly created character.
    """
    print("Welcome to D&D Adventure!")
    name = input("Enter your character's name: ")

    print("\nChoose your race:")

    races = list(RACE_BONUSES.keys())

    for index, race in enumerate(races, start=1):
        bonuses = RACE_BONUSES[race]

        if "ALL" in bonuses:
            description = f"+{bonuses['ALL']} to all stats"
        else:
            description = ", ".join(
                f"+{bonus} {stat}" for stat, bonus in bonuses.items()
            )

        print(f"{index}. {race} ({description})")

    race_choice = get_valid_choice(1, len(races))
    race = races[race_choice - 1]

    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()

    return character


def display_character(character: Character) -> None:
    """Display a character's information.

    Args:
        character: The character to display.
    """
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")

    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        sign = "+" if modifier >= 0 else ""
        print(f"{stat}: {value} ({sign}{modifier})")

    print(f"\nHP: {character.hp}/{character.max_hp}")


def play_combat(player: Character) -> bool:
    """Run an interactive combat encounter against a goblin.

    Args:
        player: The player's character.

    Returns:
        True if the player wins, otherwise False.
    """
    goblin = Goblin()
    combat = Combat(player, goblin)

    print("\nA goblin appears!")

    while not combat.is_over():
        combat.round += 1

        print(f"\n--- Round {combat.round} ---")
        print(f"{goblin.name} HP: {goblin.hp}")
        print(f"{player.name} HP: {player.hp}")

        print("\nYour turn!")
        print("1. Attack")
        print("2. Run away")
        print()

        choice = get_valid_choice(1, 2)

        if choice == 2:
            return False

        damage = combat.attack(player, goblin)

        if damage > 0:
            print(f"You hit the goblin for {damage} damage!")
        else:
            print("You missed!")

        if combat.is_over():
            break

        print("\nThe goblin attacks!")

        damage = combat.attack(goblin, player)

        if damage > 0:
            print(f"The goblin hit you for {damage} damage!")
        else:
            print("The goblin missed!")

    if player.hp <= 0:
        print("\nYou were defeated!")
        return False

    return True


def main() -> None:
    """Run the D&D adventure."""
    player = create_character()

    while True:
        print("\nWhat would you like to do?")
        print("1. Fight a goblin")
        print("2. View character")
        print("3. Quit")

        choice = get_valid_choice(1, 3)

        if choice == 1:
            victory = play_combat(player)

            if victory:
                print("\nYou defeated the goblin!")
            else:
                print("\nThe combat is over.")

        elif choice == 2:
            display_character(player)

        elif choice == 3:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
