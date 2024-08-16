# Friday Challenge! Test your skillz!

## Part 1: Setup
1. Run `bash ~/px/scripts/full-setup.sh` to reset the environment containers.

2. Create a directory in `mycode` called `fri_challenge` and cd into it. Next create a file called `secret.txt`. Place a "secret" in `secret.txt` such as a favorite food, book, or dream vacation area.

3. Open the inventory file and create a new group called `working` and place Bender, Fry, Zoidberg, and Indy within.

   `vim ~/mycode/inv/dev/hosts`

## Part 2: Creation
1. Create a playbook called `fri_challenge.yml`. On the play level this playbook should target our new working group. It should also prompt the user with a question about their favorite color. Follow best practices and have a default answer just in case.

2. Create a task that copies `secret.txt` to all the machines. Place the file within a directory called `secret`.

3. Create a series of tasks that creates a directory called `color` and then places our prompt answer inside a file called `color.txt`. This can be achieved in multiple ways! Try experimenting with the File/Shell modules.

## Part 3: Verify
1. Finally, run a post-check task or two that verifies our changes. This can also be done multiple ways!

## Part 4: Bonus
1. Include a pre-check task that shows output before the color file exists.
