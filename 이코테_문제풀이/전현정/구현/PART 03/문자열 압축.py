def solution(s):
    totalans=[]
    if len(s)==1:
        return 1
    for i in range(1,int(len(s)/2)+1):
        cpr=''
        cnt=1
        ans=''
        for j in range(0,len(s),i):
            temp=s[j:j+i]
            if cpr!=temp:
                if cnt==1:
                    ans+=cpr
                else:
                    ans+=str(cnt)+cpr
                cpr=temp
                cnt=1
            else:
                cnt+=1
        if cnt==1:
            ans+=cpr
        else:
            ans+=str(cnt)+cpr
        totalans.append(len(ans))
    return min(totalans)