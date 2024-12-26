# Root __init__.py

"""
Gantt Graph Process Algorithm App - A Python package for process scheduling visualization using Gantt charts.

This package provides tools for visualizing different process scheduling algorithms
through Gantt charts, making it easier to understand how various CPU scheduling
mechanisms work.
"""

from . import classes
from . import data
from . import ordannacement

# Module Exports
__all__ = [
    "classes",
    "data",
    "ordannacement",
]


# Package Metadata
__title__ = "Gantt Graph Process Algorithm App"
__version__ = "1.0.0"
__author__ = "Mouad Allaoui"
__author_email__ = "moadallaoui1@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2024 Mouad"
__description__ = "Process scheduling visualization using Gantt charts"
__url__ = "https://github.com/MouadALLAOUI/Gantt-Graph-Process-Algorithm-App"
__status__ = "Beta"  # Options: Development, Production, Beta

# Feature Flags
__experimental_features__ = {
    "srtf coop": True,
    "srtf prem": True,
    "fifo coop": True,
    "fifo prem": True,
    "round-robin coop": True,
    "round-robin prem": True,
}

# Configuration Defaults
__default_config__ = {
    "time_quantum": 2,  # Default time quantum for Round Robin
    "visualization_style": "standard",  # Options: standard, detailed
    "debug_mode": False,
}

# Package Requirements
__python_requires__ = ">=3.0"
__dependencies__ = [
    "matplotlib>=3.0.0",
    "random",
]


def get_version():
    """Return the package version as a string."""
    return __version__


def get_config():
    """Return the default configuration dictionary."""
    return __default_config__.copy()


def is_feature_enabled(feature_name):
    """Check if a specific feature is enabled."""
    return __experimental_features__.get(feature_name, False)


# Version information split for programmatic use
VERSION = tuple(map(int, __version__.split(".")))
