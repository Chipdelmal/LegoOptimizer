
###############################################################################
# Weight dictionaries for block preference
# -----------------------------------------------------------------------------
#   NULL: Gives no priority for any particular type of block
#   SMALL_FIRST: Prioritizes using smaller blocks over large ones
#   LARGE_FIRST (default): Prioritizes using larger blocks over smaller ones
###############################################################################
NULL_BLOCK_VALUES = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1}
BALANCED_BLOCK_VALUES = {1:1, 2:3, 3:8, 4:10, 5:9, 6:5, 7:4, 8:2}
SMALL_FIRST_BLOCK_VALUES = {1:10, 2:9, 3: 8, 4:7, 5:6, 6:5, 7:4, 8:3}
LARGE_FIRST_BLOCK_VALUES = {1:1, 2:3, 3:8, 4:10, 5:12, 6:15, 7:17, 8:20}

###############################################################################
# Blocks Supply Pools
###############################################################################
# Uniform blocks supply -------------------------------------------------------
(QTY, MAX_LEN) = (125, 8)
LIMITLESS_BLOCKS_SUPPLY = []
for i in range(1, MAX_LEN+1):
    LIMITLESS_BLOCKS_SUPPLY.extend([i]*QTY)

# Mostly small blocks supply --------------------------------------------------
(QTY, MAX_LEN) = (10, 8)
SMALL_BLOCKS_SUPPLY = []
for i in range(1, MAX_LEN+1):
    SMALL_BLOCKS_SUPPLY.extend([i]*(QTY*(MAX_LEN-i+1)))

# Mostly large blocks supply --------------------------------------------------
(QTY, MAX_LEN) = (10, 8)
LARGE_BLOCKS_SUPPLY = []
for i in range(1, MAX_LEN+1):
    LARGE_BLOCKS_SUPPLY.extend([i]*(QTY*(i)))

###############################################################################
# Lego Block Colors
############################################################################### 
LEGO_BASIC_COLOR = [
    '#F4F4F4', '#CCB98D', '#FAC80A', '#D67923', '#B40000', '#00852B',
    '#1E5AA8', '#040404', '#A5CA18', '#58AB41', '#7396C8', '#D05098',
    '#708E7C', '#70819A', '#720012', '#19325A', '#91501C', '#897D62',
    '#901F76', '#00451A', '#646464', '#969696', '#5F3109', '#441A91',
    '#FFEC6C', '#FF9ECD', '#9DC3F7', '#FCAC00', '#372100', '#AA7D55',
    '#D3F2EA', '#469BC3', '#CDA4DE', '#8B844F', '#69C3E2', '#A06EB9'
]
