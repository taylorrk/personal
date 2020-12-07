"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from typing import List
from random import random
from projects.disease_tracer import constants
from math import sin, cos, pi, sqrt


__author__ = "730322626"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Computes the distance between two points."""
        distance: float = sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Increments the infected by 1."""
        self.location = self.location.add(self.direction)
        # incremement alinfected cells sickness attr by 1
        # do i immunize

    def contract_disease(self) -> None:
        """Assigns cells to the infected constant."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns a bool if cell is vulernable."""
        if self.sickness == constants.VULNERABLE:
            return True 
        else: 
            return False
    
    def is_infected(self) -> bool:
        """Returns a bool if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "red"
        elif self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "blue"
  
    def contact_with(self, other: Cell) -> None:
        """Checks the infected state of two cells."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        if other.is_vulnerable() and self.is_infected():
            other.contract_disease()

    def immunize(self) -> None:
        """Assigns cells to the immune constant."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns a bool if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0
    default_value: int = 0

    def __init__(self, cells: int, speed: float, start_infected: int, start_immune: int = default_value):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if start_infected >= cells or start_infected <= 0:
            raise ValueError("some number of the Cell objects must be infected")
        elif start_immune >= cells or start_immune < 0:
            raise ValueError("some number of the Cell objects must be infected")
        else: 
            for _ in range(0, cells): 
                start_loc = self.random_location()
                start_dir = self.random_direction(speed)
                self.population.append(Cell(start_loc, start_dir))
            i: int = 0
            for _ in range(0, start_infected):
                self.population[i].sickness = constants.INFECTED
                i += 1
          
    def check_contacts(self) -> None:
        """Checks if two cells come in contact."""
        i: int = 0
        j: int = 1
        while i < len(self.population):
            while j < len(self.population):
                if Point.distance(self.population[i].location, self.population[j].location) < constants.CELL_RADIUS:
                    Cell.contact_with(self.population[i], self.population[j])
                j += 1
            i += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False