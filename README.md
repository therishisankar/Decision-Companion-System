# My Decision Assistant (DCS)

This is a project I built to help people make hard choices (like picking a cloud provider) using math instead of just guessing.

## What it does
I made this tool so you can put in a few different options, say what is important to you (like Cost or Reliability), and it will tell you which one is actually the best based on your scores.

### Why I built it this way:
1. **The Math is clear**: I used a "Weighted Scoring" method. It's basically like a report card where some subjects count more than others.
2. **Fair Comparison**: Since Cost might be in thousands but Uptime is a percentage, I wrote a "Normalizer" to make them all 0 to 1 so they can be compared fairly.
3. **No Bad Data**: I added a way to block options that are too expensive or don't fit your needs.

## How to use it
You just need Python installed. No extra libraries like Pandas or Pydantic needed!

1. Open your terminal in this folder.
2. Run this:
   ```bash
   python src/cli.py templates/cloud_decision.json
   ```

## Folder Setup
I tried to keep things organized:
* `src/core`: The math stuff (math logic).
* `src/models`: Just the data folders (storage).
* `src/io`: Stuff for reading files and printing to the screen.
* `src/explain`: Help for explaining the result.

## A Note on AI
I used an AI to help me brainstorm the cloud provider data and help me structure some of the documentation, but I wrote the core logic myself to make sure I understood the math!
