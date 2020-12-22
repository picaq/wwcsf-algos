# Big-O, or Computational Complexity Analysis

## Go to:
 * [Resources](#resources)
 * [Problem Sets](#problem-sets)
   * [Beginner Exercises](#Beginner-Exercises)
   * [Intermediate Exercises](#Intermediate-Exercises)
   * [Advanced Exercises](#Advanced-Exercises)

___

## Resources

### Beginner resources
- [Big O Notation, Gayle Laakmann McDowell](https://youtu.be/v4cd1O4zkGw): A short video that focuses on conceptual understanding and provides rules of thumb for evaluating run-time
- [Introduction to Big-O, William Fiset](https://youtu.be/zUUkiEllHG0): A good conceptual introduction with worked-through problems and solutions.
- [Asymptotic Notation, Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation): A good introduction to academic definitions of Big-O, Big-Theta, and Big-Omega. 
- [A Beginner’s Guide to Big O Notation- Part 1](https://medium.com/better-programming/a-beginners-guide-to-big-o-notation-pt-1-19ec031b698b): An introduction to time complexity with help from Ratatouille
- [A Beginner’s Guide to Big O Notation- Part 2](https://medium.com/swlh/a-beginners-guide-to-big-o-notation-part-2-c4ede76cea36): An introduction to time complexity with help from Ratatouille

### Intermediate and Advanced Resources
- [Lecture on Asymptotic Notation - Recurrences - Substitution, Master Method, Prof. Erik Demaine, MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-2-asymptotic-notation-recurrences-substitution-master-method/)
- [Lecture on Divide-and-Conquer: Strassen, Fibonacci, Polynomial Multiplication, Prof. Erik Demaine, MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-3-divide-and-conquer-strassen-fibonacci-polynomial-multiplication/)
### Special topics
- [Stanford CS106b handout](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1176/handouts/midterm/5-BigO.pdf): This handout walks through how to analye big - O complexity for loops and recursion.  
- [Ch. 1 Recursion, from Algorithms by Jeff Erickson](http://jeffe.cs.illinois.edu/teaching/algorithms/book/01-recursion.pdf) : A chapter discussing recursion with illustrations to help conceptualize run-time. 
- [Ch. 9 Amortized Analysis, from Algorithms by Jeff Erickson](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/09-amortize.pdf): A chapter presenting various applications of amortized analysis. 
___

## Problem Sets
### Beginner Exercises

#### Learning Goals  
1. Learn definitions of upper bound(Big-O), tight bound (Big-Theta), and lower bound(Big-Omega). What kind of bound do we usually mean by the term 'Big-O'? 
2. Given any function, learn how to drop constants and non-dominant terms to obtain a Big-O bound on that function.
3. Practice analyzing loop structures for run-time.

#### Exercises

1. Provide a tight upper bound on the runtime of the following pseudocode blocks, as a function of the input size *n*. 

    a. 
    ``` 
    sum = 0
    for (i=0; i < n; i++)
        sum += array[i]
    for (j=0;j < n; j++)
        sum -= j
    return sum
    ```

    b. 
    ```
    pairs = []
    for (i=0; i < n; i++)
        for (j=0; j <n; j++)
            pairs.append([i,j])
    ```
    c. 

    ```
    result = 0
    for (i = 0; i < (n / 2); i++)
        for (j = 0; j < 1000i; j++)
            result += i + j
    for (k = 0; k < 500n; k++)
        result -= k
    ```

    d.
    ```
    def isPrime(n)
        for (i = 2; i*i <= n, i++)
            if (n % i) == 0
                return False
        return True
    ```

3. With a partner, discuss a lower bound, an upper bound, and a tight bound on a trip you take often. What factors determine your estimated travel time for each analysis? How do these relate to the concepts of best case, worst case, and average case run time?

4. Write an code block that runs in O(n<sup>2</sup>), and another code block that runs in O(n). Can you alter the second code block so that it is slower than the first code block for some number x, 0 < n <= x?

---

### Intermediate exercises

#### Learning Goals
1. Memorize orders of growth for classes of functions.  
2. Understand the common run-times with logarithms: O(logn) and O(nlogn).
3. Memorize run-times for sorts, searches, traversals, and retrievals for various algorithms and Data Structures.
4. Practice determining the space used during computation.

#### Exercises
1. Review this list classes of functions, ordered from slowest growing to fastest growing. Where would in the list would you insert O(nlogn), also called [log-linear](https://en.wikipedia.org/wiki/Time_complexity#Linearithmic_time) time? Try graphing the functions with [Wolfram Alpha](https://www.wolframalpha.com) to check your answer. (Hint: try entering "plot x log x and x^2 from -1 to 10")

Class | Big-O(n)
---|---
Constant | O(1)
Logarithmic | O(logn)
Linear | O(n) 
Quadratic | O(n<sup>2</sup>)
Cubic | O(n<sup>3</sup>)
Polynominal | O(nk), k > 0
Exponential | O(k<sup>n</sup>), k >1
Factorial | O(n!)

2. What does the code block below do? What is its runtime? Memorize this pattern!
```
pairs = []
for (i = 0; i < n; i++)
    for (j=i+1; j < n; j++)
        pairs.append([i,j])
```

3. Write psuedocode that implements binary search. Provide a tight upper bound on its run-time.

4. Write pseudocode that implements merge sort. Provide a tight upper bound on its run-time.

5. Write a recursive program that prints out the first *n* fibonacci numbers. What is an upper bound on its run time? Now write an iterative version. How does the runtime improve?
---

### Advanced Exercises
#### Learning Opportunities
1. Explore the formal methods you can use to solve recurrences, (those you would find in a textbook or university Algorithms class, like Substitution, Iteration, Master Method). 
2. Know various techniques to trade off time for space, such as hash tables, heaps, sorting.
3. Understand amortized analysis and its applications to various data structures.
4. Memorize various patterns that are common run-times, such as a geometric series, arithmetic series. 

#### Exercises

1. Provide a common algorithm, data structure operation, or generate a code block that runs in the following run-times:  
    a. O(nlogn)  
    b. O(logn)  
    c. O(A + B)  

2. Provide pseuodocode and run-time for an optimal algorithm that implements the following common operations:  
    a. Generate all permutations
    b. Generate all triples  
    c. Generate all (ordered) substrings/subarrays  
    d. Generate all subsets

3. Describe an array resizing scheme such that append operations take constant time, amortized. Can you demonstrate that append operations will take constant time as *n* grows large?

4. Compare naive n-bit multiplication with [Karatsuba multiplication](https://en.wikipedia.org/wiki/Karatsuba_algorithm) and compare the run times. See [pseudocode for the Karastuba algorithm here](https://aaronoah.gitbooks.io/algorithm-cracker/content/divide-and-conquer/multiplication.html). Hint: Write a recurrence relation for each algorithm. The Master Method can apply to the recurrence. View a walk-through of the recurrence solution here: [](https://www.cs.princeton.edu/~wayne/teaching/multiply.pdf)

5. (Hard!) How many ways are there to write a valid string of balanced parantheses with *n* opening parantheses characters '(' and *n* closing parantheses? '('? For an example leetcode problem that applies this concept, see [Leetcode #241: Different Ways to Add Parantheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)
Hint: Don't be satisfied with an upper bound! Can you get it tighter by evaluating the sequence as a sum in terms of the first *n* terms?  
See a good discussion of the solution here on [brilliant.org](https://brilliant.org/wiki/catalan-numbers/#other-appearances-of-the-catalan-numbers) (You may need to make an account).
