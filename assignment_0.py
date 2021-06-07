############### QUESTION 1 ##########################

print("################ QUESTION 1 ###############")
n=[386,462,47,418,907,344,236,375,823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
  758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
   626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
    894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
     958,743, 527]
for x in n:
    if x==237:
        
        print(x)
        break
    elif x%2==0:
        print(x)

############ QUESTION 2 ############################
        
print("################ QUESTION 2 ###############")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1-color_list_2)


################Question 3 ###########
##Given a string check if it is Pangram or not.
##A pangram is a sentence containing every letter in the English Alphabet.
## Lowercase and Uppercase are considered the same.
print('Question 3 (pangram) -->')
UP=LO=0
In=input('Enter a string :--')
for T in In:
    if T.islower():
        LO  = LO+1
    if T.isupper():
         UP =UP+1
if LO>0 and UP>0:
        print('Input String is Pangram')
else :
    print('Input String not a Pangram')
print('-'*20)


####################### QUESTION 4 ################################

print("################ QUESTION 4 ###############")
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

###################### QUESTION 5#################################

print("################ QUESTION 5 ###############")
n = input('Enter the string in required fashion : ')
a = n.split('#')
list_1 = a[0].split()
list_2 = a[1].split()
list_1 = [int(i) for i in list_1]
list_2 = [int(i) for i in list_2]

print('list 1 : ',list_1)
print('list 2 : ',list_2)

######################### QUESTION 6#############################

print("################ QUESTION 6 ###############")
i = input("Input comma separated sequence of words::")
words = [word for word in i.split(",")]
print(",".join(sorted(list(set(words)))))



######################################
#question 7
print("Answer:7 ",end =" ")
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakh'],'Marks': [57,87,67,79]}
marks_list = d['Marks']
max_marks = max(marks_list)
max_marks_index = marks_list.index(max_marks)
student_list = d['Student']
print(student_list[max_marks_index])
print('-'*20)
######################################
#question 8
print("Answer:8 ",end =" ")
t ="HelloWorld131 !"
l =0
n =0
for i in range(len(t)):
    if(t[i].isalpha()):
        l+=1
    elif(t[i].isdigit()):
        n+=1
print('LETTERS ' + str(l))
print('DIGITS ' + str(n))

print()

#################################################################
# question 9
print("Answer:9 ",end =" ")
d = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

d1 = {'Name' : [],'Ratings' : []}
index = 0
for sub in d['Subject']:
    if(sub == 'Python'):
        d1['Name'].append(d['Name'][index])
        d1['Ratings'].append(d['Ratings'][index])
    index += 1

print('New dictionary: ',d1)

print("################ QUESTION 10 ###############")
class generator_class :
    def __init__(num,n):
        num.n = n
  
    def generator_function(num) :
        for i in range(0,num.n + 1):
            if(not i%7):
                yield i
n = int(input('Enter the value of n : '))
gen = generator_class(n)
gen_list = list(gen.generator_function())
print('List of numbers divisible by 7 in the range 0 and ',n,' = ',gen_list)

print("################ QUESTION 11 ###############")
up = eval(input('UP : '))
down = eval(input('DOWN : '))
left = eval(input('LEFT : '))
right = eval(input('RIGHT : '))

net_up = abs(up - down)
net_right = abs(right - left)

total_distance = (net_up**2 + net_right**2)**0.5

print('distance = ',round(total_distance))



