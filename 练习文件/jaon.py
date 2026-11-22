import json
date=[{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵啸虎","age":16}]
json_str=json.dumps(date,ensure_ascii=False)
print(type(json_str))
print(json_str)
d={"name":"周杰伦","addr":"台北"}
json_str2=json.dumps(d,ensure_ascii=False)
print(type(json_str2))
print(json_str2)

