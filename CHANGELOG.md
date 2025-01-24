## Changelog

- Updated project structure and CMake settings (read more at build specific changes)
- Revised unpredicted behavior ``All player getters on both sides will now return null if player isn't created/spawned``: these getters should return an empty string if player isn't created/spawned

### Build specific changes

- Project has been split into separate logical directories (docs, python, build, source)
- Added LICENSE (usual free software license)
- CMake config was split to logical files for better readabilty
- Added README.md and LICENSE for NoNut directory
- Removed unused toolchain files and build presets
- Added short ``How to build`` section to README.md