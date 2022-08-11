from django import forms
from my_job.models import Entrance

WALL_MATERIAL = [
    ('Panel', 'Панельный'),
    ('brick', 'Кирпичный'),
    ('wood', 'Деревянный'),
]


# форма для составления дв
class EntranceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntranceForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({
            'font - size': '100px',
        })

    class Meta:
        model = Entrance
        fields = '__all__'

# class EntranceForm(forms.Form):
#     address = forms.CharField(label='Адрес')
#     floor = forms.IntegerField(label='Этажность', initial='Entrance.objects.get')
#     walls = forms.CharField(max_length=30, label='Материал стен', initial='panel')
#     vestibule = forms.BooleanField(required=True, label='Тамбура')
#     number_of_vestibules = forms.IntegerField(required=False, label='Количество тамбуров')
#     ceiling = forms.FloatField(initial=0, label='Объём потолка подъезда')
#     ceiling_vestibule = forms.FloatField(initial=0, label='Объём потолка тамбура')
#     painted_walls = forms.FloatField(initial=0, label='Объём окрашенных стен подъезда')
#     painted_walls_vestibule = forms.FloatField(initial=0, label='Объём окрашенных стен тамбура')
#     whitewash_walls = forms.FloatField(required=False, label='Объём побелки стен подъезда')
#     whitewash_walls_vestibule = forms.FloatField(required=False, label='Объём побелки стен тамбура')
#     number_windows = forms.IntegerField(required=False, label='Количество окон')
#     windows_size = forms.FloatField(required=False, label='размер окна')
#     railing = forms.FloatField(required=False, label='площадь перил')
#     butt_stairs = forms.FloatField(required=False, label='площадь торца лестницы')
#     pipe_coloring = forms.FloatField(required=False, label='площадь окраски труб')
