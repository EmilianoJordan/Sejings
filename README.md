# Sejings

Sejings is meant to be a quick and simple tool to rapidly integrate 
project sejings. The problem I've seen many times with libraries is that
it's often hard to have a way for the user to change aspects or functionality 
deep in a library. Scientific libraries often have arguments for a function 
that are unavailable to a developer because they're hidden behind three function calls.
One attempt to solve this is to pass along keyword arguments, which leads to 
documentation and maintainability issues. This is evident by the popularity of
**kwargs in many data science libraries. The other solution is to work with dictionaries 
similar to matplotlib's rcParams. Yet this leads to a tedious and time consuming
developer experience by forcing `if xxx is None` checks everywhere.

To show you my solution let's first start of with a rcParams style 
function:

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

* Context manager
* __getitem__, __setitem__