from url_to_full_list import url_to_full_list

def url_to_headers(url):
    cleared_tables, raw_tables = url_to_full_list(url)
    minmax_dict = {'MINIMO':'', 'MAXIMO':''}
    
    def find_min_and_max_rows(raw_tables)->None:
        for i in range(0, len(raw_tables)):
            for j in range(0, len(raw_tables[i])):
                if(raw_tables[i][j] == 'MÍNIMO' or raw_tables[i][j] == 'MINIMO'): 
                    minmax_dict['MINIMO'] = raw_tables[i]
                    break

        for i in range(0, len(raw_tables)):
            for j in range(0, len(raw_tables[i])):
                if(raw_tables[i][j] == 'MÁXIMO' or raw_tables[i][j] == 'MAXIMO'): 
                    minmax_dict['MAXIMO'] = raw_tables[i]
                    break
    
    find_min_and_max_rows(raw_tables)

    def turn_values_to_float(minmax_dict)->None:
        for i in range(len(minmax_dict['MINIMO'])):
            try: minmax_dict['MINIMO'][i] = float(minmax_dict['MINIMO'][i])
            except: minmax_dict['MINIMO'][i] = float(0)
        
        for i in range(len(minmax_dict['MAXIMO'])):
            try: minmax_dict['MAXIMO'][i] = float(minmax_dict['MAXIMO'][i])
            except: minmax_dict['MAXIMO'][i] = float(0)

    turn_values_to_float(minmax_dict)

    return minmax_dict

