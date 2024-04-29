# MarauBot 

Simple 2D robot model and simulation, based on Python and [Cairo](https://pypi.org/project/pycairo/) Librairy.

Project Components:

- MarauBotMap : Independant librairie
- maraubot_sim : ROS2 simulator

## Install

The _MarauBot_ packages relies on  [Cairo](https://pypi.org/project/pycairo/) and provide a ROS2 simulator.
It should be cloned into your ROS2 workspace.

```sh
cd Your/ROS2/workspace
git clone git@github.com:imt-mobisyst/pkg-maraubot.git
```

### MarauBotMap

`MarauBotMap` should be installed on your computer using `pip`.

```sh
pip install cairo pygame
pip install ./pkg-maraubot/MarauBotMap
```

The 'example-simpleSim.py' file provides a simple example for _MarauBotMap_. The command `python3 example-simpleSim.py` should instanciate a simulation and open it on a windows.
 
- packaging: https://packaging.python.org/en/latest/

### maraubot_sim

Is a classical _ROS2_ package develloped on top of _MarauBotMap_ to glue ROS architeecture.

## Test

_MarauBotMap_ is developed according to the test-driven methode based on `pytest` framework.

```sh
pip install pytest
pytest
```

