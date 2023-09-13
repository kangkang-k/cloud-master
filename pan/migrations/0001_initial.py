# Generated by Django 3.2.8 on 2022-05-05 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pan.models
import pan.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('secret_key', models.CharField(db_index=True, max_length=10, verbose_name='分享密匙')),
                ('signature', models.CharField(max_length=70, verbose_name='数字签名')),
                ('expire_time', models.DateTimeField(verbose_name='过期时间')),
                ('summary', models.CharField(blank=True, max_length=100, verbose_name='分享补充描述')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '文件分享',
                'verbose_name_plural': '文件分享',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('type_name', models.CharField(max_length=50, verbose_name='类型名')),
                ('suffix', models.CharField(blank=True, max_length=10, unique=True, verbose_name='文件后缀')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '文件类型',
                'verbose_name_plural': '文件类型',
            },
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('limit_name', models.CharField(max_length=50, verbose_name='限制名称')),
                ('limit_key', models.CharField(max_length=50, unique=True, verbose_name='限制字符')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '限制',
                'verbose_name_plural': '限制',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('role_name', models.CharField(max_length=50, verbose_name='角色名称')),
                ('role_key', models.CharField(max_length=50, unique=True, verbose_name='角色字符')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='用户名')),
                ('ipaddress', models.GenericIPAddressField(verbose_name='ip地址')),
                ('browser', models.CharField(max_length=200, verbose_name='浏览器')),
                ('os', models.CharField(max_length=30, verbose_name='操作系统')),
                ('action', models.CharField(choices=[('0', '登录'), ('1', '登出'), ('2', '登录失败')], max_length=1, verbose_name='动作')),
                ('msg', models.CharField(max_length=100, verbose_name='信息')),
                ('action_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '用户登录日志',
                'verbose_name_plural': '用户登录日志',
            },
        ),
        migrations.CreateModel(
            name='ShareRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('anonymous', models.GenericIPAddressField(blank=True, null=True, verbose_name='匿名用户')),
                ('file_share', models.ForeignKey(on_delete=models.SET(pan.models.get_deleted_file_share), to='pan.fileshare', verbose_name='文件分享')),
                ('recipient', models.ForeignKey(null=True, on_delete=models.SET(pan.models.get_deleted_user), to=settings.AUTH_USER_MODEL, verbose_name='接收者')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '文件接收记录',
                'verbose_name_plural': '文件接收记录',
            },
        ),
        migrations.CreateModel(
            name='RoleLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('value', models.BigIntegerField(verbose_name='值')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('limit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.limit', verbose_name='限制')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.role', verbose_name='角色')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '角色限制',
                'verbose_name_plural': '角色限制',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('avatar', models.ImageField(default='uploads/default/user.svg', upload_to=pan.utils.get_unique_filename, verbose_name='头像')),
                ('gender', models.CharField(blank=True, choices=[('0', '女'), ('1', '男')], max_length=1, verbose_name='性别')),
                ('role', models.ForeignKey(on_delete=models.SET(pan.models.get_deleted_role), to='pan.role', verbose_name='角色')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户概要',
                'verbose_name_plural': '用户概要',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='通知内容')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '通知',
                'verbose_name_plural': '通知',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('action', models.CharField(choices=[('0', '留言'), ('1', '申请')], max_length=1, verbose_name='类型')),
                ('state', models.CharField(choices=[('0', '未审批'), ('1', '通过'), ('2', '未通过')], default='0', max_length=1, verbose_name='状态')),
                ('content', models.TextField(verbose_name='留言内容')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
            },
        ),
        migrations.CreateModel(
            name='GenericFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.TextField(blank=True, verbose_name='备注')),
                ('file_name', models.CharField(max_length=100, verbose_name='文件名')),
                ('file_uuid', models.UUIDField(default=pan.utils.get_uuid, unique=True, verbose_name='文件编号')),
                ('file_cate', models.CharField(choices=[('0', '文件'), ('1', '文件夹')], max_length=1, verbose_name='文件分类')),
                ('file_size', models.BigIntegerField(default=0, verbose_name='文件大小(字节)')),
                ('file_path', models.CharField(db_index=True, max_length=500, verbose_name='文件路径')),
                ('del_flag', models.CharField(choices=[('0', '未回收'), ('1', '已回收')], default='0', max_length=1, verbose_name='回收标识')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('file_type', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_file_type), to='pan.filetype', verbose_name='文件类型')),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pan.genericfile', to_field='file_uuid', verbose_name='上级目录')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '用户文件',
                'verbose_name_plural': '用户文件',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='fileshare',
            name='user_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.genericfile', verbose_name='文件'),
        ),
        migrations.CreateModel(
            name='UserApproval',
            fields=[
            ],
            options={
                'verbose_name': '用户申请',
                'verbose_name_plural': '用户申请',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.message',),
        ),
        migrations.CreateModel(
            name='UserDir',
            fields=[
            ],
            options={
                'verbose_name': '用户文件夹',
                'verbose_name_plural': '用户文件夹',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.genericfile',),
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
            ],
            options={
                'verbose_name': '用户文件',
                'verbose_name_plural': '用户文件',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.genericfile',),
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
            ],
            options={
                'verbose_name': '用户留言',
                'verbose_name_plural': '用户留言',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pan.message',),
        ),
    ]