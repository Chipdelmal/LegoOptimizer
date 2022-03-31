
###############################################################################
# Weight dictionaries for block preference
# -----------------------------------------------------------------------------
#   NULL: Gives no priority for any particular type of block
#   SMALL_FIRST: Prioritizes using smaller blocks over large ones
#   LARGE_FIRST (default): Prioritizes using larger blocks over smaller ones
###############################################################################
NULL_BLOCK_VALUES = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
SMALL_FIRST_BLOCK_VALUES = {1:10, 2:9, 3: 8, 4:7, 5:6, 6:5}
LARGE_FIRST_BLOCK_VALUES = {1:1, 2:3, 3:8, 4:10, 5:12, 6:15}
