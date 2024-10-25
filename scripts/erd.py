from frictionless import formats, describe, Package
from sqlalchemy import MetaData, create_engine
import os

control = formats.SqlControl()
path = 'sqlite:///db.sqlite3'
metadata = MetaData()
engine = create_engine("sqlite+pysqlite:///db.sqlite3", echo=True)
metadata.reflect(engine)
table_names = list(metadata.tables.keys())
table_names.reverse()
package = Package(name='teste')
django_default_tables = [
    'django_session',
    'django_migrations',
    'django_admin_log',
    'auth_user_user_permissions',
    'auth_user_groups',
    'auth_user',
    'django_content_type',
    'auth_permission',
    'auth_group_permissions',
    'auth_group',
]
table_names = list(set(table_names) - set(django_default_tables))

for name in table_names:
    control = formats.SqlControl(table=name, basepath='data')
    schema = describe(path=path, name =name, control=control, type="resource")
    package.add_resource(schema)
    print(schema.to_yaml())

package.to_er_diagram(path='erd.dot')
os.system("dot -Tpng erd.dot > package_erd.png")
