# Checklist & Timeline — 1 Week, Run as a Sprint

**4 build days, then a demo day.** This isn't just a schedule — it's your
first real exposure to how professional software teams actually plan
short-term work: a **sprint**. Every item below is also the actual
submission checklist — work through it in order (design before code, small
before whole), it isn't just a task list.

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
  yesterday? What am I doing today? Is anything blocking me?*
- **The backlog** — everything real, worth doing, and **deliberately not**
  in this sprint. `ABOVE_AND_BEYOND.md` *is* this project's backlog — real
  features that don't fit in a 1-week sprint without cutting something that
  matters more. It isn't a list of things you failed to do; it's how a team
  protects a sprint's deadline by explicitly deciding what's *not* in scope.
- **Sprint review / demo** (Day 5) — you show real, working software to real
  people, not a status report about what you plan to finish later. Your
  project deck is this project's sprint review.

This isn't busywork — **`project-management` becomes its own explicitly
graded skill by Module 15's final project.** This week is your first rep.

## Day 1 — Sprint planning: choose, read, design (not code)

- [ ] Repo created from the template via **"Use this template"** (not Fork)
  and cloned locally — see `README.md`.
- [ ] `.gitignore`/`LICENSE`/git history confirmed already present;
  `LICENSE`'s `[YOUR NAME]` placeholder replaced with your actual name,
  committed. Python 3 confirmed working (`python3 --version`).
- [ ] All 4 scenarios in `SCENARIOS.md` read; one picked, the other 3 data
  files deleted from your repo.
- [ ] `starter/REFLECTION.md` read through before writing any code, so it's
  clear what the finished script needs to be able to explain about itself.
- [ ] Your class's attributes sketched (paper or a scratch file) **based on
  re-reading your stakeholder's actual stated need** — not copied from a
  different scenario.
  > ⚠️ Common mistake: writing one long function that does everything
  > instead of splitting validation, reading, and summarizing into separate
  > functions — decide the split before coding, not after it's tangled.
  > ⚠️ Common mistake: picking attributes that don't actually answer your
  > stakeholder's stated question.
- [ ] First 2-3 lines of your chosen data file traced by hand — what makes
  an ADD line valid vs. invalid?
- [ ] Skim `MVP.md` (your sprint goal) and `ABOVE_AND_BEYOND.md` (your
  backlog) so you know the line between them before you start.

## Day 2 — Core build: class + validation

- [ ] `__init__` correctly stores the attributes chosen for your scenario; a
  low-stock-style check method implemented and correct.
- [ ] Confirmed (by instantiating 2+ objects and checking their attributes)
  that separate instances don't share state.
- [ ] A real docstring, written by you, on the class and every method —
  `read_batch_file`'s given docstring is the only model, not something to
  copy.
  > ⚠️ Common mistake: holding item data in loose parallel lists instead of
  > actually using the class consistently throughout the rest of the script.
- [ ] Commit: `git commit -m "add [scenario] item class"` — don't wait until
  everything is done to commit for the first time.
- [ ] `read_batch_file` reads the real file and returns its lines.
- [ ] `validate_line` correctly distinguishes a valid ADD/REMOVE/SEARCH line
  from an invalid one, tested first against a tiny 3-5 line sample.
- [ ] **At least one real `try`/`except`** for a value that's present but the
  wrong type (e.g. converting a quantity string to a number).
- [ ] Commit: `git commit -m "add batch file parsing and validation"`.

**Daily check-in:** what did you plan yesterday, what are you building
today, what (if anything) is blocking you?

## Day 3 — Integration: the real file, real edge cases

- [ ] `process_transactions` loops over your real, chosen data file, building
  a running item collection from ADD/REMOVE/SEARCH lines.
- [ ] **At least 3 distinct planted edge cases** (see `data/SOURCE.md`)
  handled with a specific, printed message — not a crash. Genuinely 3
  different *kinds* of problem, not the same one 3 times.
  > ⚠️ Common mistake: letting one malformed transaction line crash the
  > whole script instead of catching and reporting it — only testing the
  > happy path is how this gets missed.
- [ ] Commit: `git commit -m "process real batch file, handle edge cases"`.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
3 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 4 — Polish: output, export, reflection

- [ ] `find_item` implemented — a linear scan or a dict lookup, genuinely
  one or the other.
- [ ] `print_summary` prints a formatted inventory summary and a separate
  low-stock alert list.
- [ ] `export_to_json` implemented and actually called — writes
  `inventory.json`.
- [ ] `tools/search.html` opened (via `python3 -m http.server`, see that
  file) and used to interactively confirm your 3+ edge cases actually did
  what you intended.
- [ ] `REFLECTION.md`'s edge-case list filled in: the exact line and what
  your code does about it, for each of the 3+.
- [ ] Function-scope explanation filled in, in your own words.
- [ ] Big-O comparison filled in, correctly labeling *your actual*
  `find_item` implementation and tying the reasoning to your own code.
- [ ] AI-assisted edge-case-discovery reflection filled in: a real, specific
  prompt/workflow idea **and** a real, specific way to verify what it
  suggests before trusting it.
  > ⚠️ Common mistake: reciting a Big-O textbook definition without
  > connecting it to your own search implementation, or an AI reflection
  > with no actual verification step named.
- [ ] Clean sweep: no leftover debugging `print()` statements, no unused
  variables or imports.
- [ ] Commit(s) pushed — `git log --oneline` should show 3+ commits total,
  each with a real message.

**Daily check-in.**

## Day 5 — Sprint review: build your deck and demo

- [ ] Project deck built (any tool — Slides, PowerPoint, Canva), **6 slides
  max, including a live demo**. Covers: your chosen scenario/stakeholder,
  your class design decisions and why, your batch-processing approach, and
  an actual demonstration (live run or real screenshots) of your 3+ edge
  cases being handled.
- [ ] Present it like a real sprint review — showing working software, not
  describing what you're about to build.
- [ ] `README.md` accurate; repo confirmed **public**.
- [ ] Final self-check against this checklist before calling it done.

**Exit criterion:** everything above is done and pushed, including the
deck. That's the whole sprint. Backlog items (`ABOVE_AND_BEYOND.md`) are
exactly that — backlog. Picking one up after Day 5, if you have real time,
is a bonus sprint, not a requirement of this one.

## After the Day 5 demos: peer code review

Right after demos (or in a separate session), you'll swap repos with a
small group of classmates — real code, not anonymized, since you'll have
just watched each other present. You'll review each other's class design
and edge-case handling as a teammate who has to maintain the code would,
give real feedback, and reflect on your own design choices afterward. No
extra prep — just have your repo pushed and public.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. All five are detailed in `ABOVE_AND_BEYOND.md`.

- [ ] Implement a **second** search approach (whichever you didn't use for
  `find_item`) and empirically time both against a scaled-up copy of your
  data file — turn the Big-O reflection from "explain" into "prove."
- [ ] Debug `above_and_beyond/debug_challenge.py` — no template this time.
  Find and precisely name all 3 planted bugs, fix them, write up what you
  found.
- [ ] Handle a 4th distinct edge case beyond the 3 MVP needs.
- [ ] Extend `tools/search.html` yourself — sort, filter, or add a low-stock
  count, and note the change in `REFLECTION.md`.
- [ ] Run the given-code `above_and_beyond/preview_pandas.py` (Module 2
  preview) and write a short comparison to your own summary in
  `REFLECTION.md`.
