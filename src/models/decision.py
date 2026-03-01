from typing import List, Dict, Optional, Union
from dataclasses import dataclass, field

@dataclass
class Criterion:
    name: str
    weight: float
    is_cost: bool = False  # True if lower is better (e.g. Price)
    description: Optional[str] = None

@dataclass
class Option:
    name: str
    values: Dict[str, Union[float, int, str]]  # Name of criterion -> Value

@dataclass
class DecisionRequest:
    domain: str
    criteria: List[Criterion]
    options: List[Option]
    constraints: Optional[Dict[str, Union[float, bool]]] = None

@dataclass
class ScoreBreakdown:
    criterion: str
    raw_value: float
    normalized_value: float
    weighted_score: float

@dataclass
class OptionResult:
    name: str
    total_score: float
    rank: int
    breakdown: List[ScoreBreakdown]
    is_eligible: bool = True
    reason: Optional[str] = None

@dataclass
class DecisionResult:
    domain: str
    results: List[OptionResult]
