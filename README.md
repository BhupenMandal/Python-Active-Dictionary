#  Active Dictionary

## Task Description
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
We can construct this hierarchy as such. Where User is represented by str representing their ids.
Write a function that provides an efficient look up of whether the user is in a group.


## Explanation
Recursion function is been implemented to search the required element. 
Name of the group is checked first, to check if it matches the name of the user. 
Then each level is checked for the existence of the user. 
When found, simply true is printed on the console, else, False is printed. 

Contains Recursive function which depends on the depth and number of users.
That makes the Space and Time Complexity Big O(m*n)