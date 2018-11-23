# auto create graph from given excel size(158 * 3)

from py2neo import Graph, Node, Relationship, NodeMatcher
import xlrd
import numpy

# data preparation
path = 'E:/2. NaRi/1. My NaRi Projects/1. neo4j/alert2(1).bak.xlsx'
workbook = xlrd.open_workbook(path)
Data_sheet = workbook.sheets()[0]  # 通过索引获取
rowNum = Data_sheet.nrows  # sheet行数
colNum = Data_sheet.ncols  # sheet列数

# 获取所有单元格的内容
list = []
for i in range(rowNum):
    rowlist = []
    for j in range(colNum):
        rowlist.append(Data_sheet.cell_value(i, j))
    list.append(rowlist)
arr = numpy.delete(list, 0, axis = 0) # delete first row

for i in range(len(arr)):
    # connection to db s6000-demo
    graph = Graph(
        "http://localhost:7474",
        username="neo4j",
        password="1"
    )
    tx = graph.begin()
    m = NodeMatcher(graph)

    # definition
    attacker_ip = arr[i][0]
    victim_ip = arr[i][1]
    log_index = i
    attack_type = arr[i][2]
    relation_attack_log = "attack_related"
    relation_victim_log = "victim_related"

    # check existing node
    check_result = graph.nodes.match("attacker", IP = attacker_ip).first()
    if check_result == None:
        # create attacker node
        a = Node("attacker", IP = attacker_ip)
        tx.create(a)
    else:
        _a = m.match("attacker", IP = attacker_ip).first()
        a = graph.nodes[_a.identity]

    check_result = graph.nodes.match("victim", IP = victim_ip).first()
    if check_result == None:
        # create victim node
        v = Node("victim", IP = victim_ip)
        tx.create(v)
    else:
        _v = m.match("victim", IP = victim_ip).first()
        v = graph.nodes[_v.identity]

    # create log node and relationship
    l = Node("warninglog", LogIndex=log_index, ATTACKTYPE=attack_type)
    al = Relationship(a, relation_attack_log, l)
    tx.create(al)

    vl = Relationship(v, relation_victim_log, l)
    tx.create(vl)
    tx.commit()  # this line of codes should be as ending code