
###############################################################################
# Image
############################################################################### 
LEGO_DOWNSCALE_SIZE = (50, 50)

###############################################################################
# Weight dictionaries for block preference
# -----------------------------------------------------------------------------
#   NULL: Gives no priority for any particular type of block
#   BALANCED: Prioritizes medium-sized blocks
#   SMALL_FIRST: Prioritizes using smaller blocks over large ones
#   LARGE_FIRST (default): Prioritizes using larger blocks over smaller ones
###############################################################################
NULL_BLOCK_VALUES =         {1:1,  2:1, 3:1,  4:1,  5:0,  6:1,  7:0,  8:1,  9:0,  10:1 }
BALANCED_BLOCK_VALUES =     {1:2,  2:4, 3:8,  4:10, 5:0,  6:5,  7:0,  8:3,  9:0,  10:1 }
SMALL_FIRST_BLOCK_VALUES =  {1:10, 2:9, 3:8,  4:7,  5:0,  6:5,  7:0,  8:3,  9:0,  10:1 }
LARGE_FIRST_BLOCK_VALUES =  {1:1,  2:3, 3:8,  4:10, 5:0,  6:15, 7:0,  8:20, 9:0,  10:25}

###############################################################################
# Blocks Supply Pools
###############################################################################
(QTY, MAX_LEN) = (500, 10)
VALID_BLOCK_LENGTHS = (1, 2, 3, 4, 6, 8, 10)
# Uniform blocks supply -------------------------------------------------------
LIMITLESS_BLOCKS_SUPPLY = []
for i in VALID_BLOCK_LENGTHS:
    LIMITLESS_BLOCKS_SUPPLY.extend([i]*QTY)

# Mostly small blocks supply --------------------------------------------------
SMALL_BLOCKS_SUPPLY = []
for i in VALID_BLOCK_LENGTHS:
    SMALL_BLOCKS_SUPPLY.extend([i]*(QTY*(MAX_LEN-i+1)))

# Mostly large blocks supply --------------------------------------------------
LARGE_BLOCKS_SUPPLY = []
for i in VALID_BLOCK_LENGTHS:
    LARGE_BLOCKS_SUPPLY.extend([i]*(QTY*(i)))

###############################################################################
# Manual Block Supply Demo
############################################################################### 
GB_BLOCK_SUPPLY = {
    '#2d1b00': [1]*50 + [2]*80 + [3]*90 + [4]*50 + [5]*25 + [6]*10,
    '#1e606e': [1]*25 + [2]*75 + [3]*50 + [4]*50 + [5]*20 + [6]*30,
    '#5ab9a8': [1]*50 + [2]*30 + [3]*10 + [4]*90 + [5]*40 + [6]*10,
    '#c4f0c2': [1]*80 + [2]*80 + [3]*80 + [4]*80 + [5]*90 + [6]*90
}

###############################################################################
# Lego Website
###############################################################################
# 2x1: https://www.lego.com/en-us/page/static/pick-a-brick?query=%22Brick%201x2%22&page=1&sort.key=PRICE&sort.direction=ASC&filters.i0.key=variants.attributes.designNumber&filters.i0.values.i0=3004
# 2x2: https://www.lego.com/en-us/page/static/pick-a-brick?query=2x2&page=1&sort.key=PRICE&sort.direction=ASC&filters.i0.key=variants.attributes.designNumber&filters.i0.values.i0=3003
# 2x3: https://www.lego.com/en-us/page/static/pick-a-brick?query=2x3&page=1&sort.key=PRICE&sort.direction=ASC&filters.i0.key=variants.attributes.designNumber&filters.i0.values.i0=3002
# 2x4: https://www.lego.com/en-us/page/static/pick-a-brick?query=2x4&page=1&sort.key=PRICE&sort.direction=ASC&filters.i0.key=variants.attributes.designNumber&filters.i0.values.i0=3001
# 2x6: https://www.lego.com/en-us/page/static/pick-a-brick?query=2x6&page=1&sort.key=PRICE&sort.direction=ASC&filters.i0.key=variants.attributes.designNumber&filters.i0.values.i0=44237
# 2x8: https://www.lego.com/en-us/page/static/pick-a-brick?query=%22Brick%202x5%22&page=1&sort.key=RELEVANCE&sort.direction=DESC&filters.i0.key=variants.attributes.designNumber&filters.i0.values.i0=93888