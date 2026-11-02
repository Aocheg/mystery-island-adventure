
import unittest

from game import (
    new_game,
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

    def test_new_game_initial_state(self):
        self.assertEqual(self.player["name"], "Jaydee")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])
        self.assertFalse(self.player["game_over"])
        self.assertFalse(self.player["won"])

    def test_move_from_beach_to_jungle(self):
        success, message = move_player(self.player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(self.player["location"], "Jungle")

    def test_cannot_skip_a_location(self):
        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertEqual(self.player["location"], "Beach")

    def test_cannot_leave_jungle_without_rope(self):
        move_player(self.player, "Jungle")

        success, message = move_player(self.player, "Cave")

        self.assertFalse(success)
        self.assertIn("rope", message.lower())
        self.assertEqual(self.player["location"], "Jungle")

    def test_collect_rope(self):
        move_player(self.player, "Jungle")

        success, message = collect_item(self.player)

        self.assertTrue(success)
        self.assertIn("Rope", self.player["inventory"])
        self.assertTrue(can_cross_bridge(self.player))

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

    def test_cannot_leave_cave_without_lantern(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)
        move_player(self.player, "Cave")

        success, message = move_player(self.player, "Old Bridge")

        self.assertFalse(success)
        self.assertIn("lantern", message.lower())
        self.assertEqual(self.player["location"], "Cave")

    def test_collect_lantern(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)
        move_player(self.player, "Cave")

        success, message = collect_item(self.player)

        self.assertTrue(success)
        self.assertIn("Lantern", self.player["inventory"])
        self.assertTrue(can_light_lighthouse(self.player))

    def test_activate_beacon_and_win(self):
        move_player(self.player, "Jungle")
        collect_item(self.player)
        move_player(self.player, "Cave")
        collect_item(self.player)
        move_player(self.player, "Old Bridge")
        move_player(self.player, "Lighthouse")

        success, message = activate_beacon(self.player)

        self.assertTrue(success)
        self.assertTrue(self.player["won"])
        self.assertTrue(self.player["game_over"])
        self.assertIn("CONGRATULATIONS", message)

    def test_cannot_activate_beacon_without_lantern(self):
        self.player["location"] = "Lighthouse"

        success, message = activate_beacon(self.player)

        self.assertFalse(success)
        self.assertFalse(self.player["won"])
        self.assertFalse(self.player["game_over"])


if __name__ == "__main__":
    unittest.main()
