# Settings

Settings is meant to be a quick and simple tool to rapidly integrate project
settings. This was inspired by a desire to work with a solution similar
to MatPlotLibs' rcParams and to improve on it.

One advantage of Settings is the ability for IDEs to code complete the 
settings object statically (work still needs to be done on dynamically).
This allows developers to easily see what settings are available to them
without having to leave the IDE and visit project documentation. 

Obviously dictionaries would be the fastest way to accomplish settings. 
This project is meant to be friendly to developers consuming packages 
and to encourage rapid development over absolute runtime speed.

# Usage

Import settings and create the settings you need:

```python
from sejings import settings

settings.cheese_shop.cheshire.name = 'Cheshire'
settings.cheese_shop.cheshire.quantity = 0
settings.cheese_shop.liptauer.name = 'Liptauer'
settings.cheese_shop.liptauer.quantity = 0

```

To evaluate the values of settings when calling a function
use the @extract_settings decorator. This will evaluate all 
settings in the function definition and in the arguments
being passed into the function:

```python
from sejings import extract_settings
from my_project import settings

@extract_settings('cheese')
def add_stock(quantity, cheese=settings.cheese_shop.cheshire):
    cheese.quantity()  quantity
    return cheese

assert (0, 0) == add_stock(0)

settings.cheese_shop.liptauer = 20

assert (0, 20) == add_stock(0, settings.cheese_shop.liptauer)
```

The value of a settings branch can always be evaluated by calling
the attribute. Work is still being done on Settings manipulation but
most castings should work as well.

```python
from settings import settings

settings.cheese_shop.cheshire = 0
settings.cheese_shop.liptauer = 0

type(settings.cheese_shop.cheshire)
# settings.settings.Settings

type(settings.cheese_shop.cheshire())
# int

float(settings.cheese_shop.cheshire)
# 0.0

int(settings.cheese_shop.cheshire)
# 0

str(settings.cheese_shop.chesire)
# '0'

```

# More Examples

```python
from pathlib import Path
from settings import settings, extract_settings


settings.cache = True
settings.cache.path = Path(__file__).parent / 'cache'

@extract_settings
def cache_to_disk(file: Path, 
                  cache: bool=settings.cache, 
                  cache_path: Path = settings.cache.path):

    if not cache:
        return
        
    cache_path /= file.name
    
    # do cache things

```

If you'd like to have different settings you can either create another 
branch or a new instance of settings

```python
from pathlib import Path
from settings import settings, Settings


settings.cache = True
settings.cache.path = Path(__file__).parent / 'cache'
settings.warnings.DepreciatedWarning = 'ignore'
settings.warnings.UserWarning = 'default'

# or

warnings = Settings()
warnings.DepreciatedWarning = 'ignore'
warnings.UserWarning = 'default'
```

## @TODO

* Address dynamic inspection
* Property decorators
* Copy and deepcopy functionality
* Iteration
* Dictionary like functionality
* IO to file. Look into integration with configparser.