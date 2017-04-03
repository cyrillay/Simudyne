# How to run the code

Step 0 : Download python at https://www.python.org/downloads/

Step 1 : Convert the .xlsx file to a .csv (I used a free online tool like https://convertio.co/fr/xlsx-csv/)
         I included the already converted file in the repository.

Step 2 : Place the .csv file in the same directory as back_end_test.py

Step 3 : Open a command prompt in the directory (on Windows : File>Open a command prompt)

Step 4 : Run the program with the following command : "py back_end_test.py"

Step 5 : Choose your value of brand_factor and press enter

Step 6 : You can find all the output in 2 files:

        - a "data.txt" file that contains each Breed_C Agents, Breed_NC Agents, Breed_C Lost (Switched to Breed_NC), Breed_C Gained (Switch from Breed_NC), Breed_C Regained, for each year.
        
        - a "data.csv" file that only contains the "Breed_C Regained Agents" for the final year. Depending on what you want to export you can select it with the "#OUTPUT" part of the code

Step 7 : You can run the program again with a different value of brand_factor, it will create erase and create new output files.
