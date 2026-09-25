from unittest.mock import patch

from dndgame.character import Character
from dndgame.combat import Combat
from dndgame.enemy import Goblin


def make_player() -> Character:
    player = Character("Hero", "Human", 10)
    player.stats = {
        "STR": 14,
        "DEX": 12,
        "CON": 12,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }
    player.hp = 10
    player.max_hp = 10
    return player


def test_goblin_initialization() -> None:
    goblin = Goblin()

    assert goblin.name == "Goblin"
    assert goblin.hp == 5
    assert goblin.max_hp == 5
    assert goblin.armor_class == 10
    assert goblin.stats["DEX"] == 14


@patch("dndgame.combat.roll", side_effect=[15, 10])
def test_roll_initiative(mock_roll: object) -> None:
    player = make_player()
    goblin = Goblin()
    combat = Combat(player, goblin)

    order = combat.roll_initiative()

    assert order == [player, goblin]


@patch("dndgame.combat.roll", side_effect=[15, 4])
def test_attack_hits(mock_roll: object) -> None:
    player = make_player()
    goblin = Goblin()
    combat = Combat(player, goblin)

    damage = combat.attack(player, goblin)

    assert damage == 4
    assert goblin.hp == 1


@patch("dndgame.combat.roll", return_value=1)
def test_attack_misses(mock_roll: object) -> None:
    player = make_player()
    goblin = Goblin()
    combat = Combat(player, goblin)

    damage = combat.attack(player, goblin)

    assert damage == 0
    assert goblin.hp == 5


@patch("dndgame.combat.roll", side_effect=[20, 10])
def test_enemy_can_attack_player(mock_roll: object) -> None:
    player = make_player()
    goblin = Goblin()
    combat = Combat(player, goblin)

    damage = combat.attack(goblin, player)

    assert damage == 10
    assert player.hp == 0


def test_combat_is_over_when_player_reaches_zero_hp() -> None:
    player = make_player()
    player.hp = 0
    goblin = Goblin()
    combat = Combat(player, goblin)

    assert combat.is_over() is True


def test_combat_is_over_when_enemy_reaches_zero_hp() -> None:
    player = make_player()
    goblin = Goblin()
    goblin.hp = 0
    combat = Combat(player, goblin)

    assert combat.is_over() is True


def test_winner_returns_survivor() -> None:
    player = make_player()
    goblin = Goblin()
    goblin.hp = 0
    combat = Combat(player, goblin)

    assert combat.winner() is player


def test_winner_returns_none_when_combat_is_active() -> None:
    player = make_player()
    goblin = Goblin()
    combat = Combat(player, goblin)

    assert combat.winner() is None
