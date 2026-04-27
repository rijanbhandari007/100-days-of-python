
#! lists in python are like arrays where multiple data is stored in a variables. list value starts with 0. we can use append() to insert data at the end of the list. 
#! we can use random() to print random index from the list
#! if we put an index not present in the list, it throws index error

#! nested if are lists that contains 2 or more lists in it 

apple = [1,2,3,4]
ball = [5,6,7,8]

cat = [apple , ball] #! nested if example
print(cat)



states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                     "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america[1] = "pencilvania"

states_of_america.append("rijanbhandari")
print(states_of_america)