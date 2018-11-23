from py2neo import Graph, Node, Relationship, NodeMatcher

g = Graph(    "http://localhost:11004",
    username="neo4j",
    password="123")

'''
a=g.nodes[68] # input different <id> into []
g.delete(a)
'''

matcher = NodeMatcher(g)
x = matcher.match("attacker", name = "Alice").first()
g.delete(x)
