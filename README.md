# MarauBot 

Simple 2D robot model and simulation, based on Python and [Cairo](https://pypi.org/project/pycairo/) Librairy.

Project Components:

- MarauBotMap : Independant librairie
- maraubot_sim : ROS2 simulator

## Install

The _MarauBot_ packages relies on  [Cairo](https://pypi.org/project/pycairo/) and provide a ROS2 simulator.

```sh
git clone https://bitbucket.org/ktorz/wraps-python.git
pip install ./MarauBotMap
```

The 'example-421.py' file provides a simple example for _pyBbMm_ inspired from the _421_ game. The command `python3 example-simpleSim.py` should instanciate a model for _421_ and test _2_ transitions. 

- packaging: https://packaging.python.org/en/latest/

## Test

_MarauBotMap_ is developed according to the test-driven methode based on `pytest` framework.

```sh
pip install pytest
pytest
```

