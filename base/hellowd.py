print("Hello World!");
print("你好！");

i = 30;
print("i 的值是 {}", format(i));

if i >18 :
    print("你长大了。");
else :
    print("你还是未成年人呢。");
list = ["good","luck","hello",123,780.34];
tinylist = [1234,"join"];
print(list);
print(list[0]);
print(list[1:3]);
print(tinylist * 2);
print(list + tinylist);

tuple = (123,'good','hello');
print(tuple);
print(tuple[2:]);
#tuple[1] = 'ok';
#元组不能被修改
print(tuple);
print(list);
list[2] = 'OK';
print(list);

dict = {} ;
dict["老师"] = 23;
dict["学生"] = 18;
print(dict);
dict["老师"] = 50;
print(dict);

dict2 = {};
dict3 = {};
dict2 = dict;
dict3 = dict.copy(); #内存地址不一样了
if dict is dict2 :
    print("dict is dict2.");
else:
    print("no!!!");
if dict is dict3 :
    print("dict is dict3.");
else:
    print("no!!!");

print("ddddd!");

