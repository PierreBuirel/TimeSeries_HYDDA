import numpy as np

L_init = [3, 2, 2, 1, 2, 3, 1, 1, 2, 3, 4, 2, 3, 3, 3, 1]



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

#print (get_state(L_init))

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

#print(state_to_output(get_state(L_init)))

def get_feature_output(L):

    # Computing the tau list

    Lbis=state_to_output(get_state(L_init))

    # Initialization of the variables

    e = []
    f = []
    default = 0
    C = 5
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
            C=5
            for i in range(len(eiupdate)):
                e.append(C)
            eiupdate = []
    print(e)
    print(f)
    return e,f


get_feature_output(L_init)

