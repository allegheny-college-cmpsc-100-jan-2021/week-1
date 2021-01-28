# Final Activity

## Going to `class`

<div class="alert alert-block alert-info">
    This activity will ask you to work in <b>2</b> files. You'll see a file named <b>Cat.py</b> in the <b>worksheets</b> directory and another with the activity's name (<b>f1_week-1-worksheet-oop.py</b>). You'll be doing some work in both.
</div>

Creating `class`es in a single file is fun but, in reality, Python relies on creating these objects in _separate files_. This probably still seems a bit weird.

Acutally, you have the knowledge you need to make the link between the files mentioned in the information box at the top of this file.

Why do we need to `import` `Cat` twice? What's up with this `from` keyword? We need to remember the following order:

1. We use the name of the file where the `class` is located (`Cat.py`)
1. Next, we use the name of the `class` we'd like to `import`

Following these rules: `import Cat from Cat`.

Now, we need to complete a function in `Cat.py` to tell if any two cats are friends. Naturally, if two cats are tabby cats, they are 100% friends.

This function should:

* Accept `2` _parameters_: `self` and another called `cat`
  * As we'll see, `cat` is actually _another `Cat` object_!
* If the two cats are tabby cats (i.e. if `is_tabby` is `True` for both), they're friends; else, they're not
* The result of this function should be a boolean value which:
  * Is `True` if the cats are friends (i.e. are both tabby cats) 
  * Is `False` if cats are not friends (i.e. aren't both tabby cats)
  * Here's a sample: `Ulysses and Munkustrap are friends.`

**The above work should be completed in [the Cat.py file](Cat.py).**

## Notes

This work should be completed in the [f1_week-1-worksheet-oop.py](f1_week-1-worksheet-oop.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in *.py files.

There's already some code in the file to get you started.

This will require you to use a for loop to iterate over the dictionary of our cat friends. As a bonus, using a for loop means that you'll only need to create a Cat object once in the loop!

(This is a grader-specific thing: use the for statement `for cat in cats`.)