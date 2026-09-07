"""Assistant routing layer.
Routes user requests through available capabilities.
"""

from dataclasses import dataclass


@dataclass
class RouteDecision:
    mode: str
    use_rag: bool = True
    use_memory: bool = True


def route_request(prompt: str) -> RouteDecision:
    """Basic deterministic router prepared for future classifiers."""
    text = prompt.lower()

    knowledge_terms = ["explain", "what", "how", "why", "define"]
    use_rag = any(term in text for term in knowledge_terms)

    return RouteDecision(
        mode="knowledge" if use_rag else "chat",
        use_rag=use_rag,
        use_memory=True,
    )
