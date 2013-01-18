class gameInfo:

    ## Keeping the below several lines just in case...
    #### Declaration of variables
 
    ## Game segment information

    ## version (string)
    # infomation found in the header
    # examples: 0.10, 0.11, 0.12a
    # will need to truncate from full version information
    # in two formats: versionLong and versionShort
    # versionLong contains the full version information
    # versionShort keeps it at the first 6 characters


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
        
    def extractData(self):

        ## Check the header
        if len(self.header) != 0: self.extractHeader()

    ## header information stored in the following format:
    ##  Dungeon Crawl Stone Soup version 0.12-a0-1616-ge3ef79a (tiles) character file.
    def extractHeader(self):
        self.versionLong = self.header[0].split()[5]
        self.versionShort = self.versionLong[0:6]
