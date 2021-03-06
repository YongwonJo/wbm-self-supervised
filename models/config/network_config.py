# -*- coding: utf-8 -*-

"""
    Configurations for CNN architectures.
"""

ALEXNET_BACKBONE_CONFIGS = {
    'batch_norm': 'bn',
    'local_response_norm': 'lrn'
}


VGGNET_BACKBONE_CONFIGS = VGGNET_ENCODER_CONFIGS = {
    '16.original': {
        'channels': [[64, 64, 'M'], [128, 128, 'M'], [256, 256, 256, 'M'], [512, 512, 512, 'M'], [512, 512, 512, 'M']],
        'batch_norm': False,
    },
    '16.batch_norm': {
        'channels': [[64, 64, 'M'], [128, 128, 'M'], [256, 256, 256, 'M'], [512, 512, 512, 'M'], [512, 512, 512, 'M']],
        'batch_norm': True,
    }
}


RESNET_BACKBONE_CONFIGS = RESNET_ENCODER_CONFIGS = {
    '9.original': {
        'block_type': 'basic',
        'channels': [64] * 1 + [128] * 1 + [256] * 1 + [512] * 1,
        'strides': [1] + [2] + [2] + [2],
    },
    '18.original': {
        'block_type': 'basic',
        'channels': [64] * 2 + [128] * 2 + [256] * 2 + [512] * 2,
        'strides': [1, 1] + [2, 1] + [2, 1] + [2, 1]
    },
    '18.wide': {
        'block_type': 'basic',
        'channels': [64] * 2 + [128] * 2 + [256] * 2 + [512] * 2,
        'strides': [1, 1] + [2, 1] + [2, 1] + [2, 1],
        'widening_factor': 2,
    },
    '34.original': {
        'block_type': 'basic',
        'channels': [64] * 3 + [128] * 4 + [256] * 6 + [512] * 3,
        'strides': [1, 1, 1] + [2, 1, 1, 1] + [2, 1, 1, 1, 1, 1] + [2, 1, 1]
    },
    '34.wide': {
        'block_type': 'basic',
        'channels': [64] * 3 + [128] * 4 + [256] * 6 + [512] * 3,
        'strides': [1, 1, 1] + [2, 1, 1, 1] + [2, 1, 1, 1, 1, 1] + [2, 1, 1],
        'widening_factor': 2,
    },
    '50.original': {
        'block_type': 'bottleneck',
        'channels': [64] * 3 + [128] * 4 + [256] * 6 + [512] * 3,
        'strides': [1, 1, 1] + [2, 1, 1, 1] + [2, 1, 1, 1, 1, 1] + [2, 1, 1]
    },
    '50.wide': {
        'block_type': 'bottleneck',
        'channels': [64] * 3 + [128] * 4 + [256] * 6 + [512] * 3,
        'strides': [1, 1, 1] + [2, 1, 1, 1] + [2, 1, 1, 1, 1, 1] + [2, 1, 1],
        'widening_factor': 2,
    },
}


RESNET_DECODER_CONFIGS = {
    '18.original': {
        'block_type': 'basic',
        'channels': [512] * 2 + [256] * 2 + [128] * 2 + [64] * 2,
        'strides': [2, 1] + [2, 1] + [2, 1] + [2, 1]
    }
}


VGGNET_DECODER_CONFIGS = {
    '3a': [[64, 'U'], [32, 'U'], [16, 'U']],                           # 5 -> 10 -> 20 -> 40
    '3b': [[128, 'U'], [64, 'U'], [32, 'U']],                          # 5 -> 10 -> 20 -> 40
    '3c': [[256, 'U'], [128, 'U'], [64, 'U']],                         # 5 -> 10 -> 20 -> 40
    '6a': [[64, 64, 'U'], [32, 32, 'U'], [16, 16, 'U']],               # 5 -> 10 -> 20 -> 40
    '6b': [[128, 128, 'U'], [64, 64, 'U'], [32, 32, 'U']],             # 5 -> 10 -> 20 -> 40
    '6c': [[256, 256, 'U'], [128, 128, 'U'], [64, 64, 'U']],           # 5 -> 10 -> 20 -> 40
}

GENERATOR_CONFIGS = {
    '3a': [[64], [32], [16]],                                          # 5 -> 10 -> 20 -> 40
    '6a': [[64, 64], [32, 32], [16, 16]],                              # 5 -> 10 -> 20 -> 40
}

DISCRIMINATOR_CONFIGS = {
    '3a': [[16], [32], [64]],                                          # 40 -> 20 -> 10 -> 5
    '6a': [[16, 16], [32, 32], [64, 64]],                              # 40 -> 20 -> 10 -> 5
}
