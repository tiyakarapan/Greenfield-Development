from typing import List, Any, Dict
from psycopg import connect

class QueryRunner:
    def __init__(self, table: str, pk: str | List[str]):
        self.table = table
        self.pk = pk if isinstance(pk, list) else [pk]
        self.connection_string = "host='localhost' dbname='itca' user='postgres' password='itca' port=5432"
    
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
                    RETURNING {", ".join(self.pk)}, {", ".join(columns)}
                """, tuple(values.values()))
                row = cursor.fetchone()

                if not row:
                    raise Exception("Failed to insert value")

                result = {}

                for i in range(len(self.pk)):
                    result[self.pk[i]] = row[i]

                for i in range(len(self.pk), len(columns)):
                    result[columns[i]] = row[i]

                return result

    def update(self, id: Any | List[Any], values: Dict[str, Any]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                columns = list(values.keys())

                id_values = id if isinstance(id, list) else [id]
                
                cursor.execute(f"""
                    UPDATE {self.table}
                    SET {", ".join(f"{column} = %s" for column in columns)}
                    WHERE {" AND ".join(f"{pk} = %s" for pk in self.pk)}
                    RETURNING {", ".join(self.pk)}, {", ".join(columns)}
                """, tuple(list(values.values()) + id_values))
                row = cursor.fetchone()

                if not row:
                    raise Exception("Unexpected error")

                result = {}

                for i in range(len(self.pk)):
                    result[self.pk[i]] = row[i]

                for i in range(len(self.pk), len(columns)):
                    result[columns[i]] = row[i]

                return result

    def delete(self, id: Any):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                id_values = id if isinstance(id, list) else [id]
                cursor.execute(f"""
                    DELETE FROM {self.table}
                    WHERE {" AND ".join(f"{pk} = %s" for pk in self.pk)}
                """, tuple(id_values))

    def execute_raw(self, query: str, params: List[Any]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, tuple(params))
                return cursor.fetchall()