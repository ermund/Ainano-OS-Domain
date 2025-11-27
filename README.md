# Ainano OS Domain

Ainano OS uses its own private domain, `.-e`, where every device becomes a server in a self-hosted mesh. The ecosystem resolves ainano.-e without public DNS, creating a unified, secure, and distributed namespace that travels with every Ainano-powered device.

This repository collects the domain tooling, reference implementations, docs and examples for the Ainano domain and mesh ecosystem.

## Key ideas

- Private top-level domain: `.-e` — resolved locally across the mesh without public DNS.
- Each device runs a lightweight node/agent that advertises a stable ainano hostname (e.g. `device123.ainano.-e`) and offers services over HTTP(s).
- Mesh routing and service discovery are self-hosted and encrypted — no dependency on public resolvers.
- Goal: portable namespace that "travels" when devices change network.

## Quickstart (development)

Requirements:
- Python 3.10+
- pip

Install from repository (editable):
```sh
pip install -e .
```

Run a minimal example node (example in `examples/ainano_node.py`):
```sh
python3 examples/ainano_node.py --name mydevice
```

Then, from another terminal on the same machine/network:
```sh
curl http://localhost:8080/.well-known/ainano
```

This example runs a local HTTP endpoint that demonstrates how a node advertises its presence. It is intentionally minimal — see docs/architecture.md for the full design and later steps to integrate real mesh discovery.

## Repo layout

- README.md — this document
- examples/ — runnable example nodes and utilities
- docs/ — architecture and design documents
- ainano/ — core library (to be filled with the full implementation)
- tests/ — unit and integration tests

## Architecture (summary)

1. Local discovery
   - Nodes discover each other on local link using mDNS / multicast or a pluggable transport.
2. Name system
   - The `.-e` TLD is resolved by the Ainano resolver running on each device. The resolver maintains an overlay namespace mapping hostnames to reachable addresses.
3. Secure channels
   - Nodes establish mutually authenticated encrypted connections (e.g., TLS with device keys).
4. Routing & mesh
   - Lightweight peer-to-peer routing to forward requests across the mesh when direct connectivity is unavailable.

See docs/architecture.md for a longer description and design considerations.

## Roadmap / next steps

Short term:
- Implement the ainano resolver library and local agent.
- Add CLI to manage device identity and keys.
- Integrate a simple DHT or gossip for namespace replication.

Medium term:
- Implement secure peer transport and NAT traversal.
- Add tests, CI, packaging and example deployments (containers).

Long term:
- Production-grade mesh with auto-updating agents and resilient routing.

## Contributing

See CONTRIBUTING.md — the project welcomes help across coding, docs, and security review.

## License

MIT (or your preferred license)