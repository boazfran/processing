# The following tahes a ChangO clone db without a germline col and a clone col
# and adds to it germline and clone columns.
# It does it in 3 stage listed bellow:
import sys
import os
import csv
import pandas

sys.path.append('./venv/bin')
import CreateGermlines
import DefineClones

Germ_files_list = []
# stage 1:
# The bellow adds a germline column to the db
dbfile = "~/RStudioProjects/clone_different_junction_length/GMC/0.tab"
CreateGermlines.createGermlines(db_file=dbfile, references=Germ_files_list, germ_types={'full', 'dmask'})

# stage 2:
# The following adds a clone column to the db:
DefineClones.defineClones(db_file='~/RStudioProjects/clone_different_junction_length/GMC/0.tab')

# stage 3:
# This stage is probably redundant, since after running defineClones - seems like sequences are sorted by CLONE
# column, so no need to resort them again (which is what this stage is doing).
# Anyhow - when do trying to run this stage - somehow next stage (stage 4) - end with many sequences not passing
# so skipping this stage, as it is probably not needed anyway.
# Before running next stage - need to sort the db by CLONE column:
# The df_types is needed, or else the read_csv changes some integers to floating:
# df_types={'V_SEQ_START':'Int64','V_SEQ_LENGTH':'Int64',
#          'V_GERM_START_VDJ':'Int64','V_GERM_LENGTH_VDJ':'Int64','V_GERM_START_IMGT':'Int64',
#          'V_GERM_LENGTH_IMGT':'Int64','NP1_LENGTH':'Int64','D_SEQ_START':'Int64','D_SEQ_LENGTH':'Int64',
#          'D_GERM_START':'Int64','D_GERM_LENGTH':'Int64','NP2_LENGTH':'Int64','J_SEQ_START':'Int64',
#          'J_SEQ_LENGTH':'Int64','J_GERM_START':'Int64','J_GERM_LENGTH':'Int64','JUNCTION_LENGTH':'Int64',
#          'CONSCOUNT':'Int64','DUPCOUNT':'Int64','CLONE':'Int64'}
# rr=pandas.read_csv("C:\\Bar Ilan 3 data - not backed up\\HCV_B\\CI10_rename_p1_p2_germ-pass_clone-pass.tab",sep="\t",dtype =df_types)
# tt=rr.sort_values(by=['CLONE'])
# tt.to_csv("C:\\Bar Ilan 3 data - not backed up\\HCV_B\\CI10_rename_p1_p2_germ-pass_clone-pass_sorted.tab", sep="\t",index=False)


# stage 4:
# The bellow regenerates germline columns again, now that we have a clone column (sorted):
# The reason for running this again is that after 2 stages above - there are some clones that have more than one germline.
# so rerunning this stage again - so that germlines will use clone information as well, and the output
# will have only one germline per clone.
dbfile = "C:\\Bar Ilan 3 data - not backed up\\HCV_B\\CI10_rename_p1_p2_germ-pass_clone-pass.tab"
CreateGermlines.createGermlines(db_file=dbfile, references=Germ_files_list, cloned=True,
                                clone_field="CLONE", germ_types={'full', 'dmask'})
