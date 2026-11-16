import unittest
from io import StringIO
from unittest.mock import patch, call

import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from escape import (
    rooms, pickable_objects, START_LOCATION, print_location, get_directions,
    find_room_by_direction, has_key_for_room, explore_room, game_loop, start_game
)

class TestEscapeGame(unittest.TestCase):

    def setUp(self):
        # Reset pickable objects before each test to ensure isolation
        pickable_objects["Key 1"]["picked"] = False
        pickable_objects["Key 2"]["picked"] = False

    def run_game(self, inputs, location=START_LOCATION):
        input_values = iter(inputs)

        def fake_input(prompt=""):
            print(prompt.rstrip())
            return next(input_values)

        with patch('builtins.input', side_effect=fake_input), patch('sys.stdout', new=StringIO()) as fake_out:
            start_game()
            game_loop(location)
            return fake_out.getvalue()

    def test_print_location(self):
        with patch('builtins.print') as mocked_print:
            print_location("Bedroom")
            print_location("Unknown")
            self.assertEqual(
                mocked_print.call_args_list,
                [call("You are in the Bedroom."), call("Unknown location.")]
            )

    def test_startup_and_exit_transcript(self):
        output = self.run_game(['x'])
        self.assertEqual(
            output,
            "Escape Game\n"
            "You are in the Bedroom.\n"
            "You can go: {'d': 'Bathroom', 's': 'Hallway'}\n"
            "Where do you want to go? ('x' to exit)\n"
            "Exited the game.\n"
        )

    def test_locked_room_transcript(self):
        output = self.run_game(['d', 'x'])
        self.assertEqual(
            output,
            "Escape Game\n"
            "You are in the Bedroom.\n"
            "You can go: {'d': 'Bathroom', 's': 'Hallway'}\n"
            "Where do you want to go? ('x' to exit)\n"
            "You don't have the key to enter this room.\n"
            "You are in the Bedroom.\n"
            "You can go: {'d': 'Bathroom', 's': 'Hallway'}\n"
            "Where do you want to go? ('x' to exit)\n"
            "Exited the game.\n"
        )

    def test_get_directions(self):
        # Known room: returns pathways (no printing responsibility)
        directions = get_directions("Bedroom")
        self.assertEqual(directions, {"d": "Bathroom", "s": "Hallway"})

        # Unknown room: returns empty dict (no printing)
        self.assertEqual(get_directions("Unknown"), {})

    def test_find_room_by_direction(self):
        self.assertEqual(find_room_by_direction("Bedroom", "d"), "Bathroom")
        with patch('builtins.print') as mocked_print:
            self.assertEqual(find_room_by_direction("Bedroom", "x"), "Bedroom")
            mocked_print.assert_called_with("Invalid direction. Try again.")

        # Unknown current location behavior
        with patch('builtins.print') as mocked_print:
            self.assertEqual(find_room_by_direction("Unknown", "d"), "Unknown")
            mocked_print.assert_called_with("Unknown location.")

    def test_has_key_for_room(self):
        pickable_objects["Key 1"]["picked"] = True
        self.assertTrue(has_key_for_room("Bathroom"))

        pickable_objects["Key 1"]["picked"] = False
        self.assertFalse(has_key_for_room("Bathroom"))

        self.assertTrue(has_key_for_room("Bedroom"))

        # Outside requires Key 2
        pickable_objects["Key 2"]["picked"] = False
        self.assertFalse(has_key_for_room("Outside"))
        pickable_objects["Key 2"]["picked"] = True
        self.assertTrue(has_key_for_room("Outside"))

        # Unknown destination room is inaccessible
        self.assertFalse(has_key_for_room("Unknown"))

    def test_explore_room(self):
        with patch('builtins.print') as mocked_print:
            explore_room("Hallway")
            self.assertEqual(mocked_print.call_args_list, [call("You found Key 1.")])
            self.assertTrue(pickable_objects["Key 1"]["picked"])

        with patch('builtins.print') as mocked_print:
            explore_room("Bathroom")
            self.assertEqual(mocked_print.call_args_list, [call("You found Key 2.")])
            self.assertTrue(pickable_objects["Key 2"]["picked"])

    def test_explore_room_idempotent(self):
        # Discover each key only once
        with patch('builtins.print') as mocked_print:
            explore_room("Hallway")
            explore_room("Hallway")
            messages = [c.args[0] for c in mocked_print.call_args_list]
            self.assertEqual(messages.count("You found Key 1."), 1)

        with patch('builtins.print') as mocked_print:
            # Reset state for Key 2
            pickable_objects["Key 2"]["picked"] = False
            explore_room("Bathroom")
            explore_room("Bathroom")
            messages = [c.args[0] for c in mocked_print.call_args_list]
            self.assertEqual(messages.count("You found Key 2."), 1)


if __name__ == "__main__":
    unittest.main()
