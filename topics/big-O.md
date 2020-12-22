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
- [Big-O, from B Building Blocks for Theoretical Computer Science, Margaret M. Fleck ](http://mfleck.cs.illinois.edu/building-blocks/version-1.3/big-o.pdf): There may come a time in your learning when you are correctly figuring out the Big-O of any non-recursive code block, but you feel like you understand even less than you did before! If you find yourself asking baffling questions like "but what even is equality?", it's time for you to to read this chapter.
- [A Beginner’s Guide to Big O Notation- Part 1](https://medium.com/better-programming/a-beginners-guide-to-big-o-notation-pt-1-19ec031b698b): An introduction to time complexity with help from Ratatouille
- [A Beginner’s Guide to Big O Notation- Part 2](https://medium.com/swlh/a-beginners-guide-to-big-o-notation-part-2-c4ede76cea36): An introduction to time complexity with help from Ratatouille

### Intermediate and Advanced Resources
- [Back to Back SWE: Deeply Understanding Logarithms In Time Complexities & Their Role In Computer Science](https://youtu.be/M4ubFru2O80)
- [Recurrences, from Algorithms by Jeff Erickson](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/99-recurrences.pdf): Start here to learn how to solve a recurrence (how to write the Big-O for a recursive algorithm in a closed form strictly in terms of the input size *n*). 
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

2. With a partner, discuss a lower bound, an upper bound, and a tight bound on a trip you take often, such as a commute. What factors determine your estimated travel time for each analysis? How do these relate to the concepts of best case, worst case, and average case run time?

3. Write an code block that runs in O(n<sup>2</sup>), and another code block that runs in O(n). Can you alter the second code block so that it is slower than the first code block for some number x, 0 < n <= x?

#### Solutions
1a. O(n)  1b. O(n<sup>2</sup>)  1c. O(n<sup>2</sup>)  1d. O(sqrt(n))  

3. There are many possible answers. Here is an example. The O(n<sup>2</sup>) code block will be faster than the O(n) code block for 0 < n <= 10000. 

```
# O(n^2 code block)
for (i=0; i<n; i++)
    for (j=0; j<n; j++)
    print(i)

# O(n) code block
for (k=0; k<10000n; i++)
    print(i)

```


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
Polynominal | O(n<sup>k</sup>), k > 0
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

#### Solutions
1. O(nlogn) is in-between linear and quadratic time. O(n) < O(nlogn) < O(n<sup>2</sup>)
2. The code block generates all unique pairs. This is a useful and common pattern to memorize. Through careful counting you will find that it generates 1/2(n<sup>2</sup>) pairs, thus it runs in O(n<sup>2</sup>) time. 
3. See [Binary Search, by Geeks for Geeks](https://www.geeksforgeeks.org/binary-search/) for code examples. By discarding half of the search space on every iteration, the algorithm runs in O(logn) time. 
4. See [Merge Sort, by Geeks for Geeks](https://www.geeksforgeeks.org/merge-sort/) for code examples. The sort proceeds by dividing the number of elements to sort in half by each iteration, O(logn). The merge proceeds linearly, O(n). The total run time is the product: O(nlogn). This is a well-known and  efficient sort, so you can use O(nlogn) in general as a best guess for the run-time of any built-in sorting methods. 
5. See [Program for nth Fibonacci Number, by Geeks for Geeks](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/). A recursive implementation will be exponential in about O(2<sup>n</sup>) (for a tighter bound, see discussion [here](https://www.geeksforgeeks.org/time-complexity-recursive-fibonacci-program/). Note that the number of recursive calls takes up O(n) space. An iterative implementation will run in O(n). If the iterative implementation stores only the previous two fibonacci numbers, it will use O(1) space. 

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

4. Compare naive n-bit multiplication with [Karatsuba multiplication](https://en.wikipedia.org/wiki/Karatsuba_algorithm) and compare the run times. See [pseudocode for the Karastuba algorithm here](https://aaronoah.gitbooks.io/algorithm-cracker/content/divide-and-conquer/multiplication.html). Hint: Write a recurrence relation for each algorithm. The recurrence is solvable with the Master Method.

5. (Hard!) How many ways are there to write a valid string of balanced parantheses with *n* opening parantheses characters '(' and *n* closing parantheses? '('? For an example leetcode problem that applies this concept, see [Leetcode #241: Different Ways to Add Parantheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)
Hint: You might see an unfamiliar sequence of integers emerge. In an interview setting, you can and should take an upper bound on this sequence to give an answer to the Big-O runtime. For this exploration, can you explore the sequence, leave it in a non-closed form, and explore its possible applications?

#### Solutions
1a. Merge Sort   1b.  Binary Search  1c. Breadth-first-search over a graph, where A = nodes and B = edges.  

2a. See [Geeks for Geeks: print all permutations of a given string](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/?ref=lbp) for code examples and links out to examples that deal with duplicate elements. In general, there are n! permutations and you usually have to touch each element in a permutation, so we are looking at O(n*n!) time for generating permutations. See [Permutation Generation Algorithms by Robert Sedgewick](https://www.cs.princeton.edu/~rs/talks/perms.pdf) for a disucssion especially on Heap's algorithn, to reduce the **n** term to a constant. 

2b. Generating all triples takes O(n<sup>3</sup>). If that looks like overkill, it's usually because it is. Usually you are looking to filter the possible triples, so you might need to look at all pairs first and memoize their results, reducing your runtime to something in O(n<sup>2</sup>). For an example that optimizes over the brute force solution, see [Geeks for Geeks find a triplet that sum to a given value.](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)

2c. There are O(n<sup>2</sup>) substrings or subarrays. See [Geeks for Geeks: Print Substrings](https://www.geeksforgeeks.org/program-print-substrings-given-string/). This is another common pattern that might be overkill for your application. Consider the [Suffix Tree](https://en.wikipedia.org/wiki/Suffix_tree) as an alternative for generating a searchable tree of substrings in linear time.  

2d. For every element in the input set, the element will either be in a subset or not, so there are O(2<sup>n</sup>) subsets. See [Geeks for Geeks: Backtracking to find all subsets](https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/) for code examples. Again, this is a large growth rate, so you may want to consider whether you need all possible subsets for your problem application.

3. The textbook strategy is to allocate a new array of double the capacity of the original array, and then copy over every element to the new, doubled array. Without knowing the size of the array ahead of time, the doubling and copying will occur every time capactity reaches a power of two; so at push operations for elements numbered 1, 2, 4, 8, 18, 32, 64...n  

    Let's count! How many pushes are expensive, that is, they trigger the doubling and reassignment of all elements pushed so far? An expensive push occurs every power of 2 until we have pushed all *n* elements. There are lgn powers of 2 (in this discussion lg refers to the base 2 logarithm)  All other pushes are inexpensive pushes, so there are n - lgn inexpensive pushes. Thus we have: 

    - (lgn) Expensive pushes occuring at powers of 2.  
        - For every expensive push, we have to copy over the items we have pushed so far. Let's add these up, for all powers of 2 <= n:
            - **1 + 2 + 4 + 8  + ...2^(lgn)**
        - This sum works out to **2^(lgn + 1) - 1** 
            - To see why this is, check out [this post on summing the first x powers of 2](https://math.stackexchange.com/questions/1990137/the-idea-behind-the-sum-of-powers-of-2)
        - Total cost for all expensive pushes is **2^(lgn + 1) - 1**

    - (n - lgn) Inexpensive pushes, these each cost 1. Total cost for all inexpensive pushes is **n - lgn**

    Add the expensive and inexpensive pushes to get the total time for **n** pushes, and find an upper bound on that time:  
        2^(lgn + 1) - 1 + n - lgn =  
        2^lgn * 2 - 1 + n - lgn =  
        2n - 1 + n - lgn  =  
        3n - lgn - 1 =  
        **O(3n)**

    Divide the Big-O total time for n elements, by n, to get the amortized cost of a push for a single element. This is O(3n) / n, so we will get O(1) amortized time for each push.

4. View a walk-through of the recurrence solution here: [Princeton CS Integer Multiplication Slides](https://www.cs.princeton.edu/~wayne/teaching/multiply.pdf).

5. Perhaps during your analysis, you came up with the puzzling pattern 1, 1, 2, 5, 14, 42... not quite all powers of 2 although it is correct that the powers of 2 will give you an upper bound in O(2<sup>n</sup>). Congratulations, you discovered the [Catalan series](https://en.wikipedia.org/wiki/Catalan_number) for yourself! See a good discussion of the solution here on [brilliant.org](https://brilliant.org/wiki/catalan-numbers/#dyck-paths-and-acceptable-sequences) (You may need to make an account).
