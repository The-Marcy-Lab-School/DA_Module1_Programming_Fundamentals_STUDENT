# Recommended Timeline — 1.5 Weeks

This is a **suggested pace, not a rigid schedule** — roughly 7-8 working
days, working backward from what a complete submission needs.

> A note on this: you're still early in the program, so we're handing you a
> ready-made timeline again, same as Module 0. As you get more practice
> breaking projects into checkpoints yourself, later modules will expect you
> to set up your own tracking (a GitHub Projects board, a simple issue
> list, whatever fits) instead of working from a timeline someone else
> wrote for you. Treat this one as a model of what breaking a coding
> project into stages looks like, not just a checklist to follow on
> autopilot.

## Day 1 — Design, not code

- Repo created from the template (`GETTING_STARTED.md`), cloned locally.
- `.gitignore`/`LICENSE`/git history confirmed already present.
- Sketch the `Item` class on paper or in a scratch file: what attributes
  does it need, what should `is_low_stock()` actually check?
- Read `starter/REFLECTION.md` before writing any code, so you know what
  your finished script needs to be able to explain about itself.
- Trace through the first 2-3 lines of `data/inventory_transactions.txt` by
  hand — what makes an ADD line valid vs. invalid?

## Day 2 — The `Item` class, alone

- Implement `__init__` and `is_low_stock()`.
- Instantiate a couple of `Item`s by hand in a scratch script and confirm
  their attributes aren't shared between instances.
- First commit.

## Day 3 — Parsing and validation, in isolation

- Implement `read_batch_file` and `validate_line` against a tiny 3-5 line
  sample (not the full file yet) — get the conditional logic right on a
  small, controlled input before scaling up.

## Day 4 — Wire it together

- Implement `process_transactions`: loop over the real batch file, build
  the running `Item` collection, handle ADD/REMOVE/SEARCH for real.
- Commit.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
4 — `git log --oneline` should already tell a real story.

## Day 5 — Break it on purpose

- Run your script against the real `data/inventory_transactions.txt` —
  including its deliberate edge cases (the blank line, the malformed ADD,
  the REMOVE for an unknown item). Make the required one fail gracefully
  with a real, specific message instead of crashing.
- Commit.

## Day 6 — Output and reflection

- Implement `find_item` and `print_summary` — the formatted inventory
  summary and low-stock alert list.
- Write both required pieces of `REFLECTION.md`, tied to your actual code.

## Day 7 (buffer) — Polish and submit

- Clean sweep: remove leftover debugging `print()`s and unused variables.
- Confirm `README.md` is accurate and the repo is actually public.
- Final commit(s) pushed — `git log --oneline` should show 3+ commits
  total, each with a real message.
- Above & Beyond if you have real time left over — see `ABOVE_AND_BEYOND.md`
  on the template's `project-scope` branch.

**Exit criterion:** everything in `MVP.md` is done and pushed. That's the
whole submission.
