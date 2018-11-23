from py2neo import Graph, Node, Relationship, NodeMatcher

#connection to db s6000-demo
g = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1"
)

# clear all nodes and relationship from the current graph
g.delete_all()
