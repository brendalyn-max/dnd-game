from dndgame.dice import roll
from dndgame.entity import Entity


class Combat:
    """Manage combat between two entities.

    Attributes:
        player: The player participating in combat.
        enemy: The enemy participating in combat.
        round: The current combat round.
        initiative_order: The order in which combatants act.
    """

    def __init__(self, player: Entity, enemy: Entity) -> None:
        """Initialize a combat encounter.

        Args:
            player: The player participating in combat.
            enemy: The enemy participating in combat.
        """
        self.player: Entity = player
        self.enemy: Entity = enemy
        self.round: int = 0
        self.initiative_order: list[Entity] = []

    def roll_initiative(self) -> list[Entity]:
        """Determine the order in which combatants act.

        Returns:
            The combatants ordered by initiative.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Entity, defender: Entity) -> int:
        """Perform an attack from one entity against another.

        Args:
            attacker: The entity making the attack.
            defender: The entity receiving the attack.

        Returns:
            The damage dealt, or zero if the attack misses.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")

        if attack_roll >= defender.armor_class:
            damage = roll(6, 1)
            defender.hp = max(0, defender.hp - damage)
            return damage

        return 0

    def is_over(self) -> bool:
        """Check whether either combatant has reached zero HP.

        Returns:
            True if the player or enemy has zero HP.
        """
        return self.player.hp <= 0 or self.enemy.hp <= 0

    def winner(self) -> Entity | None:
        """Return the surviving combatant.

        Returns:
            The surviving entity, or None if combat is not over.
        """
        if not self.is_over():
            return None

        if self.player.hp > 0:
            return self.player

        if self.enemy.hp > 0:
            return self.enemy

        return None
