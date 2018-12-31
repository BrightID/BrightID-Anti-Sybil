import sys
sys.path.append('..')

import algorithms
from graphs.node import Node
from utils import *

OUTPUT_FOLDER = './outputs/mixed_graph_attacks/'

graph_params_1 = {
    'num_seed_nodes': 18,
    'num_attacker_to_num_honest': 0.0,
    'num_sybil_to_num_attacker': 2,
    'num_groups': 19,
    'min_group_nodes': 3,
    'max_group_nodes': 33,
    'num_joint_node': 36,
    'num_seed_groups': 1,
    'min_known_ratio': .125,
    'avg_known_ratio': .5,
    'max_known_ratio': 1,
    'sybil_to_attackers_con': 1,
    'num_inter_group_con': 360
}

graph_params_2 = {
    'start_node': 1000,
    'num_seed_nodes': 18,
    'num_attacker_to_num_honest': 0.0,
    'num_sybil_to_num_attacker': 2,
    'num_groups': 19,
    'min_group_nodes': 3,
    'max_group_nodes': 33,
    'num_joint_node': 360,
    'num_seed_groups': 1,
    'min_known_ratio': .125,
    'avg_known_ratio': .5,
    'max_known_ratio': 1,
    'sybil_to_attackers_con': .5,
    'num_inter_group_con': 360
}

graph_params_3 = {
    'start_node': 2000,
    'num_seed_nodes': 18,
    'num_attacker_to_num_honest': 0.10,
    'num_sybil_to_num_attacker': 2,
    'num_groups': 19,
    'min_group_nodes': 3,
    'max_group_nodes': 33,
    'num_joint_node': 36,
    'num_seed_groups': 1,
    'min_known_ratio': .125,
    'avg_known_ratio': .5,
    'max_known_ratio': 1,
    'sybil_to_attackers_con': 1,
    'num_inter_group_con': 360
}

algorithm_options = {
    'accumulative': False,
    'nonlinear_distribution': True,
    'group_edge_weight': 20,
    'thresholds': [.36, .24, .22, .21, .20, .19, .18, .17, .16, .15, .14, .13, .12, .11, .10, .09, .08, .07, .06, .055, .05, .045, .04, .02, .01, .005, .004, .003, .002, .0015, .001, .0005, 0],
}

