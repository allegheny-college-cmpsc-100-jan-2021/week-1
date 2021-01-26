## Final exercise

Today, we're going to pretend to be spies by _enciphering_ (translating into a secret cipher) and _deciphering_ (translating back out of that secret cipher) a message. In this case we're going to use a rather flimsy strategy, the Caesar Cipher:

>If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others.
>
>Suetonius, _Life of Julius Caesar_

Dude liked to shift stuff `4` characters. Really fooled 'em.

* write a function called `encipher` which accepts one parameter -- an entire coded phrase called `unciphered`
  * this function must shift each letter of the phrase _back_ four positions in the ASCII table
  * this will require use of both `chr` and `ord`
  * `return` the result using the variable `message`

* write a function called `decipher` which accepts one parameter -- an entire coded phrase called `enciphered`
  * this function must shift each letter of the phrase _back_ four positions in the ASCII table
  * this will require use of both `chr` and `ord`
  * `return` the result using the variable `message`
  
A hint: these two functions _very closely resemble each other_. There is only one small, but consequential change to make between them. (In fact, they're practically mirrored.)

As a reminder, recall:

* `chr` accepts `int` code points for letters
* `ord` accepts letters and turns them into `int` code points

Your code must _encipher_ and then _decipher_ a message using the functions you've created. As a goodwill offering:

> Hail, Caesar!

Should encipher to:

> Lemp0 Geiwev%

And, of course, back again.

## Notes

---

This work should be completed in the [f1_week-1-worksheet-codes.py](f1_week-1-worksheet-codes.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in `*.py` files.

There's already some code in the file to get you started.