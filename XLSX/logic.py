

import pandas as pd
from datetime import datetime
import os, shutil, random, string, re

    
def delete_files_before(folder_path):
    folder_path = folder_path or None or "path/to/folder"

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
            

def date_string():
    ''' This function gets current time and date {now}'''
    run_time =  datetime.now().strftime('%H-%M-%S')
    run_date =  datetime.now().strftime('%Y-%m-%d')
    return run_date+"_"+run_time

def random_ascii():
    res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
    return str(res) 

# def file_path(extension):
#     res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
#     path_to_upload = os.path.join('uploaded_files', str(res))
#     os.makedirs(path_to_upload)
#     path = f"{str(res)}_{date_string()}.{extension}"
    
#     return path, path_to_upload

class EXCEL():
    
    """___ EXCEL ___
    
    Purpose:
        Class containing function which converts EXCEL files.
        
    Function:
       __ to xls __ : This converts the EXCEL file to XLSX (Excel).
       __ to_csv __ : This converts the EXCEL file to CSV (Comma Seperated File).
       __ to_json __: This converts the EXCEL file to JSON (JavaScript Oriented Notation).
       __ to_xml __ : This converts the EXCEL file to XML.
       __ to_sql __ : This converts the EXCEL file to SQL (Structured Query Language).
       __ to_html __: This converts the EXCEL file to HTML (HyperText Markup Language).
       
       YET TO BE INITIALIZED:
       __ to_pdf __ : This convert the EXCEL file to PDF.
       __ to_pptx __: This convert the EXCEL file to PPTx (Powerpoint file).
       
               
    Returns:
    
        Error or None
        
    """   
    counter = 0
    
    def xls_to_df(self):
        # Read and return dataframe 
        return  pd.DataFrame(pd.read_excel(self.input_file)) 
    
    def to_xls(self):
        try:            
            df = self.xls_to_df()
            #Name the file to be the filename inputted + the current date and time
            file_save = f'{self.default_file}.xlsx'
            
            # Write the dataframe object 
            # into preferred file type
            df.to_excel(
                file_save,  
                index = None, 
                header=True
            )
            
            print(f'Sucessfully created file @ {file_save}')
        except Exception as e:
            print('Error @to_xls Generation :', e)
        
    def to_csv(self):
        try:            
            df = self.xls_to_df()
            #Name the file to be the filename inputted + the current date and time
            file_save = f'{self.default_file}.csv'
            
            # Write the dataframe object 
            # into preferred file type
            df.to_csv(
                file_save,  
                index = None, 
                header=True
            )
            
            return file_save
            print(f'Sucessfully created file @ {file_save}')
        except Exception as e:
            print('Error @to_csv Generation :', e)
    
    def to_json(self):
        try:            
            df = self.xls_to_df()
            #Name the file to be the filename inputted + the current date and time
            file_save = f'{self.default_file}.json'
            
            # Write the dataframe object 
            # into preferred file type
            df.to_json(
                file_save,  
                orient='records', 
                indent=4
            )
            
            return file_save
            print(f'Sucessfully created file @ {file_save}')
        except Exception as e:
            print('Error @to_json Generation :', e)
     
    def to_xml(self):
        try:            
            df = self.xls_to_df()
            #Name the file to be the filename inputted + the current date and time
            file_save = f'{self.default_file}.xml'
            
            # Write the dataframe object 
            # into preferred file type
            
            df.to_xml(
                file_save,
                root_name="data",
                row_name='item'
            )
            
            return file_save
            print(f'Sucessfully created file @ {file_save}')
        except Exception as e:
            print('Error @to_xml Generation :', e)
     
     
    def to_html(self):
        try:            
            df = self.xls_to_df()
            #Name the file to be the filename inputted + the current date and time
            file_save = f'{self.default_file}.html'
            
            # Write the dataframe object 
            # into preferred file type
            df.to_json(
                file_save,  
                orient='records', 
                indent=4
            )
            
            return file_save
            print(f'Sucessfully created file @ {file_save}')
        except Exception as e:
            print('Error @to_html Generation :', e)
            
    def to_sql(self):
        try:            
            df = self.xls_to_df()
            #Name the file to be the filename inputted + the current date and time
            file_save = f'{self.default_file}.sql'
            
            sql = pd.io.sql.get_schema(df.reset_index(), 'DATA_TABLE')
    
            sql_texts = []
            for index, row in df.iterrows():
                sql_texts.append(f"INSERT INTO DATA_TABLE + ({', '.join(df.columns)}) VALUES{str(tuple(row.values))} \n")
                # sql_texts.append('INSERT INTO '+ 'DATA_TABLE' + ' ('+ str(', '.join(df.columns))+  ') VALUES'+ str(tuple(row.values)) + '\n')
                        
            # Write the dataframe object 
            # into preferred file type
            with open(file_save, 'w') as fs:
                fs.write(sql)
            
            return file_save
            print(f'Sucessfully created file @ {file_save}')
        except Exception as e:
            print('Error @to_sql Generation :', e)       
    

    def __init__(self, input_file, file_to):
        try: 
            self.input_file = input_file
            self.file_to= file_to
            EXCEL.counter += 1
            
            self.default_file = f'{file_to}/file_{EXCEL.counter}_{date_string()}'
            
        except Exception as e:
            print('Error @EXCEL class __init__', e)
    
