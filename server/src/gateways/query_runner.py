from typing import List, Any, Dict
from psycopg import connect
from psycopg.rows import dict_row

class QueryRunner:
    def __init__(self, table: str, pk: str | List[str]):
        self.table = table
        self.pk = pk if isinstance(pk, list) else [pk]
        self.connection_string = "host='localhost' dbname='itca' user='postgres' password='itca' port=5432"
    
    def list_all(self, columns: List[str]):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.table}")
                return cursor.fetchall()

    def insert(self, values: Dict[str, Any]):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                columns = list(values.keys())
                
                cursor.execute(f"""
                    INSERT INTO {self.table} ({", ".join(columns)}) 
                    VALUES ({", ".join("%s" for _ in range(len(values)))}) 
                    RETURNING *
                """, tuple(values.values()))
                return cursor.fetchone()

    def update(self, id: Any | List[Any], values: Dict[str, Any]):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                columns = list(values.keys())

                id_values = id if isinstance(id, list) else [id]
                
                cursor.execute(f"""
                    UPDATE {self.table}
                    SET {", ".join(f"{column} = %s" for column in columns)}
                    WHERE {" AND ".join(f"{pk} = %s" for pk in self.pk)}
                    RETURNING *
                """, tuple(list(values.values()) + id_values))
                return cursor.fetchone()

    def delete(self, id: Any):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                id_values = id if isinstance(id, list) else [id]
                cursor.execute(f"""
                    DELETE FROM {self.table}
                    WHERE {" AND ".join(f"{pk} = %s" for pk in self.pk)}
                """, tuple(id_values))

    def _connect(self):
        return connect(self.connection_string, row_factory=dict_row)