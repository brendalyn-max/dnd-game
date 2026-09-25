from unittest.mock import patch

from dndgame.character import Character


def test_character_initialization() -> None:
    character = Character("Brendalyn", "Human", 10)

    assert character.name == "Brendalyn"
    assert character.race == "Human"
    assert character.base_hp == 10
    assert character.hp == 10
    assert character.max_hp == 10
    assert character.level == 1
    assert character.armor_class == 10


def test_get_modifier() -> None:
    character = Character("Test", "Human", 10)
    character.stats["STR"] = 14

    assert character.get_modifier("STR") == 2


@patch("dndgame.character.roll", return_value=12)
def test_roll_stats(mock_roll: object) -> None:
    character = Character("Test", "Human", 10)

    character.roll_stats()

    assert len(character.stats) == 6
    assert character.stats["STR"] == 12
    assert character.stats["DEX"] == 12
    assert character.stats["CON"] == 12
    assert character.hp == 11
    assert character.max_hp == 11


def test_human_racial_bonus() -> None:
    character = Character("Test", "Human", 10)
    character.stats = {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10,
    }

    character.apply_racial_bonuses()

    assert all(value == 11 for value in character.stats.values())


def test_elf_racial_bonus() -> None:
    character = Character("Test", "Elf", 10)
    character.stats = {"STR": 10, "DEX": 10, "CON": 10}

    character.apply_racial_bonuses()

    assert character.stats["STR"] == 10
    assert character.stats["DEX"] == 12
    assert character.stats["CON"] == 10


def test_dwarf_racial_bonus() -> None:
    character = Character("Test", "Dwarf", 10)
    character.stats = {"STR": 10, "DEX": 10, "CON": 10}

    character.apply_racial_bonuses()

    assert character.stats["CON"] == 12


def test_orc_racial_bonus() -> None:
    character = Character("Test", "Orc", 10)
    character.stats = {"STR": 10, "DEX": 10, "CON": 10}

    character.apply_racial_bonuses()

    assert character.stats["STR"] == 12
