dict_peak = {'d': {'>': {"next_state" :'d',"semantic_letter" : "out"},
        '=': {"next_state" :'d',"semantic_letter" : "out"},
        '<': {"next_state" :'r',"semantic_letter" : "out"}},
        'r': {'>': {"next_state" :'t',"semantic_letter" : "found"},
        '=': {"next_state" :'r',"semantic_letter" : "maybe_before"},
        '<': {"next_state" :'t',"semantic_letter" : "maybe_before"}},
        't': {'>': {"next_state" :'t',"semantic_letter" : "in"},
        '=': {"next_state" :'t',"semantic_letter" : "maybe_after"},
        '<': {"next_state" :'r',"semantic_letter" : "out_after"}},'beginning_state' : 'd'}