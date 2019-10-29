# Stable Matching Algorithm and its Applications 
### Caroline Barker
### NYU Courant Institute of Mathematics
### August 11, 2017

## Table of contents
- [Abstract](#abstract)
- [Introduction](#Introduction)
- [Methods](#methods)
  * [Gale Shapley Algorithm](#Gale-Shapley-Algorithm)
  * [Generating Random Examples](#Generating-Random-Examples)
  * [Quantify Satisfaction in Matches](#Quantify-Satisfaction-in-Matches)
      + [Score Calculations](#Score-Calculations)
      + [Top Percent of Ranks Rewarded](#Top-Percent-of-Ranks-Rewarded)
      + [Penalty Scoring](#Penalty-Scoring)
      + [Difference in Amounts](#Difference-in-Amounts)
- [Results and Discussion](#Results-and-Discussion)
  * [Matching Employees to Projects](#Matching-Employees-to-Projects)
  * [Matching Students to Internships](#Matching-Students-to-Internships)
  * [Internships Have a Capacity Where Students are Unmatched](#Internships-Have-a-Capacity-Where-Students-are-Unmatched)
  * [Students Listed only their Top Preferences](#Students-Listed-only-their-Top-Preferences)
- [Conclusion](#Conclusion)
- [Acknowledgements](#Acknowledgements)
- [References](#References)
- [Appendix](#Appendix)


    
## Abstract
The motivation of this project is to generate an algorithm that can efficiently
create stable matches between two data sets. Using the basic Gale-Shapley algorithm that
produces stable matches, we can further our research through modifying this algorithm to
provide for more complex data sets. Also, by generating an algorithm that would produce large
quantities of random data as well as a generating a metric, we can test the satisfactory rates of the
matches returned from the basic Gale-Shapley algorithm and its modified algorithms. 

## Introduction
*Definition of Stable Matching*: We say that a matching is stable if neither element in the pair
would prefer to be paired with another element in a different pair. 
  Example 1: Internship 1 is matched with student A and internship 2 is matched with
   student B. However, internship 1 prefers student B to student A, internship 2 prefers
   student A to student B, and vice versa student A prefers internship 2 to internship 1, and
   student B prefers internship 1 to internship A. In this, the original matching is referred to
   as unstable.
   
   ![alt text](https://i.ibb.co/TgBSPHC/Capture.png) 
       
The main example: The running example in this paper will be matching students up with
internships. The amount of students and capacity of the internship will change throughout the
paper depending on which example is being used. 

  This project is motivated by the Gale Shapley stable matching algorithm that was
developed in the 1960s and has since been used for practical solutions in the problems of
matching medical students to residency programs, students to schools, internet users to web
services, transplant organs to recipients and much more.
 The most well known application of the stable matching problem was in 1952 by the
admissions process for the medical residency school called the National Resident Matching
Program (NRMP). Based on this admissions process, David Gale & Lloyd Shapley developed an
algorithm that creates stable matches between any two data sets.
 In general, when it comes to matching two different groups of elements or individuals,
we would like to produce optimal matchings, ones that satisfy all individuals. However, in
examples where there are numerous participants, the criteria for optimal matchings are not
always obvious. The Gale-Shapley algorithm, otherwise known as the stable matching problem,
generates the “best” outcomes for either side. It creates stable pairs, guarantees each element is
matched, and makes it so that either element is assigned to its best possible match. 
       

## Methods

### Gale Shapley Algorithm
  The basic Gale-Shapley algorithm creates stable matches for two sets with the same
number of elements. The algorithm takes inputs of each individuals’ preference rankings to
create the matchings. Consider the following example: 

 Example 2: “n” students have applied for “n” internships where there is only room for
   one student in each internship. Each student rates their most preferred internship to their
   least preferred internship while the internships also rank their most preferred student to
   their least preferred student. With these lists of rankings, the algorithm can produce stable
   pairs for the internships and the students, running until all the students and internships are
   matched. 
       
We will describe the Gale Shapley algorithm using Example 2:
1. Each student proposes to their first, most preferred internship.
2. Internships will evaluate all of the proposals that it has received and reject all but the
proposal of the student that it had ranked the most preferred (since theres only four students
and four internships, each internship will only accept one student).
3. In rejecting some of the students, we are left with students that are unmatched and some
projects that are unmatched.
4. The algorithm runs again as there are still students and projects unmatched.
5. Students that have been previously declined, propose to their next most preferred internship.
6. Again the internship only keeps the proposal of the student that it had ranked the highest. 
7. The algorithm runs until there are no more unmatched students and all the internships are
paired with a student.
8. The algorithm returns a list of matched internships to students.
The results of the Gale-Shapley algorithm guarantees two things: 1. All students will be matched
with an internship 2. All pairings will be stable (refer to definition of stable match). We
implemented the Gale-Shapley algorithm in Python (See Appendix A). 


### Generating Random Examples
  Our purpose, and main motivation of generating random examples to be used in the GaleShapley code, 
is to efficiently create sample sets of realistic data that is manually hard togenerate. Given 
two sets A and B, we generate a randomized preference list of each element A by simply creating
a list of the elements of B. This is mostly done using the shuffle function in python’s numpy.random 
package. We create elements B’s preference lists in the same way. For example, say we were to create
a simulation of matching 20 students to 20 internships. The randomization algorithm will generate a 
shuffled list of students named from “employee1” to “employee20” and internships numbered from 1 to 20. 
By using these random examples, we can test multiple scoring methods to find the best way to measure
the satisfactory rates of the participants in the GaleShapley algorithm. Later modifications of the
basic Gale-Shapley algorithm will also call for its own modifications of the random example generator. We
implemented this randomizing algorithm in Python (See Appendix B). 

### Quantify Satisfaction in Matches
  To evaluate the effectiveness of the Gale Shapley algorithm, we must create a scoring
guide, or a metric, that will calculate the satisfaction rate of each match. There are several
different scoring methods that we consider:

  Example 3: There are 3 students Alyssa, Brittney, and Claire and 3 internships Math,
     Physics, and Computer Science. Alyssa was matched by the algorithm with the Physics
     internship, where she had ranked the index of the Physics internship at 1st place. Brittney
     was matched with the Math internship which she had originally ranked third place. And
     lastly Claire was matched by the algorithm with her first ranked internship, Computer
     Science. 

#### Score Calculations
  In this metric, Alyssa’s and Claire’s match will be awarded 30 points since they had been
matched with the internship that they had ranked first preferred. Brittney’s match would be
awarded 10 points because she had been matched with the internship that she had in 3rd place. In
total the overall match score is 70 points.
  Ideally in example 3, we would hope for all students, Alyssa, Brittney, and Claire, to be
paired with their 1st ranked internship, making it so that the accumulation of all matched scores 
for the students would be 90. However, in practical world situations, some internships are more
popular than others, leaving it to the internships to decide for who to choose as their internees.
So by dividing the overall match score by the ideal match score of the students we come up with
the percent student satisfaction: 70 points / 90 points = 77.78% satisfaction.
  The scoring for the overall match score of the internships will be the same where if the
algorithm matched the Computer Science internship with it’s first ranked student, Claire, that
match for the internship would be rewarded 30 points, etc. Again, dividing the overall match
score of the internships by the ideal overall match score will calculate the internship percent
satisfaction.
 Both scorings were implemented in Python (See Appendix C)

#### Top Percent of Ranks Rewarded
 This metric rewards the matches that were within the top 20% of total preferences. Lets
make it so that in example 3, only the first ranked matches will be awarded. This makes it so that
Alyssa’s and Claire’s match will still be awarded 30 points while Brittney’s match is rewarded 0
points.
 The reason for this metric is to reveal the percent of the students who were matched with
the top 20% of their preferences. This metric was implemented in Python (See Appendix D). 

#### Penalty Scoring
 Only applies to unmatched students to internships where for each unmatched student
there would be a 10 point penalty for the Average Student % Satisfactory Score. 

#### Difference in Amounts 
  In this case, since there are more students than the internships, we cant use the “ideal
scoring” for the internships where we multiply the the top score for the internship match by the
capacity size. We would have to add up the total “r” ranks of the internship, since ideally an
internship would receive matchings from the top “r” ranks. From there we again divide the
original score from this new ideal score. However, for the students we can still use scoring 2.3.1. 


## Results and Discussion
### Matching Employees to Projects 
  In this data set we are testing the satisfactory rates of the standard Gale Shapley
algorithm, wherein the number of students are equal to the number of internships “n”. Using the
randomizer referred to in 2.2 we can generate a list of internship rankings and student rankings.
Also using the scoring algorithm in 2.3.1, we can test the satisfactory rates for both the projects
and the employees. We implemented this Gale-Shapley modification into Python (See Appendix
C).
 The following table shows the average satisfaction rates of 30 rounds of different data
sets. The “n” value, or the amount of internships and students, increases by a factor of two every
ten rounds to compare the effect of larger data on the basic Gale-Shapley algorithm. Average % 
Student Satisfaction and Average % Internship Satisfaction is calculated by averaging out the
satisfaction rates of all ten rounds in that set of data. 

![alt text](https://i.ibb.co/hM3q7Qx/Capture.png) 

  We can see in Table 1, as the “n” amount of internships and employees increases, so does
the Average % Student Satisfaction and the Average % Internship Satisfaction. Also, in
agreement with the hypothesis that Gale and Shapley mentioned in their work, the data that
proposed, in this case the students, have a higher satisfaction rate than that of the other data set,
the internships. As we can see, the average student % satisfaction goes up tremendously to about
92% while the Average % Internship Satisfaction stays at around 82%-83%.
 The next table uses another set of data through the randomizer referred to in 2.2 as well
as metric 2.3.2. The “r” value is the top 20% of “n”, so the ratios are the same throughout the
table. In this set of results we are evaluating the % students given their top “r” choices and the %
internships also given their top “r” choices within the matches.

![alt text](https://i.ibb.co/nLQF8Tk/Capture.png)

 Like Table 1, we see in Table 2 as the value of “n” increases so does the % students given
their top “r” and the % internships given their top “r”. However, the values seem to increase
much more dramatically, and start off much lower than Table 1. This is because this metric is
awarding only the top “r” matches, giving all other matches zero points. Also, % Student
Satisfaction increases by two fold and internship satisfaction stays at about 68%-69%, in
agreement with Table 1. 

### Matching Students to Internships 
 This is a modification of Gale Shapley algorithm that uses a more realistic data set where
the amount of students and internships differ. In this case, the internships have a certain capacity
size allowing multiple students to be accepted into a single internship. We implemented this
Gale-Shapley modification into Python (See Appendix E). 

 Example 4: Four students Alison, Brittney, Claire, and Diana are to be paired with
   two internships, Math and Science. Each internship can accept 2 students. Again, all
   students have ranked there most preferred internship to least, and each internship has
   ranked their most preferred student to least. The algorithm will run until both internships
   have two students matched to each. 
   
 To test the satisfactory rates of these pairings we will use the basic concept of the 2.3.4
metric to compare average satisfaction rates of both internships and students.
 In the following table there are a list of “n” values for the students and “m” values for
the internships. However, throughout the ratio of students to internships stay at 10:1 so the
resulting satisfaction rates can be compared. In this figure, we are again evaluating Average %
Student Satisfaction, Average % Internship Satisfaction, and the difference between the two
percentages. 

![alt text](https://i.ibb.co/WWq1s3M/Capture.png)

 In Table 3, we see that both the average student satisfaction rate and the average
internship satisfaction rate goes up as the as the amount of students and internships go up.
However as we look towards the bottom of the table, we see that the difference between the
students and internship satisfaction rate goes into the negatives. This is because the average %
internship satisfaction is higher than the average % student satisfaction, disagreeing with our
previous hypothesis that claims students should have a higher satisfaction rate because they are
the data set proposing. This discrepancy is probably due to the fact that as there are increasingly
more amount of students than internships, making the internships have the room to become more
picky with the students that are accepted.

### Internships Have a Capacity Where Students are Unmatched 
 Even more realistic modification of the algorithm is when internships have a certain
acceptance rate, or a maximum capacity, making it so that some students will be returned
unmatched. 
 In example 4, let’s say that Ellie also decided to apply for both the Math and Science
internship. The capacity for each internship is still two, but now the numbers of students
increased to five. In any matching that were to occur, there will always return a student who is
unmatched. We implemented this Gale-Shapley modification into Python (See Appendix F).
 In the following table we are evaluating the average % student satisfaction and the
average % internship satisfaction as the acceptance rate becomes lower and lower where less
students are matched. While capacity size says the same, the number of students increase making
it so that the acceptance rate is calculated by by dividing the number of potentially accepted
students from the total amount of students. 

![alt text](https://i.ibb.co/rkcLch0/Capture.png)
 As we can see, as soon as the acceptance rate becomes lower than 100%, the average
student satisfaction dramatically lowers while the average internship satisfaction dramatically
increases until almost 100% satisfaction. This is because as the amount of students applying to
the internships increase, so does the pickiness of the internships since they can reject all but the
highest ranked students. 

### Students Listed only their Top Preferences
 In the case that there are numerous internships, students shouldn’t have to list all their
preferences but just the top preferred “k” internships. For this particular metric we will be
incorporating the penalty scoring described in 2.3.3 and using the original 2.3.1 scoring to
evaluate average satisfaction. We implemented this Gale-Shapley modification into Python (See
Appendix G).
 The only variable in this algorithm is the “k” value, or the amount of internships each
student is allowed to list. The amount of students, internships, the capacity size stays the same.
We are also only evaluating the Student % Satisfaction as well as the percent of students that
return unmatched. In the following table, we are evaluating the effect of decreasing the “k”
value. 

![alt text](https://i.ibb.co/KXfqJ3d/Capture.png)

 In evaluating Table 5 we see that the % unmatched students increase as the “k” value
decreases since there are less amount of rankings for the matching algorithm to go off of.
However, student satisfaction seems to go higher even though there is a penalty as well as more
students that are returning unmatched. 

## Conclusion
 This project surrounded the creation of the Gale Shapley algorithm as well as its
modification algorithms. It takes into consideration that stability doesn’t necessarily mean
satisfactory, and generates randomizing algorithms as well as metrics to see the satisfactory rates
of the stable matches. All in all it reinforces the fact that in the basic Gale Shapley algorithm the
proposing side is more satisfied, and in the modifications, satisfactory rates depend on the data
sets that are tested.
 In the future we hope to implement even more modifications such as giving each
internship their individual capacity size, etc. Also we hope to test realistic data, for example data
from New York City public high schools, instead of depending on the randomizing algorithm for
our data sets. Finally in the future we hope to explore or generate an even more efficient or
satisfactory stable matching algorithm. 

## Acknowledgements 
 Huge thanks to Professor Mutiara Sondjaja who made this project possible as well as the NYU Courant
 Institute of Mathematics for this oppurtunity.
 
## References

Austin, D. (2015, March). The Stable Marriage Problem and School Choice. Retrieved August
 11, 2017, from http://www.ams.org/samplings/feature-column/fc-2015-03

Gale, D., & Shapley, L. S. (1996, January). College Admissions and the Stability of Marriage.
 Retrieved from http://www.eecs.harvard.edu/cs286r/courses/fall09/papers/
 galeshapley.pdf

JohanThe Royal Swedish Academy of Sciences, Stable matching: Theory, evidence, and
 practical design. (2012). Retrieved from http://www.nobelprize.org/nobel_prizes/
 economic-sciences/laureates/2012/popular-economicsciences2012.pdf

Stable marriage problem. (2017, July 31). Retrieved from https://en.wikipedia.org/wiki/
 Stable_marriage_problem

Tullis, T. (2014, December 05). How Game Theory Helped Improve New York City's High
 School Application Process. Retrieved August 11, 2017, from https://www.nytimes.com/
 2014/12/07/nyregion/how-game-theory-helped-improve-new-york-city-high-schoolapplication-process.html 
 
 ## Appendix
[Appendix A.](AppendixA.py)

[Appendix B.](AppendixB.py)

[Appendix C.](AppendixC.py)

[Appendix D.](AppendixD.py)

[Appendix E.](AppendixE.py)

[Appendix F.](AppendixF.py)

[Appendix G.](AppendixG.py)

 
