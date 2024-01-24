import functools
from dataclasses import dataclass

from items_base import ParaboxItemInfo, ParaboxItemGenerator


@dataclass(frozen=True)
class KeyDefinition:
    name: str
    symbol: str
    id: int


@dataclass(frozen=True)
class KeyItemDefinition(KeyDefinition):
    pass


key_definitions = [
    KeyDefinition("Alpha", "α", 1),
    KeyDefinition("Beta", "β", 2),
    KeyDefinition("Gamma", "γ", 3),
    KeyDefinition("Delta", "δ", 4),
    KeyDefinition("Zeta", "ζ", 5),
    KeyDefinition("Eta", "η", 6),
    KeyDefinition("Theta", "θ", 7),
    KeyDefinition("Iota", "ι", 8),
    KeyDefinition("Kappa", "κ", 9),
    KeyDefinition("Lambda", "λ", 10),
    KeyDefinition("Mu", "μ", 11),
    KeyDefinition("Nu", "ν", 12),
    KeyDefinition("Xi", "ξ", 13),
    KeyDefinition("Omikron", "ο", 14),
    KeyDefinition("Pi", "π", 15),
    KeyDefinition("Rho", "ρ", 16),
    KeyDefinition("Sigma", "σ", 17),
    KeyDefinition("Tau", "τ", 18),
    KeyDefinition("Upsilon", "υ", 19),
    KeyDefinition("Phi", "φ", 20),
    KeyDefinition("Chi", "χ", 21),
    KeyDefinition("Psi", "ψ", 23),
    KeyDefinition("Omega", "ω", 24)
]

key_name_to_symbol = {k.name: k.symbol for k in key_definitions}


@dataclass(frozen=True)
class KeyItemGenerator(ParaboxItemGenerator):
    start_id: int

    @functools.cached_property
    def items(self) -> list[ParaboxItemInfo]:
        return [ParaboxItemInfo(k.name, k.id) for k in self.definitions]

    @functools.cached_property
    def definitions(self) -> list[KeyItemDefinition]:
        return [KeyItemDefinition(f"{k.name} Key", k.symbol, self.start_id + k.id) for k in key_definitions]
