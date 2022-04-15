
import constants as cst

###############################################################################
# USER-SELECTIONS
############################################################################### 
USER_SEL = {
    'size': [int(i*1) for i in (28, 36)],
    'palette':  12, #cst.LEGO_LIMITED, # 6,
    'blocks': cst.LIMITLESS_BLOCKS_SUPPLY,
    'priority': cst.LARGE_FIRST_BLOCK_VALUES,
    'verbose': True,
    'scaler': 30,
    'lengthMax': 500,
    'shuffler': 'length', # 'shuffler'
    'shuffleRange': (-5, 5)
}

