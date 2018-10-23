from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField,RadioField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('请输入姓名?',validators=[DataRequired()])
    submit = SubmitField('submit')


class Rpo_out(Form):
    submit = SubmitField('出库')


class RepositoryForm(Form):
    id = IntegerField('库位号',validators=[DataRequired()])
    status = RadioField(label='操作选择',choices=[('input_1', '入库(原料）'), ('input_2', '入库(成品）'),('output', '出库')],validators=[DataRequired()])
    submit = SubmitField('提交')


class RepositoryInputForm(Form):
    id = IntegerField('库位号', validators=[DataRequired()])
    product_id = IntegerField('产品编号',validators=[DataRequired()])
    submit = SubmitField('提交')


class RepositoryOutputForm(Form):
    id = IntegerField('库位号', validators=[DataRequired()])
    submit = SubmitField('提交')


class ProductEditForm(Form):
    id = IntegerField('产品编号?', validators=[DataRequired()])
    order_id= IntegerField('订单号?', validators=[DataRequired()])
    type = StringField('产品类型？', validators=[DataRequired()])
    status = StringField('产品状态?', validators=[DataRequired()])
    position = StringField('产品位置?', validators=[DataRequired()])
    submit = SubmitField('提交')


class ProductAddForm(Form):
    id = IntegerField('产品编号?', validators=[DataRequired()])
    order_id = IntegerField('订单号?', validators=[DataRequired()])
    type = StringField('产品类型？', validators=[DataRequired()])
    status = StringField('产品状态?', validators=[DataRequired()])
    position = StringField('产品位置?', validators=[DataRequired()])
    submit = SubmitField('提交')


class EquipmentAddForm(Form):
    eqt_name = StringField('设备名称', validators=[DataRequired()])
    status = StringField('设备状态?', validators=[DataRequired()])
    position = StringField('设备位置?', validators=[DataRequired()])
    submit = SubmitField('提交')

class TaskAddForm(Form):
    proc_id = IntegerField('产品编号?', validators=[DataRequired()])
    rpo_id = IntegerField('库位号?', validators=[DataRequired()])
    state = StringField('出库/入库?', validators=[DataRequired()])
    progress = IntegerField('进度?', validators=[DataRequired()])
    submit = SubmitField('提交')
