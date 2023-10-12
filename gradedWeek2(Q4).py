#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses
# 1)the accumulation pattern to compute the average (sum divided by number of items) 
#2) assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float)
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
split_step=week_temps_f.split(",")
sumnumber=0
for i in split_step:
      sumnumber=sumnumber+float(i)
avg_temp=sumnumber/len(split_step)
print(avg_temp)
