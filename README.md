
# Part 3: Improving Room and Object Handling

In this part, you will refactor and enhance the handling of rooms, pathways, and objects to make the game architecture more modular, flexible, and extendable.

You will do this by using dictionaries to structure and store information about each room, the pathways that connect them, and the key items that influence gameplay.

By the end of this part, the game's core structure will be ready for expansion in Part 4. You'll have a flexible system that makes adding new rooms, objects, or mechanics straightforward, allowing you to expand the game in whichever direction you choose.

This part builds directly on the game you completed in Part 2.

You may continue from your own Part 2 solution or copy the instructor solution for Part 2 posted in D2L.

In this part, you will refactor that game to use the provided dictionary-driven structure for rooms, pathways, and objects. If you use the instructor solution, you are still responsible for understanding and explaining your final code.

**All game data, including room connections, access requirements, and item states, must be accessed and managed through the provided dictionary structures to maintain consistency and scalability.**

## Goal

* Implement dictionaries to define each room, its connections, and any required keys or conditions for access, creating a structured and modular layout for navigation.

## House Map

The house map is not changed for this version.

- The `X` in the diagram below represents that the room is locked and requires a key to access it.
- `Key 1`: Found in the `Hallway`. Unlocks access to the `Bathroom`.
- `Key 2`: Found in the `Bathroom`. Unlocks the final exit to the `Outside`.

```
            |----------|-----------|
(unlock w/  |          | (unlock w/| 
    Key 2)  |          |   Key 1)  | 
    Outside | Bedroom  X Bathroom  | 
            |          |   *Key 2* |
  |----X----|---    ---|-----------|
  |         |          |
  | Kitchen   Hallway  | 
  |         |   *Key 1*| 
  |---------|----------|
```

### Example Flow
- The player starts in the `Bedroom`.
- The player tries to move to the `Bathroom`, but is denied since `Key 1` was not collected.
- The player moves to the Hallway and finds `Key 1`.
- Using `Key 1`, the player can enter the Bathroom and find `Key 2`.
- With both keys in hand, the player moves through the `Kitchen` and `Hallway` to reach the `Outside` and escape.

## Dictionary Structure
We will use dictionaries to define both the rooms and the objects (keys) in the game. The helpers must read and write exclusively through these dictionaries.

* The `rooms` dictionary is a structured representation of each room in the game. Each key in the `rooms` dictionary represents the name of a room (e.g., `"Bedroom"`, `"Hallway"`, etc.), while the corresponding value is itself a dictionary that provides additional details about that room. This inner dictionary uses two main keys:

   ``` python
      rooms = {
         "Bedroom": {
               "pathways": {"d": "Bathroom", "s": "Hallway"}, 
               "open_with": ""
               },
         "Hallway": {
               "pathways": {"w": "Bedroom", "a": "Kitchen"}, 
               "open_with": ""
               },
         "Bathroom": {
               "pathways": {"a": "Bedroom"}, 
               "open_with": "Key 1"
               },
         "Kitchen": {
               "pathways": {"d": "Hallway", "w": "Outside"}, 
               "open_with": ""
               },
         "Outside": {
               "pathways": {"s": "Kitchen"}, 
               "open_with": "Key 2"
               },
      }
   ```

   - **pathways**: A dictionary that maps directions (`"d"`, `"s"`, `"w"`, `"a"`) to the rooms they lead to. For example, in the `"Bedroom"`, `"d"` leads to the `"Bathroom"` and `"s"` to the `"Hallway"`. This structure allows for flexible navigation options in each room.

   - **open_with**: A string that specifies which key (if any) is needed to access the room. If no key is required, `open_with` is an empty string (`""`). For instance, entering the `"Bathroom"` requires `"Key 1"`, while the `"Outside"` requires `"Key 2"`.


* The `pickable_objects` dictionary stores details about objects (like keys) that can be found and collected within the game.

   ```python
      pickable_objects = {
         "Key 1": {"location": "Hallway", "picked": False},
         "Key 2": {"location": "Bathroom", "picked": False}
      }
   ```

   - **location**: Specifies the location where the object (key) can be found initially in the game.
   - **picked**: Tracks whether the player has already collected the object, with `False` indicating it hasn’t been picked up yet. Keys are picked up automatically when entering the room that contains them and should only be announced once.

