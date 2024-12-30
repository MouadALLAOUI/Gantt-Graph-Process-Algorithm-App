# Changelog
All notable changes to Gantt Graph Process Algorithm App will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-12-29
### Added
- add gui using pyqt5
- add AppGui classes for gui
### Fixed
- fix bug with infinite loop in rrc
- fix some simple algorithme
- fix test data generation
- fix some error handling

## [1.0.0] - 2024-12-26
### Added
- Initial release of Gantt Graph Process Algorithm App
- Core scheduling algorithms:
    - First In First Out (FIFO)
    - Round Robin (RR)
    - Shortest Remaining Time First (SRTF)
- Process visualization using Gantt charts
- Multiple data input methods:
    - Console input
    - CSV file import
    - Test dataset integration
- Basic project structure with modular design
- Documentation:
  - README.md
  - LICENSE (MIT)
  - Initial CHANGELOG

### Under Development
- fixing algorithme bugs

## [Unreleased]
### Planned Features
- Gui saving prossess
- Export functionality for Gantt charts
- Additional scheduling algorithms:
    - Multi-level Queue Scheduling
- Performance metrics calculation:
    - Average waiting time
    - Average turnaround time
    - CPU utilization

### Known Issues
- Limited error handling for invalid input data
- Visualization scaling issues with large datasets
- Some algorithme still show incorrect data

---
## Version History

### Version Format
- MAJOR version (X.0.0) - Incompatible API changes
- MINOR version (0.X.0) - Added functionality in a backward compatible manner
- PATCH version (0.0.X) - Backward compatible bug fixes

### Version Numbers
- v1.0.0 - Initial Release
- Future versions will be listed here

---
## How to Update This Changelog

1. List changes in reverse chronological order (newest on top)
2. Use the following categories:
   - `Added` for new features
   - `Changed` for changes in existing functionality
   - `Deprecated` for soon-to-be removed features
   - `Removed` for now removed features
   - `Fixed` for any bug fixes
   - `Security` for vulnerability fixes

3. Always include:
   - Version number
   - Release date
   - List of changes
   - Any relevant links or references

---