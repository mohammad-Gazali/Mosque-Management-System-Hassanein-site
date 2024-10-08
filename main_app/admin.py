from django.contrib import admin
from django.db.models import JSONField
from django.http import HttpRequest
from django_json_widget.widgets import JSONEditorWidget
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import QuerySet
from main_app import models


admin.site.site_title = f"لوحة إدارة مسجد {settings.MASJED_NAME}"
admin.site.site_header = f"إدارة مسجد {settings.MASJED_NAME}"


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(models.Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ["name", "mother_name", "category", "student_group", "registered", "registered_at"]
    search_fields = ["name"]
    list_select_related = ["category"]
    list_filter = ["category", "student_group", "registered_at", "registered"]
    list_editable = ["student_group", "category"]

    def hide_student(self, _, queryset: QuerySet[models.Student]):
        control_settings = models.ControlSettings.objects.first()

        for student in queryset:
            control_settings.hidden_ids.append(int(student.id))
        
        control_settings.save()

    def add_coming_for_non_before_coming_students(self, request: HttpRequest, queryset: QuerySet[models.Student]):
        master = models.Master.objects.get(user_id=request.user.id)
        control_settings = models.ControlSettings.objects.first()

        for student in queryset:
            models.Coming.objects.get_or_create(
                student=student,
                category_id=settings.Q_COMING_CATEGORY_ID,
                master=master,
                is_doubled=control_settings.double_points,
            )


    def get_actions(self, request: HttpRequest):
        actions = super().get_actions(request)

        actions["hide_student"] = (self.hide_student, "hide_student", "إخفاء الطلاب المحددين")
        actions["add_coming_for_non_before_coming_students"] = (self.hide_student, "add_coming_for_non_before_coming_students", "تسجيل حضور الطلاب المحددين الذين لم يسجلوا حضور")

        def action_category_maker(value):
            def action_func(_, __, queryset: QuerySet[models.Student]):
                for student in queryset:
                    student.category = value
                    student.save()
            return action_func

        actions["set_no_category"] = (action_category_maker(None), "set_no_category", "إزالة الفئة للطلاب المحددين")

        for category in models.Category.objects.all():
            actions[f"set_category_{category.pk}"] = (action_category_maker(category), f"set_category_{category.pk}", f"التعديل لفئة {category}")

        return actions

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
    list_display = ["id", "master_full_name", "student", "message_type", "sended_at"]
    list_select_related = ["master__user", "student"]
    readonly_fields = [
        "master",
        "student",
        "message_type",
        "sended_at",
        "first_info",
    ]
    list_filter = ["master", "message_type"]
    search_fields = ["student_string"]
    exclude = ["student_string", "second_info"]

    def master_full_name(self, obj: models.MemorizeMessage) -> str:
        return f"{obj.master.user.first_name} {obj.master.user.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

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
    list_select_related = ["master__user", "student"]
    readonly_fields = ["master", "student", "content", "sended_at"]
    list_filter = ["master"]
    search_fields = ["student_string"]
    exclude = ["student_string"]

    def master_full_name(self, obj: models.MemorizeNotes) -> str:
        return f"{obj.master.user.first_name} {obj.master.user.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

    def has_change_permission(self, _, __=None) -> bool:
        return False

    def has_add_permission(self, _, __=None) -> bool:
        return False


@admin.register(models.ComingCategory)
class ComingCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "points"]


@admin.register(models.Coming)
class ComingAdmin(admin.ModelAdmin):
    list_display = ["student", "master_full_name", "category", "registered_at"]
    list_filter = ["registered_at", "category", "student__category"]
    list_select_related = ["student", "master__user", "category"]

    def master_full_name(self, obj: models.Coming) -> str:
        return f"{obj.master.user.first_name} {obj.master.user.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

    def has_change_permission(self, _, __=None):
        return False

    def has_add_permission(self, _, __=None):
        return False


@admin.register(models.DoublePointMessage)
class DoublePointMessageAdmin(admin.ModelAdmin):
    list_display = ["student", "points", "sended_at"]
    list_select_related = ["student"]
    readonly_fields = ["student", "points", "content"]

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
    list_select_related = ["student", "cause", "master__user"]

    def master_full_name(self, obj: models.MemorizeNotes) -> str:
        return f"{obj.master.user.first_name} {obj.master.user.last_name}"
    master_full_name.short_description = "اسم الأستاذ"

    def has_change_permission(self, _, __=None):
        return False

    def has_add_permission(self, _, __=None):
        return False
    

admin.site.unregister(User)

@admin.action(description = "تعطيل المستخدمين العاديين")
def set_unactive(_, __, queryset: QuerySet[User]):
        for user in queryset:
            if user.is_superuser or user.groups.filter(name="تسميع خارج الدورة"):
                continue
            user.is_active = False
            user.save()

@admin.action(description = "تفعيل المستخدمين")
def set_active(_, __, queryset: QuerySet[User]):
    for user in queryset:
        user.is_active = True
        user.save()


@admin.register(User)
class AdminUser(UserAdmin):
    list_display = ["id", "full_name", "username", "is_superuser", "is_active"]
    list_filter = ["is_superuser", "is_active", "groups"]
    actions = [set_active, set_unactive]

    def full_name(self, obj: User) -> str:
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "اسم الأستاذ"


@admin.register(models.StudentGroup)
class AdminStudentGroup(admin.ModelAdmin):
    pass


@admin.register(models.AssetsCategory)
class AdminAssetsCategory(admin.ModelAdmin):
    pass


@admin.register(models.AssetFile)
class AdminAssetFile(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]


@admin.action(description="إضافة الطلاب")
def add_students_action(_, __, queryset: QuerySet[models.NewStudent]):
    for ns in queryset:
        name = f"{ns.first_name} {ns.father_name} {ns.last_name}"
        models.Student.objects.create(
            name=name,
            mother_name=ns.mother_name,
            birthdate=ns.birthdate,
            static_phone=ns.static_phone,
            cell_phone=ns.cell_phone,
            father_phone=ns.father_phone,
            mother_phone=ns.mother_phone,
            father_work=ns.father_work,
            notes=ns.notes,
            registered=True,
        )
        ns.delete()

@admin.register(models.NewStudent)
class AdminNewStudent(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "father_name", "mother_name", "birthdate", "student_class"]
    actions = [add_students_action]
    list_filter = ["student_class"]