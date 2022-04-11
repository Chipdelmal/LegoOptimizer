
import constants as cst

###############################################################################
# USER-SELECTIONS
############################################################################### 
USER_SEL = {
    'size': [int(i*1) for i in (50, 50)],
    'palette': cst.LEGO_LIMITED, # 6,
    'blocks': cst.LIMITLESS_BLOCKS_SUPPLY,
    'priority': cst.LARGE_FIRST_BLOCK_VALUES,
    'verbose': True,
    'scaler': 30,
    'lengthMax': None,
    'shuffler': 'length',
    'shuffleRange': (-3, 3)
}

