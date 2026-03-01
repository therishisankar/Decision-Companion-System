# How I Built This

I wanted to make sure my code was clean and didn't have a lot of confusing parts. Here is my process:

## My Code Pipeline
1. **Read Data**: Get the JSON file from the user.
2. **Filter**: Check if anything is way too expensive and remove it.
3. **Normalize**: Turn all the different numbers into 0 to 1.
4. **Score**: Multiply by the weights to see who wins.
5. **Report**: Print a nice table to the screen!

## How to run the demos
I made two templates to show how it works:
* `cloud_decision.json`: A standard test.
* `budget_violation.json`: To show what happens when an option is too expensive.

To run them:
```bash
# Set path (on windows)
$env:PYTHONPATH = "."; python src/cli.py templates/cloud_decision.json
```

## Running Tests
I wrote some basic tests to make sure my math functions didn't break.
```bash
python -m unittest discover tests
```
