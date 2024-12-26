#  premtif __init__.py

from .fifo import Fifo_Prem
from .round_robin import Round_Robin_Prem
from .srtf import SRTF_Prem

__all__ = ["Fifo_Prem", "Round_Robin_Prem", "SRTF_Prem"]
