class Entity:
    """Represent a participant in the D&D game.

    Attributes:
        name: The entity's name.
        stats: The entity's ability scores.
        base_hp: The entity's starting hit points.
        hp: The entity's current hit points.
        max_hp: The entity's maximum hit points.
        level: The entity's current level.
        armor_class: The entity's armor class.
    """

    def __init__(self, name: str, base_hp: int) -> None:
        """Initialize an entity.

        Args:
            name: The entity's name.
            base_hp: The entity's starting hit points.
        """
        self.name: str = name
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = base_hp
        self.max_hp: int = base_hp
        self.level: int = 1
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate the modifier for an ability score.

        Args:
            stat: The ability score name.

        Returns:
            The calculated ability modifier.
        """
        return (self.stats[stat] - 10) // 2
