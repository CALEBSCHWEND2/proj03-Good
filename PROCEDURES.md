## ASSIGNMENT COMPLETION PROCEDURES

Use the following steps to complete this single-script project part.

1. **Follow the instructions to complete the assignment**

    - Open the README in this folder for the instructions.
    - Write your code in the supplied Python script file (`escape.py`).

2. **Run the script to test it yourself**

    Choose one of the following options to run your scripts. _**This is
    primarily how you should test your script**_. The automated tests provide
    little to no feedback, so you will not be able to "debug" your scripts using
    automated tests alone.

    **Option 1**

    From the _terminal_, navigate to this project part folder
    using the `cd` command. For example:
    ```bash
    cd project03-yourusername/
    ```

    Then you can execute your script using directly. For example:
    ```bash
    python escape.py
    ```

    **Option 2**

    Alternatively you can simply execute your scripts using full relative paths.
    For example:
    ```bash
    python project03-yourusername/escape.py
    ```

3. **Test the script**

    To ensure that you got the assignment correctly, you can run local tests before
    you submit your code. If the code passes the test, you are good to submit. If
    not, you can check the test(s) that failed and fix your code.

    Follow these steps to test your code:

    - Click on the beaker icon on the left tab.
    - Locate the test you want to run.
    - Click on the play arrow to run the test.
    - If it is green, the test passed and you should be good to submit this
      assignment.
    - If it is red, you possibly made a mistake. Check the error in the test "Test
      Results" tab on the view at the bottom of the screen (same location as the
      Terminal view)
    - Repeat the above after each significant change and before you submit.

## General Tips

- Make sure to frequently save and push your changes to your GitHub repository.
- Run your code after each significant modification.
  + Also run the automated test for this assignment after each
    change when you are "done" but still tweaking.
- Commit and sync your code before you stop working for the day to ensure that
  your repository and Codespace stay in sync and you don't risk losing your work.

## How to Submit

Most of you will now choose to use the VSCode Source Control extension to submit
your assignments. However, you can always use the terminal.

- Use the VS code Source Control Tab to submit your assignment:
    - Click the + next to the list of "Changes" to stage all changes that
      you have made.
    - Write a commit message, e.g., "Finished with part 1" or "Finished with
      assignment"
      > _**YOU MUST SUPPLY A COMMIT MESSAGE OR YOU WILL GET ERRORS THAT YOU MAY
      > OR MAY NOT EVEN NOTICE**_
    - Click "Commit"
    - Click "Sync"
      > _**IF YOU DO NOT "Stage" ALL CHANGES, THEN YOU MUST `push` INSTEAD OF
      > `sync`.**_ To do this, either:
      > 
      > - click the ellipsis (...) to the right of the**v SOURCE CONTROL**
      >   header (this is the lower of the two things that say "SOURCE
      >   CONTROL"...yes this is confusing) and select Push
      > 
      > or:
      >
      > - instead of clicking "Commit" in the previous step, click the down
      >   arrow and select Commit & Push.

- Alternatively, you can use git to add, commit, and push your changes. Make
  sure you are in your `project03-yourusername` folder. `cd` your way there if not.
  Then type:
  
  ```bash
  git add .
  git commit -m "YOUR MEANINGFUL MESSAGE"
  git push
  ```
