# Repository Guidelines

## Project Structure & Module Organization
Keep the layout consistent so firmware, tooling, and references stay discoverable. Place production code in `src/`, with MCU modules under `src/firmware/` and desktop helpers in `src/host/`. Collect headers in `include/` and reusable patterns in `src/patterns/` using `pattern_<behavior>.c`. Mirror the code tree in `tests/` (`tests/patterns/test_rainbow.c`, `tests/host/test_cli.py`). Store pinouts and BOMs in `hardware/` and place design docs in `docs/`. Add directories proactively when introducing new features.

## Build, Test, and Development Commands
Standardize on the Makefile targets below (add or update them when tooling changes):
- `make setup` installs toolchains, Python deps, and udev rules for flashing.
- `make build` compiles firmware and stores artifacts in `build/`.
- `make flash` uploads the latest binary to the connected board.
- `make monitor` opens the serial console with `miniterm`.
- `make test` runs host tests and firmware simulations in `tests/`.

## Coding Style & Naming Conventions
Run `clang-format` with the repo defaults before committing. Use 2-space indentation for C/C++ and 4 spaces for Python. Firmware functions and globals stay in `snake_case`, while structs and enums use `CamelCase`. Prefix hardware abstractions with their subsystem (`gpio_init_led()`, `timer_start_ms()`). Keep filenames lowercase: hyphens for Python utilities (`led-cli.py`) and underscores for C modules (`pattern_wave.c`). Execute `make lint` (wrapping `clang-tidy` and `ruff`) prior to pushing.

## Testing Guidelines
Keep fast unit tests near the code they cover and mirror firmware behavior with host simulations. Name files `test_<module>.c` or `test_<feature>.py`. Target ≥80% coverage for host utilities and capture at least one hardware-in-the-loop run for every new blink pattern in `tests/hitl/README.md`. Note fixtures (boards, sensors). Run `make test` and any relevant `make hitl` targets before opening a PR.

## Commit & Pull Request Guidelines
Follow Conventional Commits (`feat:`, `fix:`, `docs:`) with present-tense subjects under 72 characters and squash WIP changes locally. Each PR must outline the behavior change, link issues, list executed commands, and include photos or clips showing the pattern on hardware. When firmware touches timing or power, paste the measured data. Request review from a firmware maintainer and wait for CI to pass before merging.

## Hardware & Configuration Tips
Record board settings in `configs/<board>/config.mk` and load them with `make build BOARD=<board>`. Keep `.env.example` current with USB vendor IDs and tooling environment variables. When adding LED assemblies, update `hardware/pinout.md` and store calibration constants in `configs/`. Document manual calibration steps in `docs/calibration.md` so others can reproduce measurements.