sybil_edges1 = [
    [26, 's1'],
    [26, 's2'],
    [26, 's3'],
    # [26, 's4'],
    # [26, 's5'],
    # [26, 's6'],
    # [26, 's7'],
    # [26, 's8'],
    [27, 's1'],
    [27, 's2'],
    [27, 's3'],
    # [27, 's4'],
    # [27, 's5'],
    # [27, 's6'],
    # [27, 's7'],
    # [27, 's8'],
    [28, 's1'],
    [28, 's2'],
    [28, 's3'],
    # [28, 's4'],
    # [28, 's5'],
    # [28, 's6'],
    # [28, 's7'],
    # [28, 's8'],
    # [29, 's1'],
    # [29, 's2'],
    # [29, 's3'],
    # [29, 's4'],
    # [29, 's5'],
    # [29, 's6'],
    # [29, 's7'],
    # [29, 's8'],
    # [21, 's1'],
    # [21, 's2'],
    # [21, 's3'],
    # [21, 's4'],
    # [21, 's5'],
    # [21, 's6'],
    # [21, 's7'],
    # [21, 's8'],
    # [22, 's1'],
    # [22, 's2'],
    # [22, 's3'],
    # [22, 's4'],
    # [22, 's5'],
    # [22, 's6'],
    # [22, 's7'],
    # [22, 's8'],
    # [23, 's1'],
    # [23, 's2'],
    # [23, 's3'],
    # [23, 's4'],
    # [23, 's5'],
    # [23, 's6'],
    # [23, 's7'],
    # [23, 's8'],
    # [24, 's1'],
    # [24, 's2'],
    # [24, 's3'],
    # [24, 's4'],
    # [24, 's5'],
    # [24, 's6'],
    # [24, 's7'],
    # [24, 's8'],
    # [25, 's1'],
    # [25, 's2'],
    # [25, 's3'],
    # [25, 's4'],
    # [25, 's5'],
    # [25, 's6'],
    # [25, 's7'],
    # [25, 's8'],
    # [20, 's1'],
    # [20, 's2'],
    # [20, 's3'],
    # [20, 's4'],
    # [20, 's5'],
    # [20, 's6'],
    # [20, 's7'],
    # [20, 's8'],
    # [26, 's1001'],
    # [26, 's1002'],
    # [26, 's1003'],
    # [26, 's1004'],
    # [26, 's1005'],
    # [26, 's1006'],
    # [26, 's1007'],
    # [26, 's1008'],
    # [27, 's1001'],
    # [27, 's1002'],
    # [27, 's1003'],
    # [27, 's1004'],
    # [27, 's1005'],
    # [27, 's1006'],
    # [27, 's1007'],
    # [27, 's1008'],
    # [28, 's1001'],
    # [28, 's1002'],
    # [28, 's1003'],
    # [28, 's1004'],
    # [28, 's1005'],
    # [28, 's1006'],
    # [28, 's1007'],
    # [28, 's1008'],
    # [29, 's1001'],
    # [29, 's1002'],
    # [29, 's1003'],
    # [29, 's1004'],
    # [29, 's1005'],
    # [29, 's1006'],
    # [29, 's1007'],
    # [29, 's1008'],
    # [21, 's1001'],
    # [21, 's1002'],
    # [21, 's1003'],
    # [21, 's1004'],
    # [21, 's1005'],
    # [21, 's1006'],
    # [21, 's1007'],
    # [21, 's1008'],
    # ['s1001', 's1002'],
    # ['s1003', 's1004'],
    # ['s1005', 's1006'],
    # ['s1007', 's1008'],
    # ['s1001', 's2'],
    # ['s1003', 's4'],
    # ['s1005', 's6'],
    # ['s1007', 's8'],
    # ['s1', 's1002'],
    # ['s3', 's1004'],
    # ['s5', 's1006'],
    # ['s7', 's1008'],
    ['s1', 's2'],
    ['s1', 's3'],
    ['s3', 's2'],
    # [6, 26]
]

sybil_edges2 = [
    [1026, 's1b'],
    [1026, 's2b'],
    [1026, 's3b'],
    [1027, 's1b'],
    [1027, 's2b'],
    [1027, 's3b'],
    [1028, 's1b'],
    [1028, 's2b'],
    [1028, 's3b'],
    ['s1b', 's2b'],
    ['s1b', 's3b'],
    ['s3b', 's2b'],
]


sybil_edges1b = [
    [0, 's21'],
    [0, 's22'],
    [0, 's23'],
    [1, 's21'],
    [1, 's22'],
    [1, 's23'],
    [2, 's21'],
    [2, 's22'],
    [2, 's23'],
    # [3, 's21'],
    # [3, 's22'],
    # [3, 's23'],
    # [4, 's21'],
    # [4, 's22'],
    # [4, 's23'],
    # [5, 's21'],
    # [5, 's22'],
    # [5, 's23'],
    # [6, 's21'],
    # [6, 's22'],
    # [6, 's23'],
    # [7, 's21'],
    # [7, 's22'],
    # [7, 's23'],
    # [8, 's21'],
    # [8, 's22'],
    # [8, 's23'],
    # [9, 's21'],
    # [9, 's22'],
    # [9, 's23'],
    # [10, 's21'],
    # [10, 's22'],
    # [10, 's23'],
    # [11, 's21'],
    # [11, 's22'],
    # [11, 's23'],
    # [12, 's21'],
    # [12, 's22'],
    # [12, 's23'],
    # [13, 's21'],
    # [13, 's22'],
    # [13, 's23'],
    ['s21', 's22'],
    ['s21', 's23'],
    ['s22', 's23'],
]

