import psycopg2
import re

connect_to_db = psycopg2.connect(
    database="markapi",
    user="dev_rw",
    password="2H8OmJLt",
    host="mark-cn-pdb01.msk.stage.mark.puls.local",
    port=5432
)
cursor = connect_to_db.cursor()
cursor.execute("select distinct sscc from warehouse_warehouseproductstore "
               "where branch_id = '00000000100852' and gtin = '50754041389897' and outer_ssccs = '{}' and sscc != '' "
               "order by sscc limit 5;")

a = cursor.fetchall()
print(f'Доступные коды: {a}')
connect_to_db.close()
