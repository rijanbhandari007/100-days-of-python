
#! multiple ifs means there are different if statements which occur only if it is triggered my previous condition

score = 85

# Each check happens regardless of the others
if score > 70:
    print("You passed!")  # This will run

if score > 80:
    print("You did great!")  # This will also run