sybil_edges2b = [
    [1000, 's21b'],
    [1000, 's22b'],
    [1000, 's23b'],
    [1001, 's21b'],
    [1001, 's22b'],
    [1001, 's23b'],
    [1002, 's21b'],
    [1002, 's22b'],
    [1002, 's23b'],
    ['s21b', 's22b'],
    ['s21b', 's23b'],
    ['s22b', 's23b'],
]

sybil_edges3 = [
    [16, 's21'],
    [16, 's22'],
    [16, 's23'],
    [16, 's24'],
    [16, 's25'],
    [16, 's26'],
    [16, 's27'],
    [16, 's28'],
    # [6, 's31'],
    # [6, 's32'],
    # [6, 's33'],
    # [6, 's34'],
    # [6, 's35'],
    # [6, 's36'],
    # [6, 's37'],
    # [6, 's38'],
    ['s21', 's22'],
    ['s23', 's24'],
    ['s25', 's26'],
    ['s27', 's28'],
    # ['s31', 's32'],
    # ['s33', 's34'],
    # ['s35', 's36'],
    # ['s37', 's38'],
    # ['s21', 's32'],
    # ['s23', 's34'],
    # ['s25', 's36'],
    # ['s27', 's38'],
    # ['s31', 's22'],
    # ['s33', 's24'],
    # ['s35', 's26'],
    # ['s37', 's28'],
]

sybil_edges4 = [
    [16, 's41'],
    [16, 's42'],
    [16, 's43'],
    [16, 's44'],
    [16, 's45'],
    [16, 's46'],
    [16, 's47'],
    [16, 's48'],
    ['s41', 's42'],
    ['s43', 's44'],
    ['s45', 's46'],
    ['s47', 's48']
]

sybil_edges5 = [
    [16, 's51'],
    [16, 's52'],
    [16, 's53'],
    [16, 's54'],
    [16, 's55'],
    [16, 's56'],
    [16, 's57'],
    [16, 's58'],
    ['s51', 's52'],
    ['s53', 's54'],
    ['s55', 's56'],
    ['s57', 's58']
]

sybil_edges6 = [
    [16, 's61'],
    [16, 's62'],
    [16, 's63'],
    [16, 's64'],
    [16, 's65'],
    [16, 's66'],
    [16, 's67'],
    [16, 's68'],
    ['s61', 's62'],
    ['s63', 's64'],
    ['s65', 's66'],
    ['s67', 's68']
]

sybil_edges7 = [
    [16, 's71'],
    [16, 's72'],
    [16, 's73'],
    [16, 's74'],
    [16, 's75'],
    [16, 's76'],
    [16, 's77'],
    [16, 's78'],
    ['s71', 's72'],
    ['s73', 's74'],
    ['s75', 's76'],
    ['s77', 's78']
]

sybil_edges8 = [
    [16, 's81'],
    [16, 's82'],
    [16, 's83'],
    [16, 's84'],
    [16, 's85'],
    [16, 's86'],
    [16, 's87'],
    [16, 's88'],
    ['s81', 's82'],
    ['s83', 's84'],
    ['s85', 's86'],
    ['s87', 's88']
]

sybil_edges9 = [
    [16, 's91'],
    [16, 's92'],
    [16, 's93'],
    [16, 's94'],
    [16, 's95'],
    [16, 's96'],
    [16, 's97'],
    [16, 's98'],
    ['s91', 's92'],
    ['s93', 's94'],
    ['s95', 's96'],
    ['s97', 's98']
]

sybil_edges10 = [
    [16, 's101'],
    [16, 's102'],
    [16, 's103'],
    [16, 's104'],
    [16, 's105'],
    [16, 's106'],
    [16, 's107'],
    [16, 's108'],
    ['s101', 's102'],
    ['s103', 's104'],
    ['s105', 's106'],
    ['s107', 's108']
]

