# Generated by Django 4.2.15 on 2024-09-27 14:31

from django.db import migrations

"""
Update the created_by field on Advisory from the old qualified_name
to the new pipeline_id.
"""


def update_created_by(apps, schema_editor):
    from vulnerabilities.pipelines.github_importer import GitHubAPIImporterPipeline

    Advisory = apps.get_model("vulnerabilities", "Advisory")
    Advisory.objects.filter(created_by="vulnerabilities.importers.github.GitHubAPIImporter").update(
        created_by=GitHubAPIImporterPipeline.pipeline_id
    )



def reverse_update_created_by(apps, schema_editor):
    from vulnerabilities.pipelines.github_importer import GitHubAPIImporterPipeline

    Advisory = apps.get_model("vulnerabilities", "Advisory")
    Advisory.objects.filter(created_by=GitHubAPIImporterPipeline.pipeline_id).update(
        created_by="vulnerabilities.importers.github.GitHubAPIImporter"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("vulnerabilities", "0066_update_gitlab_advisory_created_by"),
    ]

    operations = [
        migrations.RunPython(update_created_by, reverse_code=reverse_update_created_by),
    ]