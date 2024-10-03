# Test Yourself Some More!

## Part 1: Setup
1. In the directory `~/mycode/files` create a `congrats.txt` file. Add a nice, congratulatory message!

   `mkdir -p ~/mycode/files`

   `student@bchd:~/mycode/files` `touch congrats.txt`

## Part 2: Creation
1. Create a playbook that targets the Fry machine. Copy `congrats.txt` to our remote target.

2. Create a handler section that will be notified as soon as the file is copied to Fry. Have the Handler task append a line to the file. Something like, "New line added! Yay!"

3. Up in the regular task section have a task that displays the contents of the file to the screen. This could be done with command or shell. The idea is to see whether the handler task added our new line before we display the file to standard out. 
