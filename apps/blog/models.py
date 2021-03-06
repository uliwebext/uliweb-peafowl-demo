#coding=utf8

from uliweb.orm import *
from uliweb.i18n import ugettext_lazy as _

class BlogCategory(Model):
    name = Field(str, max_length=80, verbose_name=_('Name'), required=True, index=True, unique=True)
    
    def __unicode__(self):
        return self.name

class BlogTag(Model):
    name = Field(str, max_length=80, verbose_name=_('Name'), required=True, index=True, unique=True)

    def __unicode__(self):
        return self.name
    
class Blog(Model):
    title = Field(str, max_length=200, verbose_name=_('Title'), required=True)
    content = Field(TEXT, verbose_name=_('Content'), required=True)
    html = Field(TEXT, verbose_name=_('HTML'))
    created_time = Field(datetime.datetime, verbose_name=_("Created Time"), 
        auto_now_add=True, index=True)
    modified_time = Field(datetime.datetime, verbose_name=_("Modified Time"), 
        auto_now_add=True)
    category = Reference('blogcategory', verbose_name=_('Category'), index=True)
    tags = ManyToMany('blogtag', verbose_name=_('Tag'))
    draft = Field(bool, verbose_name=_('Draft'))
    
    def __unicode__(self):
        return self.title