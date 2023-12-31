import sqlite3

# اتصال بقاعدة البيانات - سيتم إنشاء ملف قاعدة البيانات إذا لم يكن موجودًا
conn = sqlite3.connect('MBEDB.db')

# إنشاء cursor لتنفيذ العبارات SQL
cursor = conn.cursor()

# إنشاء جدول
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
'''
cursor.execute(create_table_query)

# تأكيد التغييرات وحفظها
conn.commit()

# إغلاق الاتصال بقاعدة البيانات
conn.close()

