
def check_even():
    with open('practice2.txt','r') as f:
        data=f.read()
        list1=data.split(',')
        count=0
        result=[int(x) for x in list1]
        for i in range(0,len(result)):

            
            if(result[i]%2==0):
                count+=1
        return count

print(check_even())
