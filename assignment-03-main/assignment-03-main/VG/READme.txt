VG

3) pretty_print_subdirectories.py

I firstly have imported OS so that I'm able to get access "getcwd and scandir".I used a function
with one parameter(path). inside the function I have used "try and except" keyword so I would be
able to handle any occuring errors. Inside the "try" block I used "for loop" and"if statment" to
avoid printing the hidden file which might start with "." or "_" in my directory and subdirectories.

7) 7_count_lines.py
I used "import OS" in order to get "getcwd" and able to read by creating a function to open my file
with "with-as" method. I also used "for-loop" so that will read the directory. My second and main
function is "count_py_lines" with one parameter inside. I have used keywords like "startswith" (".")
and "endswith" (.py) so that will be counting the lines inside the files which end with (.py). 
Inside my main function i used "try" and "except" in order to not get any error while the path_dir
go through to read the files or directory.

9) 9_letter_count.py
i used "for loop" that includes "with-as" method to read my file and close it
atomatically. inside the "for loop" i have also used another "for loop" that contains
"strip" to manage API and "lower" keywords that convert the text into lower-case.
I finally have used two f form to concatinate strings and varibales then print it.
