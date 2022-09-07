import sys
decodename=str(sys.argv[1])
icofind=sys.argv[2]
dn=open(decodename,'r')
dnr=dn.read()
bracket,brackethist=0,0
ico=[]
icocurrent=''
icoend=False
rnii=False
rniiend=False
subject=''
ik=False
userdef=False
for i in dnr:
    if rnii:
        if i=='[':
            bracket+=1
        elif i==']':
            bracket-=1
        if ik:
            if i!="," and bracket==4 and brackethist==4:
                user.write(i)
            if bracket==3:
                subject=''
                ik=False
                rniiend=False
                user.write("\n")
        if rniiend:
            user.write(subject)
            ik=True
            rniiend=False
            brackethist=bracket
            continue
        if userdef:
            userdef=False
            user=open(str(ico[0]),'w')
        if bracket==3 and brackethist==3 and i!="'":
            if i ==',':
                rniiend=True
                continue
            subject+=str(i)
        brackethist=bracket
        if bracket<2 and brackethist<2:
            break
    else:
        if i=='[':
            bracket+=1
        elif i==']':
            bracket-=1
        if icoend:
            if int(icocurrent)==icofind:
                ico.append(icocurrent)
                rnii=True
                continue
            icocurrent=''
            icoend=False
        if bracket==2 and brackethist==2:
            if i ==',':
                icoend=True
                userdef=True
                continue
            icocurrent+=i
        brackethist=bracket
user.close()