import json

from app import BASE_DIR


def build_login_data():
    """登录数据解析"""
    dataList = []
    with open(BASE_DIR + '/data/login.json', encoding='utf-8') as f:  # ? 小心乱码哦~
        data = json.load(f)
        for i in data:
            dataList.append((
                i.get('mobile'),
                i.get('password'),
                i.get('status_code'),
                i.get('success'),
                i.get('code'),
                i.get('message')
            ))
    return dataList


def build_insert_emp_data():
    """新增员工数据解析"""
    dataList = []
    with open(BASE_DIR + '/data/employee.json') as f:
        data = json.load(f).get('add_emp')
        dataList.append(
            (data.get('username'),
             data.get('mobile'),
             data.get('status_code'),
             data.get('success'),
             data.get('code'),
             data.get('message')))
    return dataList


def build_query_del_emp_data():
    """查询/删除员工数据解析"""
    dataList = []
    with open(BASE_DIR + '/data/employee.json') as f:
        data = json.load(f).get('query_del_emp')
        dataList.append(
            (data.get('status_code'),
             data.get('success'),
             data.get('code'),
             data.get('message'))
        )
    return dataList


def build_modify_emp_data():
    """修改员工数据解析"""
    dataList = []
    with open(BASE_DIR + '/data/employee.json') as f:
        data = json.load(f).get('modify_emp')
        dataList.append((
            data.get('departmentName'),
            data.get('status_code'),
            data.get('success'),
            data.get('code'),
            data.get('message')
        ))
    return dataList


if __name__ == '__main__':
    print(build_login_data())
    print(build_insert_emp_data())
    print(build_query_del_emp_data())
    print(build_modify_emp_data())
