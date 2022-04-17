
import constants as cst

###############################################################################
# USER-SELECTIONS
############################################################################### 
USER_SEL = {
    'size': [int(i*.75) for i in (74, 57)],
    'palette': cst.GB_BLOCK_SUPPLY, # 6,
    'blocks': cst.LIMITLESS_BLOCKS_SUPPLY,
    'priority': cst.LARGE_FIRST_BLOCK_VALUES,
    'verbose': True,
    'scaler': 25,
    'lengthMax': 500,
    'shuffler': 'length', # 'shuffler'
    'shuffleRange': (-5, 5)
}

