def CompareModuleInfo(res_text_modules,DB_QueryResult):
    """
    用于判断接口返回值与数据库查询结果是否一致
    :param res_text_modules:接口返回内容
    :param DB_QueryResult:数据查询结果
    :return:
    """
    Modules=[]
    SerialNumber=[]
    Vendor=[]
    for i in range(len(res_text_modules)):
        Modules.append(res_text_modules[i]['module'])
        SerialNumber.append(res_text_modules[i]['moduleSerialNumber'])
        Vendor.append(res_text_modules[i]['vendor'])
    new_res_result=[]
    for j in range(len(Modules)):
            new_res_result.append((Modules[j]+'-Serial Number',SerialNumber[j]))
            new_res_result.append((Modules[j]+'-Vendor',Vendor[j]))
    #比较是否相等 集合方式比较 顺序不同不影响比较
    CompareResult=set(new_res_result)==set(DB_QueryResult)
    return CompareResult

