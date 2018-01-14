# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 19:19
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20180114_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunicationChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(help_text='Name of the communication tool your project uses. E.g. "a mailing list", "IRC", "Zulip", "Mattermost", or "Discourse"', max_length=100)),
                ('url', models.CharField(help_text='URL for the communication channel applicants will use to reach mentors and ask questions about this internship project. IRC URLs should be in the form irc://<host>[:port]/[channel]. Since many applicants have issues with IRC port blocking at their universities, IRC communication links will use <a href="https://kiwiirc.com/">Kiwi IRC</a> to direct applicants to a web-based IRC client. If this is a mailing list, the URL should be the mailing list subscription page.', max_length=200, validators=[django.core.validators.URLValidator(schemes=['http', 'https', 'irc'])])),
                ('instructions', ckeditor.fields.RichTextField(blank=True, help_text='(Optional) After following the communication channel link, are there any special instructions? For example: "Join the #outreachy channel and make sure to introduce yourself.')),
                ('norms', ckeditor.fields.RichTextField(blank=True, help_text="(Optional) What communication norms would a newcomer need to know about this communication channel? Example: newcomers to open source don't know they should Cc their mentor or the software maintainer when asking a question to a large mailing list. Think about what a newcomer would find surprising when communicating on this channel.")),
                ('communication_help', models.URLField(blank=True, help_text='(Optional) URL for the documentation for your communication tool. This should be user-focused documentation that explains the basic mechanisms of logging in and features. Suggestions: IRC - https://wiki.gnome.org/Outreachy/IRC; Zulip - https://chat.zulip.org/help/; Mattersmost - https://docs.mattermost.com/guides/user.html')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_help',
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_norms',
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_tool',
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_url',
        ),
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Description of the internship project, excluding applicant skills and communication channels. Those will be added in the next step.'),
        ),
        migrations.AddField(
            model_name='communicationchannel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project'),
        ),
    ]
