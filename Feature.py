import numpy as np

# Input time serie
L_init = [3, 2, 2, 1, 2, 3, 1, 1, 2, 3, 4, 2, 3, 3, 3, 1]

# Output features Output_Features = [[guard_list,c_list,feature value],]

dict_peak = {'d': {'>': {"next_state" :'d',"semantic_letter" : "out"},
        '=': {"next_state" :'d',"semantic_letter" : "out"},
        '<': {"next_state" :'r',"semantic_letter" : "out"}},
        'r': {'>': {"next_state" :'t',"semantic_letter" : "found"},
        '=': {"next_state" :'r',"semantic_letter" : "maybe_before"},
        '<': {"next_state" :'t',"semantic_letter" : "maybe_before"}},
        't': {'>': {"next_state" :'t',"semantic_letter" : "in"},
        '=': {"next_state" :'t',"semantic_letter" : "maybe_after"},
        '<': {"next_state" :'r',"semantic_letter" : "out_after"}},'beginning_state' : 'd'}

dict_footprint = {'out' : {'guard' : "0",'C' : 'C'},
                    'out_before' : {'guard' : "0",'C' : 'C'},
                    'out_after' : {'guard' : "0",'C' : 'C'},
                    'maybe_before' : {'guard' : "nextguard",'C' : 'C'},
                    'maybe_after' : {'guard' : "nextguard",'C' : 'C'},
                    'found_end' : {'guard' : "Cincr",'C' : 'Cincr'},
                    'found' : {'guard' : "Cincr",'C' : 'Cincr'},
                    'in' : {'guard' : "C",'C' : 'C'}}

# Cf page 12 time_series_journal.pdf

dict_feature = {'one' : {'neutralf' : 'func_one', 'minf' : 1, 'maxf' : 1, 'phif' : 'max', 'deltaf' : 0},
                'width' : {'neutralf' : '', 'minf' : '', 'maxf' : '', 'phif' : '', 'deltaf' : ''},
                'surface' : {'neutralf' : '', 'minf' : '', 'maxf' : '', 'phif' : '', 'deltaf' : ''},
                'max' : {'neutralf' : -np.Infinity, 'minf' : -np.Infinity, 'maxf' : +np.Infinity, 'phif' : 'max', 'deltaf' : 'x'},
                'min' : {'neutralf' : '', 'minf' : '', 'maxf' : '', 'phif' : '', 'deltaf' : ''}}

# Dictionnaire table de décoration

dict_decoration_table = {'out' :
                             {'C' : {'function' : 'None', 'parameters' : ['C']}},
                    'out_before' :
                        {'C' : {'function' : 'None', 'parameters' : ['C']}},
                    'out_after' :
                             {'C' : {'function' : 'default_gf', 'parameters' : [{'function' : 'None', 'parameters' : ['']}]}},
                    'maybe_before' :
                             {'C' : {'function' : 'None', 'parameters' : ['C']}},
                    'maybe_after' :
                             {'C' : {'function' : 'None', 'parameters' : ['C']}},
                    'found' :
                             {'C' : {'function' : 'update_found_c', 'parameters' : [{'function' : 'None', 'parameters' : ['']}]}},
                    'in' :
                             {'C' : {'function' : 'update_in_c', 'parameters' : [{'function' : 'None', 'parameters' : ['']}]}},
                    'found_end' :
                             {'C' : {'function' : 'None', 'parameters' : ['C']}}}

# Dictionnaire update

dict_update_decoration_table = {'found' :
                             {'C' : {'function' : 'phi_f', 'parameters' :
                                 [{'function' : 'phi_f', 'parameters' :
                                     [{'function' : "None", 'parameters' :
                                         ['D']},{'function' : 'delta_f','parameters' :
                                         [{'function' : 'None', 'parameters' : ['']}]}]},
                                  {'function' : 'delta_f', 'parameters' :
                                      ['']}]}},
                    'out_before' : {'C' : {'function' : 'phi_f', 'parameters' :
                        [{'function' : 'None','parameters':['C']},
                         {'function' : 'phi_f','parameters':
                             [{'function' : 'None','parameters':['D']},{'function' : 'delta_f','parameters':[{'function' : 'None', 'parameters' : ['']}]}]}]}
                                    },
                    }


def functionDecorationTable(func,arg) :

    # func = requete nécessaire pour accéder à une fonction dans le dictionnaire
    # dic ??????
    # arg

    if(func.get('function')=="None"):
        return(func.get(parameters)[0])

    if(func.get('parameters').)

    else:




