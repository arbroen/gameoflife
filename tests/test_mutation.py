# -*- coding: utf8 -*-
from shine_on_life.worlds import CellTypes
from shine_on_life.mutation import cell_lives, cell_spawns


class TestCycleConditions:
    def test_cell_stays_alive(self):
        assert not cell_lives(cycle=CellTypes.ALIVE, count=1)
        assert cell_lives(cycle=CellTypes.ALIVE, count=3)
        assert cell_lives(cycle=CellTypes.ALIVE, count=2)
        assert not cell_lives(cycle=CellTypes.ALIVE, count=4)

        assert not cell_lives(cycle=CellTypes.SPAWNED, count=1)
        assert cell_lives(cycle=CellTypes.SPAWNED, count=3)
        assert cell_lives(cycle=CellTypes.SPAWNED, count=2)
        assert not cell_lives(cycle=CellTypes.SPAWNED, count=4)

        assert not cell_lives(cycle=CellTypes.DEAD, count=1)
        assert not cell_lives(cycle=CellTypes.DEAD, count=3)
        assert not cell_lives(cycle=CellTypes.DEAD, count=2)
        assert not cell_lives(cycle=CellTypes.DEAD, count=4)

    def test_cell_spawns_life(self):
        assert not cell_spawns(cycle=CellTypes.DEAD, count=2)
        assert cell_spawns(cycle=CellTypes.DEAD, count=3)
        assert not cell_spawns(cycle=CellTypes.DEAD, count=4)

        assert not cell_spawns(cycle=CellTypes.ALIVE, count=2)
        assert not cell_spawns(cycle=CellTypes.ALIVE, count=3)
        assert not cell_spawns(cycle=CellTypes.ALIVE, count=4)

        assert not cell_spawns(cycle=CellTypes.SPAWNED, count=2)
        assert not cell_spawns(cycle=CellTypes.SPAWNED, count=3)
        assert not cell_spawns(cycle=CellTypes.SPAWNED, count=4)
