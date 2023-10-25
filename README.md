# First Game with Pygame

Welcome to this simple 2-player spaceship game developed using the Pygame library. The aim of the game is to reduce the health of the opposing player's spaceship by shooting bullets. The player whose spaceship's health goes down to zero first loses.

## Features:
- 2-player controls.
- Shooting mechanism with bullet limit.
- Dynamic health system.
- Winner announcement.
- Background music and sound effects.

## Game Controls:

### Player 1:
- **W**: Move Up
- **A**: Move Left
- **S**: Move Down
- **D**: Move Right
- **LCTRL**: Shoot

### Player 2:
- **Arrow Up**: Move Up
- **Arrow Left**: Move Left
- **Arrow Down**: Move Down
- **Arrow Right**: Move Right
- **RCTRL**: Shoot

## Assets Used:
The game utilizes several assets including background music, shooting sounds, and spaceship images. Make sure to have the "Assets" folder in the same directory as the game script, containing:
- `mixkit-electronic-retro-block-hit-2185.wav`: Sound for bullet hit.
- `mixkit-explainer-video-game-alert-sweep-236.wav`: Sound for bullet fire.
- `mixkit-arcade-mechanical-bling-210.wav`: Winning announcement sound.
- `digital-love-127441.mp3`: Background music.
- `ship1.png`: Image of Player 1's spaceship.
- `ship2.png`: Image of Player 2's spaceship.
- `background2.png`: Background space image.

## Installation and Running:
Ensure you have `pygame` installed. If not, install it using:

```bash
pip install pygame
