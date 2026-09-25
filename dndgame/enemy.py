from dndgame.entity import Entity


class Enemy(Entity):
    """Represent an enemy that can participate in combat.

    Attributes:
        name: The enemy's name.
        stats: The enemy's ability scores.
        hp: The enemy's current hit points.
        max_hp: The enemy's maximum hit points.
        armor_class: The enemy's armor class.
    """

    def __init__(
        self,
        name: str,
        hp: int,
        stats: dict[str, int],
        armor_class: int = 10,
    ) -> None:
        """Initialize an enemy.

        Args:
            name: The enemy's name.
            hp: The enemy's starting and maximum hit points.
            stats: The enemy's ability scores.
            armor_class: The enemy's armor class.
        """
        super().__init__(name, hp)
        self.stats = stats
        self.armor_class = armor_class


class Goblin(Enemy):
    """Represent a standard goblin enemy."""

    def __init__(self) -> None:
        """Initialize a goblin with standard combat statistics."""
        super().__init__(
            name="Goblin",
            hp=5,
            stats={
                "STR": 8,
                "DEX": 14,
                "CON": 10,
                "INT": 8,
                "WIS": 8,
                "CHA": 8,
            },
            armor_class=10,
        )
