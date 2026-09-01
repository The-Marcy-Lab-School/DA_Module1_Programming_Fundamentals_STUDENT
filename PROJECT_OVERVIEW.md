# Project Overview: Inventory Tracker

## The objective

Pick one of 4 real stakeholder scenarios (`SCENARIOS.md`), then build a
plain-Python command-line inventory tracker for them:

- **Design your own class** for tracking one inventory item — there's no
  single right answer, figure out what your specific stakeholder actually
  needs to track.
- **Write standalone functions** to read and validate a real 430-row batch
  file of ADD/REMOVE/SEARCH transactions.
- **Handle at least 3 distinct kinds** of messy/malformed input without
  crashing.
- **Export your results** so you can interactively search and double-check
  your own work.
- **Close it out with a written reflection** — including how you'd use AI
  to help find *more* edge cases than the ones you caught by hand, and how
  you'd verify what it tells you.
- **Present it** in a short (6-slide max) deck with a live demo.

## Why it matters

This is the first project of the program where you actually write code —
Module 0 was terminal-only on purpose. Nobody's handing you the data model
this time: a real analyst constantly has to figure out what actually
matters to track for a given problem, not just fill in a template. The
specific habits this project builds — designing a class instead of being
handed one, validating messy real input instead of trusting the happy
path, and using AI as a tool you verify rather than one you blindly trust —
get used constantly for the rest of the program: real Python shows up
again starting in **Module 3**, and by **Module 4** you're combining it
with SQL for real data work.

## Deliverables at a glance

- A **public GitHub repo**, created from the template via "Use this
  template" (not Fork).
- One scenario chosen from `SCENARIOS.md`, the other 3 data files deleted.
- `starter/inventory.py` filled in: your own class (design decisions are
  yours), the batch-file functions, real docstrings you wrote yourself,
  at least one `try`/`except`, and `export_to_json` actually called.
- At least **3 distinct edge cases** found and handled — real ones,
  actually in your data file, not invented.
- `starter/REFLECTION.md` filled in — the edge cases you found, the
  function-scope explanation, the Big-O comparison, and the AI-assisted
  edge-case-discovery reflection.
- A short **project deck** (6 slides max, including a live demo of your
  edge-case handling).
- Your final `README.md` replaced with your own real project README — the
  scenario/stakeholder you chose, your design decisions, and your key
  takeaways (see `CHECKLIST_TIMELINE.md`'s final day for the exact
  sections).
- A clean submission and at least **3 well-messaged commits**.

## Skills you'll practice

- **Control flow** — loops and conditionals that actually handle real,
  messy input, not just the happy path.
- **Functions & modular programming** — splitting a script into small,
  testable functions with clear inputs and real return values.
- **Object-oriented programming** — deciding, yourself, what data and
  behavior belong bundled into a class for your specific scenario.
- **Algorithmic complexity (Big-O)** — reasoning about how your own code's
  runtime changes as the data it works on grows.
- **Attention to detail** — finding and handling real problems in a
  430-row file you can't just eyeball, and presenting proof you did.

## Above & beyond (optional)

Finished the MVP with real time to spare? `ABOVE_AND_BEYOND.md` (on this
template's `project-scope` branch — see `README.md`) has 5 real stretch
items: a second search approach timed against your own, a no-template
debugging challenge, a 4th edge case, extending `tools/search.html`, and
a Module 2 preview. **None of it is required** — pick one or two if you
want, a complete MVP without any of them is still a full, passing
submission.

## Timeline

3 build days plus a share-out day. See `CHECKLIST_TIMELINE.md` for the
day-by-day sprint pace and the full submission checklist.

## Where to start

New here? Go to `README.md` — it walks through turning this template into
your own repo, step by step.
