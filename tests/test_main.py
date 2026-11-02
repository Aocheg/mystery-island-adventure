
import unittest
from unittest.mock import patch

from main import main


class TestMainApplication(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        "Jaydee",   # First player's name
        "6",        # Quit first adventure
        "y",        # Choose replay
        "Heley",    # Second player's name
        "5",        # Check status
        "6",        # Quit second adventure
        "n",        # Decline another replay
    ])
    def test_replay_starts_a_fresh_game(self, mock_input):
        with patch("builtins.print") as mock_print:
            main()

        output = "\n".join(
            str(call) for call in mock_print.call_args_list
        )

        # Both adventures should start successfully.
        self.assertIn("Welcome, Jaydee.", output)
        self.assertIn("Welcome, Heley.", output)

        # Both adventures should begin with 5 energy.
        self.assertGreaterEqual(
            output.count("Energy: 5/5"), 2
        )

        # The second player's inventory should be empty.
        self.assertIn("- Empty", output)

        # The game should reach its final exit message.
        self.assertIn(
            "Thank you for playing Mystery Island Adventure!",
            output
        )

    @patch("builtins.input", side_effect=[
        "Jaydee",   # Player's name
        "6",        # Quit adventure
        "invalid",  # Invalid replay response
        "n",        # Decline replay
    ])
    def test_invalid_replay_response_is_rejected(self, mock_input):
        with patch("builtins.print") as mock_print:
            main()

        printed_messages = [
            str(call) for call in mock_print.call_args_list
        ]

        self.assertTrue(
            any(
                "Invalid response" in message
                for message in printed_messages
            )
        )


if __name__ == "__main__":
    unittest.main()
