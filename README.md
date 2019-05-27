A very simple twitter bot.

This will read from a file called 'datafile' in the same directory which will contain
information about the textfile to read tweets from, the line it is currently on, and
the number of lines in the file:

example:5:25

Will read from a file called 'example', tweet line 5 out of 25, then update the datafile
so it will read from line 6 next tweet. It won't attempt to tweet past line 24 in this
case.

Provide your own text, use text.py to extract lines from a large body of text.
