Title: Optimization Problems
Author: Enrique Rendon
Date: 2019-11-08 10:41
Category: blog
Tags: statistics, data science, python
Slug: intro-to-opt-problems
Status: published


- **Optimization** models:
  * Whenever are solving a problem that
involves finding:
    + the biggest,
    + the smallest,
    + the most,
    + the fewest,
    + the fastest,
    + the least expensive,
    + et cetera.
  * There's a good chance that you can map that problem
onto a classic optimization problem for which there is
a known computational solution.

### What is?

1. An objective function that is to be maximized or minimized.
2. A set of constraints that most be honored.

For example:
 - Minimized the time of travelling from Madrid to Luxembourg:
  * Cannot spend more than 250 EUR / week
  * Must be in Luxembourg before 10:00 AM

##### Takeways:
- Many real problems can be formulated as an optimization problems
- Reducing a new problem to an instance of a well-known problem
- Reuse pre-existing methods to solve it
- Computational challenging (Run for really long time)
- Not usually solved, but approximated solution (Good enough)


##### Knapsack/Bin-packing Problem:
- You have limited strength (Maximum Weight)
- You would like to take more stuff than what can carry
- How do you choose which stuff to take or leave behind?
- Does not have to be a physical one
- Two variants:
  * 0/1 problem  (Harder)
  * Continuous or fractional problem

##### Knapsack Problem, formalized:
- Each item is represented by a pair **<value, weight\>**
- Weight no larger than **w**
- A vector **L**, of length **n**, represents the total set of available items. Each element is an item
- A vector **V**, of length **n**, is used to indicate whether or not items are taken. (1 means taken; 0 means not taken)

Find a V that maximizes:

$$
\sum_{i=0}^{n-1} V[i]*L[i].value
$$

subject to:

$$
\sum_{i=0}^{n-1} V[i]*L[i].weight \leq w
$$
