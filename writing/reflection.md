# Reflection: Rock, Paper, Scissors Lab

Name: Kathryn Boidock
Date: 02/16/2026

Please answer the following questions after you have completed the programming lab. Write your answers in complete sentences and provide thoughtful responses.

## Comprehension Questions

1. What is the purpose of breaking a program into functions? How did this help you in completing the lab?

Your Response:

It allowed me to recall these functions over and over as needed, instead of repeating the same code. It makes your code not only run smoother, but it looks neater as well. Using these functions, the lab was easier to complete. Instead of rewriting these functions multiple times, I only had to call them.


2. Describe how you validated user input in your version of the Rock, Paper, Scissors game. Why is input validation important?

Your Response:

I asked the user for their input in the get_user_choice() function. This function gets the users input then validated it by checking to see if the input is in the dictionary of valid choices, which are 1, 2, and 3. If not then it checks to see if the input is in the list of rock, paper, and scissors. This makes sure the user enters the correct and needed input, if they don't input one of these values then the rest of the code will not work.

3. How did you use comments and docstrings in your code? Give an example of a helpful comment or docstring you wrote.

Your Response:

I used comments to help organize my code and when rereading it I know exactly what my code does at a glance. Doctrings helps to summarize what a function or module does at a glance. One helpful comment I wrote was `	# main game loop for loop through rounds` in the main() function is important because it summarizes the main for loop of the code.

4. Explain how the computer's move is generated in your program. What Python features did you use to accomplish this?

Your Response:

The library random was important for this part of the code. I use this library in the get_computer_choice() function when I use the .random() function to get the computer's move.

5. What was the most challenging part of refactoring the spaghetti code into a more structured program? How did you overcome this challenge?

Your Response:

The most challenging part of the refactoring was the get user choice. I wasn't sure how to handle the error handling, at leasnt in the way it was supposted to be handled. I took a glance at the spaghetti code and compared the code to what I had and changed my code accordingly.

## Ethical Reflection Questions

1. Why is it important to write code that is easy for others to read and maintain? How does this relate to your responsibilities as a programmer?

Your Response:

It is important as it allows others to really get a grasp on what exactly our code does, and add or replicate it in the case they want to do this. As a programmer it is our job to provide ethical and usable code.

2. Consider the use of open source code (like the spaghetti code provided). What are some ethical considerations when using, modifying, or sharing code written by others?

Your Response:

You need to make sure that the source code is ethically sourced. You don't just want to take code off of the internet and change it around and release it as original content. Asking for permission is important. 

---

(Did you remember to add your name and date at the top of your reflection file?)
(yes)