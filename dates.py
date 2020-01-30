from datetime import datetime,timedelta,date

a=[{'start':{'dateTime': '2020-01-26T13:00:00+05:30'},'end':{'dateTime': '2020-01-26T14:00:00+05:30'}},{'start':{'dateTime': '2020-01-25T11:00:00+05:30'},'end':{'dateTime': '2020-01-25T11:45:00+05:30'}}]
b=[{'start':{'dateTime': '2020-01-26T10:15:00+05:30'},'end':{'dateTime': '2020-01-26T11:00:00+05:30'}},{'start':{'dateTime': '2020-01-25T14:45:00+05:30'},'end':{'dateTime': '2020-01-25T15:30:00+05:30'}}]
l=[a,b]
l1={}
m=int(input("enter time in minutes:"))
p1=datetime.strptime(input(), '%Y-%m-%d %H:%M:%S')
q1=datetime.strptime(input(), '%Y-%m-%d %H:%M:%S')
#q1=int(input())
while(p1<=q1):

    #p=datetime(2020,1,p1,9,0,0)
    #q=datetime(2020,1,p1,17,0,0).astimezone().isoformat()
    p=p1
    q=p1+timedelta(hours=8)
    q=q.astimezone().isoformat()
    a1=0
    a2=1
    while(1):
    #t1=datetime(2020,1,25,9,0,0).astimezone().isoformat()
        t11=p+timedelta(minutes=a1)
        t1=t11.astimezone().isoformat()
        t22=p+timedelta(minutes=m*a2+a1)
        t2=t22.astimezone().isoformat()
    #t2=datetime(2020,1,25,9+(m*a2)/60,0,0).astimezone().isoformat()
        if(t1>q or t2>q):
            break
        a1+=30
    #a2+=1
        flag = 1
        for x in l:
            for event in x:
                j=event["start"]["dateTime"]
                k=event["end"]["dateTime"]
                if((j<=t1 and k>=t2) or (j<t1 and t1<k and k<t2) or (j>t1 and t2>j and k>t2) or (j>=t1 and k<=t2)):
                    #print("break")
                    flag=0
                    break
            if flag==0:
                break
        if flag:
            #l1.append([t1,t2])
            x=p1.date()
            if x not in l1:
                l1[x]=[(t1,t2)]
            else:
                l1[x].append((t1,t2))
    p1=p1+timedelta(days=1)
print(l1)
for x in l1:
    print(x)




