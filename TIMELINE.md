# Recommended Timeline — About 2 Weeks

This is a **suggested pace, not a rigid schedule** — roughly 9-10 working
days, working backward from what a complete submission needs. This project
has more open-ended design work than a typical first project (you're
choosing a scenario and designing your own class), so the pace below
leaves real room for that instead of assuming it's instant.

> A note on this: you're still early in the program, so we're handing you a
> ready-made timeline again, same as Module 0. As you get more practice
> breaking projects into checkpoints yourself, later modules will expect you
> to set up your own tracking (a GitHub Projects board, a simple issue
> list, whatever fits) instead of working from a timeline someone else
> wrote for you.

## Day 1 — Choose, read, design (not code)

- Repo created from the template (`GETTING_STARTED.md`), cloned locally.
- `.gitignore`/`LICENSE`/git history confirmed already present.
- Read all 4 scenarios in `SCENARIOS.md`, pick one, delete the other 3
  data files.
- Sketch your class on paper or in a scratch file: what does *your*
  stakeholder actually need tracked? Why?

## Day 2 — The class, alone

- Implement `__init__` and your low-stock-style check, with real
  docstrings you wrote yourself.
- Instantiate a couple of your objects by hand in a scratch script and
  confirm their attributes aren't shared between instances.
- First commit.

## Day 3-4 — Parsing and validation, in isolation

- Implement `read_batch_file` and `validate_line` against a tiny 3-5 line
  sample (not the full file yet) — get the conditional logic right on a
  small, controlled input before scaling up.
- Use a real `try`/`except` for the quantity-type check.

## Day 5 — Wire it together

- Implement `process_transactions`: loop over your real 420+ row data
  file, build the running collection, handle ADD/REMOVE/SEARCH for real.
- Commit.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
5 — `git log --oneline` should already tell a real story.

## Day 6 — Hunt for edge cases on purpose

- Run your script against the real data file. Find **at least 3 distinct**
  planted problems (see `data/SOURCE.md`) and make each fail gracefully
  with a real, specific message instead of crashing.
- Commit.

## Day 7 — Output, export, and interactive check

- Implement `find_item` and `print_summary`.
- Implement and call `export_to_json`; open `tools/search.html` and use it
  to actually confirm your 3+ edge cases did what you think they did.

## Day 8 — Reflection

- Write all 4 required pieces of `REFLECTION.md`, including the
  AI-assisted edge-case-discovery reflection.

## Day 9 — Deck and polish

- Build your 6-slide-max project deck (scenario/stakeholder, class design
  decisions, batch-processing approach, a live demo of your edge cases).
- Clean sweep: remove leftover debugging `print()`s and unused variables.
- Confirm `README.md` is accurate and the repo is actually public.
- Final commit(s) pushed — `git log --oneline` should show 3+ commits
  total, each with a real message.

## Day 10 (buffer) — Above & Beyond or finish up

- Catch-up day if you're behind, or Above & Beyond work if you're not —
  see `ABOVE_AND_BEYOND.md` on the template's `project-scope` branch.

**Exit criterion:** everything in `MVP.md` is done and pushed, including
the deck. That's the whole submission.