def updateP(index,list,val):
    verif=True
    while(index>=0 and verif==True):
        if(list[index]<0):
            list[index]=val
        else:
            verif=False
        index=index-1
    return(list)


# Fonction retournant les lettres semantiques a partir d'une serie temporelle et d'un dictionnaire

def get_output_from_dict(L):

    #State list
    currentstate = dict_peak.get('beginning_state')

    #Semantic letters
    output=[]

    #C list
    C=0
    c_list=[]

    #Guard list
    guard=0
    guard_list=[]


    i = 0;
    while(i<len(L)-1):

        # Signature

        if L[i] < L[i + 1]:
            signature="<"
        elif L[i] == L[i + 1]:
            signature="="
        else:
            signature=">"

        # Update of the semantic letter

        semantic_letter = dict_peak.get(currentstate).get(signature).get("semantic_letter")
        output.append(semantic_letter)

        # Update of the state

        currentstate = dict_peak.get(currentstate).get(signature).get("next_state")

        # Update of the footprint

        guard_temp = dict_footprint.get(semantic_letter).get("guard")
        C_temp = dict_footprint.get(semantic_letter).get("C")

        # Update of the guard

        if(guard_temp=="0"):
            guard=0
            guard_list=updateP(i-1,guard_list,guard)
        elif(guard_temp=="nextguard"):
            # We set the value to -1 so it will be easy to find which one to update
            guard=-1
        elif(guard_temp=="Cincr"):
            guard=C+1
            guard_list = updateP(i-1, guard_list, guard)
        elif(guard_temp=="C"):
            guard=C
            guard_list = updateP(i-1, guard_list, guard)

        # Update of C

        if(C_temp=="Cincr"):
            C=C+1

        # Update of the lists

        guard_list.append(guard)
        c_list.append(C)

        # Computing of the feature


        i=i+1;

    print(output)
    print(guard_list)
    print(c_list)

    return(output,guard_list,c_list)




get_output_from_dict(L_init)







# En dessous c'est ce qu'on avait fait avant






def get_signature(L):
   S = []
   for i in range(len(L)-1):
       if L[i] < L[i+1]:
           S.append("<")
       elif L[i] == L[i+1]:
           S.append("=")
       else:
           S.append(">")
   return S

#print (get_signature(L_init))


def signature_to_state(L):
   E = ["s"]
   for i in range(len(L)):
       if (E[i]=="s"):
           if (L[i]==">" or L[i]=="="):
               E.append("s")
           else:
               E.append("r")
       elif (E[i]=="r"):
           if (L[i]=="<" or L[i]=="="):
               E.append("r")
           else:
               E.append("t")
       else:
           if L[i]=="=":
               E.append("t")
           elif L[i]==">":
               E.append("t")
           else:
               E.append("r")
   return E

def get_state(L):
   return signature_to_state(get_signature(L))



def state_to_output(L):
   Out = []
   for i in range(len(L)-1):
       if (L[i]=="s" and L[i+1]=="s") or (L[i]=="s" and L[i+1]=="r"):
           Out.append("out")
       elif (L[i]=="r" and L[i+1]=="r"):
           Out.append("maybe_b")
       elif (L[i]=="r" and L[i+1]=="t"):
           Out.append("found")
       elif (L[i]=="t" and L[i+1]=="t"):
           if(L_init[i]==L_init[i+1]):
               Out.append("maybe_a")
           else:
               Out.append("in")
       elif (L[i]=="t" and L[i+1]=="r"):
           Out.append("out_a")
   return Out

print(state_to_output(get_state(L_init)))

def get_feature_output(L):

    # Computing the tau list

    Lbis=state_to_output(get_state(L_init))

    # Initialization of the variables

    e = []
    f = []
    default = L[0]
    C = 1
    D = -1000
    eiupdate=[]

    # Automate

    for i in range(len(Lbis)):
        if (Lbis[i]=="out"):
            f.append(default)
            e.append(default)
        elif (Lbis[i]=="maybe_b"):
            D=max(D,L_init[i+1])
        elif (Lbis[i]=="found"):
            C=max(D,L_init[i+1])
            D=-1000
        elif (Lbis[i]=="maybe_a"):
            f.append(default)
            eiupdate.append(i)
        elif (Lbis[i] == "in"):
            C=max(C,np.max(D,np.max(L_init[i+1])))
            D=-1000
            f.append[default]
            eiupdate.append(i)
        elif (Lbis[i]=="out_a"):
            eiupdate.append(i)
            D=-1000
            C=min(e,C)
            for i in range(len(eiupdate)):
                e.append(C)
            eiupdate = []


    return e,f


