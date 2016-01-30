
def findNodePrefix(prefix):
    return str(prefix[0])

def nodePos(prefix,infix):
    return infix.find(findNodePrefix(prefix))
    
    

def infixLeft(infix,prefix):
    nodePosition = nodePos(findNodePrefix(prefix),infix)
    infixleft = infix[:nodePosition]
    return infixleft

def infixRight(infix,prefix):
    infixright = infix[nodePos(findNodePrefix(prefix),infix)+1:]
    return infixright

def prefixLeft(prefix,infix):
    prefixleft = ""
    for i in prefix[1:]:
        if i in infixLeft(infix,prefix):
            prefixleft+=i
    return prefixleft

def prefixRight(prefix,infix):
    prefixright = ""
    for i in prefix[len(prefixLeft(prefix,infix))+1:]:
        if i in infixRight(infix,prefix):
            prefixright += i  
    return prefixright
def validation(format1, format2):
    if (set(format2) != set(format1)) or (len(format1) != len(format2)):
        return False
    for i in format1 :
        if format2.count(i) != format1.count(i):
            return False
    return True

def showNodes(prefix,infix,i):
    if not validation(prefix, infix):
        print ("ERROR")
        return 0
    i+=1
    print (findNodePrefix(prefix)+':'+ str(i)+'>')
    if len(infixLeft(infix,prefix))>0:
        print("<L")
        showNodes(prefixLeft(prefix,infix),infixLeft(infix,prefix),i)
    if len(infixRight(infix,prefix))>0:
        print("<R")
        showNodes(prefixRight(prefix,infix),infixRight(infix,prefix),i)

def showNodes2(prefix,infix,i):
    if not validation(prefix, infix):
        print ("ERROR")
        return 0
    i+=1
    node = findNodePrefix(prefix)
    
    print ("("+node+")")
    print '------------------'
    if len(infixLeft(infix,prefix))>0:
        print("["+node+"]<L")
        showNodes2(prefixLeft(prefix,infix),infixLeft(infix,prefix),i)
    if len(infixRight(infix,prefix))>0:
        print("["+node+"]<R")
        showNodes2(prefixRight(prefix,infix),infixRight(infix,prefix),i)
def showNodes3(prefix,infix,node):
    if not validation(prefix, infix):
        print ("ERROR")
        return 0
    root = findNodePrefix(prefix)
    node.update({root:{"<":None,">":None}})
    print '------------------'
    if len(infixLeft(infix,prefix))>0:
        prefixleft = prefixLeft(prefix,infix)
        infixleft = infixLeft(infix,prefix)
        node[root]["<"] = findNodePrefix(prefixleft)
        showNodes3(prefixleft,infixleft,node)
    if len(infixRight(infix,prefix))>0:
        prefixright= prefixRight(prefix,infix)
        infixright = infixRight(infix,prefix)
        node[root][">"] = findNodePrefix(prefixright)
        showNodes3(prefixright,infixright,node)
    return root
