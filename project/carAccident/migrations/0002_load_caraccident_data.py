import re
from pathlib import Path

from django.db import migrations

SQL_DUMP_PATH = Path(__file__).resolve().parents[3] / "Project.sql"


def load_data(apps, schema_editor):
    if not SQL_DUMP_PATH.exists():
        return

    Caraccident = apps.get_model("carAccident", "Caraccident")
    if Caraccident.objects.exists():
        return

    sql = SQL_DUMP_PATH.read_text(encoding="utf-8")
    insert_statements = re.findall(r"INSERT INTO `caraccident`.*?;\n", sql, re.DOTALL)

    with schema_editor.connection.cursor() as cursor:
        for statement in insert_statements:
            cursor.execute(statement)


def unload_data(apps, schema_editor):
    Caraccident = apps.get_model("carAccident", "Caraccident")
    Caraccident.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("carAccident", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_data, unload_data),
    ]
