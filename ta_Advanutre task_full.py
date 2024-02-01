#Advanutre task


class Node():
    def __init__ (self,data,weight=0,value=0,depth=0):
        self.data=data
        self.left=None
        self.right=None
        self.children=[]
        self.weight=weight
        self.val=value
        self.depth=depth

class Bintree():
    def __init__(self,root=None):
        self.root=root

    def brintr(self,start=None,tracker=0):    # recursive--- Beautiful pRINT Recursive = BRINTR
        if not start:
            start=self.root
        if start==self.root:
            tracker=0
        output="0  "
        for _ in range(tracker):
            output+=f"{tracker}:  "
        output+=str(start.data)
        output+=str(start.weight)+' '
        output+=str(start.val)+' '
        print(output)
        if start.left:
            self.brintr(start.left,tracker+1)
        if start.right:
            self.brintr(start.right,tracker+1)
            
    def decalgo (self,datalist,weightlist,valuelist,start=None):
        if not start:
            start=self.root
        if datalist != [] and start.depth<=3:
            start.left=Node(start.data + ',  ',start.weight,start.val,start.depth+1)
            if start.depth<3:
                start.right=Node(start.data + ',  '+ datalist[0], start.weight + weightlist[0],start.val + valuelist[0], start.depth + 1 )
            self.decalgo(datalist[1:],weightlist[1:],valuelist[1:],start.left)
            self.decalgo(datalist[1:],weightlist[1:],valuelist[1:],start.right)

class Ntree():
    def __init__(self,root=None):
        self.root=root
    def brintr(self,start=None,tracker=0):    # recursive--- Beautiful pRINT Recursive = BRINTR
        if not start:
            start=self.root
        if start==self.root:
            tracker=0
        output="0  "
        for _ in range(tracker):
            output+=f"{tracker}:  "
        output+=str(start.data)
        output+=str(start.weight)+' '
        output+=str(start.val)+' '
        print(output)
        for thing in start.children:
            self.brintr(thing,tracker+1)

    def decalgo(self,datalist,weightlist,valuelist,start=None):
        if not start:
            start=self.root
        if datalist != [] and start.depth<3:
            if start.weight<=10:
                for i in range(len(datalist)):
                    start.children.append(Node(start.data + ',  '+ datalist[i], start.weight + weightlist[i],start.val + valuelist[i], start.depth + 1 ))
                    
                    self.decalgo(datalist,weightlist,valuelist,start.children[i])



#testcases
a=["Goldener Kelch ","Antike Statue ","Seltener Edelstein ","Historisches Gemälde "]
b=[120,200,250,150]
c=[3,5,2,4]
tav=Bintree()
tav.root=Node("Backpack")
tav.decalgo(a,c,b)
#tav.brintr()
vali=Ntree()
vali.root=Node("Backpack")
vali.decalgo(a,c,b)
vali.brintr()
