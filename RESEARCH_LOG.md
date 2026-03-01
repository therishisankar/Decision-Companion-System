# My Thinking & Research Log

This is where I kept notes of why I chose certain ways to code this system.

## 1. How to calculate the results?
I looked at a few ways to do this. I chose **Simple Additive Weighting**. 
* **Why?** It's easy for a person to understand. If I show a big table of math, they can see exactly why one option won. Some other ways (like AHP) were way too complicated for this project.

## 2. Why just plain Python?
I could have used Pydantic or external libraries, but I wanted this to run on ANY computer right away. So I stuck with just normal Python "dataclasses". It's cleaner and doesn't require the user to install anything.

## 3. How I handled different units?
Comparing Dollars to Percentages is hard. I used **Min-Max Scaling**.
* This turns every number into a score from 0 to 1.
* Higher is better for things like "Speed".
* Lower is better for things like "Cost".

## Things I could do better (Lessons Learned)
* **Outliers**: If one option is super expensive, it makes the others look like $0. In the future, I'd like to fix this by capping the range.
* **Missing Data**: Right now, if data is missing, I just say it's "Ineligible". Maybe in the future, I could use an average.

## Who I read to learn this?
I looked up "Multi-criteria decision making" on Wikipedia and some tutorials to get the math right!
