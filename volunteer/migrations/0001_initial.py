# Generated by Django 5.1.7 on 2025-03-18 22:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import portal.models
import volunteer.constants
from volunteer.constants import RoleTypes


def create_initial_roles(apps, schema_editor):
    Role = apps.get_model("volunteer", "Role")
    for role_type in RoleTypes:
        Role.objects.create(short_name=role_type, description=role_type)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("portal", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="portal.basemodel",
                    ),
                ),
                (
                    "short_name",
                    models.CharField(max_length=40, verbose_name="name"),
                ),
                (
                    "description",
                    models.CharField(max_length=1000, verbose_name="description"),
                ),
            ],
            bases=("portal.basemodel",),
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="portal.basemodel",
                    ),
                ),
                (
                    "short_name",
                    models.CharField(max_length=40, verbose_name="name"),
                ),
                (
                    "description",
                    models.CharField(max_length=1000, verbose_name="description"),
                ),
            ],
            bases=("portal.basemodel",),
        ),
        migrations.CreateModel(
            name="VolunteerProfile",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="portal.basemodel",
                    ),
                ),
                (
                    "application_status",
                    models.CharField(
                        choices=[
                            (
                                volunteer.constants.ApplicationStatus["PENDING"],
                                volunteer.constants.ApplicationStatus["PENDING"],
                            ),
                            (
                                volunteer.constants.ApplicationStatus["APPROVED"],
                                volunteer.constants.ApplicationStatus["APPROVED"],
                            ),
                            (
                                volunteer.constants.ApplicationStatus["REJECTED"],
                                volunteer.constants.ApplicationStatus["REJECTED"],
                            ),
                            (
                                volunteer.constants.ApplicationStatus["CANCELLED"],
                                volunteer.constants.ApplicationStatus["CANCELLED"],
                            ),
                        ],
                        default=volunteer.constants.ApplicationStatus["PENDING"],
                        max_length=50,
                    ),
                ),
                ("coc_agreement", models.BooleanField(default=False)),
                (
                    "github_username",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "discord_username",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "instagram_username",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "bluesky_username",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "mastodon_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "x_username",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "linkedin_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "pronouns",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "languages_spoken",
                    portal.models.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("af", "Afrikaans"),
                                ("ar", "Arabic"),
                                ("ar-dz", "Algerian Arabic"),
                                ("ast", "Asturian"),
                                ("az", "Azerbaijani"),
                                ("bg", "Bulgarian"),
                                ("be", "Belarusian"),
                                ("bn", "Bengali"),
                                ("br", "Breton"),
                                ("bs", "Bosnian"),
                                ("ca", "Catalan"),
                                ("ckb", "Central Kurdish (Sorani)"),
                                ("cs", "Czech"),
                                ("cy", "Welsh"),
                                ("da", "Danish"),
                                ("de", "German"),
                                ("dsb", "Lower Sorbian"),
                                ("el", "Greek"),
                                ("en", "English"),
                                ("en-au", "Australian English"),
                                ("en-gb", "British English"),
                                ("eo", "Esperanto"),
                                ("es", "Spanish"),
                                ("es-ar", "Argentinian Spanish"),
                                ("es-co", "Colombian Spanish"),
                                ("es-mx", "Mexican Spanish"),
                                ("es-ni", "Nicaraguan Spanish"),
                                ("es-ve", "Venezuelan Spanish"),
                                ("et", "Estonian"),
                                ("eu", "Basque"),
                                ("fa", "Persian"),
                                ("fi", "Finnish"),
                                ("fr", "French"),
                                ("fy", "Frisian"),
                                ("ga", "Irish"),
                                ("gd", "Scottish Gaelic"),
                                ("gl", "Galician"),
                                ("he", "Hebrew"),
                                ("hi", "Hindi"),
                                ("hr", "Croatian"),
                                ("hsb", "Upper Sorbian"),
                                ("hu", "Hungarian"),
                                ("hy", "Armenian"),
                                ("ia", "Interlingua"),
                                ("id", "Indonesian"),
                                ("ig", "Igbo"),
                                ("io", "Ido"),
                                ("is", "Icelandic"),
                                ("it", "Italian"),
                                ("ja", "Japanese"),
                                ("ka", "Georgian"),
                                ("kab", "Kabyle"),
                                ("kk", "Kazakh"),
                                ("km", "Khmer"),
                                ("kn", "Kannada"),
                                ("ko", "Korean"),
                                ("ky", "Kyrgyz"),
                                ("lb", "Luxembourgish"),
                                ("lt", "Lithuanian"),
                                ("lv", "Latvian"),
                                ("mk", "Macedonian"),
                                ("ml", "Malayalam"),
                                ("mn", "Mongolian"),
                                ("mr", "Marathi"),
                                ("ms", "Malay"),
                                ("my", "Burmese"),
                                ("nb", "Norwegian Bokmål"),
                                ("ne", "Nepali"),
                                ("nl", "Dutch"),
                                ("nn", "Norwegian Nynorsk"),
                                ("os", "Ossetic"),
                                ("pa", "Punjabi"),
                                ("pl", "Polish"),
                                ("pt", "Portuguese"),
                                ("pt-br", "Brazilian Portuguese"),
                                ("ro", "Romanian"),
                                ("ru", "Russian"),
                                ("sk", "Slovak"),
                                ("sl", "Slovenian"),
                                ("sq", "Albanian"),
                                ("sr", "Serbian"),
                                ("sr-latn", "Serbian Latin"),
                                ("sv", "Swedish"),
                                ("sw", "Swahili"),
                                ("ta", "Tamil"),
                                ("te", "Telugu"),
                                ("tg", "Tajik"),
                                ("th", "Thai"),
                                ("tk", "Turkmen"),
                                ("tr", "Turkish"),
                                ("tt", "Tatar"),
                                ("udm", "Udmurt"),
                                ("ug", "Uyghur"),
                                ("uk", "Ukrainian"),
                                ("ur", "Urdu"),
                                ("uz", "Uzbek"),
                                ("vi", "Vietnamese"),
                                ("zh-hans", "Simplified Chinese"),
                                ("zh-hant", "Traditional Chinese"),
                            ],
                            max_length=32,
                        ),
                        size=None,
                    ),
                ),
                (
                    "pyladies_chapter",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "timezone",
                    models.CharField(
                        choices=[
                            ("UTC+14", "UTC+14"),
                            ("UTC+13", "UTC+13"),
                            ("UTC+12", "UTC+12"),
                            ("UTC+11", "UTC+11"),
                            ("UTC+10", "UTC+10"),
                            ("UTC+9", "UTC+9"),
                            ("UTC+8", "UTC+8"),
                            ("UTC+7", "UTC+7"),
                            ("UTC+6", "UTC+6"),
                            ("UTC+5", "UTC+5"),
                            ("UTC+4", "UTC+4"),
                            ("UTC+3", "UTC+3"),
                            ("UTC+2", "UTC+2"),
                            ("UTC+1", "UTC+1"),
                            ("UTC", "UTC"),
                            ("UTC-1", "UTC-1"),
                            ("UTC-2", "UTC-2"),
                            ("UTC-3", "UTC-3"),
                            ("UTC-4", "UTC-4"),
                            ("UTC-5", "UTC-5"),
                            ("UTC-6", "UTC-6"),
                            ("UTC-7", "UTC-7"),
                            ("UTC-8", "UTC-8"),
                            ("UTC-9", "UTC-9"),
                            ("UTC-10", "UTC-10"),
                            ("UTC-11", "UTC-11"),
                            ("UTC-12", "UTC-12"),
                        ],
                        max_length=6,
                    ),
                ),
                (
                    "roles",
                    models.ManyToManyField(
                        blank=True,
                        related_name="roles",
                        to="volunteer.role",
                        verbose_name="Roles",
                    ),
                ),
                (
                    "teams",
                    models.ManyToManyField(
                        blank=True,
                        related_name="team",
                        to="volunteer.team",
                        verbose_name="team",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("portal.basemodel",),
        ),
        migrations.AddField(
            model_name="team",
            name="team_leads",
            field=models.ManyToManyField(
                related_name="team_leads",
                to="volunteer.volunteerprofile",
                verbose_name="team leads",
            ),
        ),
        migrations.RunPython(create_initial_roles, migrations.RunPython.noop),
    ]
