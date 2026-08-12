# Choose Your Scenario

Pick **one** of the four scenarios below. Each one gives you a stakeholder,
their actual need, and a real batch file of transactions (`data/*.txt`,
430 rows — long enough that you can't just eyeball it for problems).
**None of them tell you what attributes your class needs.** That's
deliberate — figuring out what data actually matters for *this*
stakeholder's problem is part of the assignment. Whichever you pick, delete
the other three data files from your repo so it's clear which one you're
actually using.

## Option 1: Bookstore Inventory

**Stakeholder:** Maya, who owns a small independent used bookstore.

> "I'm still tracking my inventory in a notebook and it's a mess. I need
> something that tells me what I have, lets me look up a title fast when a
> customer asks, and warns me before I run out of something people keep
> buying. Some books are new, some are used — I don't know if that matters
> to you, but it matters to my pricing."

**Data:** `data/bookstore_transactions.txt`

## Option 2: Restaurant Kitchen Inventory

**Stakeholder:** Diego, kitchen manager at a mid-size restaurant.

> "We run out of things mid-service and it's always a scramble. I need to
> know what's low *before* dinner rush, not during it. Some of what we
> stock spoils fast, some doesn't — that's probably relevant. I don't
> care about a fancy interface, I care about not getting caught short on a
> Friday night."

**Data:** `data/restaurant_transactions.txt`

## Option 3: Healthcare / Medical Supplies Inventory

**Stakeholder:** Priya, supply coordinator at a community health clinic.

> "If we run out of gloves or gauze mid-appointment, that's a real
> problem, not an inconvenience. I need to know what's running low, and
> I need whoever builds this to actually think about what could go wrong
> with tracking supplies where getting it wrong has real consequences —
> not just build the happy path."

**Data:** `data/healthcare_transactions.txt`

## Option 4: Athletic Wear / Sporting Goods Inventory

**Stakeholder:** Jordan, manager at a local sporting goods store.

> "Same item, different sizes, and customers ask for a specific one. I
> need to know what's in stock, what's almost out, and I need to be able
> to look something up fast when someone's standing at the counter asking
> for it."

**Data:** `data/athletic_transactions.txt`

## What to do with this

Before writing any code: read your chosen stakeholder's actual words above
again. What are they really asking for? What would you need to track to
answer their real questions (not just "what fields does a spreadsheet
usually have")? That's the design work `starter/inventory.py` asks you to
do yourself — see `MVP.md` for the actual bar, and `README.md` for where
to start.
