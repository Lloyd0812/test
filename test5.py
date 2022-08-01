def test(k):
    key={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    if k=="1":
        return 1
    elif k=="*":
        return "*"
    elif k=="0":
        return 0
    elif k=="#":
        return "#"
    elif len(k)==0:
        return " "
    elif len(k)==1:
        return key[k]
    k1=test(k[1:])
    result=[]
    for i in k1:
        for j in key[k[0]]:
            result.append(i+j)
    return result

k=input('请输入数字：')
print(test(k))