connectors = [
    [101, 1101],
    [101, 1103],
    [101, 1104],
    [101, 1105],
    [101, 1105],
    [101, 1106],
    [101, 1107],
    [101, 1108],
    [102, 1101],
    [102, 1102],
    [102, 1103],
    [102, 1104],
    [102, 1105],
    [102, 1106],
    [102, 1107],
    [102, 1108],
    [103, 1101],
    [103, 1102],
    [103, 1103],
    [103, 1104],
    [103, 1105],
    [103, 1106],
    [103, 1107],
    [103, 1108],
    [104, 1101],
    [104, 1102],
    [104, 1103],
    [104, 1104],
    [104, 1105],
    [104, 1106],
    [104, 1107],
    [104, 1108],
    [105, 1101],
    [105, 1102],
    [105, 1103],
    [105, 1104],
    [105, 1105],
    [105, 1106],
    [105, 1107],
    [105, 1108],
    [106, 1101],
    [106, 1102],
    [106, 1103],
    [106, 1104],
    [106, 1105],
    [106, 1106],
    [106, 1107],
    [106, 1108],
    [107, 1101],
    [107, 1102],
    [107, 1103],
    [107, 1104],
    [107, 1105],
    [107, 1106],
    [107, 1107],
    [107, 1108],
    [108, 1101],
    [108, 1102],
    [108, 1103],
    [108, 1104],
    [108, 1105],
    [108, 1106],
    [108, 1107],
    [108, 1108],
    [101, 102],
    [101, 103],
    [101, 104],
    [101, 105],
    [102, 103],
    [102, 104],
    [102, 105],
    [103, 104],
    [103, 105],
    [104, 105],
    [106, 107],
    [107, 108],
    [1107, 108],
    [1101, 102],
    [1101, 103],
    [1101, 104],
    [1101, 105],
    [1102, 103],
    [1102, 104],
    [1102, 105],
    [1103, 104],
    [1103, 105],
    [1104, 105],
    [1106, 107],
    [1106, 108],
    [1107, 108],
]


def add_sybils(graph, sybil_edges, group):
    nodes_dic = {node.name: node for node in graph.nodes()}
    edges = []
    for edge in sybil_edges:
        for node_name in edge:
            if node_name not in nodes_dic:
                nodes_dic[node_name] = Node(node_name, 'Sybil', groups=set([group, group + '-2']))
        edges.append((nodes_dic[edge[0]], nodes_dic[edge[1]]))
    graph.add_edges_from(edges)


graph_1 = graphs.generators.group_based.generate(graph_params_1)

# graph_2 = graphs.generators.group_based.generate(graph_params_2)
# graph_3 = graphs.generators.group_based.generate(graph_params_3)

# add_sybils(graph, connectors, 'connectors')
add_sybils(graph_1, sybil_edges1, 'sybil1')
add_sybils(graph_1, sybil_edges1b, 'sybil1b')
# add_sybils(graph_2, sybil_edges2, 'sybil2')
# add_sybils(graph_2, sybil_edges2b, 'sybil2b')
# add_sybils(graph, sybil_edges3, 'sybil3')
# add_sybils(graph, sybil_edges4, 'sybil4')
# add_sybils(graph, sybil_edges5, 'sybil5')
# add_sybils(graph, sybil_edges6, 'sybil6')
# add_sybils(graph, sybil_edges7, 'sybil7')
# add_sybils(graph, sybil_edges8, 'sybil8')
# add_sybils(graph, sybil_edges9, 'sybil9')
# add_sybils(graph, sybil_edges10, 'sybil10')

# graph = nx.compose(graph_1, graph_2)
# graph = nx.compose(graph, graph_3)

outputs = []

