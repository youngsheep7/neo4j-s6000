from py2neo import Graph, Node, Relationship, NodeMatcher

#connection to db s6000-demo
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1"
)

# definition
attacker_ip = "192.168.13.1"
victim_ip = "101.227.139.217"
log_index = 1
attack_type = "Web漏洞攻击"
relation_attack_log = "attack_related"
relation_victim_log = "victim_related"

# create attack node and relationship
tx = graph.begin()
a = Node("attacker", IP=attacker_ip)
tx.create(a)
l = Node("warninglog", LogIndex=log_index, ATTACKTYPE=attack_type)
al = Relationship(a, relation_attack_log, l)
tx.create(al)

# create victim node and relationship
v = Node("victim", IP=victim_ip)
tx.create(v)
vl = Relationship(v, relation_victim_log, l)
tx.create(vl)
tx.commit()  # this line of codes should be as ending code
