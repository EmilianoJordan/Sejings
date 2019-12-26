# Sejings

Sejings is meant to be a quick and simple tool to rapidly integrate 
project sejings. This was inspired by a desire to work with a 
solution similar to MatPlotLib's rcParams and to improve on the 
developer experience and developing speed by avoiding None checks.

This is the development experience I'm trying to avoid:
```python
def add(*nums, cache=None, cache_path=None):
    
    if cache is None:
        cache = sejings['cache']
    if cache_path is None:
        cache_path = sejings['cache.path']
    
    result = sum(nums)
    
    if cache: # True
        save_to_cache(result, cache_path) #'/some/dir/path'
    
    return result
```

Obviously dictionaries would be computationally the fastest way to 
accomplish sejings. This project is meant to be friendly to developers 
consuming packages and to encourage rapid development over absolute 
runtime speed. We're using Python after all, right?

# Usage

Import sejings and create the sejings you need:

```python
from sejings import sejings

sejings.cache = True
sejings.cache.path = '/some/dir/path'

```
 
To evaluate sejings passed into a function as an argument 
use the @extract_sejings decorator. This will evaluate all 
sejings in the function definition and in the arguments
being passed into the function:

```python
from sejings import extract_sejings

@extract_sejings
def add(*nums, cache=sejings.cache, cache_path=sejings.cache.path):
    result = sum(nums)
    
    if cache: # True
        save_to_cache(result, cache_path) #'/some/dir/path'
    
    return result
```

A branch is also evaluated when an endpoint is called.

```python
assert sejings.cache()
assert sejings.cache.path() == '/some/dir/path'

def add(*nums, cache=sejings.cache, cache_path=sejings.cache.path):
    result = sum(nums)
    
    if cache(): # True
        save_to_cache(result, cache_path()) #'/some/dir/path'
    
    return result
```

In some cases defining arguments as a Sejings object may be
desired. This is accomplished by adding the argument name to the 
@extract_sejings arguments.

```python
@extract_sejings('cache')
def add(*nums, cache=sejings.cache):
    result = sum(nums)
    
    if cache(): # True
        save_to_cache(result, cache.path()) #'/some/dir/path'
    
    return result
```

## @TODO

* I'm exploring options right now to allow methods to be called directly
    on self._val but am weighing the pros and cons. The SejingsNumber
    class published is something I'm exploring and should not be 
    depended on as it may change. 
* Context manager
* Copy functionality
* Iteration
* __getitem__, __setitem__
* IO to file. Look into integration with configparser.