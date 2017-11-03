# dict2uml

[![Build Status](https://travis-ci.org/martisak/dict2uml.svg?branch=master)](https://travis-ci.org/martisak/dict2uml) [![PyPI version](https://badge.fury.io/py/dict2uml.svg)](https://badge.fury.io/py/dict2uml)

Python library that prints a Python `dict` as [PlantUML](http://plantuml.com/) code or as an inline picture in a [Jupyter](http://jupyter.org/) Notebook.

Heavily inspired by [json-to-plantuml](https://github.com/meteorbites/json-to-plantuml) by [meteorbites](https://github.com/meteorbites) and [IPlantUML](https://github.com/jbn/IPlantUML) by [John B Nelson](https://github.com/jbn).

## Installation

Install `plantuml`, for example with `brew install plantuml`. The location should be `/usr/local/bin/plantuml`. This is hardcoded for now, so if you need to change it, please install from source.

~~~
pip install dict2uml
~~~

## Usage

This can be used either at command line or in a notebook. You can generate an SVG or print the code that generated the diagram.

### Setup

~~~
import dict2uml
d = {"beers": ["Heineken","Budweiser","Guinness"]}
~~~

### Print SVG

To print the class diagram of the dict `d` in [Jupyter](http://jupyter.org/), do

~~~~
dict2uml.dict2svg(d)
~~~~

### Print PlantUML source code

Print the source code for the PlantUML](http://plantuml.com/) class diagram.

~~~~
print(dict2uml.dict2plantuml(d))
~~~~

## Example

~~~
cat example.json | python dict2uml.py | plantuml -pipe | open -a Preview.app -f
~~~

![example](example.png)

## References

* Wikipedia contributors, "JSON," Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=JSON&oldid=806502500 (accessed November 3, 2017).
* [json-to-plantuml](https://github.com/meteorbites/json-to-plantuml) by [meteorbites](https://github.com/meteorbites)
* [IPlantUML](https://github.com/jbn/IPlantUML) by [John B Nelson](https://github.com/jbn).
* [PlantUML](http://plantuml.com/)