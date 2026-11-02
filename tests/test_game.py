
import unittest

from game import (
    new_game,
    spend_energy,
    move_player,
    collect_item,
    can_cross_bridge,
    can_light_lighthouse,
    activate_beacon,
)


class TestMysteryIsland(unittest.TestCase):

    def setUp(self):
        """Create a fresh player before every test."""
        self.player = new_game("Jaydee")

    def prepare_player_for_cave(self):
        """Move the player to the Cave with the rope."""
        move_player(self.player, "Jungle")
        collect_item(self.player)
        move_player(self.player, "Cave")

    def prepare_player_for_bridge(self):
        """Move the player to the Old Bridge with required items."""
        self.prepare_player_for_cave()
        collect_item(self.player, "careful")
        move_player(self.player, "Old Bridge")

    # INITIAL STATE TESTS

    def test_new_game_initial_state(self):
        self.assertEqual(self.player["name"], "Jaydee")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])
        self.assertFalse(self.player["game_over"])
        self.assertFalse(self.player["won"])

    # MOVEMENT TESTS

    def test_move_from_beach_to_jungle(self):
        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_cannot_skip_a_location(self):
        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_cannot_leave_jungle_without_rope(self):
        move_player(self.player, "Jungle")

        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertIn("rope", message.lower())
        self.assertEqual(self.player["location"], "Jungle")

    def test_safe_jungle_route_costs_one_energy(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)

        success, message = move_player(
            self.player, "Cave", "safe"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 3)

    def test_dangerous_jungle_route_costs_two_energy(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)

        success, message = move_player(
            self.player, "Cave", "dangerous"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 2)

    def test_invalid_jungle_route_does_not_cost_energy(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)

        success, message = move_player(
            self.player, "Cave", "invalid"
        )

        self.assertFalse(success)
        self.assertEqual(self.player["energy"], 4)
        self.assertEqual(self.player["location"], "Jungle")

    # INVENTORY TESTS

    def test_collect_rope(self):
        move_player(self.player, "Jungle")

        success, message = collect_item(self.player)

        self.assertTrue(success)
        self.assertIn("Rope", self.player["inventory"])
        self.assertTrue(can_cross_bridge(self.player))
        self.assertEqual(self.player["energy"], 4)

    def test_cannot_collect_same_item_twice(self):
        move_player(self.player, "Jungle")

        collect_item(self.player)
        success, message = collect_item(self.player)

        self.assertFalse(success)
        self.assertEqual(self.player["inventory"].count("Rope"), 1)

    def test_cannot_collect_item_on_beach(self):
        success, message = collect_item(self.player)

        self.assertFalse(success)
        self.assertEqual(self.player["inventory"], [])
        self.assertEqual(self.player["energy"], 5)

    def test_cannot_leave_cave_without_lantern(self):
        self.prepare_player_for_cave()

        success, message = move_player(
            self.player, "Old Bridge"
        )

        self.assertFalse(success)
        self.assertIn("lantern", message.lower())
        self.assertEqual(self.player["location"], "Cave")

    def test_careful_lantern_search_costs_no_extra_energy(self):
        self.prepare_player_for_cave()

        energy_before = self.player["energy"]

        success, message = collect_item(
            self.player, "careful"
        )

        self.assertTrue(success)
        self.assertIn("Lantern", self.player["inventory"])
        self.assertTrue(can_light_lighthouse(self.player))
        self.assertEqual(self.player["energy"], energy_before)

    def test_rushed_lantern_search_costs_one_energy(self):
        self.prepare_player_for_cave()

        energy_before = self.player["energy"]

        success, message = collect_item(
            self.player, "rushed"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], energy_before - 1)

    # ENERGY MANAGEMENT TESTS

    def test_spend_energy(self):
        success, message = spend_energy(self.player, 2)

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 3)

    def test_cannot_spend_more_energy_than_available(self):
        success, message = spend_energy(self.player, 6)

        self.assertFalse(success)
        self.assertEqual(self.player["energy"], 5)
        self.assertFalse(self.player["game_over"])

    def test_energy_cannot_be_negative(self):
        spend_energy(self.player, 5)

        self.assertEqual(self.player["energy"], 0)
        self.assertGreaterEqual(self.player["energy"], 0)

    def test_zero_energy_causes_immediate_loss(self):
        success, message = spend_energy(self.player, 5)

        self.assertTrue(success)
        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])
        self.assertFalse(self.player["won"])

    def test_cannot_spend_negative_energy_cost(self):
        success, message = spend_energy(self.player, -1)

        self.assertFalse(success)
        self.assertEqual(self.player["energy"], 5)

    def test_rushed_bridge_crossing_can_cause_loss(self):
        self.prepare_player_for_bridge()

        self.player["energy"] = 2

        success, message = move_player(
            self.player, "Lighthouse", "rushed"
        )

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Lighthouse")
        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])
        self.assertFalse(self.player["won"])

    # VICTORY TESTS

    def test_cannot_activate_beacon_without_lantern(self):
        self.player["location"] = "Lighthouse"

        success, message = activate_beacon(self.player)

        self.assertFalse(success)
        self.assertFalse(self.player["won"])
        self.assertFalse(self.player["game_over"])

    def test_minimum_winning_path_leaves_one_energy(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)
        move_player(self.player, "Cave", "safe")
        collect_item(self.player, "careful")
        move_player(self.player, "Old Bridge")
        move_player(self.player, "Lighthouse", "careful")

        self.assertEqual(self.player["energy"], 1)

        success, message = activate_beacon(self.player)

        self.assertTrue(success)
        self.assertTrue(self.player["won"])
        self.assertTrue(self.player["game_over"])
        self.assertEqual(self.player["energy"], 1)
        self.assertIn("CONGRATULATIONS", message)


if __name__ == "__main__":
    unittest.main()
