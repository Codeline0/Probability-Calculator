# Budget App

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

## Table of contents

-   [Overview](#overview)
    -   [Rules](#rules)
    -   [Testing](#testing)
    -   [Screenshot](#screenshot)
-   [My process](#my-process)
    -   [Built with](#built-with)
    -   [What I learned](#what-i-learned)
-   [Author](#author)

## Overview

### Rules

First, the Hat class should: 

- Take a variable number of arguments that specify the number of balls of each color that are in the hat. 
- The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color.
- The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Lastly an experiment function that should return a probability, function should accept:

- hat: A hat object containing balls that should be copied inside the function.
- expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
- num_balls_drawn: The number of balls to draw out of the hat in each experiment.
- num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

### Testing

The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.

### Screenshot

![](/probability_calculator.png)

### Executing program

-   Run the main.py script in terminal

```
python main.py
```

## My process

### Built with

-   Python 3.9.12 

### What I learned

List comprehension with 2 loops.

```python
self.contents = [key for key, val in self.color.items() for num in range(val)]
```

## Authors

-   Project assigned by FreeCodeCamp - [FreeCodeCamp](https://www.freecodecamp.org/learn/)
-   Marco Cámez - [Codeline0](https://github.com/Codeline0)