from django.contrib import admin
from django.db.models import JSONField
from main_app import models
from django_json_widget.widgets import JSONEditorWidget
from django.conf import settings


admin.site.site_title = f"لوحة إدارة مسجد {settings.MASJED_NAME}"
admin.site.site_header = f"إدارة مسجد {settings.MASJED_NAME}"


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(models.Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ["name", "age", "category", "mother_name"]
    search_fields = ["name"]
    list_select_related = ["category"]
    list_filter = ["category"]

    # here changed the widget of JSONField into another widget, this widget is imported from django_json_widget.widgets
    # we should firstly install the module 'django-json-widget' by using 'pip install django-json-widget', then we should go INSTALLED_APPS in settings.py and add 'django_json_widget'
    formfield_overrides = {
        JSONField: {
            "widget": JSONEditorWidget(
                mode="code",
                options={
                    "modes": ["code", "form"],
                    "mode": "code",
                    "search": True,
                },
            )
        }
    }

    # here we will define method that make us to edit 'add object' and 'change object' separatly
    def get_form(self, request, obj=None, **kwargs):
        # here the property kwargs (which we used below) has these keys: form, fields, exclude, formfield_callback

        # here when the object has already been added (change object case)
        if obj:
            pass

        # here when the object doesn't exisit (add object case)
        else:
            kwargs["exclude"] = (
                "q_memorizing",
                "q_test",
                "q_awqaf_test",
                "q_awqaf_test_looking",
                "q_awqaf_test_explaining",
                "alarbaein_alnawawia_old",
                "alarbaein_alnawawia_new",
                "riad_alsaalihin_old",
                "riad_alsaalihin_new",
                "allah_names_old",
                "allah_names_new",
            )
        return super().get_form(request, obj, **kwargs)


@admin.register(models.MemorizeMessage)
class AdminMemorizeMessage(admin.ModelAdmin):
    list_display = ["id", "master_name", "student", "message_type", "sended_at"]
    list_select_related = ["master_name__user", "student"]
    readonly_fields = [
        "master_name",
        "student",
        "message_type",
        "sended_at",
        "first_info",
    ]
    list_filter = ["master_name", "message_type"]
    search_fields = ["student_string"]
    exclude = ["student_string", "second_info"]

    # this method prevent admin from deleting objects in this model
    def has_delete_permission(self, _, __=None):
        return False

    def has_change_permission(self, _, __=None) -> bool:
        return False

    def has_add_permission(self, _, __=None) -> bool:
        return False

    ormfield_overrides = {
        JSONField: {
            "widget": JSONEditorWidget(
                mode="code",
                options={
                    "modes": ["code", "form"],
                    "mode": "code",
                    "search": True,
                },
            )
        }
    }


@admin.register(models.MemorizeNotes)
class AdminMemorizeNote(admin.ModelAdmin):
    list_display = ["master_full_name", "student", "sended_at"]
    list_select_related = ["master_name__user", "student"]
    readonly_fields = ["master_name", "student", "content", "sended_at"]
    list_filter = ["master_name"]
    search_fields = ["student_string"]
    exclude = ["student_string"]

    def master_full_name(self, obj: models.MemorizeNotes) -> str:
        return f"{obj.master_name.first_name} {obj.master_name.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

    def has_delete_permission(self, _, __=None):
        return False

    def has_change_permission(self, _, __=None) -> bool:
        return False

    def has_add_permission(self, _, __=None) -> bool:
        return False


@admin.register(models.ComingCategory)
class ComingCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Coming)
class ComingAdmin(admin.ModelAdmin):
    list_display = ["student", "master_full_name", "category", "registered_at"]
    list_filter = ["registered_at", "category"]
    list_select_related = ["student", "master_name__user", "category"]

    def master_full_name(self, obj: models.MemorizeNotes) -> str:
        return f"{obj.master_name.first_name} {obj.master_name.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

    def has_delete_permission(self, _, __=None):
        return False

    def has_change_permission(self, _, __=None):
        return False

    def has_add_permission(self, _, __=None):
        return False


@admin.register(models.DoublePointMessage)
class DoublePointMessageAdmin(admin.ModelAdmin):
    list_display = ["student", "points", "sended_at"]
    list_select_related = ["student"]
    readonly_fields = ["student", "points", "content"]

    def has_delete_permission(self, _, __=None):
        return False

    def has_change_permission(self, _, __=None):
        return False

    def has_add_permission(self, _, __=None):
        return False


@admin.register(models.PointsAddingCause)
class PointsAddingCauseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MoneyDeletingCause)
class MoneyDeletingCauseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AwqafTestNoQ)
class AwqafTestNoQAdmin(admin.ModelAdmin):
    list_display = ["name", "points"]


@admin.register(models.PointsAdding)
class PointsAddingAdmin(admin.ModelAdmin):
    list_display = ["student", "master_full_name", "cause", "created_at"]
    list_select_related = ["student", "cause", "master_name__user"]

    def master_full_name(self, obj: models.MemorizeNotes) -> str:
        return f"{obj.master_name.first_name} {obj.master_name.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

    def has_delete_permission(self, _, __=None):
        return False

    def has_change_permission(self, _, __=None):
        return False

    def has_add_permission(self, _, __=None):
        return False