## Behavior Contracts (Helpers)
Implement the following behaviors and exact messages. All game data must be accessed only via the `rooms` and `pickable_objects` dictionaries.

- `print_location(location)`
  - If `location` exists in `rooms`: print `You are in <Room>.`
  - Otherwise: print `Unknown location.`

- `get_directions(location)`
  - If `location` exists in `rooms`: return `rooms[location]["pathways"]`.
  - Otherwise: return `{}`.

- `game_loop(location)`
  - Calls `print_location(location)` and `explore_room(location)` each turn.
  - Retrieves directions via `get_directions(location)` and prints `You can go: {<pathways dict>}`.
  - Handles user input and uses `find_room_by_direction` + `has_key_for_room` to gate movement.

- `find_room_by_direction(location, direction)`
  - If `location` is unknown: print `Unknown location.` and return the original `location`.
  - If `direction` exists in `rooms[location]["pathways"]`: return the destination room.
  - Otherwise: print `Invalid direction. Try again.` and return the original `location`.

- `has_key_for_room(room_id)`
  - If `room_id` is unknown: return `False` (treat as inaccessible).
  - If `rooms[room_id]["open_with"]` is empty: return `True`.
  - Otherwise: return whether `pickable_objects[required_key]["picked"]` is `True`.

- `explore_room(location)`
  - If `location` matches an object’s `location` and that object’s `picked` is `False`, set it to `True` and print `You found <Key>.`
  - If there is no object to pick up or it was already picked up, do nothing (do not print again). This behavior must be idempotent.



## Getting Started

- Starting from your Part 2 code or the instructor Part 2 solution posted in D2L, refactor the game to use the provided dictionary-based structure.
- Open `escape.py` to start working on the project.

## How to Run 
- Run the script directly in your terminal with `python escape.py` to see the output.

## Inputs
- Directions for movement:
  - `d` (right)
  - `s` (down)
  - `w` (up)
  - `a` (left)
- Exit the game:
  - `x` (ends the game)

- Keys will be picked up automatically when entering the corresponding room.


## Expected Output
When you run your program, the console should display the following text exactly:

```
   Escape Game
   You are in the Bedroom.
   You can go: {'d': 'Bathroom', 's': 'Hallway'}
   Where do you want to go? ('x' to exit)
``` 
If the player types `d`, the game should display:
``` 
   You don't have the key to enter this room.
   You are in the Bedroom.
   You can go: {'d': 'Bathroom', 's': 'Hallway'}
   Where do you want to go? ('x' to exit)
```
If the player is in the `Kitchen` and types `w`, trying to go `Outside` without collecting `Key 2`, the game should display:
```
   You don't have the key to enter this room.
   You are in the Kitchen.
   You can go: {'d': 'Hallway', 'w': 'Outside'}
   Where do you want to go? ('x' to exit)
```
- If the player is in the `Bedroom` and types `d` (assuming `Key 1` has already been picked up in the `Hallway`), the game should display:
```
   You are in the Bathroom.
   You found Key 2.
   You can go: {'a': 'Bedroom'}
   Where do you want to go? ('x' to exit)
```
- If the player types `k` (which is an invalid direction), the game should display:
```
   Invalid direction. Try again.
   You are in the Bathroom.
   You can go: {'a': 'Bedroom'}
   Where do you want to go? ('x' to exit)
```

- If the player collected the 2 keys, is in the `Kitchen` and types `w`, the game should display:
```
   You have escaped!
```

If the player types `x`, the game exits, and the game should display:
``` 
   Exited the game.
``` 

## Assignment Completion Procedures

You will complete and submit this assignment in a similar way to prior
assignments. To avoid cluttering up this README with the same instructions each
time, they have been broken out into a separate file. Please reference
[PROCEDURES.md](PROCEDURES.md) to see the details if you have forgotten.

In summary:

  1.  Complete the code for the assignment per the instructions
  2.  Run the script to test and debug
  3.  Execute the automated tests to ensure expected functionality

When finished, do not forget to:

  1.  Commit and Sync:
      - Switch to version control tab
      - Stage all changed files
      - _**Enter a commit message**_
      - Click Commit
      - Click Sync
  2. Validate your submission in GitHub
