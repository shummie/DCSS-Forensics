class gameInfo:

    ## Keeping the below several lines just in case...
    #### Declaration of variables
 
    ## Game segment information

    ## version (string)
    # infomation found in the header
    # examples: 0.10, 0.11, 0.12a
    # will need to truncate from full version information
    version = ""

    rawData = []
    header = []
    hiscore = []
    stats = []
    misc = []
    notes = []
    inventory = []
    turns_by_place = []
    skills = []
    spells = []
    overview = []
    mutations = []
    monlist = []

    ## score (int)
    # 
    score = -1

    ## species (str)
    #
    species = ""

    ## speciesAbbrev
    # 
    speciesAbb = ""

  
    def __init__(self, data):
        self.rawData = data

    ## This function extracts the data from the data element fields.
    ## It will populate data only if the data element field is not empty.
        
    def extractData():
        
