import re
from django import forms


class QuestionLstFilterArgsForm(forms.Form):
    db_table = forms.CharField(max_length=100, required=True)
    min_id = forms.IntegerField(required=False)
    max_id = forms.IntegerField(required=False)
    question_url = forms.CharField(max_length=100, required=False)
    current_question_id = forms.IntegerField(required=False)
    filter_method = forms.ChoiceField(
        choices=(
            ('asc', '顺序'), ('desc', '倒序'), ('random', '随机'),
            ('next', '下一组'), ('previous', '上一组')),
        required=False
    )
    size = forms.IntegerField(max_value=4, min_value=1, required=False)

    def clean_db_table(self):
        data = self.cleaned_data['db_table']
        if re.search('\s+', data):
            raise forms.ValidatitonError('表名不应包含空白符号')
        return data

    def clean(self):
        cleaned_data = super(QuestionLstFilterArgsForm, self).clean()
        # 当筛选条件为next或者previous时，必须有current_question_id参数
        if cleaned_data.get('filter_method') and \
                cleaned_data['filter_method'] in ('next', 'previous'):
            if not isinstance(
                cleaned_data['current_question_id'], int
            ):
                raise forms.ValidationError(
                    '选择上一题或者下一题时必须提供当前question_id'
                )
        if cleaned_data.get('max_id') \
                and cleaned_data.get('min_id') \
                and cleaned_data['max_id'] < cleaned_data['min_id']:
            raise forms.ValidationError(
                'max_id需要比min_id大'
            )
        if cleaned_data.get('spider_url', None) is None and \
                cleaned_data.get('filter_method') is None:
            raise forms.ValidationError(
                '必须提供spider_url或者其他查询方法'
            )
        return cleaned_data
