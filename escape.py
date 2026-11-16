# House map
#             |----------|-----------|
# (unlock w/  |          | (unlock w/| 
#     Key 2)  |          |   Key 1)  | 
#     Outside | Bedroom  X Bathroom  | 
#             |          |   *Key 2* |
#   |----X----|---    ---|-----------|
#   |         |          |
#   | Kitchen   Hallway  | 
#   |         |   *Key 1*| 
#   |---------|----------|

rooms = {
    "Bedroom": {"pathways": {"d": "Bathroom", "s": "Hallway"}, "open_with": ""},
    "Hallway": {"pathways": {"w": "Bedroom", "a": "Kitchen"}, "open_with": ""},
    "Bathroom": {"pathways": {"a": "Bedroom"}, "open_with": "Key 1"},
    "Kitchen": {"pathways": {"d": "Hallway", "w": "Outside"}, "open_with": ""},
    "Outside": {"pathways": {"s": "Kitchen"}, "open_with": "Key 2"},
}

pickable_objects = {
    "Key 1": {"location": "Hallway", "picked": False},
    "Key 2": {"location": "Bathroom", "picked": False}
}

START_LOCATION = "Bedroom"

def print_location(location: str) -> None:
    """
    Print the description of the current location.
    
    Update this function to check whether the room exists in the rooms dictionary.
    
    If the room exists, print the current location (e.g., "You are in the Kitchen.")
    
    Otherwise, print "Unknown location."
    """
    if location in rooms:
        print(f"You are in the {location}.")
    else:
        print("Unknown location.")
        
def get_directions(location: str) -> dict[str, str]:
    """
    Return possible directions to move from the current location.
    
    Update this function to read the pathways from the dictionary and return
    the pathways dictionary without printing.
    
    Example return value: {'d': 'Hallway', 'w': 'Outside'}
    
    If the room is unknown, return an empty dict: {}
    """
    return rooms.get(location, {}).get("pathways", {})

def find_room_by_direction(location: str, direction: str) -> str:
    """
    Determine the new location based on the current location and direction.
    
    Modify this function to search the dictionary for the next room to navigate to based
    on the current location and direction provided.
    
    Return the new location after moving in the specified direction.
    
    If the current location is unknown, print "Unknown location." and return the
    original location. If the direction is invalid, print an error message and
    return the current location.
    """
    if location not in rooms:
        print("Unknown location.")
        return location
    pathways = rooms.get(location, {}).get("pathways", {})
    if direction in pathways:
        return pathways[direction]
    else:
        print("Invalid direction. Try again.")
        return location

def has_key_for_room(room_id: str) -> bool:
    """
    Check if the player has the key to enter a specified room.
    
    Modify this function to consult the rooms and pickable_objects dictionaries to
    determine whether the destination room requires a key and if that key has been picked.
    
    Return True if the player can enter the room, False otherwise.
    """
    if room_id not in rooms:
        return False
    required_key = rooms.get(room_id, {}).get("open_with", "")
    if required_key == "":
        return True
    if required_key in pickable_objects:
        return pickable_objects[required_key]["picked"]
    return False
    
def explore_room(location: str) -> None:
    """
    Handle picking up objects in the current room.

    This function checks the current room against the `pickable_objects`
    dictionary. If an unpicked object is located in the room, it marks that
    object as picked and prints the corresponding "You found <Key>." message.
    
    If there is no matching object, or it was already picked up, the function
    should do nothing.
    
    Modify this function to search the pickable_objects dictionary. When the player
    enters a room containing an unpicked key, update the `picked` flag to True and
    print the message indicating the key was found. This should work through the
    dictionary data rather than hardcoded room checks.
    """
    for key, info in pickable_objects.items():
        if info["location"] == location and not info["picked"]:
            info["picked"] = True
            print(f"You found {key}.")
    

def game_loop(location: str) -> None:
    """
    Main game loop handling room navigation.
    Parameters:
    location (str): The starting location of the player.
    The function continuously prints the current location, retrieves possible directions,
    and prompts the player to choose a direction to move. The loop continues until the 
    player decides to exit by entering 'x'. The location is updated based on the player's 
    chosen direction.
    The function relies on the following helper functions:
    - print_location(location): Prints the current location.
    - get_directions(location): Retrieves possible directions from the current location (no printing).
    - The game loop is responsible for printing: "You can go: {<pathways dict>}" using the value returned by get_directions.
    - find_room_by_direction(location, chosen_direction): Finds the next room based on the current location and chosen direction.
    When the player exits, a message "Exited the game." is printed.
    """
    while True:    
        print_location(location)
        explore_room(location)
        available_directions = get_directions(location)
        print(f"You can go: {available_directions}")
        chosen_direction = input("Where do you want to go? ('x' to exit) ").lower()
        if chosen_direction  == 'x':
            print("Exited the game.")
            break
        
        next_room = find_room_by_direction(location, chosen_direction)
        if has_key_for_room(next_room):
            location = next_room
        else:
            print("You don't have the key to enter this room.")
        
        if location == "Outside":
            print("You have escaped!")
            break


def start_game() -> None:
    """
    Start the game.

    This function initializes the Escape Game by printing the game title to the console.
    It serves as the entry point for the game.
    """

    print("Escape Game")

if __name__ == "__main__":
    start_game()
    game_loop(START_LOCATION)
