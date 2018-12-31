import sys
sys.path.append('..')

import algorithms
from graphs.node import Node
from utils import *

OUTPUT_FOLDER = './outputs/collusion_separate_sybil/'

graph_params = {
    'num_seed_nodes': 28,
    'num_attacker_to_num_honest': 0.00,
    'num_sybil_to_num_attacker': 2,
    'num_groups': 19,
    'min_group_nodes': 3,
    'max_group_nodes': 25,
    'num_joint_node': 20,
    'num_seed_groups': 2,
    'min_known_ratio': .125,
    'avg_known_ratio': .5,
    'max_known_ratio': 1,
    'sybil_to_attackers_con': 1,
    'num_inter_group_con': 200
}

algorithm_options = {
    'accumulative': False,
    'weaken_under_min': False,
    'min_degree': 8,
    'weaken_seed': 0,
    'nonlinear_distribution': True,
    'group_edge_weight': 20,
    'thresholds': [.36, .24, .22, .21, .20, .19, .18, .12, .06, .04, .02, .01, .005, .004, .003, .002, .0015, .001, .0005, 0],
    # 'weaken_inconsistency_ratio': .1,
    'min_reliable_rank': 0,
}

sybil_to_non_seed = [
    [26, 's1'],
    [26, 's2'],
    [26, 's3'],
    [26, 's4'],
    [26, 's5'],
    [26, 's6'],
    [26, 's7'],
    [26, 's8'],
    # [27, 's1'],
    # [27, 's2'],
    # [27, 's3'],
    # [27, 's4'],
    # [27, 's5'],
    # [27, 's6'],
    # [27, 's7'],
    # [27, 's8'],
    # [28, 's1'],
    # [28, 's2'],
    # [28, 's3'],
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
    ['s3', 's4'],
    ['s5', 's6'],
    ['s7', 's8']
]

sybil_to_seed = [
    [6, 's1'],
    [6, 's2'],
    [6, 's3'],
    [6, 's4'],
    [6, 's5'],
    [6, 's6'],
    [6, 's7'],
    [6, 's8'],
    [7, 's1'],
    [7, 's2'],
    [7, 's3'],
    [7, 's4'],
    [7, 's5'],
    [7, 's6'],
    [7, 's7'],
    [7, 's8'],
    # [8, 's1'],
    # [8, 's2'],
    # [8, 's3'],
    # [8, 's4'],
    # [8, 's5'],
    # [8, 's6'],
    # [8, 's7'],
    # [8, 's8'],
    # [9, 's1'],
    # [9, 's2'],
    # [9, 's3'],
    # [9, 's4'],
    # [9, 's5'],
    # [9, 's6'],
    # [9, 's7'],
    # [9, 's8'],
    # [1, 's1'],
    # [1, 's2'],
    # [1, 's3'],
    # [1, 's4'],
    # [1, 's5'],
    # [1, 's6'],
    # [1, 's7'],
    # [1, 's8'],
    # [2, 's1'],
    # [2, 's2'],
    # [2, 's3'],
    # [2, 's4'],
    # [2, 's5'],
    # [2, 's6'],
    # [2, 's7'],
    # [2, 's8'],
    # [3, 's1'],
    # [3, 's2'],
    # [3, 's3'],
    # [3, 's4'],
    # [3, 's5'],
    # [3, 's6'],
    # [3, 's7'],
    # [3, 's8'],
    # [4, 's1'],
    # [4, 's2'],
    # [4, 's3'],
    # [4, 's4'],
    # [4, 's5'],
    # [4, 's6'],
    # [4, 's7'],
    # [4, 's8'],
    # [5, 's1'],
    # [5, 's2'],
    # [5, 's3'],
    # [5, 's4'],
    # [5, 's5'],
    # [5, 's6'],
    # [5, 's7'],
    # [5, 's8'],
    # [6, 's1001'],
    # [6, 's1002'],
    # [6, 's1003'],
    # [6, 's1004'],
    # [6, 's1005'],
    # [6, 's1006'],
    # [6, 's1007'],
    # [6, 's1008'],
    # [7, 's1001'],
    # [7, 's1002'],
    # [7, 's1003'],
    # [7, 's1004'],
    # [7, 's1005'],
    # [7, 's1006'],
    # [7, 's1007'],
    # [7, 's1008'],
    # [8, 's1001'],
    # [8, 's1002'],
    # [8, 's1003'],
    # [8, 's1004'],
    # [8, 's1005'],
    # [8, 's1006'],
    # [8, 's1007'],
    # [8, 's1008'],
    # [9, 's1001'],
    # [9, 's1002'],
    # [9, 's1003'],
    # [9, 's1004'],
    # [9, 's1005'],
    # [9, 's1006'],
    # [9, 's1007'],
    # [9, 's1008'],
    # [1, 's1001'],
    # [1, 's1002'],
    # [1, 's1003'],
    # [1, 's1004'],
    # [1, 's1005'],
    # [1, 's1006'],
    # [1, 's1007'],
    # [1, 's1008'],
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
    # ['s1', 's2'],
    # ['s3', 's4'],
    # ['s5', 's6'],
    # ['s7', 's8']
]

sybil_edges2 = [
    [6, 's11'],
    [6, 's12'],
    [6, 's13'],
    [6, 's14'],
    [6, 's15'],
    [6, 's16'],
    [6, 's17'],
    [6, 's18'],
    ['s11', 's12'],
    ['s13', 's14'],
    ['s15', 's16'],
    ['s17', 's18']
]

