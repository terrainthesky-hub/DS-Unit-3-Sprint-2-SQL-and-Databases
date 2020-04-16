# ACID and Database Scalability Tradeoffs

Comparing the costs and benefits of relational and non-relational approaches -
can we have the best of both worlds?

## Learning Objectives

- Understand and explain the advantages and disadvantages of traditional SQL
  databases
- Make informed decisions about alternative databases

## Before Lecture

So far in this sprint you've used SQLite, PostgreSQL, and MongoDB. For each of
these, consider the following questions:

- What was easy about using this technology?
- What was hard about using this technology?
- What more would you like to learn about it?

Write a summary in the style of a possible blog post, and bring the
questions/discussion to class. Bonus - later on, follow up and complete a real
blog post about different database technologies!

This technology had some barriers to entry. It requires certain parameters on intake which make the process of transfering data from one type of database to another fairly involved. I'd like to learn more about the value of using mongodb because relational databases seem more straightfoward in terms of what you would expect in how they operate.

## Live Lecture Task

We covered a lot of ground this week - today we'll bring it together, both
summarizing and resolving lingering questions. We'll also continue the
discussion from the before lecture activity, and explore the cutting edge
"NewSQL" techniques in active development.

As time allows, we'll go back to practicing good old SQL. It's important to have
a broad awareness of the database universe, but SQL is a time-tested tool that
has and will continue to be useful across a wide range of situations. It will
also be the largest part of the sprint challenge, and likely a component of many
job interviews.

## Assignment

Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:

- How many passengers survived, and how many died?
342 survived
545 died
- How many passengers were in each class?
216
487
184

- How many passengers survived/died within each class?
Survived:
87
119
136
Died:
80
368
97
- What was the average age of survivors vs nonsurvivors?
Survived:
28.4083918128655
Died:
30.1385321100917
- What was the average age of each passenger class?
38.7889814814815
25.1887474332649
29.8686413043478
- What was the average fare by passenger class? By survival?
PC:
84.1546874999999
13.7077073921971
20.6621831521739
Survival:
22.2085840366972
48.3954076023392
- How many siblings/spouses aboard on average, by passenger class? By survival?
PC:
0.41666666666666666667
0.62012320328542094456
0.40217391304347826087
Survival:
0.55779816513761467890
0.47368421052631578947

- How many parents/children aboard on average, by passenger class? By survival?
PC:
0.35648148148148148148
0.39630390143737166324
0.38043478260869565217

Survival:
0.33211009174311926606
0.46491228070175438596


- Do any passengers have the same name?
SELECT titanic."Name"
FROM titanic
GROUP BY titanic."Name"
HAVING count(*) > 1

I don't think so, that query tells me 0.

- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.

## Resources and Stretch Goals

The assignment drilled core SQL, but *didn't* review joins - revisit the RPG
data, and do more joins (explicit or implicit) to make sure you understand how
to connect data across tables.

If you got the Titanic data in your MongoDB cluster - see if you can also answer
the above questions using MongoDB!

Read up on [database
normalization](https://en.wikipedia.org/wiki/Database_normalization) - a variety
of formal techniques for reducing the redundancy of data stored in a relational
database.

Keep working on your written summary from the "before lecture" exercise, and
grow it into a proper blog post. Consider focusing it on one particular
technology or technique, and compare/contrast it with the alternatives.

Get more reps in! Check out [SQLBolt](https://sqlbolt.com/) and [w3schools SQL
Tutorial](https://www.w3schools.com/sql/), both of which include interactive
exercises. Mastering SQL is all about practice, so get it down now and you'll be
confident for your job interviews.
