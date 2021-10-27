# Generated by Django 3.2 on 2021-10-27 07:22

from django.db import migrations, models
import django_rest_admin.model_field


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='routeexec',
            name='import_py_code',
            field=models.TextField(blank=True, help_text='needed if the model need to import from somewhere else. eg:from django.auth import User', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='desc',
            field=models.TextField(blank=True, help_text='表功能描述. eg: this is the rest description', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='filter_keys',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='过滤项. eg: [{"filter_name": "name", "field_name": "name", "filter_type": "text", "lookup_expr": "icontains"}]', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='foreign_key_id',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='外键定义.关联删除属性：CASCADE-关联删除, SET_NULL-字段变空, DO_NOTHING-不做操作. eg: {"user":["User", "CASCADE"], "article":["Article", "SET_NULL"]}', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='foreign_key_ro',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='外键关联的只读内容. eg: {"article_name":"article.name"}', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='foreign_slug_kf',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='一对多外键关联的字段列表. eg: {"StatKucun_wuliao": ["kucun", "jinjia"]}', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='model_object_list',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='可显示字段. eg: ["id", "name", "daima"]', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='no_need_login',
            field=models.IntegerField(blank=True, help_text='访问是否需要登陆。1，0. eg: 0 ', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='ordering',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='默认排序字段，数组，每个项是字符串. eg:["id", "name"]', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='ordering_fields',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='可用排序字段，数组，每个项是字符串. eg:["id", "name"]', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='params',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='AUTO-GENERATED FIELD. DO NOT EDIT THIS MANUALLY.', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='route',
            field=models.TextField(blank=True, help_text='the route name. eg: /Danwei', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='search_fields',
            field=django_rest_admin.model_field.JSONField(blank=True, help_text='可用排序字段，数组，每个项是字符串. eg: ["name", "zhujima"]', null=True),
        ),
        migrations.AlterField(
            model_name='routeexec',
            name='table_name',
            field=models.TextField(blank=True, help_text='the table real name. eg: danwei', null=True),
        ),
    ]
