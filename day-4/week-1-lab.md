# CMPSC 100: HumanQuest

![Because anything else would be boring](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-humanquest.png)

As a gator who falls prey to the latest trends sweeping the Gator Kingdom, G. Wiz and his friends Slippy Toad, Frogger, and Lyle Crocodile find themselves caught up in playing HumanQuest, a game in which the friends form a party and role-play mundane human jobs and tasks. They've been playing a 10-hour marathon session, and they have one final push through the last day of the week: Friday.

Your job in this activity is to finish the Python file which helps them play out their latest adventure: to survive a normal human workday through a series of encounters with various in-office occupational hazards.

## Requirements

* Evaluate the pre-existing function code in order to understand _and document_ what it does.
  * Use single-line comments (lines prefixed with a `#`)
* Use the `players.txt` and `monsters.txt` files to load the player and monster data, respectively.
* Iterate over the various monsters totaling the _players' total group roll_ and
* Compare it to a _single_ monster's difficulty, noting:
  * if the group wins, they gain a point
  * if the group loses, they lose a point
* At the end of the various encounters: 
  * if the players' total points are positive, they survive
  * if the players' total points are negative, they lose
* `print` each encounter in a format similar to the following:

```
A(n) Spilled Hot Coffee appears!
Spilled Hot Coffee rolls a 15!
G. Wiz rolls a 1!
Slippy Toad rolls a 2!
Frogger rolls a 8!
Lyle rolls a 2!
The group rolled a total of: 13!
The players failed to beat the Spilled Hot Coffee!
```

(There are `5` such encounters.)

* `print` the final verdict: whether the player triumph or fall into the pit of professional despair
  * To give you a sense of professional despair, I require `f-strings` throughout

## Notes

This work should be completed in the [week-1-lab.py](week-1-lab.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in *.py files.

There's already quite some code to help get you started. Your job is to figure out _how to use it_.