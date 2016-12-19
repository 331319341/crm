# coding=utf-8
from django.contrib import admin
from django.forms import models
from django.forms import fields,TextInput,Textarea
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.generic import GenericTabularInline
from common import generic
from basedata.models import ValueList,ValueListItem,Address,Partner,BankAccount,Project,Measure,Material,Brand,\
    Category,Warehouse,TechnicalParameterName,TechnicalParameterValue,Trade,ExpenseAccount,Employee,Family,Education,\
    WorkExperience,ExtraParam,DataImport,Document


class ValueListItemInline(admin.TabularInline):
    model = ValueListItem
    exclude = ['group_code']#排除

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 3


class ValueListAdmin(generic.BOAdmin):
    CODE_NUMBER_WIDTH = 3
    CODE_PREFIX = 'S'
    list_display = ['code', 'name', 'module', 'status']  #指定要显示的字段
    fields = (('code',),('name',),('module',),('status','init','locked',),('locked_by','lock_time',)) #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
    raw_id_fields = ['module'] #在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    readonly_fields = ['locked_by','lock_time'] #只读字段
    inlines = [ValueListItemInline] #内联
    search_fields = ['code','name']#指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词


def save_model(self, request, obj, form, change):
        super(ValueListAdmin,self).save_model(request,obj,form,change)
        obj.valuelistitem_set.update(group_code=obj.code)


class AddressAdmin(generic.BOAdmin):
    list_display = ['address','phone','contacts']# 指定要显示的字段
    exclude = ['content_type','object_id','creator','modifier','creation','modification','begin','end']#排除


class AddressInline(GenericTabularInline):  #通用表格内联
    model = Address
    exclude = ['content_type','object_id','creator','modifier','creation','modification','begin','end']#排除
    extra = 1


class BankAccountInline(admin.TabularInline):
    model = BankAccount
    fields = ['account','title','memo']# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


class PartnerForm(models.ModelForm):
    tax_address = fields.CharField(widget=TextInput(attrs={'size': 119,}),required=False,label=_("tax address"))
    memo = fields.CharField(widget=Textarea(attrs={'rows':3,'cols':85}),required=False,label=_("memo"))

    class Meta:
        model = Partner
        fields = '__all__'# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性


class PartnerAdmin(generic.BOAdmin):
    list_display = ['code','name','partner_type','level']# 指定要显示的字段
    list_display_links = ['code','name']#它的作用是提供一个超链接，转到form_change页面，就是修改页面。

    fields = (('code','name',),('short','pinyin',),('partner_type','level'),('tax_num','tax_account',),
              ('tax_address',),('contacts','phone',),('memo',),)# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
    search_fields = ['code','name','pinyin']# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    form = PartnerForm
    save_on_top = True
    inlines = [AddressInline,BankAccountInline]#内联

    def get_queryset(self, request):
        if request.user.is_superuser or (request.user.has_perm('basedate.view_all_customer') and request.user.has_perm('basedate.view_all_supplier')):
            return super(PartnerAdmin,self).get_queryset(request)
        elif request.user.has_perm('basedata.view_all_customer'):
            return super(PartnerAdmin,self).get_queryset(request).filter(partner_type='C')
        else:
           return super(PartnerAdmin,self).get_queryset(request).filter(partner_type='S')


class ProjectForm(models.ModelForm):
    income = fields.DecimalField(required=False,widget=TextInput(attrs={'readonly':'true'}))
    expand = fields.DecimalField(required=False,widget=TextInput(attrs={'readonly':'true'}))

    class Meta:
        model = Project
        fields = '__all__'# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性


