
import palettes as pal
import constants as cst

###############################################################################
# USER-SELECTIONS
############################################################################### 
USER_SEL = {
    'size': [int(i*1) for i in (16, 20)],
    'palette': pal.NES['palette'],
    'blocks': cst.LIMITLESS_BLOCKS_SUPPLY,
    'priority': cst.LARGE_FIRST_BLOCK_VALUES,
    'shuffler': 'length',
    'lengthMax': 500,
    'shuffleRange': (-5, 5),
    'scaler': 25,
    'verbose': True
}