# ranker = algorithms.SybilRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'SybilRank_mixed'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SybilRank_mixed.html'))
#
# reset_ranks(graph)
#
# ranker = algorithms.SybilGroupRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'SybilGroupRank_mixed'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SybilGroupRank_mixed.html'))
#
# reset_ranks(graph)
#
# ranker = algorithms.GroupSybilRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'IntraGroupWeight_mixed'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'IntraGroupWeight_mixed.html'))
#
# reset_ranks(graph)
#
# ranker = algorithms.GroupMergingRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'GroupMerge_mixed'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'GroupMerge_mixed.html'))

ranker = algorithms.SybilRank(graph_1, algorithm_options)
ranker.rank()
outputs.append(generate_output(graph_1, 'SybilRank_sparse_out'))
draw_graph(graph_1, os.path.join(OUTPUT_FOLDER, 'SybilRank_sparse_out.html'))

reset_ranks(graph_1)

# ranker = algorithms.SybilGroupRank(graph_1, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_1, 'SybilGroupRank_sparse_out'))
# draw_graph(graph_1, os.path.join(OUTPUT_FOLDER, 'SybilGroupRank_sparse_out.html'))
#
# reset_ranks(graph_1)
#
# ranker = algorithms.GroupSybilRank(graph_1, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_1, 'IntraGroupWeight_sparse_out'))
# draw_graph(graph_1, os.path.join(OUTPUT_FOLDER, 'IntraGroupWeight_sparse_out.html'))
#
# reset_ranks(graph_1)
#
# ranker = algorithms.GroupMergingRank(graph_1, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_1, 'GroupMerge_sparse_out'))
# draw_graph(graph_1, os.path.join(OUTPUT_FOLDER, 'GroupMerge_sparse_out.html'))

# ranker = algorithms.SybilRank(graph_2, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_2, 'SybilRank_dense'))
# draw_graph(graph_2, os.path.join(OUTPUT_FOLDER, 'SybilRank_dense.html'))
#
# reset_ranks(graph_2)
#
# ranker = algorithms.SybilGroupRank(graph_2, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_2, 'SybilGroupRank_dense'))
# draw_graph(graph_2, os.path.join(OUTPUT_FOLDER, 'SybilGroupRank_dense.html'))
#
# reset_ranks(graph_2)
#
# ranker = algorithms.GroupSybilRank(graph_2, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_2, 'IntraGroupWeight_dense'))
# draw_graph(graph_2, os.path.join(OUTPUT_FOLDER, 'IntraGroupWeight_dense.html'))
#
# reset_ranks(graph_2)
#
# ranker = algorithms.GroupMergingRank(graph_2, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_2, 'GroupMerge_dense'))
# draw_graph(graph_2, os.path.join(OUTPUT_FOLDER, 'GroupMerge_dense.html'))
#
# ranker = algorithms.SybilRank(graph_3, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_3, 'SybilRank_sparse_in'))
# draw_graph(graph_3, os.path.join(OUTPUT_FOLDER, 'SybilRank_sparse_in.html'))
#
# reset_ranks(graph_3)
#
# ranker = algorithms.SybilGroupRank(graph_3, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_3, 'SybilGroupRank_sparse_in'))
# draw_graph(graph_3, os.path.join(OUTPUT_FOLDER, 'SybilGroupRank_sparse_in.html'))
#
# reset_ranks(graph_3)
#
# ranker = algorithms.GroupSybilRank(graph_3, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_3, 'IntraGroupWeight_sparse_in'))
# draw_graph(graph_3, os.path.join(OUTPUT_FOLDER, 'IntraGroupWeight_sparse_in.html'))
#
# reset_ranks(graph_3)
#
# ranker = algorithms.GroupMergingRank(graph_3, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph_3, 'GroupMerge_sparse_in'))
# draw_graph(graph_3, os.path.join(OUTPUT_FOLDER, 'GroupMerge_sparse_in.html'))
#
write_output_file(outputs, os.path.join(OUTPUT_FOLDER, 'result.csv'))
