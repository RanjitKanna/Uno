# Skyline Sprint — Build Plan

## Goal

Ship a small, polished, single-page browser game that works without a build step or external services.

## Experience

Players pilot a neon skimmer through a shifting city corridor. They move left and right to collect energy shards, avoid drones, and survive as the pace rises. A short run, responsive controls, and a local best score make it replayable.

## Scope

1. Build a responsive canvas-based game with an accessible HTML interface.
2. Provide keyboard, pointer/touch, and on-screen controls.
3. Add collision detection, scoring, progressive difficulty, pause/restart, and locally saved best score.
4. Use CSS and canvas rendering for the visual language so the game remains self-contained.
5. Verify the complete flow in a live browser and record the results under `.logs/`.

## Completion checks

- The start screen explains the goal and controls.
- Starting, moving, collecting, colliding, pausing, and restarting all work.
- The layout remains usable on narrow screens.
- No external assets, network requests, or build tooling are required.
