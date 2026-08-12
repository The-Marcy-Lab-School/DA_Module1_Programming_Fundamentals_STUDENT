# Recommended Timeline — 1 Week, Run as a Sprint

**4 build days, then a demo day.** This isn't just a schedule — it's your
first real exposure to how professional software teams actually plan
short-term work: a **sprint**.

## What's a sprint, and why does this project run as one?

A sprint is a short, fixed block of time (commonly 1-2 weeks) where a team
commits to a specific, achievable set of work, builds it, then **stops and
shows what they built** — a real demo, not a status update. The fixed
deadline is the point: it forces real decisions about what actually fits,
instead of scope quietly growing until the "done" date slips. You'll use
real agile vocabulary this week:

- **Sprint planning** (Day 1) — deciding, up front, what's actually
  achievable in the time you have. For this project, that decision is
  already made for you (see `MVP.md`) — but you're still doing the same
  underlying step every sprint starts with: understanding the goal before
  you touch any code.
- **Daily check-in** — at the start of each build day, spend 2 minutes
  answering three questions for yourself (a real team does this out loud,
  together, in ~10 minutes total — a "stand-up"): *What did I finish
  yesterday? What am I doing today? Is anything blocking me?* Write your
  answers in your terminal log or a scratch note — it's a habit, not a
  deliverable.
- **The backlog** — everything real, worth doing, and **deliberately not**
  in this sprint. `ABOVE_AND_BEYOND.md` *is* this project's backlog: real
  features (a second search implementation, more edge cases, extending the
  search tool) that don't fit in a 1-week sprint without cutting something
  that matters more. A backlog isn't a list of things you failed to do —
  it's how a team protects a sprint's actual deadline by explicitly
  deciding what's *not* in scope, on purpose, instead of letting "just one
  more thing" quietly blow up the schedule.
- **Sprint review / demo** (Day 5) — you show real, working software to
  real people (your instructor, maybe classmates), not a status report
  about what you plan to finish later. Your project deck is this project's
  sprint review.

This isn't busywork — **`project-management` becomes its own explicitly
graded skill by Module 15's final project.** This week is your first rep.

## Day 1 — Sprint planning: choose, read, design (not code)

- Repo created from the template (`README.md`), cloned locally.
- `.gitignore`/`LICENSE`/git history confirmed already present.
- Read all 4 scenarios in `SCENARIOS.md`, pick one, delete the other 3
  data files.
- Sketch your class on paper or in a scratch file: what does *your*
  stakeholder actually need tracked? Why?
- Skim `MVP.md` (your sprint goal) and `ABOVE_AND_BEYOND.md` (your
  backlog) so you know the line between them before you start.

## Day 2 — Core build: class + validation

- Implement your class (`__init__`, your low-stock-style check), with
  real docstrings you wrote yourself.
- Implement `read_batch_file` and `validate_line` against a tiny 3-5 line
  sample first — including a real `try`/`except` for the quantity-type
  check.
- Commit at least once today — don't wait for "done" to commit.

**Daily check-in:** what did you plan yesterday, what are you building
today, what (if anything) is blocking you?

## Day 3 — Integration: the real file, real edge cases

- Implement `process_transactions`: loop over your real 430-row data file,
  build the running collection, handle ADD/REMOVE/SEARCH for real.
- Find and handle **at least 3 distinct** planted edge cases (see `data/
  SOURCE.md`) — real ones, with specific messages, not crashes.
- Commit.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
3 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 4 — Polish: output, export, reflection

- Implement `find_item` and `print_summary`.
- Implement and call `export_to_json`; use `tools/search.html` to actually
  confirm your 3+ edge cases did what you think they did.
- Write all 4 required pieces of `REFLECTION.md`, including the
  AI-assisted edge-case-discovery reflection.
- Clean sweep: remove leftover debugging `print()`s and unused variables.
- Final commit(s) pushed — `git log --oneline` should show 3+ commits
  total, each with a real message.

**Daily check-in.**

## Day 5 — Sprint review: build your deck and demo

- Build your 6-slide-max project deck: your scenario/stakeholder, your
  class design decisions and why, your batch-processing approach, and a
  **live demo (or real screenshots) of your 3+ edge cases actually being
  handled.**
- Present it like a real sprint review — you're showing working software,
  not describing what you're about to build.
- Confirm `README.md` is accurate and the repo is actually public.

**Exit criterion:** everything in `MVP.md` is done and pushed, including
the deck. That's the whole sprint. Backlog items (`ABOVE_AND_BEYOND.md`)
are exactly that — backlog. Picking one up after Day 5, if you have real
time, is a bonus sprint, not a requirement of this one.
