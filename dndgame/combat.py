from dndgame.dice import roll


class Combat:
    """Manage combat between a player and an enemy.

    Attributes:
        player: The player character participating in combat.
        enemy: The enemy participating in combat.
        round: The current combat round.
        initiative_order: The order in which combatants take their turns.
    """

    def __init__(self, player, enemy):
        """Initialize a combat encounter.

        Args:
            player: The player character participating in combat.
            enemy: The enemy participating in combat.
        """
        self.player = player
        self.enemy = enemy
        self.round = 0
        self.initiative_order = []

    def roll_initiative(self):
        """Determine the order in which combatants act.

        Initiative is calculated by rolling a d20 and adding each
        combatant's DEX modifier.

        Returns:
            A list containing the player and enemy in initiative order.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker, defender):
        """Perform an attack from one combatant against another.

        The attacker rolls a d20 and adds their STR modifier. If the
        result meets or exceeds the defender's armor class, the attack
        deals 1d6 damage.

        Args:
            attacker: The combatant making the attack.
            defender: The combatant receiving the attack.

        Returns:
            The amount of damage dealt, or 0 if the attack misses.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6
        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp -= damage
            return damage
        return 0