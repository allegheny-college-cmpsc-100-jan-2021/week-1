# Worksheet 1.0.f1: Counting Vowels

Knowing what we now know about strings, your final task is to combine a bit of knowledge we already have with a bit more that we gained in this worksheet. Your task is to write code that:

* takes `input` from the keyboard
* contains at least `5` _original_ comments (not copies of the `TODO` comments)
* counts the total number of vowels in the `string` (vowels: `a`,`e`,`i`,`o`,`u`)
* counts the number of each individual vowel
* `print`s the total count of vowels
* `print`s the total count for _each vowel_
  * The letter should be separated from the number by a tab (`\t`)
* Looks like the output below:

```
Enter a string:

Your input string: THE STRING INPUT ABOVE

The string has # vowels:
e       8
i       4
a       2
u       1
o       3
```

This must pass the test case input:

```
The wizard quickly jinxed the gnomes before they vaporized.
```

Keep in mind:

* captial `A` and lowercase `a` are _different_
  * Your program should be able to handle _both_
* there are at least 3 different ways to do this, but they almost all involve:
   * a `for` loop
   * at least one method (likely more)
* this is the perfect application for a `dictionary` whose `keys` are the individual vowels

## Notes

---

This work should be completed in the [f1_week-1-worksheet-letters.py](f1_week-1-worksheet-letters.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in `*.py` files.

There's already some code in the file to get you started.