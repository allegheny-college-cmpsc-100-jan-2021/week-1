# CMPSC 100: Jan 2021, Week 1

* Distributed: 25 January, 2021
* Due: 31 January, 2021

## Point values

The following table lists point values for all of the week's various pieces.

|Type         |Point value          |
|-------------|---------------------|
|Worksheets   |75 pts.              |
|Lab          |100 pts.             |
|Participation|50 pts.              |
|             |                     |
|Total        |225 pts.             |
|             |22.5% of course total|

## A few reminders

This repository represents an entire week of content -- and you'll receive a repository like this at the beginning of week. A couple of things that this means:

1. You are free to work ahead of our course's pace if you want to engage, knowing that we'll cover each day sequentially.
2. Each day is "gradeable" by itself; simply `cd` to the `day-{N}` and run GatorGrader to get your progress on a given day's content.

You're also free to wait for us to address each day's topics in class. Regardless, all work for a given week is due _the Sunda after it is assigned_. Due dates are at the top of the `README.md` file in the lowest-level folder (this file).

## Student support

At any time -- during class, after class -- filing a "support ticket" guarantees that either I or a TL will be in contact about your issue. However, _it is your responsibility_ to schedule office hours with either myself or a TL to discuss your ticket in the most detail.

You can file support tickets here:

* [https://chomp.link/support-tickets](https://chomp.link/support-tickets)

(A bookmark might not hurt.)

## Accepting the assignment

---

- [ ] Log into the `#assignments` channel in our class [Slack](https://cmpsc-100-00-ja-2021.slack.com)
- [ ] Click the link provided for the lab assignment and accept it in GitHub classroom
- [ ] Once the assignment finishes building, click the link to go to your personal repository assignment

## "Cloning" a repository

### Using the correct download link

- [ ] On this repository's page, click the `Clone or download` button in the upper right hand corner
* You may need to scroll up to see it
- [ ] In the upper right corner of the box that appears, click `Use SSH`
- [ ] Copy the link that appears in the textbox below the phrase "Use a password with a protected key."

#### Cloning

* [ ] Type `ls` in your terminal window
* You should be in your `~` directory
- [ ] Once there, "clone" the repository using the link copied above
  * If I (the instructor) were to clone my own repository, I'd enter (your link will look different):

```
git clone git@github.com:allegheny-college-cmpsc-100-jan-2021/cmpsc-100-jan-2021-week-1-dluman
```

## Wrap-up

---

### GatorGrader

GatorGrader is an Allegheny College-developed, student-written and maintained application that grades your work for you. The long and short of it, before and when you turn in your assignments, you can know what your approximate grade will be.

(It doesn't do _everything_ for us, but it gives us a good starting point for evaluating your work.)

You don't need to do anything to get it -- I will distribute all the files you need with every repository. You realize the following benefits:

* Complete grading transparency
* Grading criteria _never_ changes
* The criteria is very specific; you will know what changes you need to make

This application runs in your terminal tab, and can grade:

* The whole repository
* Just worksheets
* Just the lab

## Checking your work

---

No matter where you are in your repository, the command to start and run GatorGrader is always the same:

```
gradle grade
```

However, you need to be _in the right place_ to get the right result (i.e. the right `day-{N}` folder).

### Submitting the assignment/saving progress

The GitHub platform is a place to store your work. So, it makes some sense that should be able to _clone_ (download) from it, and push back (upload) to it. Here, we'll learn this second part.

- [ ] `cd` to your `~` folder
- [ ] Locate your `cmpsc-100-jan-2021-week-1` folder and `cd` to it.

Once in this folder, we need to tell git that there have been changes.

- [ ] Type `git add .` and press `Enter`
* This tells git to look through the _entire_ folder structure for new changes and "stage" them

- [ ] Type `git commit -m "YOUR COMMIT MESSAGE"` to "label" the commit
* This is typically something like `git commit -m "Fixing a typo"` -- the message in quotes should be as descriptive as possible, while still remaining somewhat short

- [ ] To send all changes to the server, type `git push`
- [ ] At the prompt, input the password associated with the `SSH Key` you created earlier in this exercise (yesterday)

Once the process finishes successfully, we're done!

#### A strong warning

<div class="alert alert-block alert-danger">
    <p><strong>While we may use this server to store code, <u>you</u> are responsible for using GitHub as your main backup.</strong></p>
    <p>While I back this server up on a regular basis, I cannot guarantee that I'll have the ability to restore up-to-the-minute data for your work.</p>
    <p>Remember: to err is human; to back up your work is divine.</p>
</div>