class ProjectAdmin(generic.BOAdmin):
    CODE_PREFIX = 'PJ'
    list_display = ['code','name','status','income','expand']# 指定要显示的字段
    list_display_links = ['code','name']#它的作用是提供一个超链接，转到form_change页面，就是修改页面。
    fields = (
        ('code','name',),('short','pinyin',),
        ('partner',),('status','prj_type',),
        ('description',),
        ('budget','income','expand',),('blueprint',),('offer',),('business',),('users',),
    )# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
    search_fields = ['code','name']# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    readonly_fields = ['status']#只读字段
    raw_id_fields = ['partner']#在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    filter_horizontal = ['users']#过滤内置条件
    form = ProjectForm


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['code','name','location']# 指定要显示的字段
    filter_horizontal = ['users']#过滤内置条件

    def save_model(self, request, obj, form, change):
        super(WarehouseAdmin,self).save_model(request,obj,form,change)
        try:
            code = getattr(obj,'code')
            if not code:
                obj.code = '%s%02d' % ('A',obj.id)
                obj.save()
        except Exception,e:
            self.message_user(request,'ERROR:%s' % e,level=messages.ERROR)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','pinyin']# 指定要显示的字段


class MeasureAdmin(admin.ModelAdmin):
    list_display = ['code','name','status']# 指定要显示的字段


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code','name','path']# 指定要显示的字段

    def save_model(self, request, obj, form, change):
        super(CategoryAdmin,self).save_model(request,obj,form,change)
        try:
            code = getattr(obj,'code')
            if not code:
                obj.code = '%s%02d' % ('F',obj.id)
                obj.save()
            if obj.parent:
                if obj.parent.path:
                    obj.path = obj.parent.path + '/'+obj.parent.name
                else:
                    obj.path = obj.parent.name
                obj.save()
        except Exception,e:
            self.message_user(request,'ERROR:%s' % e,level=messages.ERROR)


class MaterialForm(models.ModelForm):
    name = fields.CharField(widget=TextInput(attrs={"size":"119"}),label=_("material name"))
    spec = fields.CharField(widget=TextInput(attrs={"size":"119"}),required=False,label=_("specifications"))

    class Mata:
        model = Material
        fields = '__all__'# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性


class ExtraParamInline(admin.TabularInline):
    model = ExtraParam
    fields = ['name','data_type','data_source']# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


class MaterialAdmin(generic.BOAdmin):
    CODE_PREFIX = 'IT'
    CODE_NUMBER_WIDTH = 5
    list_display = ['code','name','spec','tp']# 指定要显示的字段
    list_display_links = ['code','name']#它的作用是提供一个超链接，转到form_change页面，就是修改页面。
    list_filter = ['brand','tp']# 指定列表过滤器，
    search_fields = ['code','name']# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    fields = (
        ('code','barcode'),('name',),('spec',),
        ('brand',),('category',),('status','is_equip','can_sale','is_virtual',),
        ('warehouse',),('tp',),('measure',),('stock_price','purchase_price','sale_price',),
    )# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
    filter_horizontal = ['measure']#过滤内置条件
    inlines = [ExtraParamInline]#内联
    form = MaterialForm


class TechParamValueInline(admin.TabularInline):
    model = TechnicalParameterValue


class TechParamNameAdmin(admin.ModelAdmin):
    list_display = ['name','category']# 指定要显示的字段
    inlines = [TechParamValueInline]#内联


class TradeAdmin(admin.ModelAdmin):
    list_display = ['code','name','parent']# 指定要显示的字段


class ExpenseAdmin(generic.BOAdmin):
    CODE_PREFIX = 'FC'
    list_display = ['code','name','category']# 指定要显示的字段
    list_display_links = ['code','name']#它的作用是提供一个超链接，转到form_change页面，就是修改页面。
    list_filter = ['category']# 指定列表过滤器，
    search_fields = ['name']# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词


class FamilyForm(models.ModelForm):
    name = fields.CharField(widget=TextInput(attrs={"size":"25"}),label=_("name"))
    phone = fields.CharField(widget=TextInput(attrs={"size":"25"}),label=_("phone"))

    class Meta:
        model = Family
        fields = '__all__'# 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性


class FamilyInline(admin.TabularInline):
    model = Family
    exclude = ['creator','modifier','creation','modification','begin','end']#排除
    form = FamilyForm
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    exclude = ['creator','modifier','creation','modification']#排除
    extra = 0


class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    exclude = ['creator','modifier','creation','modification']#排除
    extra = 1


