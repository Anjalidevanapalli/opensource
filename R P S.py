v,c=input().split()
if((v=='S') and (c=='P')) or ((v=='P') and (c=='R')) or ((v=='R') and (c=='S')):
    print("Vignesh")
elif((v=='P') and (c=='S')) or ((v=='R') and (c=='P')) or ((v=='S') and (c=='R')):
    print("Charan")
elif((v=='S') and (c=='R')) or ((v=='P') and (c=='S')) or ((v=='R') and (c=='P')):
    print("Charan")
elif((v=='R') and (c=='S')) or ((v=='S') and (c=='P')) or ((v=='P') and (c=='R')):
    print("Vignesh")
else:
    print("NULL")
