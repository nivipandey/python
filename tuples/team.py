team=['A','B','C','D']
team.append('E')
team.extend(['f','g','h'])
team.remove('C')
x=team.pop(4)
size=len(team)
print("the size of team is:"+str(size))
print("")
print("the players are:=")
for idx,val in enumerate(team):
     print("%s:%s"%(idx,val))
print("")
print("removed player is:"+(x))



