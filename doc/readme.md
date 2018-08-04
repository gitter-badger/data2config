readme.md


config.yml
~~~ yml

# 输出字段过滤器，为空表示输出所有，否则仅输出包含在data_filter里的字段
# 不区分大小写
data_filter: AC

# 输出文件夹
output_dir: ../dest/
# excel目录
data_dir: excel/
# 模板目录
template_dir: templates/lua

# 管理器的模板
main_templates:
  - staticData.txt

# 每个excel的默认模板
cls_templates:
  - classForMap.txt
  - classForMapExtend.txt: true

# 对于某个数据文件要使用的模板
# 先去 specific_template 查找, 未找到才会使用 cls_templates

# 具体文件的模板,未实现
specific_template:
  - xxxfile.xlsx:
    - classForMap.txt
    - dontOverride.txt: true

~~~


#### Excel文件头格式

1. 简单描述
2. 变量名 INT,FLOAT,STRING,BOOL
3. 变量类型
4. 变量输出标签 A:All(导出到所有) C:Client(导出到客户端) S:Server(导出到服务器) N:Note(不导出，紧策划看)
5. 内容正式开始

例如：

| 序号 | 道具名字 |  价格 |   Note   |
|:----:|:--------:|:-----:|:--------:|
|  id  |   name   | price |   Note   |
|  INT |  STRING  |  INT  |  STRING  |
|   A  |     A    |   A   |     N    |
|  100 |   石头   |   10  | 这是说明 |
|  101 |   木材   |   10  | 这是说明 |
