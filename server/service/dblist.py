import psycopg2
import logging


class DBList():
    def get_table_struct(self):
        def tuple_first(in_tuple):
            return in_tuple[0]
        conn = psycopg2.connect(
            database="lazyshot", user="wot", password="123", host="127.0.0.1", port="5432")

        cursor = conn.cursor()

        all_data_table_sql = "select tablename from pg_tables where schemaname='public'"
        cursor.execute(all_data_table_sql)
        temp_table_name_list = list()
        for table_name in cursor.fetchall():
            temp_table_name_list.append(table_name[0])
        # table struct to dict
        back_list = list()
        for table_str in temp_table_name_list:
            part_table_struct_sql = """SELECT column_name, data_type, is_nullable 
            FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{}'
            """.format(table_str)
            primary_key_sql = """SELECT a.attname, format_type(a.atttypid, a.atttypmod) AS data_type
            FROM pg_index i JOIN pg_attribute a ON a.attrelid = i.indrelid
            AND a.attnum = ANY(i.indkey)
            WHERE i.indrelid = '{}'::regclass
            AND i.indisprimary;
            """.format(table_str)
            cursor.execute(part_table_struct_sql)
            part_table_list = cursor.fetchall()
            cursor.execute(primary_key_sql)
            primary_key_list = list(map(tuple_first, cursor.fetchall())) 
            
            for key in part_table_list:
                table_struct_data = {
                    "name": key[0],
                    "type": key[1],
                    "is_null": key[2],
                    "is_primary": False
                }
                if key[0] in primary_key_list:
                    table_struct_data["is_primary"] = True
                back_list.append(table_struct_data)
        print(back_list)
        return back_list
