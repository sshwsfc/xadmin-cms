#coding:utf-8
import exadmin
from exadmin.layout import Fieldset, Field
from exadmin.views.base import CommAdminView

from models import Article, Category

class GolbeSetting(object):
    globe_search_models = [Article, ]
    globe_models_icon = {
        Article: 'file', Category: 'cloud'
    }
exadmin.site.register(CommAdminView, GolbeSetting)

class ArticleAdmin(object):
    list_display = ('title', 'categories', 'date')
    list_display_links = ('title',)

    search_fields = ('title', 'content')
    list_editable = ('date',)
    list_filter = ('categories', 'date')

    form_layout = (
        Fieldset('基本信息',
            'title', 'date'
        ),
        Fieldset('文章内容',
            Field('content', template="xcms/content_field.html")
        ),
    )
    style_fields = {'content': 'wysi_ck', 'categories':'m2m_tree'}

class CategoryAdmin(object):
    list_display = ('name', 'parent')
    list_display_links = ('id', 'name',)

    search_fields = ('name', )
    list_editable = ('name', )
    list_filter = ('parent', )

exadmin.site.register(Article, ArticleAdmin)
exadmin.site.register(Category, CategoryAdmin)
