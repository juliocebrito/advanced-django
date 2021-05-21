from django.conf import settings
from django.db import models
from django.contrib import admin


class BaseModel(models.Model):
    """Base model.

    This acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + updated (DateTime): Store the last datetime the object was updated.
        + created_by (ForeignKey): Store the user relationship which the object was created.
        + updated_by (ForeignKey): Store the user relationship which the object was updated.
        + state (BooleanField): Store the Main object state.
        + substate (BooleanField): Store the Secondary object state.
    """

    created_at = models.DateTimeField('created at', auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    updated_at = models.DateTimeField('updated at', auto_now=True,
        help_text='Date time on which the object was last updated.'
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, 
        null=True, blank=True, editable=False, related_name='%(class)s_created_by_user',
        help_text='User by the object was created.'
    )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, 
        null=True, blank=True, editable=False, related_name='%(class)s_updated_by_user',
        help_text='User by which the object was last updated.'
    )
    state = models.BooleanField('main state', default=False, editable=False,
        help_text='Main object state.'
    )
    substate = models.BooleanField('secondary state', default=False, editable=False,
        help_text='Secondary object state.'
    )

    class Meta:
        """Meta options."""

        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']


    def __str__(self) -> int:
        return self.id


class BaseModelAdmin(admin.ModelAdmin):
    # list_display = (...,)
    actions = [
        'change_state_true',
        'change_state_false',
        'change_substate_true',
        'change_substate_false',
    ]

    def change_state_true(self, request, queryset):
        queryset.update(state=True)
        self.message_user(request, f'{queryset.count()} objects updated')
    change_state_true.short_description = 'Make selected main state to true'

    def change_state_false(self, request, queryset):
        queryset.update(state=False)
        self.message_user(request, f'{queryset.count()} objects updated')
    change_state_false.short_description = 'Make selected main state to false'

    def change_substate_true(self, request, queryset):
        queryset.update(state=True)
        self.message_user(request, f'{queryset.count()} objects updated')
    change_substate_true.short_description = 'Make selected secondary state to true'

    def change_substate_false(self, request, queryset):
        queryset.update(state=False)
        self.message_user(request, f'{queryset.count()} objects updated')
    change_substate_false.short_description = 'Make selected secondary state to false'
