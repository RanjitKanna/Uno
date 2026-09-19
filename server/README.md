# Color Clash Room Server

This directory is reserved for the authoritative online game server. It will own room membership, hidden hands, the deck, and turn validation.

Both LAN and public deployment run the same server. Configure its advertised address through `PUBLIC_BASE_URL`; see `../ONLINE_ROOMS.md` for the safe hosting options.

Before publishing a public room service, the server must be deployed behind HTTPS and given a persistent store for reconnection support. Do not use browser-only state for online card hands.
