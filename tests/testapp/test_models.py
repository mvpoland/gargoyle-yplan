from django.core.management import call_command


def test_no_migrations_required(db):
    try:
        call_command("makemigrations", "gargoyle", check=1)
    except SystemExit:
        raise AssertionError("Migrations required")
