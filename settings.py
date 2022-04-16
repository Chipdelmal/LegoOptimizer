
import constants as cst

###############################################################################
# USER-SELECTIONS
############################################################################### 
USER_SEL = {
    'size': [int(i*.25) for i in (74, 57)],
    'palette': cst.LEGO_LIMITED, #cst.GB_BLOCK_SUPPLY, #cst.LEGO_LIMITED, # 6,
    'blocks': cst.LIMITLESS_BLOCKS_SUPPLY,
    'priority': cst.LARGE_FIRST_BLOCK_VALUES,
    'verbose': True,
    'scaler': 30,
    'lengthMax': 500,
    'shuffler': 'length', # 'shuffler'
    'shuffleRange': (-5, 5)
}

