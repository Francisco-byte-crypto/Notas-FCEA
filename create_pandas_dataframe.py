from url_to_full_list import url_to_full_list
import pandas as pd 
import numpy

def create_pandas_dataframe(_url_):
    cleared_tables, raw_tables = url_to_full_list(url=_url_)

    try:
    # Clear the columns labels.
        for i in range(0,len(cleared_tables[0])):
            cleared_tables[0][i] = cleared_tables[0][i].replace("º", "")
            cleared_tables[0][i] = cleared_tables[0][i].replace("°", "")
            cleared_tables[0][i] = cleared_tables[0][i].replace("\n", "")
            cleared_tables[0][i] = cleared_tables[0][i].replace(" ", "")

    except Exception as e: pass

    dataframe = pd.DataFrame(data=cleared_tables, columns=cleared_tables[0]).drop(index=0)
    dataframe = dataframe.drop(columns=[''])

    try:
        dataframe["NOTA"] = dataframe["NOTA"].str.strip('B.B.B B.B.MB MB.MB.B MB.MB.MB MB.MB.S S.S.MB S.S.S ()')
    
    except Exception as e: pass

    def floatify(x):
        try: return float(x)
        except: return numpy.nan

    def stringify(x):
        return str(x)

    for column in dataframe.columns:
        try:
            # We turn every , to a . so that we can make all those values convert to float correctly.
            dataframe[column] = dataframe[column].apply(lambda x: x.replace(',', '.'))

            if(column != 'NOMBRE' and column != 'CÉDULA'):
                dataframe[column] = dataframe[column].apply(floatify)

            if(column == 'NOMBRE'):
                dataframe[column] = dataframe[column].apply(stringify)

        except Exception as e:
            print("Problema al limpiar los datos. ", e)

    return dataframe

