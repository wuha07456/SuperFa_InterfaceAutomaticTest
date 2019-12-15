import unittest,requests,json
from SuperFa_InterfaceTest.Lib import ConnectDataBase,CompareAttributeInfo,FindDiffrence
class Test_getAttributesBySnandStation(unittest.TestCase):
    """
    按SN和Station查询Attribute信息
    """
    @classmethod
    def setUpClass(cls) :
        cls.url="http://10.175.94.153:8959/ins/Attribute.json?"

    def test_getAttributesBySnandStation_RightSn_Station_All(self):
        """
        存在的sn和station=All 查询到sn所有工站下的Attribute信息
        """
        data = {}
        data['sn'] = 'G6TZJ00CP82Y'
        data['station']='All'
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        res_text_attributes = res_text['attributes']
        # 对返回值进行断言
        assert res_text['resultCode'] == '200'
        assert res_text['message'] == 'OK'
        assert res_text['attributes'] != []
        # 返回的attributes与数据库查询结果相比较
        # 调用数据库函数进行查询
        SQL="select ta.attribute_name,ta.attribute_value from ins_test_record tr join ins_test_attribute ta on tr.unit_id=ta.unit_id and tr.record_id=ta.record_id where tr.record_info like '%"+data['sn']+"_%'"
        DB_QueryResult=ConnectDataBase.ConnectDataBase_154(SQL)
        #处理DB_QueryResult 为None值 替换为‘’
        for i in range(len(DB_QueryResult)):
            if DB_QueryResult[i][1]==None:
                DB_QueryResult[i]=(DB_QueryResult[i][0],'')
        # 判断返回结果和数据库查询结果是否一致 一致则为TRUE
        CompareResult=CompareAttributeInfo.CompareAttributeInfo(res_text_attributes,DB_QueryResult)
        assert len(res_text_attributes)==len(DB_QueryResult)
        assert CompareResult==True


    def test_getAttributesBySnandStation_RightSn_Station_One(self):
        """
        存在的sn和station=FACT查询到sn 工站FACT的Attribute信息
        """
        data = {}
        data['sn'] = 'G6TZJ00CP82Y'
        data['station']='FACT'
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        res_text_attributes = res_text['attributes']
        # 对返回值进行断言
        assert res_text['resultCode'] == '200'
        assert res_text['message'] == 'OK'
        assert res_text['attributes'] != []
        # 返回的attributes与数据库查询结果相比较
        # 调用数据库函数进行查询
        SQL="select ta.attribute_name,ta.attribute_value from ins_test_record tr join ins_test_attribute ta on tr.unit_id=ta.unit_id and tr.record_id=ta.record_id where tr.record_info like '%"+data['sn']+"_%' and tr.file_name like '%"+data['station']+"%'"
        DB_QueryResult=ConnectDataBase.ConnectDataBase_154(SQL)
        #处理DB_QueryResult 为None值 替换为‘’
        for i in range(len(DB_QueryResult)):
            if DB_QueryResult[i][1]==None:
                DB_QueryResult[i]=(DB_QueryResult[i][0],'')
        #判断返回结果和数据库查询结果是否一致 一致则为TRUE
        CompareResult=CompareAttributeInfo.CompareAttributeInfo(res_text_attributes,DB_QueryResult)
        assert len(res_text_attributes)==len(DB_QueryResult)
        assert CompareResult==True

    def test_getAttributesBySnandStation_SNandStationIsNull(self):
        """
        sn和station都为空
        """
        data = {}
        data['sn'] = ''
        data['station']=''
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        res_text_attributes = res_text['attributes']
        # 对返回值进行断言
        assert res_text['resultCode'] == '400'
        assert res_text['message'] == "Bad Request. 'sn' , 'station' is required parameter."
        assert res_text['attributes'] == []

    def test_getAttributesBySnandStation_SNIsNotNullandStationIsNull(self):
        """
        sn不为空 station为空
        """
        data = {}
        data['sn'] = 'G6TZJ00CP82Y'
        data['station'] = ''
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        res_text_attributes = res_text['attributes']
        # 对返回值进行断言
        assert res_text['resultCode'] == '400'
        assert res_text['message'] == "Bad Request. 'sn' , 'station' is required parameter."
        assert res_text['attributes'] == []

    def test_getAttributesBySnandStation_SNIsNullStationIsAll(self):
        """
        sn为空 station为All
        """
        data = {}
        data['sn'] = ''
        data['station'] = 'All'
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        res_text_attributes = res_text['attributes']
        # 对返回值进行断言
        assert res_text['resultCode'] == '400'
        assert res_text['message'] == "Bad Request. 'sn' , 'station' is required parameter."
        assert res_text['attributes'] == []
