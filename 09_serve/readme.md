## K09: Putting it Together"
## Due: 2024-09-26w


_Step 0: Establish team comms. Fetch KtS._

As a trio...

1. In a new folder in your workshop, save a copy of the flask starter kit, versions 0-4.
1. As a team, for each version, one at a time...
  - Read (for understanding!) through each file.
  - **Note anything notable.**
  - Predict expected behaviors.
  - "Spin up" your website on the loopback interface (a.k.a. "localhost"|127.0.0.1) and reconcile behavior with prediction.
  - Repeat for each successive version.
  - Record your responses as comments in each python file.
1. Once your team has done this, write a flask app to send the output of your occupation-chooser to a webpage:
  - Do this as simply as possible. (A team planning discussion will be in order...)
  - Show a newly-selected occupation upon each reload.
  - Display the list of occupations.
  - Display TNPG+roster at top of served page.
  - PROTIP: Versioning will help. Start with something simple, save a copy as soon as it works, add more features –  then *"lather/rinse/repeat"*. You are welcome/encouraged to save your backups in this work folder, along with CSV file.


DELIVERABLE: Identical code in each teammates' workshop, in specified location.


```
path/to/your/workshop$ tree 09_serve
.
├── app.py
├── occupations.csv
├── readme
├── v0
│   └── app.py
├── v1
│   └── app.py
├── v2
│   └── app.py
├── v3
│   └── app.py
└── v4
    └── app.py
```