class EmployeeAdmin(generic.BOAdmin):
    CODE_PREFIX = '1'
    list_display = ['code','name','position','gender','idcard','age','work_age','literacy','phone','email']# 指定要显示的字段
    search_fields = ['code','name','idcard','pinyin']# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    fieldsets = [
        (None,{'fields':[('code','phone',),('name','pinyin',),('gender','birthday',),('idcard','country',),
                         ('position',),('rank','category'),('status','ygxs',),('workday','startday',)]}),
        (_('other info'),{'fields':[('hometown','address',),('banknum','bankname',),('email','office',),
        ('emergency','literacy',),('religion','marital',),('party','nation',),('spjob','health',),
        ('major','degree',),('tag1','tag2',),('tag3','tag4',),('user',),],'classes':['collapse']}),
    ]# 分组表单
    readonly_fields = ['status','ygxs','rank','category']#只读字段
    inlines = [FamilyInline,EducationInline,WorkExperienceInline]#内联
    raw_id_fields = ['user']#在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.has_perm('basedata.view_all_employee'):
            return super(EmployeeAdmin,self).get_queryset(request)
        else:
            return super(EmployeeAdmin,self).get_queryset(request).filter(user=request.user)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['status','ygxs','rank','category','position','user']


class DataImportAdmin(generic.BOAdmin):
    list_display = ['imp_date','title','status']# 指定要显示的字段
    list_display_links = ['imp_date','title']#它的作用是提供一个超链接，转到form_change页面，就是修改页面。
    raw_id_fields = ['content_type']#在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    readonly_fields = ['status']#只读字段
    extra_buttons = [{'href':'action','title':_('import')}]

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if object_id:
            obj = DataImport.objects.get(id=object_id)
            if obj.status == '1':
                extra_context = extra_context or {}
                extra_context.update(dict(readonly=True))
        return super(DataImportAdmin,self).changeform_view(request,object_id,form_url,extra_context)


class DocumentForm(models.ModelForm):
    title = fields.CharField(widget=TextInput(attrs={"size":"119"}),label=_("title"))
    keywords = fields.CharField(widget=TextInput(attrs={"size":"119"}),label=_("keywords"))

    class Meta:
        model = Document
        fields = '__all__'


class DocumentAdmin(generic.BOAdmin):
    CODE_PREFIX = 'FD'
    CODE_NUMBER_WIDTH = 4
    list_display = ['code','title','keywords','tp','business_domain','status','creation']# 指定要显示的字段
    list_display_links = ['code','title']#它的作用是提供一个超链接，转到form_change页面，就是修改页面。
    fields = (('code','status',),('title',),('keywords',),('description',),('business_domain','tp',),('attach',))
    readonly_fields = ['status']#只读字段
    list_filter = ['tp','business_domain']# 指定列表过滤器，
    search_fields = ['title','keywords','code']# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    form = DocumentForm
    actions = ['publish']
    date_hierarchy = 'begin'# 日期型字段进行层次划分。

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status=='1':
            return ['code','status','title','keywords','description','business_domain','tp','attach',]
        else:
            return ['status']

    def publish(self,request,queryset):
        import datetime
        cnt = queryset.filter(status='0').update(status='1',pub_date=datetime.datetime.now())
        self.message_user(request,u'%s 个文档发布成功'%cnt)

    publish.short_description = _('publish selected %(verbose_name_plural)s')

# admin.site.register(Address,AddressAdmin)
admin.site.register(ValueList,ValueListAdmin) #值列表
admin.site.register(Partner,PartnerAdmin)    #合作伙伴
admin.site.register(Project,ProjectAdmin)    #项目
admin.site.register(Material,MaterialAdmin)  #物料
admin.site.register(Warehouse,WarehouseAdmin) #仓库
admin.site.register(Brand,BrandAdmin)        #品牌
admin.site.register(Measure,MeasureAdmin)    #计量单位
admin.site.register(Category,CategoryAdmin)  #分类
admin.site.register(TechnicalParameterName,TechParamNameAdmin) #技术参数
admin.site.register(Trade,TradeAdmin)        #经济行业
admin.site.register(ExpenseAccount,ExpenseAdmin) #费用科目
admin.site.register(Employee,EmployeeAdmin)    #职员
admin.site.register(DataImport,DataImportAdmin) #导入
admin.site.register(Document,DocumentAdmin)     #文档