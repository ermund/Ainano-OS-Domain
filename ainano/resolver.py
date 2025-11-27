"""Resolver stubs for Ainano domain.

This module contains minimal classes to be extended: an in-memory resolver and
an agent interface used by the example.
"""
from typing import Dict, Optional

class InMemoryResolver:
    def __init__(self):
        self._store: Dict[str, str] = {}

    def register(self, name: str, addr: str):
        """Register a name -> address mapping."""
        self._store[name] = addr

    def resolve(self, name: str) -> Optional[str]:
        return self._store.get(name)


class Agent:
    def __init__(self, name: str, addr: str, resolver: InMemoryResolver):
        self.name = name
        self.addr = addr
        self.resolver = resolver

    def advertise(self):
        self.resolver.register(self.name, self.addr)