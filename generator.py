file=open('temp.txt','w')

for i in range(1,32):
    s='<li><button type="button" id="'+str(i)+'" onclick='+'"myFunc()" class ="btn btn-lg btn-info dates">'+str(i)+'</button></li>'
    file.write(s+"\n")
