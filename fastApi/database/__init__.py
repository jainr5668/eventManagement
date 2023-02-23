import sqlite3

from utills.constants import DatabaseQueryStringSelect, DatabaseTableCreationQueries


class Database():
    def __init__(self):
        cnxn = sqlite3.connect("db.db")
        self.__cursor = cnxn.cursor()
        for query in DatabaseTableCreationQueries:
            self.__cursor.execute(query.value)
        
    def select(self, query:DatabaseQueryStringSelect, args=None):
        result = None
        if not args:
            result = self.__cursor.execute(query).fetchall()
        else:
            result = self.__cursor.execute(query.format(args)).fetchall()
        resultList = []
        for i in result:
            resultElement = {}
            for j in range(len(i)):
                resultElement[i.cursor_description[j][0]] = i[j]
            resultElement= dict(sorted(resultElement.items()))
            resultList.append(resultElement)
        return resultList
    
    def insert(self, table_name, data:dict,check=True,columns:list=None):
        insert_string = 'insert into {} ({}) VALUES {};'
        result = []
        queryParameter = []
        for column in data.keys():
            if type(data[column]) == type('string'):
                queryParameter.append(f"{column} = '{data[column]}'")
            else:
                queryParameter.append(f"{column} = {data[column]}")
        queryParameter = ' and '.join(queryParameter)
        result = self.__cursor.execute('select * from {} where {};'.format(table_name,queryParameter)).fetchall()
        if len(result) == 0:
            value = str(tuple(data.values()))
            if value[-2] ==',':
                value = value[:-2]+')'
            self.__cursor.execute(insert_string.format(table_name, ', '.join(tuple(data.keys())),value ))
            self.__cursor.commit()
            result = self.__cursor.execute('select * from {}'.format(table_name)).fetchall()[-1:]
        resultElement = {}
        for i in result:
            for j in range(len(i)):
                resultElement[i.cursor_description[j][0]] = i[j]
        return resultElement
    
    def update(self,table_name:str ,data: dict,condition:dict):
        update_string = ', '.join([f'{key} = {data[key]}' for key in list(data.keys())])
        condition_string = ' and '.join([f'{key} = {condition[key]}' for key in list(condition.keys())])
        query_string = 'UPDATE {} SET {} WHERE {};'
        self.__cursor.execute(query_string.format(table_name,update_string,condition_string))

