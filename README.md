# Kuramoto Fireflies Simulation

This project simulates the synchronization behavior of fireflies using the Kuramoto model, a conceptual framework used to study the synchronization of coupled oscillators. The simulation is implemented in Python using the Pygame library, providing a visual representation of the fireflies' flashing patterns as they interact with each other.

<!--  gif from giphy -->
![Fireflies](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDQzam42OWJueW1lc3p1OXBiaWVrbjg2ZDlxMGV4bThlcGFzdTZyayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/b2PXZ16BAi836HYbUP/giphy.gif)

## Getting Started

To run the Kuramoto Fireflies simulation, you'll need to have Python installed on your system along with the Pygame library.

### Prerequisites

- Python 3.6 or later
- Pygame

### Installation

First, make sure you have Python installed.

Next, install Pygame using pip:

```bash
pip install pygame
```

### Running the Simulation

With Python and Pygame installed, you can run the simulation by executing the script:

```bash
python Kuramato_pygame.py
```

This will open a window displaying the simulation of the fireflies. The fireflies will move around the screen and flash with a certain frequency. Over time, you'll observe them synchronizing their flashing, a phenomenon inspired by the real-world behavior of fireflies.

## Simulation Details

- `NUM_FIREFLIES`: The number of fireflies in the simulation.
- `FLY_CLOCK_SPEED`: The base speed at which a firefly's internal clock progresses.
- `FLY_RADIUS`: The radius within which fireflies influence each other's clock speed.
- `FLY_PULL`: The strength of the pull fireflies exert on each other to synchronize.
- `FLY_SYNC`: A boolean indicating whether fireflies are trying to synchronize.

## Firefly Behavior

Each firefly is represented as a point on the screen with its own phase and frequency. The fireflies influence each other within a certain radius (`FLY_RADIUS`), nudging their neighbors' phases to be closer to their own.

## Controls

There are no interactive controls for this simulation; it's purely observational. Watch as the patterns emerge and change over time as the fireflies come into sync and then drift apart again.

## License

This project is dedicated to the public domain under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

## Acknowledgements

- The Kuramoto model and its application to firefly synchronization is a well-studied phenomenon in complex systems and nonlinear dynamics.
- This simulation is inspired by the collective behavior of fireflies and is meant for educational and entertainment purposes.
- Inspired by the work of Steven Strogatz and other researchers in the field of synchronization.
- Implementation inspired by this repository [Fireflies](https://github.com/ncase/fireflies) by Nicky Case. 
- link to the original [Kuramoto model](https://en.wikipedia.org/wiki/Kuramoto_model)
- link to interactive and educational simulation [Fireflies](https://ncase.me/fireflies/) by Nicky Case.
- YT video [Fireflies](https://youtu.be/ZGvtnE1Wy6U?si=LDekwMowxBP3XCYb&t=54) by user 'robin meier'.

Feel free to adjust the content to better fit your project's specifics or to add more details if necessary.