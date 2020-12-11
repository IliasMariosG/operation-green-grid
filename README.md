# Commit bot
## aka "Operation Green Grid"
### By John Baxter
***
[Scope](#scope) / 
[Motivation](#motivation) / 
[Disclaimer](#disclaimer) / 
[Tech](#tech-used) / 
[Features](#features) / 
[Code example](#code-example) / 
[<u>How to use</u>](#how-to-use) / 
[Future development](#future-development) / 
[Credits](#credits) 

## [^](#by-john-baxter)Scope
This project aims to create a script which will automatically push commits to my 
[GitHub][github] 
account while the program is running.

## [^](#by-john-baxter)Motivation
The motivation for this project came from an offhand jokey comment that was made during a conversation about the process of looking for a job after graduating from a coding bootcamp. \
Hiring managers are apparently keen to see applicants who have been continuing to code on a regular basis, a situation which can be replicated by writing some code that does this for you. \
I took this in the humour that it was intended but also saw it as a learning opportunity; I'd never before made a program which interacted with the command line or any external web based service so I decided to pursue that and see if I could learn how this was done.

## [^](#by-john-baxter)Disclaimer
This program does push commits to my GitHub profile, but has not been used to artificially boost my contributions except for a 
[single weekend][commit-bot-insight-commits] 
where I allowed it to run uninterupted immediately after I had completed writing the first iteration.

## [^](#by-john-baxter)Tech used
The project is written in Python 3\
In the current state the whole project is using the Python standard library with no additional packages.

## [^](#by-john-baxter)Features
The project currently has the following features:
- Opened and run through the command line
- Adds a new line of text consisting of a date-time stamp into a `.txt` file
- Saves, `add`s, `commit`s  and `push`es the new update to GitHub
- Repeatedly adds, puches etc. at random intervals of between 30 and 60 minutes
- Continues running unsupervised until the user stops the program

## [^](#by-john-baxter)Code example
Some of the lines of code as used in the program:
```python
import os
import datetime

os.system("echo '%s' >> time_date_log.txt" % timestamp)
```

## [^](#by-john-baxter)How to use
Users who would like to use this code should do the following:
- Clone this repository to their own machine
- Ensure that they have their GitHub account set up with an 
[SSH key][github-ssh-key-guide]
- Open the command line and navigate to the local version of the repo
- Enter the following command:\
`python3 commit_bot.py`
- Use `Ctrl & C` to exit

## [^](#by-john-baxter)Future development
Ideas for additional functionality that might be able to be implemented include:
- A time limiter that allows the program to run for a finite amount of time
- Options to input the user's choice of random interval (min and/or max)
- Option to input the user's choice of finite running duration

And something that may require a fundamental change to the code:
- Find some way that the code (or similar code) can be run in a more automated way; without the user needing to run and/or stop the program each time.

## [^](#by-john-baxter)Credits
The original idea comes from a fellow Makers alum who should remain nameless as I do not have permission to include their name here. Additional thanks to the numerous bloggers and 
[stack**overflow**][stack-overflow] 
users without whom finding the relevant syntax would have been much more difficult.

[github]: <https://github.com/john-baxter>
[commit-bot-insight-commits]: <https://github.com/john-baxter/operation-green-grid/graphs/commit-activity>
[github-ssh-key-guide]: <https://docs.github.com/en/enterprise/2.15/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>
[stack-overflow]: <https://stackoverflow.com/>
