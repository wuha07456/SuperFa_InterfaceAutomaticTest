def CompareAttributeInfo(res_text_attributes,DB_QueryResult):
    """
    用于判断接口返回值与数据库查询结果是否一致
    :param res_text_attributes:接口返回内容
    :param DB_QueryResult:数据查询结果
    :return:
    """
    attributeKey=[]
    value=[]
    #把对应的attribute和value取出来
    for i in range(len(res_text_attributes)):
        attributeKey.append(res_text_attributes[i]['attributeKey'])
        value.append(res_text_attributes[i]['value'])
    new_res_result=[]
    for j in range(len(attributeKey)):
        new_res_result.append((attributeKey[j],value[j]))
    #比较是否相等 集合方式比较 顺序不同不影响比较
    CompareResult=set(new_res_result)==set(DB_QueryResult)
    return CompareResult

