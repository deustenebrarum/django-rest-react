from django.contrib import admin
from api.models import Clients, Employee, Expense, Income, Message
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.template.defaultfilters import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.action(description="Switch status")
def switch_status(selfmodeladmin, request, queryset):
    for query in queryset:
        query.status = not query.status

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    actions = [switch_status]
    list_filter = ['user']
    search_fields = ['name']
    list_display = ['id', 'name', 'get_user_name', 'status', 'role', 'salary_per_hour', 'hours_per_week']
    def get_user_name(self, obj):
        return mark_safe('<a href="{0}?id={2}">{1}</a>'
                .format(reverse("admin:auth_user_changelist"),
                    escape(obj.user.id),
                    escape(obj.user.username)))
    get_user_name.short_description = 'User'

class ClientsResource(resources.ModelResource):
    class Meta:
        model = Clients
@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    resource_class = ClientsResource
    list_filter = ['user']
    list_display =  ['id', 'flow', 'stamp', 'user']
    def get_user_name(self, obj):
        return mark_safe('<a href="{0}?id={2}">{1}</a>'
                .format(reverse("admin:auth_user_changelist"),
                    escape(obj.user.id),
                    escape(obj.user.username)))
    get_user_name.short_description = 'User'

class IncomeResource(resources.ModelResource):
    class Meta:
        model = Income
@admin.register(Income)
class IncomeAdmin(ImportExportModelAdmin):
    resource_class = IncomeResource
    list_filter = ['user']
    list_display = ['id', 'amount', 'description', 'stamp', 'user']
    def get_user_name(self, obj):
        return mark_safe('<a href="{0}?id={2}">{1}</a>'
                .format(reverse("admin:auth_user_changelist"),
                    escape(obj.user.id),
                    escape(obj.user.username)))
    get_user_name.short_description = 'User'

class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expense
@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    resource_class = ExpenseResource
    list_filter = ['user']
    list_display = ['id', 'amount', 'description', 'stamp', 'user']
    def get_user_name(self, obj):
        return mark_safe('<a href="{0}?id={2}">{1}</a>'
                .format(reverse("admin:auth_user_changelist"),
                    escape(obj.user.id),
                    escape(obj.user.username)))

class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin):
    resource_class = MessageResource
    list_filter = ['owner']
    search_fields = ['text']
    list_display = ['id', 'text', 'stamp', 'owner', 'user']
    def get_user_name(self, obj):
        return mark_safe('<a href="{0}?id={2}">{1}</a>'
                .format(reverse("admin:auth_user_changelist"),
                    escape(obj.user.id),
                    escape(obj.user.username)))
    get_user_name.short_description = 'User'