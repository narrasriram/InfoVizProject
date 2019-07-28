# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CanadaDataTemp(models.Model):
    stat_name = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    province = models.CharField(max_length=2, blank=True, null=True)
    mean_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_wo_mean_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mean_temp_diff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    month_max_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_wo_max_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    month_min_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_wo_min_temp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    snowfall = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_wo_snowfall = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nor_snowfall_per = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_precip = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_wo_total_precip = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    norm_precip_per = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    snow_on_grd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_w_precip = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bright_sun = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_wo_brighsun = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    norm_brighsun_per = models.CharField(max_length=5, blank=True, null=True)
    days_below_18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_above_18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    climat_id = models.CharField(max_length=10, blank=True, null=True)
    data_month = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    yearmon = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canada_data_temp'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderInfo(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    delivery_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_info'
# Unable to inspect table 'sample'
# The error was: permission denied for table sample

