import collaborative_attacks as collaborative
import lone_attacks as lone
import manual_attack as manual
from anti_sybil import algorithms

OUTPUT_FOLDER = './outputs/simple_attacks/'
INPUT_FOLDER = './inputs/'
BACKUP_URL = 'https://storage.googleapis.com/brightid-backups/brightid.tar.gz'

# Select Attacks
ATTACKS = {
    'one attacker targeting seeds': lone.targeting_seeds,
    'one attacker targeting top nodes': lone.targeting_honest,
    'one attacker targeting random nodes': lone.targeting_honest,
    'one attacker group target attack': lone.group_attack,
    'one seed as attacker': lone.collsion_attack,
    'one honest as attacker': lone.collsion_attack,
    'one group targeting seeds': collaborative.targeting_seeds,
    'one group targeting top nodes': collaborative.targeting_honest,
    'one group targeting random nodes': collaborative.targeting_honest,
    'one group group target attack': collaborative.group_attack,
    'one group of seeds as attacker': collaborative.collsion_attack,
    'one group of honests as attacker': collaborative.collsion_attack,
    'n groups targeting seeds': collaborative.targeting_seeds,
    'n groups targeting top nodes': collaborative.targeting_honest,
    'n groups targeting random nodes': collaborative.targeting_honest,
    'n groups of seeds as attacker': collaborative.collsion_attack,
    'n groups of honests as attacker': collaborative.collsion_attack,
    # 'manual attack': manual.attack
}

# Attacks options
# number of targets (top seed, top honest or random honest in the different algorithm)
N_TARGETS = 20
# number of sybils
N_SYBILS = 40
# number of attackers
N_ATTACKERS = 20
# number of connections between sybils
N_STITCHES = 100
# number of sybil groups in group target attacks
N_GROUPS = 100
# number of unfaithful seeds in seeds as attacker attacks
N_UNFAITHFUL_SEEDS = 10
# number of unfaithful honests in honests as attacker attacks
N_UNFAITHFUL_HONESTS = 30

# manual attack options
# use `honest_ + integer` format to connect to the honests nodes
# use `seed_ + integer` format to connect to the seed nodes
# use the Brightid of a node to connect to the node
# if use a name that doesn't exists in the graph a new sybil node will create
# When the "top" is True, the `integer` part is the position in the list of the nodes sorted in descending order
MANUAL_ATTACK_OPTIONS = {
    'top': True,
    'connections': [
        ['xGUyVQLYV80pajm8QP-9cfHC7xri49V58k02kqTAiUI', 'sybil1'],
        ['xGUyVQLYV80pajm8QP-9cfHC7xri49V58k02kqTAiUI', 'sybil2'],
        ['xGUyVQLYV80pajm8QP-9cfHC7xri49V58k02kqTAiUI', 'sybil3'],
        ['sybil1', 'sybil2'],
        ['sybil1', 'sybil3'],
    ],
    'groups': {
        'new_group_1': [
            'sybil1',
            'sybil2',
            'sybil3'
        ]
    }
}

ATTACKS_OPTIONS = {
    'one attacker targeting seeds': {'num_seeds': N_TARGETS, 'num_sybils': N_SYBILS, 'stitches': N_STITCHES},
    'one attacker targeting top nodes': {'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'top': True, 'stitches': N_STITCHES},
    'one attacker targeting random nodes': {'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'top': False, 'stitches': N_STITCHES},
    'one attacker group target attack': {'num_sybils': N_SYBILS, 'num_groups': N_GROUPS, 'stitches': N_STITCHES},
    'one seed as attacker': {'attacker_type': 'Seed', 'num_sybils': N_SYBILS, 'stitches': N_STITCHES},
    'one honest as attacker': {'attacker_type': 'Honest', 'num_sybils': N_SYBILS, 'stitches': N_STITCHES},
    'one group targeting seeds': {'num_attacker': N_ATTACKERS, 'num_seeds': N_TARGETS, 'num_sybils': N_SYBILS, 'one_group': True, 'stitches': N_STITCHES},
    'one group targeting top nodes': {'num_attacker': N_ATTACKERS, 'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'one_group': True, 'top': True, 'stitches': N_STITCHES},
    'one group targeting random nodes': {'num_attacker': N_ATTACKERS, 'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'one_group': True, 'top': False, 'stitches': N_STITCHES},
    'one group group target attack': {'num_attacker': N_ATTACKERS, 'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'num_groups': N_GROUPS, 'stitches': N_STITCHES},
    'one group of seeds as attacker': {'attacker_type': 'Seed', 'num_attacker': N_UNFAITHFUL_SEEDS, 'num_sybils': N_SYBILS, 'one_group': True, 'stitches': N_STITCHES},
    'one group of honests as attacker': {'attacker_type': 'Honest', 'num_attacker': N_UNFAITHFUL_HONESTS, 'num_sybils': N_SYBILS, 'one_group': True, 'stitches': N_STITCHES},
    'n groups targeting seeds': {'num_attacker': N_ATTACKERS, 'num_seeds': N_TARGETS, 'num_sybils': N_SYBILS, 'one_group': False, 'stitches': N_STITCHES},
    'n groups targeting top nodes': {'num_attacker': N_ATTACKERS, 'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'one_group': False, 'top': True, 'stitches': N_STITCHES},
    'n groups targeting random nodes': {'num_attacker': N_ATTACKERS, 'num_honests': N_TARGETS, 'num_sybils': N_SYBILS, 'one_group': False, 'top': False, 'stitches': N_STITCHES},
    'n groups of seeds as attacker': {'attacker_type': 'Seed', 'num_attacker': N_UNFAITHFUL_SEEDS, 'num_sybils': N_SYBILS, 'one_group': False, 'stitches': N_STITCHES},
    'n groups of honests as attacker': {'attacker_type': 'Honest', 'num_attacker': N_UNFAITHFUL_HONESTS, 'num_sybils': N_SYBILS, 'one_group': False, 'stitches': N_STITCHES},
    'manual attack': MANUAL_ATTACK_OPTIONS
}

# Select Algorithms
ALGORITHMS = {
    'SybilRank': algorithms.SybilRank,
    # 'GroupSybilRank_V1': algorithms.V1GroupSybilRank,
    'GroupSybilRank': algorithms.GroupSybilRank,
    'WeightedSybilRank': algorithms.WeightedSybilRank,
    # 'IntraGroupWeight': algorithms.GroupSybilRank,
    # 'GroupMergingRank': algorithms.GroupMergingRank,
}

# Algorithms options
ALGORITHMS_OPTIONS = {
    'SybilRank': {'accumulative': False, 'nonlinear_distribution': False},
    'GroupSybilRank_V1': {'accumulative': False, 'nonlinear_distribution': False},
    'GroupSybilRank': {'accumulative': False, 'nonlinear_distribution': False},
    'WeightedSybilRank': {'accumulative': False, 'nonlinear_distribution': False},
    'IntraGroupWeight': {'group_edge_weight': 5},
    'GroupMergingRank': {'thresholds': [.36, .24, .18, .12, .06, .04, .02, .01, .005, .004, .003, .002, .0015, .001, .0005, 0]},
}