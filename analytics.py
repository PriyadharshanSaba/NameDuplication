import sys
import pandas as pd

#sys.path.append("/usr/local/lib/python3.6/site-packages")


def fetch_unique_records():
    fname = dset.iloc[:,3:4]
    lname = dset.iloc[:,:1]
#   for i in p.iterrows():
#print(i)
    names_dset= dset.values
    ufn = dset.fn.unique()
    uln = dset.ln.unique()

    print(len(ufn))
    print("\n")
    print(len(uln))
    if(len(ufn) == len(uln)):
        print("Suc")
    else:
        print("diff")

dset = pd.read_csv('dset.csv')
record = pd.DataFrame(columns=['ln','dob','gn','fn'])
#print(dset)

fetch_unique_records()



#p.iterrows()
#len(df.index)
