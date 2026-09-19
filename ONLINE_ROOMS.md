# Online Rooms Configuration

Color Clash supports the same room rules in two hosting modes. In both, the room host chooses a maximum of 2–4 players; the server refuses further joins after that limit.

## LAN mode

Use this when everyone is on the same Wi-Fi or local network.

1. Start the room server on the host computer.
2. Choose **LAN** when creating a room.
3. Share the generated network address with friends on that network.

No third party is needed, but the host computer must remain on while the game is being played.

## Public mode

Use this when friends are joining from different networks.

1. Deploy the same room server to a public host, or expose it with an approved secure tunnel.
2. Set the server's `PUBLIC_BASE_URL` to its public HTTPS address.
3. Choose **Public** when creating a room and share the generated invite link.

Do not expose an unprotected home-computer port directly to the internet. A hosting provider or secure tunnel handles HTTPS and inbound access safely.

## Server settings

| Setting | LAN example | Public example |
| --- | --- | --- |
| `PORT` | `8080` | hosting provider's assigned port |
| `BIND_ADDRESS` | `0.0.0.0` | provider default |
| `PUBLIC_BASE_URL` | `http://192.168.1.25:8080` | `https://cards.example.com` |
| `MAX_PLAYERS` | host chooses 2–4 per room | host chooses 2–4 per room |

The client and server use the same room protocol in either configuration, so a room can never mix LAN and public invite links accidentally.
