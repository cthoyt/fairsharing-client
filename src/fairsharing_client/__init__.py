# -*- coding: utf-8 -*-

"""A client to the FAIRsharing API."""

from .api import FairsharingClient, ensure_fairsharing, get_fairsharing_to_orcids, load_fairsharing

__all__ = [
    "load_fairsharing",
    "ensure_fairsharing",
    "FairsharingClient",
    "get_fairsharing_to_orcids",
]
