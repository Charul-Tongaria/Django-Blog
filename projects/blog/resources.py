from import_export import resources, widgets, fields
from .models import Post, Category

class CharRequiredWidget(widgets.CharWidget):
    def clean(self, value, row=None, *args, **kwargs):
        val = super().clean(value)
        if val:
            return val
        else:
            raise ValueError('This field is required!')

class ForeignkeyRequiredWidget(widgets.ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value:
            print(self.field, value)
            return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: value})
        else:
            raise ValueError(self.field+ " required")

class PostResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignkeyRequiredWidget(Category, 'title'),saves_null_values=False) # title Category modelindeki kolon ismi
    description = fields.Field(saves_null_values=False, column_name='description', attribute='description',widget=CharRequiredWidget())

    class Meta:
        model = Post
        fields = ('title', 'text', 'created_date')
        clean_model_instances = True