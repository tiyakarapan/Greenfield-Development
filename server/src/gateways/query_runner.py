from typing import List, Any, Dict
from psycopg import connect

class QueryRunner:
    def __init__(self, table: str, pk: str):
        self.table = table
        self.pk = pk
        self.connection_string = "host='localhost' dbname='postgres' user='postgres' password='itca' port=5432"
    
    def list_all(self, columns: List[str]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {", ".join(columns)} FROM {self.table}")
                result = cursor.fetchall()

                return [dict([(columns[i], row[i]) for i in range(len(columns))]) for row in result]

    def insert(self, values: Dict[str, Any]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                columns = list(values.keys())
                
                cursor.execute(f"""
                    INSERT INTO {self.table} ({", ".join(columns)}) 
                    VALUES ({", ".join("%s" for _ in range(len(values)))}) 
                    RETURNING {self.pk}, {", ".join(columns)}
                """, tuple(values.values()))
                row = cursor.fetchone()

                if not row:
                    raise Exception("Failed to insert value")

                result = {}
                result[self.pk] = row[0]
                for i in range(1, len(columns)):
                    result[columns[i]] = row[i]

                return result

    def update(self, id: Any, values: Dict[str, Any]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                columns = list(values.keys())
                
                cursor.execute(f"""
                    UPDATE {self.table}
                    SET {", ".join(f"{column} = %s" for column in columns)}
                    WHERE {self.pk} = %s
                    RETURNING {self.pk}, {", ".join(columns)}
                """, tuple(list(values.values()) + [id]))
                row = cursor.fetchone()

                if not row:
                    raise Exception("Unexpected error")

                result = {}
                result[self.pk] = row[0]
                for i in range(1, len(columns)):
                    result[columns[i]] = row[i]

                return result

    def delete(self, id: Any):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"""
                    DELETE FROM {self.table}
                    WHERE {self.pk} = %s
                """, tuple([id]))

    def execute_raw(self, query: str, params: List[Any]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, tuple(params))
                return cursor.fetchall()