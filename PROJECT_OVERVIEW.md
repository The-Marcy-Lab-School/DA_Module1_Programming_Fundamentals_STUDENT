# Project Overview: Inventory Tracker

## The objective

Build a plain-Python (no libraries beyond the standard library) command-line
inventory tracker for a small lending library. Define an `Item` class,
write standalone functions to read and validate a batch file of ADD/REMOVE/
SEARCH transactions, update a running collection of `Item` objects, and
print a formatted inventory summary plus a low-stock alert list. Close it
out with a short written reflection comparing the time complexity of your
own search approach against the alternative, tied to your actual code.

## Why it matters

This is the first project of the program where you actually write code —
Module 0 was terminal-only on purpose. Everything here (loops, functions,
classes, reasoning about how code scales) gets used constantly for the rest
of the program: real Python shows up again starting in **Module 3**, and
by **Module 4** you're combining it with SQL for real data work. The
specific habit this project builds — wrapping related data and behavior
into a class instead of juggling parallel lists, and writing small,
testable functions instead of one long script — is exactly what makes
larger programs (the kind you'll build from Module 4 onward) manageable
instead of unreadable.

## Deliverables at a glance

- A **public GitHub repo**, created from the template via "Use this
  template" (not Fork).
- `starter/inventory.py` filled in: a working `Item` class, the batch-file
  reading/validation/processing functions, and the formatted summary +
  low-stock output — actually run against the provided
  `data/inventory_transactions.txt`, including its deliberate edge cases.
- `starter/REFLECTION.md` filled in: the function-scope explanation and the
  Big-O comparison, tied to your real `find_item` implementation.
- A clean submission — no leftover debugging `print()` statements or unused
  variables.
- At least **2 well-messaged commits** (not one "final" dump).

## Skills you'll practice

- **Control flow** — loops and conditionals that actually handle real,
  messy input, not just the happy path.
- **Functions & modular programming** — splitting a script into small,
  single-purpose functions with clear inputs and outputs.
- **Object-oriented programming** — bundling related data and behavior
  (an item's quantity, its low-stock check) into a class.
- **Algorithmic complexity (Big-O)** — reasoning about how your code's
  runtime changes as the data it works on grows, not just whether it works
  right now.
- **Attention to detail** — a submission that's actually clean: no
  leftover debug output, no loose ends.

## Timeline

See `TIMELINE.md` for a suggested day-by-day pace.

## Where to start

New here? Go to `GETTING_STARTED.md` — it walks through turning this
template into your own repo, step by step.
