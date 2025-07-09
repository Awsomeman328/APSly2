# Sly 2: Band of Thieves Archipelago
An archipelago implementation of Sly 2.

## What does randomization do in this game?
Each gadget and chapter of each episode is shuffled into the item pool, and optionally the bottles as well. The checks are completing jobs, collecting treasures, opening the vaults, purchasing items from ThiefNet, and optionally collecting bottles.

**Additional features include:**
- The ability to skip video cutscenes by pressing the X button.

## Setup

### Requirements
In order to play the Sly 2 Archipelago randomizer, you need:

- [Archipelago Multiworld Randomizer](https://github.com/ArchipelagoMW/Archipelago/releases).
- [The Sly 2 apworld](https://github.com/NikolajDanger/APSly2/releases).
- [PCSX2](https://pcsx2.net/downloads/). Must be v1.7 or higher.
- A Sly 2 US ISO (`SCUS-97316`).

### PCSX2 Settings
Enable PINE in PCSX2
- In PCSX2, under `Tools`, check `Show Advanced Settings`.
- In PCSX2, `System -> Settings -> Advanced -> PINE Settings`, check `Enable` and ensure `Slot` is set to `28011`.

### Playing a game
1. Start the game in PCSX2.
2. Start the Sly 2 client from the Archipelago launcher, and connect to the multiworld.
3. Ensure that the "Press START ..." message has changed before playing.
4. Start a new game.

## Skipping the intro
You can skip the intro with the `\menu` command in the client. This might disable saving, so refer to "There's no "save and quit" option in the pause menu" in the Troubleshooting section.

## Skipping Cutscenes
I recommend using [this patch](https://github.com/andshrew/Sly2-Cutscene-Skip/tree/main) to enable cutscene skipping.

## Troubleshooting
### The client won't connect to my PCSX2 instance
Make sure you have PINE enabled and that you're playing the US version of the game.

### I'm stuck in the tutorial
Type `/menu` command in the client and you should be taken to the menu.

### There's no "save and quit" option in the pause menu
You can save the game manually in Options.

## Acknowledgment
This project was heavily inspired by and built upon the structure and PINE code from [Evilwb's Archipelago Ratchet and Clank 2 implementation](https://github.com/evilwb/APRac2).
