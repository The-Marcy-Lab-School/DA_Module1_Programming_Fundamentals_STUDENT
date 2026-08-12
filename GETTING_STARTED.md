# Getting Started

This repo is a **GitHub template** — a starting point, not something you edit
directly on Marcy's copy of it.

## Step 1: Get your own copy

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

## Step 2: Clone your new repo locally

Open **Terminal**, then on your own new repo's page (not this template),
click the green **Code** button, copy the HTTPS URL:

```bash
git clone <the URL you copied>
cd <your-repo-name>
```

## Step 3: Confirm your environment — it's already set up

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

Confirm `python3 --version` works in this folder before going further — if
it doesn't, install Python 3 first (see `README.md`).

## Step 4: Pick your scenario, design before you code

Read `SCENARIOS.md` and pick **one** of the 4 stakeholder scenarios —
delete the other 3 data files from `data/` once you've chosen, so it's
clear which one you're using. Open `starter/inventory.py` — every
function already has a signature; the class and the logic are yours to
design and write. Before writing any code: re-read your stakeholder's
actual words, sketch what your class needs to track and why, and read
through `starter/REFLECTION.md` so you know what your finished script
needs to be able to explain about itself. Trace through the first 2-3
lines of your data file by hand — decide what a valid ADD line looks like
vs. an invalid one — before writing the loop that processes them.

## Step 5: Do the actual project

See `PROJECT_OVERVIEW.md` for what you're building and why, `README.md` for
the data, and `TIMELINE.md` for a suggested day-by-day pace. Commit
incrementally as you go — a `git commit` after your class works, then
another after the batch-processing loop works, not one commit at the very
end. Once your script produces `inventory.json`, use `tools/search.html`
(see that file for how to run it) to interactively confirm your edge cases
actually did what you think they did.

Don't forget the two deliverables beyond the code itself: `REFLECTION.md`
(all 4 sections) and a short project deck (6 slides max, including a live
demo) — see `MVP.md` for exactly what each needs to cover.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` or
`ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting in
your portfolio repo. Ask your instructor for the link to this template's
`project-scope` branch (it'll look like `.../tree/project-scope` on the
*template's* GitHub page, not your own copy) to read them, or check the
checklist your instructor shares through the classroom, which covers the
same ground.
