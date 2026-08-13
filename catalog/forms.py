from django import forms
from .models import Product

# Список запрещённых слов (все в нижнем регистре)
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):         #класс формы на основе модели
    class Meta:
        model = Product                     #привязываем форму к модели Product
        fields = ['name', 'description', 'image', 'category', 'price']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({
                    'class': 'form-control'
                })
            # Чекбокс и FileField оформляем отдельно
            self.fields['image'].widget.attrs.update({
                'class': 'form-control-file'
            })

        # Валидация поля name
        def clean_name(self):
            name = self.cleaned_data.get('name')
            if name:
                for word in FORBIDDEN_WORDS:
                    if word in name.lower():
                        raise forms.ValidationError(f'Поле "Название" содержит запрещённое слово: {word}')
            return name

        # Валидация поля description
        def clean_description(self):
            description = self.cleaned_data.get('description')
            if description:
                for word in FORBIDDEN_WORDS:
                    if word in description.lower():
                        raise forms.ValidationError(f'Поле "Описание" содержит запрещённое слово: {word}')
            return description

        def clean_price(self):              #проверяет, что цена не отрицательная
            price = self.cleaned_data.get('price')
            if price is not None and price < 0:
                raise forms.ValidationError('Цена не может быть отрицательной.')
            return price