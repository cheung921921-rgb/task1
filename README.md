#Introduction Video Link
https://drive.google.com/file/d/1COxdgyDovX8SEPUazy5TiGcHbIhR928t/view?usp=sharing
# task1
a promodoro
Upon launching, the program will display a main menu. Enter a number from 1 to 5 to select your desired function:

1. Start Pomodoro (Default)
Initiates a standard Pomodoro session. This consists of 25 minutes of focus time followed by a 5-minute break, repeating for a total of 4 rounds.

2. Start Custom Pomodoro
Allows you to customize your timer. You will be prompted to enter your preferred focus duration (in minutes), break duration (in minutes), and the total number of rounds.
(Note: Please enter integer numbers only to prevent errors.)

3. Add Event
Adds a new task or meeting to your schedule. The system will ask for the event name, date (year, month, day), start time (hour, minute), and the duration of the event.
(Note: Please ensure the date and time entered are valid, e.g., avoiding dates like February 30th.)

4. View Calendar
Displays all your scheduled events in chronological order (from earliest to latest). If no events have been added, the system will notify you that the schedule is currently empty.

5. Exit
Safely closes the application. (You can also type q or exit to quit the program).

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

## Graph

The script allows user to create a graph with 5 customized nodes and edges. And also with several function to use.  

First, user have to enter the name of 5 nodes.  
After that, user has to connect the nodes(Below image shows how it works), it can also not connected to any nodes.  

Then, there are three option to choose:
1. Check connection
2. Check shortest distance from node to node
3. exit programme

Enter the corresponding number to use the function. For Option 1, user can check the connection of the node they choose.  

For option 2, user can check the shortest distance from a node to an other node. For example, [A->B,C] , [B->D] . We want to obtain the shortest distance from A to D. The programme will return A,B,D as result.  

