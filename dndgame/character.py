from dndgame.dice import roll


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


class Character:
    """Represent a player character in the D&D adventure.

    Attributes:
        name: The character's name.
        race: The character's race.
        stats: The character's six ability scores.
        base_hp: The character's starting hit points.
        hp: The character's current hit points.
        max_hp: The character's maximum hit points.
        level: The character's current level.
        armor_class: The character's armor class used when defending.
    """

    def __init__(self, name: str, race: str, base_hp: int) -> None:
        """Initialize a new character.

        Args:
            name: The character's name.
            race: The character's race.
            base_hp: The character's starting hit points.
        """
        self.name: str = name
        self.race: str = race
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = 0
        self.max_hp: int = 0
        self.level: int = 1
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate the ability modifier for a stat.

        Args:
            stat: The name of the ability score, such as STR or DEX.

        Returns:
            The ability modifier calculated from the stat score.
        """
        return (self.stats[stat] - 10) // 2

    def roll_stats(self) -> None:
        """Roll and assign values for the character's ability scores.

        The character receives values for STR, DEX, CON, INT, WIS,
        and CHA. Maximum and current HP are then calculated using
        the character's base HP and CON modifier.
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
            for stat in self.stats:
                self.stats[stat] += bonuses["ALL"]

        for stat, bonus in bonuses.items():
            if stat != "ALL":
                self.stats[stat] += bonus