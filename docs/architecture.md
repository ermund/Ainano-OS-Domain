# Ainano Domain Architecture

This document outlines the high-level architecture for the Ainano private domain and mesh.

1) Local discovery

Nodes should be able to find nearby peers without central coordination. Options include:
- mDNS / multicast for local links
- UDP-based peer discovery
- A pluggable transport interface so non-local discovery (Bluetooth, other overlays) can be used

2) Namespace & resolver

Each device exposes one or more stable hostnames under the ainano.-e TLD. Resolvers on each device maintain a mapping of names to current addresses. The resolver is designed to be:
- Private: Not registered on public DNS
- Replicated: Namespace entries propagate via gossip or DHT
- Consistent enough for service discovery

3) Security

Devices should authenticate peers and encrypt traffic. Initial designs:
- Each device has an identity keypair (Ed25519 / X25519 for key agreement)
- TLS or Noise protocol for encrypted channels
- Optional PKI or web-of-trust for verifying hostnames

4) Routing & mesh

When direct connectivity is impossible, nodes can forward requests through other peers. Components:
- Lightweight peer routing tables
- Relay nodes and NAT traversal helpers (STUN/TURN as optional)

5) Implementation plan

Start with a Python reference implementation that provides:
- A resolver library with pluggable backends (in-memory, gossip/DHT)
- A local agent that runs discovery, serves the resolver API, and exposes an HTTP control endpoint
- Example nodes and integration tests that simulate multiple devices on a single machine