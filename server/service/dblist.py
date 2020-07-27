import psycopg2
import logging
import pymysql


class DBList():
    def get_table_struct(self):
        def tuple_first(in_tuple):
            return in_tuple[0]
        conn = psycopg2.connect(
            database="lazyshot", user="root", password="root", host="127.0.0.1", port="5432")
        cursor = conn.cursor()

        all_data_table_sql = "select tablename from pg_tables where schemaname='public'"
        cursor.execute(all_data_table_sql)
        tables_list = list()
        for table_name in cursor.fetchall():
            tables_list.append({
                "name": table_name[0],
                "struct": []
            })
        # table struct to dict
        for i in range(len(tables_list)):
            part_table_struct_sql = """SELECT column_name, data_type, is_nullable 
            FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{}'
            """.format(tables_list[i]["name"])
            primary_key_sql = """SELECT a.attname, format_type(a.atttypid, a.atttypmod) AS data_type
            FROM pg_index i JOIN pg_attribute a ON a.attrelid = i.indrelid
            AND a.attnum = ANY(i.indkey)
            WHERE i.indrelid = '{}'::regclass
            AND i.indisprimary;
            """.format(tables_list[i]["name"])
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
                tables_list[i]["struct"].append(table_struct_data)
        print(tables_list, '----')
        return tables_list

    # mysql
    def get_table_struct_for_mysql(self):
        init_table_list = list()
        def is_primary(field):
            return True if field == 'PRI' else False
        con = self.connect_db()
        cur = con.cursor()
        cur.execute("SHOW tables")
        back_table_list = cur.fetchall()
        for table_one in back_table_list:
            cur.execute("DESC {}".format(table_one[0]))
            data = cur.fetchall()
            # set back table struct
            table_item = {
                "name": 'shit',
                "struct": []
            }
            for i in data:
                table_item["struct"].append({
                    "name": i[0],
                    "type": i[1],
                    "is_null": i[2],
                    "is_primary": is_primary(i[3])
                })
            init_table_list.append(table_item)
        return init_table_list

    # connect
    def connect_db(self):
        return pymysql.connect(
            "localhost",
            "root",
            "root",
            "lazyshot"
        )
