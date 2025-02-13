# A Python Library for the Rego 600 HP controllers

A library for monitoring and controlling a Rego 600 heat pump controller. The Rego 6xx controllers family is used in many heat pumps such as IVT/Bosch/Autotherm/Carrier and others.

Rego 6xx unit contain an interface marked as service. Header of this interface is close to the control unit. This is 5V (TTL) serial interface and is connected by a 9 pin can/d-sub connector.

The library was designed primarily to support the development of a Home Assistant integration.

## Installation

The package can be installed from PyPi as usual:

```bash
pip install pyrego600
```

## Example Usage

```python
import asyncio

from pyrego600 import HeatPump, SerialConnection


async def hp_example():
    connection = SerialConnection(url="<your HP>")
    hp = HeatPump(connection)

    try:
        print("Connecting to Heat Pump...")
        await hp.verify()
        print("Connected!")

        for register in hp.registers:
            value = await hp.read(register)
            print(f"register {register.identifier} = {value}")
    except Exception as e:
        print(f"Reading registries from Heat Pump failed due {e!r}")
    finally:
        await hp.dispose()


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.run(hp_example())
```

## Clone the repository

```python
git clone https://github.com/crnjan/pyrego600
cd pyrego600

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dev/project dependencies
pip install -e '.[dev]'
```

## Run the tests

```python
pytest -s
# Lint the code
ruff check --fix
# Format the code
ruff format
```