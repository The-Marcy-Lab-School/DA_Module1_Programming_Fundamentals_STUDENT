# Project Overview: Inventory Tracker

## The objective

Pick one of 4 stakeholder scenarios (`SCENARIOS.md`) and build a
plain-Python command-line inventory tracker for them:

- **Design your own class** for one inventory item, based on what your
  stakeholder needs. There's no single right answer.
- **Write separate functions** to read and validate a 430-line batch file
  of `ADD`, `REMOVE`, and `SEARCH` transactions.
- **Handle at least 3 different types** of bad input without crashing.
- **Export your results** to `inventory.json`.
- **Write a reflection** on your assumptions, your edge cases, scope,
  Big-O, and how you'd use AI to find more edge cases and check what it
  tells you.
- **Write a README an employer can read**, then share your project out
  loud on Day 5.

## Why it matters

This is the first project where you write real code. Module 0 was
terminal-only. No one hands you the data model this time. Deciding what
to track for a real problem is a core analyst skill. You'll keep using
the habits from this project for the rest of the program: designing a
class, validating messy input, and checking AI's answers instead of
trusting them. Python comes back in **Module 3**, and in **Module 4**
you'll combine it with SQL.

## Deliverables at a glance

- A **public GitHub repo** created with "Use this template" (not Fork).
- One scenario chosen from `SCENARIOS.md`, with the other 3 data files
  deleted.
- `starter/inventory.py` complete. It needs:
  - your own class and the batch-file functions
  - docstrings you wrote yourself
  - at least one `try`/`except`
  - a call to `export_to_json`
- At least **3 different types** of edge case handled. They must be real
  lines in your data file.
- `starter/REFLECTION.md` complete, with all six sections.
- Your own **README.md** replacing this template's. It covers your
  stakeholder, business scenario, findings, key decisions, how to run it,
  and a short reflection.
- At least **3 commits** with clear messages.
- **Day 5 share-out:** a pair repo review and a 90-second project
  walkthrough. No slides.

## Skills you'll practice

- **Control flow:** loops and conditionals that handle messy input, not
  just the happy path.
- **Functions and modular programming:** small functions, each with one
  job, clear inputs, and a return value.
- **Object-oriented programming:** deciding what data and behavior belong
  in a class for your scenario.
- **Algorithmic complexity (Big-O):** how your code's runtime changes as
  the data grows.
- **Attention to detail:** finding real problems in a file too long to
  check by eye, and showing proof you handled them.

## Above & Beyond (optional)

Finished the MVP with time to spare? The Above & Beyond section at the
bottom of `CHECKLIST_TIMELINE.md` has 5 stretch items. They go past what
was taught in class, so you'll research them yourself, with starter
links. None are required.

## Timeline

5 days: 4 build days and a share-out day. See `CHECKLIST_TIMELINE.md`.

## Where to start

Go to `README.md`. It walks you through setting up your repo.
