# -------------------------------------------------------------------
# File Path: /DigitalDreamscape/main.py
# Description: This file serves as the entry point for the Digital Dreamscape game. 
# It handles game initialization, the main game loop, and event management.
# -------------------------------------------------------------------

import time
from game_core.state import GameState
from game_core.character import Character
from game_core.mission import MissionManager
from ui.cli import CLI

# -------------------------------------------------------------------
# Section 1: Game Initialization
# -------------------------------------------------------------------

def initialize_game():
    """Initialize the game by setting up the game state, player character, and missions."""
    print("Initializing Digital Dreamscape...")

    # Create an initial game state
    game_state = GameState()

    # Create the player character
    player = Character(name="Victor", abilities=['cosmic_manipulation', 'super_strength'])

    # Initialize the mission manager and set up the first mission
    mission_manager = MissionManager()
    mission_manager.load_initial_missions()

    # Initialize CLI or GUI based on the interface preference
    cli = CLI()

    print("Game Initialized Successfully.")
    return game_state, player, mission_manager, cli

# -------------------------------------------------------------------
# Section 2: Game Update Logic
# -------------------------------------------------------------------

def update_game(game_state, player, mission_manager, cli):
    """
    Update the game logic, handle missions, and interact with the player.
    This is the main loop that continuously runs, processing player input and game events.
    """
    print("Entering the Game Loop...")

    # Main game loop
    while game_state.is_running:
        # Get player input through CLI for now (could be GUI later)
        player_input = cli.get_player_input()

        # Handle different inputs like movement, combat, interaction, etc.
        if player_input == "explore":
            mission_manager.process_exploration(player)
        elif player_input == "combat":
            mission_manager.process_combat(player)
        elif player_input == "quit":
            game_state.is_running = False
        else:
            print(f"Unknown command: {player_input}")

        # Update game state as per player actions or events
        mission_manager.update_missions(game_state, player)

        # Add some delay to simulate real-time events
        time.sleep(1)

# -------------------------------------------------------------------
# Section 3: Event Handling
# -------------------------------------------------------------------

def handle_event(game_state, event_type, event_data):
    """Handles game events dynamically triggered by player actions or world state."""
    if event_type == "mission_complete":
        print(f"Mission '{event_data}' completed! Reward collected.")
        game_state.update_mission_progress(event_data)
    elif event_type == "character_death":
        print(f"Player {event_data} has been defeated.")
        game_state.is_running = False
    else:
        print(f"Event {event_type} triggered with data: {event_data}")

# -------------------------------------------------------------------
# Example Usage (Main Section)
# -------------------------------------------------------------------

if __name__ == "__main__":
    # Initialize the game
    game_state, player, mission_manager, cli = initialize_game()

    # Main update loop
    update_game(game_state, player, mission_manager, cli)
    
    # If game is over, exit
    print("Game Over. Thanks for playing!")
