# -*-coding:Latin-1 -*

#Author : Cyril LAY - Student at UTC
#Date : 03/04/2017

import csv

#0. DATA LOADING

# Loading the data into a list "data"
with open('Simudyne_Backend_Test.csv', 'r') as input_file:
  reader = csv.reader(input_file)
  data = list(reader)

#Opening the output files
#each ofile corresponds to a .csv output file
output_file = open("data.txt", "w")
ofile = open('Breed_C Agents.csv', 'w', newline='')
owriter = csv.writer(ofile, delimiter=',',quoting=csv.QUOTE_ALL)
ofile2 = open('Breed_NC Agents.csv', 'w', newline='')
owriter2 = csv.writer(ofile2, delimiter=',',quoting=csv.QUOTE_ALL)
ofile3 = open('Breed_C Lost Agents.csv', 'w', newline='')
owriter3 = csv.writer(ofile3, delimiter=',',quoting=csv.QUOTE_ALL)
ofile4 = open('Breed_C Gained.csv', 'w', newline='')
owriter4 = csv.writer(ofile4, delimiter=',',quoting=csv.QUOTE_ALL)
ofile5 = open('Breed_C Regained.csv', 'w', newline='')
owriter5 = csv.writer(ofile5, delimiter=',',quoting=csv.QUOTE_ALL)
#end of opening

#row numbers
row_breed = 0 
row_ID = 1
row_age = 2
row_social_grade = 3  #social_grade is the 3rd row of the .csv file
row_payment_at_purchase = 4 #payment at purchase is the 4th row of the .csv file
row_brand = 5
row_price = 6
row_promotions = 7
row_auto_renew = 8
row_inertia = 9


#1. INPUT

brand_factor = 0
while brand_factor < 0.1 or brand_factor > 2.9: #brand_factor must be between 0.1 and 2.9; so we ask again another value
    brand_factor = float(input("Enter your brand_factor, the value must be between 0.1 and 2.9\n"))
#TODO : exception if user enters something different from a number


#2. PROCESSING

lost = [[0] * 15 for _ in range(len(data))]     #lists of booleans, lost/gained/regained[i][year] is true if the the i-th agent has lost/gained/regained Breed_C at the year-th year
gained = [[0] * 15 for _ in range(len(data))]
regained = [[0] * 15 for _ in range(len(data))]  

####MAIN LOOP - Run for 15 years
for year in range(0,15): 

    #DATA LOOP - Loop to iterate through the data and evaluate each agent
    for i in range(1,len(data)):

        if not int(data[i][row_auto_renew]): #auto_renew=False
            #Get the different values from the agent n°i
            payment_at_purchase = float(data[i][row_payment_at_purchase])
            attribute_price = float(data[i][row_price])
            attribute_promotions = float(data[i][row_promotions])
            inertia = float(data[i][row_inertia])
            breed = str(data[i][row_breed])
            social_grade = float(data[i][row_social_grade])
            attribute_brand = float(data[i][row_brand])

            #affinity calculus
            affinity = (payment_at_purchase / attribute_price) + 2 * attribute_promotions * inertia

            #Breed_C->Breed_NC
            if (breed == "Breed_C" and (affinity < (social_grade * attribute_brand))):
                data[i][row_breed] = "Breed_NC"
                lost[i][year] = 1
                regained[i][year] = 0
                gained[i][year] = 0
                continue

            #Breed_NC->Breed_C
            elif (breed == "Breed_NC" and (affinity < (social_grade * attribute_brand * brand_factor))):
                data[i][row_breed] = "Breed_C"
                gained[i][year] = 1
                if lost[i][year-1]:  #if the agent switched to Breed_NC at the last year
                    regained[i][year] = 1
                    lost[i][year] = 0
                continue
                        
        lost[i][year] = 0     #if the agent doesn't match any of the above 
        gained[i][year] = 0
        regained[i][year] = 0
    #END OF DATA LOOP


#3. OUTPUT
        

    output_file.write("\n\nYear n° :"+str(year)+"\n\n")

    
    #Breed_C Agents output
    print("Exporting Breed_C Agents for year " + str(year) + "...\n\n")
    output_file.write("\n\nBreed_C Agents\n\n")
    for i in range(1,len(data)):
        if data[i][row_breed] == "Breed_C":
            output_file.write(str(data[i])+"\n")
            owriter.writerow([data[i],year])
                
    #Breed_NC Agents output
    print("Exporting Breed_NC Agents for year " + str(year) + "...\n\n")
    output_file.write("Breed_NC Agents\n\n")
    for i in range(1,len(data)):
        if data[i][row_breed] == "Breed_NC":
            output_file.write(str(data[i])+"\n")
            owriter2.writerow([data[i],year])
                
    #Breed_C Lost output
    print("Exporting Breed_C Lost Agents for year " + str(year) + "...\n\n")
    output_file.write("Breed_C Lost Agents:\n\n")
    for i in range(1,len(data)):
        if lost[i][year]:
            output_file.write(str(data[i])+"\n")
            owriter3.writerow([data[i],year])
              
    #Breed_C Gained output
    print("Exporting Breed_C Gained Agents for year " + str(year) + "...\n\n")
    output_file.write("Breed_C Gained Agents:\n\n")
    for i in range(1,len(data)):
        if gained[i][year]:
            output_file.write(str(data[i])+"\n")
            owriter4.writerow([data[i],year])

    #Breed_C Regained output
    print("Exporting Breed_C Regained Agents for year " + str(year) + "...\n\n")
    output_file.write("\n\nBreed_C Regained Agents:\n\n")
    for i in range(1,len(data)):
        if regained[i][year]:
            output_file.write(str(data[i])+"\n")
            owriter5.writerow([data[i],year])

    #END OF OUTPUT

####END OF MAIN LOOP
output_file.close()
ofile.close()
ofile2.close()
ofile3.close()
ofile4.close()
ofile5.close()
