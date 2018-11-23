from py2neo import Graph, Node, Relationship, NodeMatcher

#connection to db
g = Graph(    "http://localhost:11004",
    username="neo4j",
    password="123")

m = NodeMatcher(g)
n = m.match("attacker", name = "12").first()
# n = g.nodes[105] #如果node只剩下标签，只能通过这种方式对nodes进行定位
# n = m.match("attacker", ID = 105).first() #这种写法不能成功

n['age'] = 21 # add/modify new property 'age' to the node
n['name'] = '12' # add/modify name of the node

n['age'] = None # delete existing property

g.push(n)