import sys
sys.path.append('../')

from algorithms.group_merging import GroupMergingRank
from algorithms.group_sybil_rank import GroupSybilRank
import graphs
import os
from utils import *

OUTPUT_FOLDER = './outputs/tests_group_merging/'

graph = graphs.generators.group_based.generate({
    'num_groups': 20,
    'num_seed_groups': 5,
    'min_group_nodes': 3,
    'max_group_nodes': 20,
    'max_known_ratio': 1,
    'avg_known_ratio': .5,
    'min_known_ratio': .2,
    'num_seed_nodes': 20,
    'num_attacker_to_num_honest': .1,
    'num_sybil_to_num_attacker': 5,
    'sybil_to_attackers_con': .5,
    'num_joint_node': 0,
    'num_inter_group_con': 2000
})

GroupMergingRank(graph, {
    "thresholds": [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.01, 0]
}).rank()

draw_graph(graph, os.path.join(OUTPUT_FOLDER, '1.html'))

#for node in graph:
#    print node.name, node.rank, node.node_type, [g for g in node.groups]

out1 = generate_output(graph)

reset_ranks(graph)

GroupSybilRank(graph, {
    'min_degree': 2,
    'accumulative': False,
    'weaken_under_min': False,
    'nonlinear_distribution': False,
    'group_edge_weight': 2,
}).rank()
draw_graph(graph, os.path.join(OUTPUT_FOLDER, '2.html'))

out2 = generate_output(graph)

write_output_file([out1, out2], os.path.join(OUTPUT_FOLDER, 'result.csv'))
