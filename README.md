# shrewsbury-fll-ecoengineers
ECO Engineers' Pybricks SPIKE Prime base code.

This project is intended to be developed locally in VS Code, largely replacing day-to-day use of the Pybricks WebIDE; see [docs/pybricks_setup_for_vscode.md](docs/pybricks_setup_for_vscode.md) for setup instructions.

## Bee & Harvest Lab

Explore the interactive farm simulation on the [Bee & Harvest Lab website](https://shrewsbury-fll-eco-engineers.github.io/shrewsbury-fll-ecoengineers/).

GitHub Pages publishes only the simulation as the site homepage. To enable deployment, set **Settings → Pages → Build and deployment → Source** to **GitHub Actions**. Merging the deployment workflow to `main` publishes the site and future simulation updates.

## Files

| File | Purpose |
|---|---|
| `robot.py` | Robot configuration (ports, motor directions, wheel geometry, speeds, gyro) — the single source of truth used by every other file |
| `main.py` / `menu.py` | Startup and on-hub mission menu |
| `mission_*.py` | One file per mission |
| `xbox_controller.py` | Drive the robot with an Xbox controller; can record a path and print it as mission code |
| `recorded_mission.py` | Example path recorded with the Xbox controller |
| `port_test.py` | Diagnostic: reports which hub ports have a motor connected |
| `robot_check.py` | One-minute self-test: gyro, distance, turns, drift (PASS/CHECK results) |

## Robot configuration (lucky-chicken-2, verified 2026-09-27)

| Setting | Value |
|---|---|
| Drive motors | Left = Port B (`COUNTERCLOCKWISE`), Right = Port F (`CLOCKWISE`) |
| Attachment motors | Left = Port A, Right = Port E |
| Wheels | 56 x 28 mm black wheels; `AXLE_TRACK` 114 mm (best value from a 104-119 mm sweep; a ruler says 119 mm). The 56 x 14 blue wheels need 113 mm |
| Driving | Gyro-assisted, `STRAIGHT_ACCEL` 500, heading gain x8 |
| Gyro calibration | `HEADING_CORRECTIONS` in `robot.py`: lucky-chicken-2 = 363.7 (its gyro reads ~1% high); each hub needs its own value |
| Layout | Two rear drive wheels + front ball caster |

Sign convention: `straight(+)` drives **forward**, `turn(+)` turns **right** (clockwise).

Measured accuracy: 300 mm commanded = ~300 mm driven; 90° turns within 1°; 3 mm sideways drift over 3 m of forward/back driving.

**Keep the robot still for about 1 second after starting a program** — the gyro calibrates at startup.

## Xbox controller

| Input | Action |
|---|---|
| D-pad Up / Down | Drive forward / backward |
| D-pad Right / Left | Turn right / left in place |
| RB / LB | Left attachment motor forward / backward |
| Y | Start / stop recording (prints mission code when stopped) |
| A | Replay the last recording |

## Other robots

The configuration was calibrated on lucky-chicken-2. Before using another robot, run `robot_check.py` and the checks in [docs/pybricks_setup_for_vscode.md](docs/pybricks_setup_for_vscode.md) section 14.

## How we calibrated the robot

See [docs/robot_experiments.md](docs/robot_experiments.md) — the experiments, results, and fixes, written for students.
