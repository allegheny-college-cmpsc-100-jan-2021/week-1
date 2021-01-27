## Final exercise

On any given day of the week, G. Wiz is likely to do any 3 of 7 different things (after that, they get tired). These are all _very serious activities_. Given their ability to forget things, G. Wiz decided to to turn to you -- their comptuationally-inclined friends -- to help create an agenda program to schedule their time.

This list is provided for you in the Python file.

Here's my question to you: on each given day of the week, following my rule above, what would a "schedule" of tasks look like? Here's how it might look:

```
Monday, 01 February, 2021       make potions, think hard about life, adjunct at wizard college
Tuesday, 02 February, 2021      make potions, catch newts, adjunct at wizard college
Wednesday, 03 February, 2021    do political job, think hard about life, shop for hats
Thursday, 04 February, 2021     do political job, polish crystal ball, adjunct at wizard college
Friday, 05 February, 2021       do political job, shop for hats, make potions
Saturday, 06 February, 2021     adjunct at wizard college, make potions, think hard about life
Sunday, 07 February, 2021       do political job, catch newts, think hard about life
```

Your job is to print a calendar for our friend using:

* the `gator_tasks` list
* `2` functions:
  * a method or use of `random` to select 3 items from the list _without repeating_
    * each day _must be a unique set of names_ (i.e. names can't repeat for a given day)
    * there are at least 2 ways to do this
  * a function used to calculate and return formatted dates for the agenda
* to print these after each day in a _formatted string_ (`f-string`) exactly like those above

## Notes

This work should be completed in the [f1_week-1-worksheet-agenda.py](f1_week-1-worksheet-agenda.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in *.py files.

There's already some code in the file to get you started.

### Where might I start?

It may make sense to figure out one of the following things first:

* How do I get a list of 3 random, non-repeating items?
* How might I do the date math?

One convenient use of a `for` loop that we haven't directly discussed is to count a number of iterations:

```python
for i in range(7):
    # Do something 7 times, store incrementing value in i,
    # which makes this run from 0 - 6
```

I will also volunteer the following code snippet, which you can use to calculate _next Monday_:

```python
starting_date = today + timedelta(days=-today.weekday(), weeks=1)
```

In addition, you _could_ challenge yourself to:

* Implement an `input` to allow our gator friend to request a specific number of days in the future to forecast