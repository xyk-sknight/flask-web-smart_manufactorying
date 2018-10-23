from app.models import Product,Repository


# 定义入库方法
def Rpo_Input(rpo_id, proc_id):
    product = Product.query.filter_by(id=proc_id).first()
    # 更新仓库数据
    Repository.query.filter_by(id=rpo_id).update({'type': product.type, 'product_id': proc_id})
    # 更新产品数据
    Product.query.filter_by(id=rpo_id).update({'rpo_id': rpo_id, 'status': '在库', 'position': '仓库'})


# 定义出库方法
def Rpo_output(rpo_id, proc_id):
    # 更新仓库数据
    Repository.query.filter_by(id=rpo_id).update({'type': '空', 'product_id': None})
    # 更新产品数据
    Product.query.filter_by(id=proc_id).update({'rpo_id': 0, 'status': '已出库', 'position': '工作台'})