sybil_edges3 = [
    [6, 's21'],
    [6, 's22'],
    [6, 's23'],
    [6, 's24'],
    [6, 's25'],
    [6, 's26'],
    [6, 's27'],
    [6, 's28'],
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
    [6, 's41'],
    [6, 's42'],
    [6, 's43'],
    [6, 's44'],
    [6, 's45'],
    [6, 's46'],
    [6, 's47'],
    [6, 's48'],
    ['s41', 's42'],
    ['s43', 's44'],
    ['s45', 's46'],
    ['s47', 's48']
]

sybil_edges5 = [
    [6, 's51'],
    [6, 's52'],
    [6, 's53'],
    [6, 's54'],
    [6, 's55'],
    [6, 's56'],
    [6, 's57'],
    [6, 's58'],
    ['s51', 's52'],
    ['s53', 's54'],
    ['s55', 's56'],
    ['s57', 's58']
]

sybil_edges6 = [
    [6, 's61'],
    [6, 's62'],
    [6, 's63'],
    [6, 's64'],
    [6, 's65'],
    [6, 's66'],
    [6, 's67'],
    [6, 's68'],
    ['s61', 's62'],
    ['s63', 's64'],
    ['s65', 's66'],
    ['s67', 's68']
]

sybil_edges7 = [
    [6, 's71'],
    [6, 's72'],
    [6, 's73'],
    [6, 's74'],
    [6, 's75'],
    [6, 's76'],
    [6, 's77'],
    [6, 's78'],
    ['s71', 's72'],
    ['s73', 's74'],
    ['s75', 's76'],
    ['s77', 's78']
]

sybil_edges8 = [
    [6, 's81'],
    [6, 's82'],
    [6, 's83'],
    [6, 's84'],
    [6, 's85'],
    [6, 's86'],
    [6, 's87'],
    [6, 's88'],
    ['s81', 's82'],
    ['s83', 's84'],
    ['s85', 's86'],
    ['s87', 's88']
]

sybil_edges9 = [
    [6, 's91'],
    [6, 's92'],
    [6, 's93'],
    [6, 's94'],
    [6, 's95'],
    [6, 's96'],
    [6, 's97'],
    [6, 's98'],
    ['s91', 's92'],
    ['s93', 's94'],
    ['s95', 's96'],
    ['s97', 's98']
]

sybil_edges10 = [
    [6, 's101'],
    [6, 's102'],
    [6, 's103'],
    [6, 's104'],
    [6, 's105'],
    [6, 's106'],
    [6, 's107'],
    [6, 's108'],
    ['s101', 's102'],
    ['s103', 's104'],
    ['s105', 's106'],
    ['s107', 's108']
]


def add_sybils(graph, sybil_edges, group):
    nodes_dic = {node.name: node for node in graph.nodes()}
    edges = []
    for edge in sybil_edges:
        for node_name in edge:
            if node_name not in nodes_dic:
                nodes_dic[node_name] = Node(node_name, 'Sybil', groups=set([group]))
        edges.append((nodes_dic[edge[0]], nodes_dic[edge[1]]))
    graph.add_edges_from(edges)


graph = graphs.generators.group_based.generate(graph_params)
add_sybils(graph, sybil_to_seed, 'sybil_to_seed')
# add_sybils(graph, sybil_to_non_seed, 'sybil_to_non_seed')
# add_sybils(graph, sybil_edges2, 'sybil2')
# add_sybils(graph, sybil_edges3, 'sybil3')
# add_sybils(graph, sybil_edges4, 'sybil4')
# add_sybils(graph, sybil_edges5, 'sybil5')
# add_sybils(graph, sybil_edges6, 'sybil6')
# add_sybils(graph, sybil_edges7, 'sybil7')
# add_sybils(graph, sybil_edges8, 'sybil8')
# add_sybils(graph, sybil_edges9, 'sybil9')
# add_sybils(graph, sybil_edges10, 'sybil10')

outputs = []

# ranker = algorithms.SybilRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'SybilRank'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SybilRank.html'))
#
# reset_ranks(graph)

ranker = algorithms.SybilGroupRank(graph, algorithm_options)
ranker.rank()
outputs.append(generate_output(graph, 'SybilGroupRank'))
draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SybilGroupRank.html'))

reset_ranks(graph)

# ranker = algorithms.GroupSybilRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'IntraGroupWeight'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'IntraGroupWeight.html'))
#
# reset_ranks(graph)

algorithm_options['weaken_seed'] = 5000

ranker = algorithms.SybilGroupRank(graph, algorithm_options)
ranker.rank()
outputs.append(generate_output(graph, 'SGR_weaken_seed'))
draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SGR_weaken_seed.html'))

reset_ranks(graph)

algorithm_options['weaken_seed'] = 0
algorithm_options['min_neighborhood_factor'] = 5

ranker = algorithms.SybilGroupRank(graph, algorithm_options)
ranker.rank()
outputs.append(generate_output(graph, 'SGR_neighbor_factor'))
draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SGR_neighbor_factor.html'))

reset_ranks(graph)

# reset_ranks(graph)
# algorithm_options['weaken_under_min'] = True
#
# ranker = algorithms.SybilRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'SR_weaken'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'SR_weaken.html'))
#
# reset_ranks(graph)
#
# ranker = algorithms.GroupSybilRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'IGW_weaken'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'IGW_weaken.html'))
#
# reset_ranks(graph)
#
# ranker = algorithms.GroupMergingRank(graph, algorithm_options)
# ranker.rank()
# outputs.append(generate_output(graph, 'GroupMerge'))
# draw_graph(graph, os.path.join(OUTPUT_FOLDER, 'GroupMerge.html'))
#
# reset_ranks(graph)

write_output_file(outputs, os.path.join(OUTPUT_FOLDER, 'result.csv'))