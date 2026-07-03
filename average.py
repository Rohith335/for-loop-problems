# 06. Given a list of exam scores, use a for loop to calculate the average score and print it.
exam_score=[89,75,95,67,58]
count=0
for x in exam_score:
    count=count+x
    average=count/len(exam_score)
print("average marks:", average)