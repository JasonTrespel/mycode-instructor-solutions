# Test Yourself!

## Part 1: Setup
1. Create a new directory within `mycode` called `small_challenges` and cd in to it. Next create a playbook called `small_solution01.yml`

   `student@bchd:~$` `mkdir -p ~/mycode/small_challenges`

   `~/mycode/small_challenges` `vim small_solution01.yml`

## Part 2: Creation
1. Within your new playbook target the localhost. Create a task that sends a GET request to one of these Open APIs:
   1. https://swapi.dev/
   2. https://www.anapioficeandfire.com/
  
2. Have the response saved as a variable.

3. Display the contents of that variable to standard out.

## Part 3: Bonus
1. Modify your playbook to target the planetexpress group (exclude Farnsworth). Create a new task that sends a GET request to an API, but then places the response into a file. Copy the file to the target machines.

## Part 4: Xtra Bonus
1. Slice through the JSON response and return the value to a key of your choosing. Read the API documentation to see what keys are available.
