# Genetic Algorithm made Right!

My first contact with this algorithm was at my first year on college. My professor sent us a task to solve the TSP (Traveller Salesman Problem) by any means we could find! Well, my college and I decided to search for methods on the internet, and then, GA came about. 

<p align="center"><img src="https://i1.wp.com/blog.datascienceheroes.com/content/images/2019/01/evolutionary_algortihm-1.gif?w=584&ssl=1" alt="ga" /></p>

By that time, GA implementations was naive, we sought to implement every single feature, which worked a lot better than other approaches, but, because our lack of knowledge on the language (which was pure C) we couldn’t get the best solution!

Even though we got a great result, I always sought to implement it right! Now, with my python skills very rooted, I decided to put in practice, that dream.

## Summary
- [What is GA?](#what-is-tsp-and-ga)
- [Implementation](#implementation)

## What is TSP and GA?

Genetic Algorithm is a Meta-Heuristic to solve Combinatorial Optimization Problems, those ones, which the solution is a combination of the original set. A known Problem in this area is the Traveller Salesman Problem. This problem consists in a Salesman which wants to sale his products in different cities, therefore, he does not want to spend much in his journey, so he decided to calculate which route is the quickest (or cheapest). 

<p align="center"><img src="https://www.math.uwaterloo.ca/tsp/usa50/img/olson_screen.png" alt="tsp" /></p>

Imagine, there are 5 cities to go, there are also **5!** different combinations which pass all the cities, calculating the distance for all those **120 possible chances** we find one which is the best. Well, 120 is cheap for a machine to calculate, but, as the number of cities scales, such as 20, gives back over **2.432902e+18** possible chances, for 100! which is **9.332622e+157** possible combinations, gives more chances than planets in the galaxies, and 100 cities is not so many if you think about it.

<p align="center"><img src="https://miro.medium.com/max/1307/1*jol-QJa3rZ0MSHfPPtmMzA.gif" alt="tsp" /></p>

Then, a smarter approach is needed, there are many, such as the nearest neighbour, which gives a nice result, but is very expensive. GA though, is smart and cheap solution.

One can read more about it in [this very good article](https://towardsdatascience.com/introduction-to-optimization-with-genetic-algorithm-2f5001d9964b) which explain very well how the GA works under the roots and inspired my on the matter which I couldn’t remember! The general idea is that GA use facts that happens in Darwin’s evolution theory. It strives to run through the solution web intelligently, jumping over bad solutions and walking towards better solutions, using a little of random to avoid local best solutions.

## Implementation

I strive to create as generic as possible; the idea is to lay down a foundation for future project which may use GA as means to solve it. I also used the Builder Pattern, a pattern which I know better, to construct the model and solve it. So far, I think is a good choice.

<p align="center"><img src="https://localdomain.files.wordpress.com/2009/09/builder_example12.gif?w=323&h=226" alt="tsp" /></p>
