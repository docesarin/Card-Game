# Relancinho

## Overview
This project is a **Card Matching Game** named **Relancinho**, developed as part of a college assignment. The goal was to create a simple yet functional game that demonstrates the use of **lists**, **queues**, and **stacks** in Python. The game provides a fun and interactive way to practice data structure concepts.

## Gameplay
The game is based on the concept of forming **sets of three cards** (trincas) using the following rules:
- A set of three cards with the **same value** but **different suits**.
- A sequential set of three cards (e.g., 3, 4, 5) with the **same suit**.

### How to Play:
1. Each player starts with **6 cards** in hand.
2. Players take turns to:
   - Pick a card from the **deck** or the **discard pile**.
   - Discard a card from their hand to the discard pile.
3. Players attempt to form valid **trincas** with their cards.
4. The first player to have **no cards** left in their hand wins the game.

## Features
1. **Deck and Hand Management:**
   - The deck is implemented as a **list**, shuffled at the beginning of the game.
   - Players' hands are represented as lists, with operations to add, remove, and organize cards.

2. **Discard Pile:**
   - The discard pile is implemented as a **stack**, where players add and retrieve cards from the top.

3. **Turn Queue:**
   - Player turns are managed using a **queue**, ensuring a fair turn order.

## How It Works
### Data Structures Used:
- **List:**
  - To represent the deck and players' hands.
  - To check and organize cards into trincas.

- **Queue:**
  - To maintain the turn order of players.
  - Implemented using `collections.deque` for efficient operations.

- **Stack:**
  - To manage the discard pile.
  - Players can only interact with the top card.

--

** |\---/| 
** |     | 
**  \_ _/ doce sarin.
