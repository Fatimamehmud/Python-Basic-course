# The variable sentence stores a string. Write code 
# 1)that determine how many words in sentence start and end with the same letter, including one-letter words
# 2) Store the result in the variable same_letter_count.
# Hard-coded answers will receive no credit.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
split_step=sentence.split()
same_letter_count=0
for i in split_step:
    if i[0]==i[-1]:
        same_letter_count=same_letter_count+1
print(same_letter_count)
