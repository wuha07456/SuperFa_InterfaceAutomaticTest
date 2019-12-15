import unittest,requests,json
from SuperFa_InterfaceTest.Lib import ConnectDataBase,CompareModuleInfo
class Test_getModulesBySn(unittest.TestCase):
    """
    按SN查询Module信息
    """
    @classmethod
    def setUpClass(cls) :
        cls.url="http://10.175.94.153:8959/ins/Module.json?"

    def test_getModulesBySn_WrongSn(self):
        """
        错误的sn 查询不到Module信息
        """
        data = {}
        data['sn'] = 'CXXAABBCCDD'
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        # 对返回值进行断言
        assert res_text['resultCode'] == '204'
        assert res_text['message'] == 'No Content'
        assert res_text['modules'] == []

    def test_getModulesBySn_RightSn(self):
        """
        存在的sn 查询到相关Module信息
        """
        data = {}
        data['sn'] = 'G6TZJ00CP82Y'
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        record_time=res_text['modules'][0]['moduleRecordTime']
        res_text_modules = res_text['modules']
        # 对返回值进行断言
        assert res_text['resultCode'] == '200'
        assert res_text['message'] == 'OK'
        assert res_text['modules'] != []
        # 返回的module与数据库查询结果相比较
        #调用数据库函数进行查询
        SQL="select tm.module_name,tm.module_value from ins_test_record tr join ins_test_module tm on tr.unit_id=tm.unit_id where tr.record_info like '%"+data['sn']+"_"+record_time+"'"
        DB_QueryResult=ConnectDataBase.ConnectDataBase_154(SQL)
        # 处理DB_QueryResult 为None值 替换为‘’
        for i in range(len(DB_QueryResult)):
            if DB_QueryResult[i][1] == None:
                DB_QueryResult[i] = (DB_QueryResult[i][0], '')
        #调用比较函数ShouldBeEqual 结果为TRUE则数据一致
        CompareResult=CompareModuleInfo.CompareModuleInfo(res_text_modules, DB_QueryResult)
        assert CompareResult==True

    def test_getModulesBySn_SnIsNull(self):
        """
        sn为空 查询不到Module信息
        """
        data = {}
        data['sn'] = ' '
        res = requests.get(self.url, params=data)
        # 将返回的json数据转成dict格式
        res_text = json.loads(res.text)
        # 对返回值进行断言
        assert res_text['resultCode'] == '204'
        assert res_text['message'] == 'No Content'
        assert res_text['modules'] == []
