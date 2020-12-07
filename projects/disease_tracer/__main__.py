"""This specially named module makes the package runnable."""

from projects.disease_tracer import constants
from projects.disease_tracer.model import Model
from projects.disease_tracer.ViewController import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.START_INFECTED, constants.START_IMMUNE)
    vc = ViewController(model)
    vc.start_simulation()


if __name__ == "__main__":
    main()