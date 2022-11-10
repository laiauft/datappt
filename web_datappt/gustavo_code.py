import pandas as pd

# file_name = file_name_function()

max_std = 10
# data = pd.read_csv(f'static/upload/data.csv') # dataset
# columns = data.columns

# # num_instances, num_attibutes = data.shape
# print()
# print("O Número de Instâncias é: ", num_instances)
# print("O Número de Atributos é: ", num_attibutes)


def convert_file2data(f):
    data = pd.read_csv(f'web_datappt/static/upload/'+f.name)
    return data


def has_outliers(data, col):   
    if(data[col].std() >= max_std):
        return True;
    else:
        return False;

def column_attributes(data):
    list_of_columns = []
    # Percorre cada coluna do dataset e define seus atributos
    for col in data.columns:
        # Atributos baseado em propriedades estatísticas de cada coluna
        attributes = ['mean', 'std', 'max', 'min', 'hasoutliers?']
        column_mean = data[col].mean()  # MEDIA
        column_std = data[col].std()    # DESVIO PADRÃO    
        column_max = data[col].max()    # VALOR MAXIMO
        column_min = data[col].min()    # VALOR MINIMO 
        # Por ultimo utiliza de uma função para verificar se há outliers
        outliers = has_outliers(data, col)

        column = pd.Series(
            data=[column_mean, column_std, column_max, column_min, outliers], 
            index=[attributes], 
            name=col
        )

        list_of_columns.append(column)
        df_final = pd.DataFrame(list_of_columns)
        # final2html = df_final.to_html()
    return df_final

# print()
# print("INFORMAÇÕES SOBRE CADA ATRIBUTO: ")
# print(column_attributes(data))