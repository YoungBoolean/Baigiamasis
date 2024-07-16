# Koshmaras

**Version 0.0.1**

Koshmaras Game is an interactive game that guides the player through a series of immersive scenes, making choices that affect the game's outcome.

## Game Genre
- Story-based
- Hardcore
- Creepy
- 2D
- Multiple-choice

## About the Game
The game was written in Python using the pygame library. It also uses SQLAlchemy to store user save data in a database. At this moment, it serves as a demo to showcase its functionality and to demonstrate the creator's coding skills.

## Features
- **Immersive Storyline**: Follow a gripping narrative that unfolds based on the choices you make.
- **Multiple Endings**: Different choices lead to different outcomes, providing replay value.
- **Perma Death**: If you die, your current character's save games are permanently deleted.
- **Resolution Changes**: Seamlessly change the game's resolution from the main menu. All calculations such as collisions, map point markers, character movement, buttons, backgrounds, or text will accommodate the change.
- **2D Animations**: Includes moving backgrounds, shadows, moving clouds, character walking, and button animations.
- **Enemies That Chase the Character**: Enemies will try to catch you while on the world map. If they do, you're dead.
- **Enemies That Multiply**: Every 10 seconds, a new enemy will spawn and chase you, so think fast.
- **Object Collisions**: Implemented object collisions on the main map.
- **Enterable Locations**: You can walk around the main map and enter different locations.
- **Load Menu List of Saves**: The load menu will show all valid save files. If the character dies, their save files are deleted.
- **Seamless Loading and Saving**: Seamlessly save the game while playing, as well as load the most recent save, without exiting to the main menu.
- **Character Interaction**: Engage with various characters, each with their own backstories and motivations.
- **Dynamic Environments**: Explore richly detailed environments that change based on the game’s progression.
- **Puzzles**: Solve puzzles to progress further.
- **Soundtrack and Sound Effects**: Enjoy a beautiful soundtrack (not turned on yet), as well as sound effects that enhance the immersive experience.

## Requirements
- greenlet==3.0.3
- pygame==2.5.2
- SQLAlchemy==2.0.30
- typing_extensions==4.12.0

