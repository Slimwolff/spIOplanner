import pandas as pd

df = pd.read_csv('./source_imported/for_.csv',sep=";",encoding_errors=False,engine='python',na_filter=False)





def tdt(a,removeChars="",reduce=-1,reduceLast=-1):
    arr = a
    for a in range(len(arr)):
        arr[a] = str(arr[a])

    if(removeChars != ""):
        rc = list(removeChars)
        for i in range(len(arr)):
            for x in rc:
                arr[i] = arr[i].replace(x, "")
    
    if(reduce != -1):
        for i in range(len(arr)):
            arr[i] = arr[i][0:reduce]

    if(reduceLast != -1):
        for i in range(len(arr)):
            arr[i] = arr[i][0:len(arr[i])-reduceLast]

    return arr

def doCSV(csv):
    data["FCOD"] = tdt(csv["Cód. Int."].tolist(),reduceLast=3)
    data["FNOME"] = tdt(csv["Nome"].tolist(),reduce=60)

# doCSV(df)



