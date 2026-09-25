from dndgame.dice import roll
from dndgame.entity import Entity


RACE_BONUSES: dict[str, dict[str, int]] = {
    "Human": {
        "ALL": 1,
    },
    "Elf": {
        "DEX": 2,
    },
    "Dwarf": {
        "CON": 2,
    },
    "Orc": {
        "STR": 2,
    },
}


class Character(Entity):
    """Represent a player character in the D&D adventure.

    Attributes:
        name: The character's name.
        race: The character's race.
        stats: The character's six ability scores.
        base_hp: The character's starting hit points.
        hp: The character's current hit points.
        max_hp: The character's maximum hit points.
        level: The character's current level.
        armor_class: The character's armor class.
    """

    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a player character.

        Args:
            name: The character's name.
            race: The character's race.
            base_hp: The character's starting hit points.
        """
        super().__init__(name, base_hp)
        self.race: str = race

    def roll_stats(self) -> None:
        """Roll and assign the character's ability scores.

        The character receives values for STR, DEX, CON, INT, WIS,
        and CHA. Maximum and current HP are then calculated.
        """
        print("Rolling stats...\n")

        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self) -> None:
        """Apply ability score bonuses based on the character's race.

        Humans gain +1 to every ability score, Elves gain +2 DEX,
        Dwarves gain +2 CON, and Orcs gain +2 STR.
        """
        bonuses = RACE_BONUSES[self.race]

        if "ALL" in bonuses:
            self.stats = {
                stat: value + bonuses["ALL"]
                for stat, value in self.stats.items()
            }

        self.stats = {
            stat: value + bonuses.get(stat, 0)
            for stat, value in self.stats.items()
        }
