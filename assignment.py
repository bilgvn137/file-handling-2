# You can remove 'pass' if you written code in the function
# Exercise 1

def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    file=open(filename,"r")
    sum=0
    c=0
    lst=file.readlines()
    if lst==[]:
        return 0
    else:
        for i in range(len(lst)):
            if lst[i]!="\n":
                a= lst[i].split(",")
                sum += int(a[1])
                c=c+1
        return round(sum/(c),1)
    file.close()
    pass

# Exercise 3
def filter_passed(source, destination, pass_mark):
    file=open(source,"r")
    c=0
    lst=file.readlines()
    for i in range(len(lst)):
        if lst[i]!="\n":
            a=lst[i].split(",")
            if int(a[1])>=pass_mark:
                file1=open(destination,"a")
                file1.write(f"{a[1]}")
                c+=1
                file.close()
    file.close()
    return c
    pass
# Exercise 4
def replace_word(filename, old_word, new_word):
    file=open(filename,"r")
    c=0
    lst=file.readlines()
    for i in range(len(lst)):
        if lst[i]!="\n":
            a=lst[i].split(" ")
            for j in range(len(a)):
                if a[j]==old_word:
                    a[j]=a[j].replace(old_word,new_word)
                    c+=1
    file.close()
    return c
    pass

# Exercise 5
def remove_line(filename, line_number):
    # Write your code here
    pass
