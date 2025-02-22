import requests
import pymupdf as pf 

def url_to_full_list(url):

    r = requests.get(url)
    data = r.content
    doc = pf.Document(stream=data)
    start_index = None
    raw_tables = []
    cleared_tables = []

    for pages in doc:
        # Pushes a table registry from the table of each page of the pdf.
        try:
            raw_tables.extend(pages.find_tables().tables[0].extract())
        except Exception as e:
            print("Problem while finding tables: ", e)

    for i in range(0, len(raw_tables)):
        """What we do here is check if the first value is an INT because in case it is then that means
            that row is a registry. If it's not possible to convert that value to an int then we just pass and 
            not append it to the clear_tables list."""
        try:
            if(int(raw_tables[i][0])): 
                cleared_tables.append(raw_tables[i])

            if(int(raw_tables[i][0]) == 1 and start_index == None): start_index = i
            
        except Exception:
            pass
    
    cleared_tables.insert(0, raw_tables[start_index - 1])
    
    return cleared_tables, raw_tables
