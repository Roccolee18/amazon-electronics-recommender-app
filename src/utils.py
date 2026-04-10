# helper function from Claude to keep the columns being used in other scripts consistent 
# and easily editable in one place via a text file where milestone exploration notebook is
# (instead of hardcoding them in multiple scripts which could change) 

    #specific with default meta columns path 
def read_meta_txt_columns(filepath = "notebooks/meta_columns.txt"):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

    #specific with default review columns path 
def read_review_txt_columns(filepath = "notebooks/review_columns.txt"):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]