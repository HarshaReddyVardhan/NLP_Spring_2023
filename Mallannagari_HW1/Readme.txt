This Folder has 5 .py files and 1 input file.

1. currency.py
2. date.py
3. driver.py
4. phone_numbers.py
5. tags.py

driver.py is the main file from which the program can start.

The input file contains the input_data for testing the regular expressions.
the date.py file contains multiple patterns.

The output contains:
The input line 
in the next line, if any thing matches,
the matched ones are printed to the console.
if nothing matches the next line is printed and follows.

OUTPUT SAMPLE :
$954.49 
Found Valid Currency :  <re.Match object; span=(0, 7), match='$954.49'>

09804309876
Found Valid Mobile Number :  <re.Match object; span=(0, 11), match='09804309876'>

<span> this is nothing </span>
Found a Line with tags :  <re.Match object; span=(0, 30), match='<span> this is nothing </span>'>

January 05, 1960 February 20, 2025
Date Matched with pattern 1 :  <re.Match object; span=(0, 16), match='January 05, 1960'>
Date Matched with pattern 1 :  <re.Match object; span=(17, 34), match='February 20, 2025'>