# task1
a promodoro


# Task 2
## Cocktail Sort

The script allows user to enter 5 number, it will return a sorted array with using Cocktail sort. Moreover, it also shows the process of how cocktail sort works.

![Image fail to load](https://github.com/cheung921921-rgb/task1/blob/main/Task%202/photo/Cocktail_sort.PNG?raw=true)    


For example, when user enters 5 4 3 2 1, it will return:

Original list: [5, 4, 3, 2, 1]  
After forward pass: [4, 3, 2, 1, 5]  
After backward pass: [1, 4, 3, 2, 5]  
After forward pass: [1, 3, 2, 4, 5]  
After backward pass: [1, 2, 3, 4, 5]  
After forward pass: [1, 2, 3, 4, 5]  
Final sorted list: [1, 2, 3, 4, 5]  

Code explaination :  

The code start at creating a function. Which is used for creating the starting point and the end point of the sorting. And also to create a boolean for determine whether the swapping should run or not.  

The sorting start with forward passing(from start to end of the array), if the element i > larger than its next element i+1, they swap their position. Which means the larger number move backward. Until the largest number reaches the end of the array.  

After that the sorting start at the end of the array and passing backward. As the End of the array has been sorted, end should -1, as well as the start -1 to include element 0. Same as the above, if element i > next element i+1, they swapped. Which means the smaller number swapped to the front as the loop is counting down.  

Moreover, after each sorting, the processed array will be printed.  
