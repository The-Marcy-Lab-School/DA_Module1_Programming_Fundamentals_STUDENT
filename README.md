# Programming Fundamentals Project: Inventory Tracker

**New here?** Start with `PROJECT_OVERVIEW.md` for what you're building and
why. This file (`README.md`) is where the step-by-step setup lives — you're
already in the right place.

**Due:** 1 week, run as a sprint — 4 build days plus a demo day. See
`CHECKLIST_TIMELINE.md` for the day-by-day pace, what "sprint"/"backlog"
mean here, and the full submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

### Step 1: Get your own copy

On this repo's GitHub page, you'll see two buttons that both sound like "make
a copy" but do different things:

- **"Use this template"** ← use this one. It creates a brand-new, independent
  repository under *your* GitHub account, with no visible link back to this
  template. That's what you want for something that becomes part of your
  portfolio.
- **"Fork"** — creates a copy that stays linked to this one (GitHub will show
  "forked from marcy-lab-school/..." on your repo forever). Fork is the right
  tool when you intend to contribute changes back to the original project —
  that's not this. Don't use Fork here.

Click **"Use this template" → "Create a new repository,"** name it something
like `inventory-tracker`, keep it **public** (the assignment requires a
public repo), and create it.

### Step 2: Set up your tools

- **Python 3** — check you have it: open Terminal and run `python3
  --version`. If it's missing, install from https://python.org (the macOS
  installer) or via Homebrew (`brew install python3`).
- **VS Code** — already introduced in Module 0.
- **[Python Tutor](https://pythontutor.com/)** — free, browser-based. Not
  required to complete the project, but genuinely useful for stepping
  through your own loop/function code line by line if you get stuck on why
  a variable has the value it does.

### Step 3: Clone your new repo locally

Open **Terminal**, then on your own new repo's page (not this template),
click the green **Code** button, copy the HTTPS URL:

```bash
git clone <the URL you copied>
cd <your-repo-name>
```

### Step 4: Confirm your environment — it's already set up

Unlike Module 0, this template already comes with `.gitignore`, `LICENSE`,
and a real git history — `git-version-control` isn't the skill being tested
this module, so there's no reason to rebuild those from scratch. Confirm
they're there and move straight to the actual project:

```bash
ls -a          # should show .gitignore among the files
cat LICENSE    # should show the MIT License text
git log --oneline
```

**One real edit still needed, easy to miss since the file already
exists:** open `LICENSE` and replace the placeholder `[YOUR NAME]` on the
copyright line with your actual name — a public repo with a literal
"[YOUR NAME]" left in it is a small but real tell nobody actually looked
at the file. Commit that change (`git commit -m "add my name to LICENSE"`)
alongside your other early commits.

## Your scenario and data

See `SCENARIOS.md` and pick **one** of the 4 stakeholder scenarios. Each
one's data file is already included at `data/<scenario>_transactions.txt`
(430 rows, no download needed) — delete the other 3 once you've chosen.
See `data/SOURCE.md` for what's deliberately planted in every file and why
it's long enough that you can't just eyeball it for problems.

Before writing any code: re-read your stakeholder's actual words, sketch
what your class needs to track and why, and read through `starter/
REFLECTION.md` so you know what your finished script needs to be able to
explain about itself. Trace through the first 2-3 lines of your data file
by hand — decide what a valid ADD line looks like vs. an invalid one —
before writing the loop that processes them.

## What to do

See `starter/inventory.py` — you design the class yourself (see
`SCENARIOS.md`); the function structure is given but the logic isn't, and
you write your own docstrings (one example is given as a model). `starter/
REFLECTION.md` is the required written piece once your script runs.
`tools/search.html` is a given interactive tool for double-checking your
own results — once your script produces `inventory.json`, use it to
interactively confirm your edge cases actually did what you think they
did. `CHECKLIST_TIMELINE.md` has the suggested pace. Commit incrementally as you go —
a `git commit` after your class works, then another after the
batch-processing loop works, not one commit at the very end.

Don't forget the two deliverables beyond the code itself: `REFLECTION.md`
(all 4 sections) and a short project deck (6 slides max, including a live
demo). Your instructor shares the full step-by-step checklist and grading
rubric — including exactly what each of these needs to cover — separately
through the classroom, not this repo.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your **M**inimum **V**iable **P**roduct —
the required baseline) or `ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting in
your portfolio repo. Ask your instructor for the link to this template's
`project-scope` branch (it'll look like `.../tree/project-scope` on the
*template's* GitHub page, not your own copy) to read them, or check the
checklist your instructor shares through the classroom, which covers the
same ground.
