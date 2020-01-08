import requests

import app


class EmpApi:
    """员工模块"""

    def __init__(self):
        self.emp_url = app.HOST + '/api/sys/user'
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        """新增员工"""
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": '2020-01-01',
            "formOfEmployment": 2,
            "workNumber": '121214',
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-30T16:00:00.000Z"
        }
        print('新增请求头：', self.headers)
        return requests.post(self.emp_url, json=data, headers=self.headers)

    def query_emp(self):
        """查询员工"""
        url = self.emp_url + '/' + app.EMP_ID
        print(url)
        return requests.get(url, headers=self.headers)

    def update_emp(self, update_data):
        """修改员工"""
        url = self.emp_url + '/' + app.EMP_ID
        print(url)
        return requests.put(url, json=update_data, headers=self.headers)

    def del_emp(self):
        """删除员工"""
        url = self.emp_url + '/' + app.EMP_ID
        print(url)
        return requests.delete(url, headers=self.headers)

    def query_emp_list(self, page, size):
        url = self.emp_url + '?page=' + str(page) + '&size=' + str(size)
        print(url)
        return requests.get(url, headers=self.headers)
