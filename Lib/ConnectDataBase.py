#连接数据库
import cx_Oracle as cx
DataBase_154="INSIGHT/insight@10.175.94.154:1525/orcl"#注意端口要写
DataBase_155="INSIGHT/insight@10.175.94.155:1521/orcl"
def ConnectDataBase_154(sql):
    """
    :param sql: sql语句
    :return:查询结果
    """
    con=cx.connect(DataBase_154)#创建连接
    cur=con.cursor()#创建游标
    cur.execute(sql)#执行SQL语句
    rowdata =cur.fetchall()#抓取全部数据 fetchone 抓单笔数据
    return rowdata
def ConnectDataBase_155(sql):
    con=cx.connect(DataBase_155)#创建连接
    cur=con.cursor()#创建游标
    cur.execute(sql)#执行SQL语句
    rowdata =cur.fetchall()#抓取全部数据 fetchone 抓单笔数据
    return rowdata
