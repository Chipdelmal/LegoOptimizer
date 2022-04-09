
###############################################################################
# Image
############################################################################### 
LEGO_DOWNSCALE_SIZE = (25, 25)

###############################################################################
# Weight dictionaries for block preference
# -----------------------------------------------------------------------------
#   NULL: Gives no priority for any particular type of block
#   BALANCED: Prioritizes medium-sized blocks
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
(QTY, MAX_LEN) = (300, 5)
# Uniform blocks supply -------------------------------------------------------
LIMITLESS_BLOCKS_SUPPLY = []
for i in range(1, MAX_LEN+1):
    LIMITLESS_BLOCKS_SUPPLY.extend([i]*QTY)

# Mostly small blocks supply --------------------------------------------------
SMALL_BLOCKS_SUPPLY = []
for i in range(1, MAX_LEN+1):
    SMALL_BLOCKS_SUPPLY.extend([i]*(QTY*(MAX_LEN-i+1)))

# Mostly large blocks supply --------------------------------------------------
LARGE_BLOCKS_SUPPLY = []
for i in range(1, MAX_LEN+1):
    LARGE_BLOCKS_SUPPLY.extend([i]*(QTY*(i)))

###############################################################################
# Lego Block Colors
############################################################################### 
BASE_COLORS_NUMBER = 16
LEGO_BASIC_COLOR = (
    '#F4F4F4', '#CCB98D', '#FAC80A', '#D67923', '#B40000', '#00852B',
    '#1E5AA8', '#040404', '#A5CA18', '#58AB41', '#7396C8', '#D05098',
    '#708E7C', '#70819A', '#720012', '#19325A', '#91501C', '#897D62',
    '#901F76', '#00451A', '#646464', '#969696', '#5F3109', '#441A91',
    '#FFEC6C', '#FF9ECD', '#9DC3F7', '#FCAC00', '#372100', '#AA7D55',
    '#D3F2EA', '#469BC3', '#CDA4DE', '#8B844F', '#69C3E2', '#A06EB9'
)
WIDE_COLORS = (
    '#210c5c', '#760760', '#bd0463', '#ff2951', '#ff8f1b', '#ffce2f', 
    '#fdfdfd', '#fed347', '#f5a20a', '#e66d19', '#d32b2c', '#9e093d', 
    '#571845', '#601423', '#902b0e', '#b94b09', '#ce7923', '#e2a53b', 
    '#f7d053', '#f8f8f8', '#fdca84', '#f6965a', '#e75f32', '#b73f2c', 
    '#881f27', '#590023', '#005638', '#32723f', '#618c46', '#90a64d', 
    '#b6c363', '#dae17e', '#ffff99', '#96ea6f', '#0ace37', '#00a732', 
    '#008131', '#005d30', '#003b2f', '#062a78', '#104d95', '#1a70b3', 
    '#2495d1', '#2ebcf1', '#72e0ff', '#d1ffff', '#a0d6ee', '#70addd', 
    '#4185cc', '#165cb8', '#1b358c', '#401d6c', '#69358b', '#944eab', 
    '#c168cd', '#ee84ee', '#f7bbef', '#ffedef', '#ffb9c9', '#ff7f9e', 
    '#f93166', '#ba226b', '#7b1270', '#340075', '#4a0020', '#6f2737', 
    '#934d4e', '#b77365', '#dd9a7c', '#ffc498', '#fffacd', '#e4db99', 
    '#c8bc67', '#a7a041', '#72883e', '#3c703b', '#0b0b0b', '#2f2f2f', 
    '#535353', '#7b7b7b', '#a5a5a5', '#d1d1d1', '#ffffff'
)
GB_COLORS = (
    '#040c06', '#112318', '#1e3a29', '#305d42', '#4d8061', '#89a257', 
    '#bedc7f', '#eeffcc'
)    
SGBA_COLORS = ('#ffe8cf', '#df904f', '#af2850', '#301850')
LEGO_LIMITED = (
    '#040404', '#F4F4F4', '#FCAC00', '#969696', '#AA7D55', '#372100', '#fffacd'
)
