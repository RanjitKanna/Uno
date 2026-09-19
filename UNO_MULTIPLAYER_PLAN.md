# Multiplayer UNO Game — Plan

## Goal

Create a friendly browser-based UNO-style card game that supports 2–4 players, beginning with local multiplayer and growing into online rooms.

## Game modes

### Local multiplayer (first version)

- Two to four people take turns on one device.
- Each player has a hand of cards; only the active player's hand is visible.
- The game includes number cards, Skip, Reverse, Draw Two, Wild, and Wild Draw Four.
- Players can draw, play a valid card, choose a colour after a Wild card, call UNO with one card left, and start a new round.
- The game tracks points and declares a round winner.

### Online multiplayer (next version)

- A player creates a private room and shares a short room code or invite link.
- Other players join the room from their own browser.
- The server, rather than the browser, validates turns, card rules, deck order, scores, and winners.
- Reconnecting a player can restore their hand and turn state.

### Hosting configurations

- **LAN:** the host runs the room server on their computer and shares its local-network invite address.
- **Public:** the identical server is deployed or exposed through a secure HTTPS tunnel; invite links use the configured public address.
- In both modes, the host selects a room capacity from 2–4 players at room creation. The server rejects extra join requests.

## Suggested technology

| Area | First version | Online version |
| --- | --- | --- |
| Interface | HTML, CSS, and JavaScript | React or the existing interface, if preferred |
| Game rules | Browser-side JavaScript | Shared rules module plus server validation |
| Multiplayer | Pass-and-play on one device | Node.js server with Socket.IO or WebSockets |
| Rooms and scores | Browser storage | Server memory for prototypes; database for persistent games |

## Core rules

1. Deal seven cards to every player and place one card in the discard pile.
2. A player may play a card matching the top card's colour, number, or symbol, or play a Wild card.
3. If no card can be played, the player draws a card; they may play it immediately if it is valid.
4. Skip skips the next player; Reverse changes direction; Draw Two makes the next player draw two and lose their turn.
5. Wild changes the active colour; Wild Draw Four changes the active colour and makes the next player draw four.
6. A player must call UNO when reducing their hand to one card. The first player with no cards wins the round.

## Build order

1. Create the game table, card component, start screen, player panel, discard pile, and draw pile.
2. Build the deck, shuffle/deal flow, turn rotation, playable-card checks, draw action, and scoring.
3. Add each action card and the colour-picker interaction.
4. Add local pass-and-play privacy screens so the next player can safely reveal their own hand.
5. Add accessible keyboard controls, touch-friendly controls, and a responsive layout.
6. Add online rooms only after local rules are complete and tested.
7. Test turns, action cards, edge cases, joining/leaving rooms, reconnection, and invalid moves.

## Online safety and fairness

- Never send another player's cards to a client.
- Keep deck shuffling and rule validation on the server.
- Treat every client action as a request, not a trusted result.
- Use room IDs that are difficult to guess and clean up abandoned rooms.

## Definition of done for the first version

- 2–4 people can complete a local round.
- Every listed card type behaves correctly.
- A player cannot play an invalid card or act out of turn.
- The game works on desktop and phone-sized screens.
- The game can be restarted without refreshing the page.
