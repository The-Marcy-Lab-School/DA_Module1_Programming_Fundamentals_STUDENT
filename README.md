# Programming Fundamentals Project: Inventory Tracker

**New here?** Start with `PROJECT_OVERVIEW.md` to see what you're building
and why. This file walks you through setup.

**Timeline:** a 5-day sprint: 4 build days, then a share-out day. See
`CHECKLIST_TIMELINE.md` for the day-by-day plan and `RUBRIC.md` for how
the project is graded.

This repo is a **GitHub template**: a starting point that you copy, not
something you edit directly.

## Getting started

### Step 1: Get your own copy

This repo's GitHub page has two buttons that both sound like "make a
copy." Use the right one:

- **"Use this template"**: use this one. It creates a new, independent
  repo under your GitHub account, with no link back to this template.
  That's what you want for a portfolio project.
- **"Fork"**: don't use this. It creates a copy that stays linked to this
  one. Forking is for contributing changes back to someone else's
  project.

Click **"Use this template" → "Create a new repository"**. Name it
something like `inventory-tracker`, keep it **public**, and create it.

### Step 2: Set up your tools

- **Python 3:** open Terminal and run `python3 --version`. If it's
  missing, install it from https://python.org or with Homebrew
  (`brew install python3`).
- **VS Code:** you set this up in Module 0.
- **[Python Tutor](https://pythontutor.com/)** (optional): a free browser
  tool for stepping through code line by line. Useful when a variable
  doesn't have the value you expect.

### Step 3: Clone your new repo

On **your** new repo's page (not this template), click the green **Code**
button, copy the HTTPS URL, then in Terminal:

```bash
git clone <the URL you copied>
cd <your-repo-name>
```

### Step 4: Confirm what's already set up

This template already includes `.gitignore`, `LICENSE`, and a git
history. Check that they're there:

```bash
ls -a          # .gitignore should be in the list
cat LICENSE    # should show the MIT License text
git log --oneline
```

Open `LICENSE` and replace `[YOUR NAME]` on the copyright line with your
name. Then commit it:

```bash
git add LICENSE
git commit -m "add my name to LICENSE"
```

## Your scenario and data

Read `SCENARIOS.md` and pick **one** of the 4 stakeholders. Each one's
data file is already in `data/`. Delete the other 3 once you've chosen.
`data/SOURCE.md` lists the edge cases planted in every file.

Before you write code:

1. Re-read your stakeholder's words and sketch what your class needs to
   track.
2. Write down your assumptions (QAR) in `starter/REFLECTION.md`.
3. Trace the first 3 lines of your data file by hand.

## What to do

- `starter/inventory.py` is your script. You design the class. The
  function names are given, but you write the logic and the docstrings.
  `read_batch_file`'s docstring is your model.
- `starter/REFLECTION.md` is the written part, filled in once your script
  runs.
- Run your script from the repo's top folder:
  `python3 starter/inventory.py`
- Commit as you go: after your class works, after validation works, and
  after the full file runs. Don't save it all for one commit at the end.
- `tools/search.html` is optional. See Day 4 of `CHECKLIST_TIMELINE.md`.

## Where's the exact bar for "done"?

Use the **MVP checklist in the LMS**. The same list is in `MVP.md` on the
original template's `project-scope` branch: go to the template on GitHub
and switch branches. Optional stretch work is in the Above & Beyond
section at the bottom of `CHECKLIST_TIMELINE.md`.

When you finish, you'll replace this README with your own. Day 4 of the
checklist lists what to include.
