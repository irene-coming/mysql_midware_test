# -*- coding=utf-8 -*-
# Copyright (C) 2016-2020 ActionTech.
# License: https://www.mozilla.org/en-US/MPL/2.0 MPL version 2 or higher.
# @Time    : 2020/8/27 AM10:29
# @Author  : irene-coming


from threading import Thread

import requests

class Flag:
    exception = None

global base_url
global my_token

def login_in():
    global my_token

    login_api="/v4/user/login"
    login_data = {"user_name":"admin","user_password":"admin"}
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    r1 = requests.post(url=base_url+login_api, data=login_data, headers=header)
    r1_json = r1.json()
    my_token = r1_json["token"]
    print("token:",my_token)

def do_request(url, form_data, headers, files = [('sql_audit_task_input_sql_file',None)]):
    r = requests.post(url, data=form_data, headers=headers, files=files)
    print(r.request.body.decode('utf-8'))
    print("response:",r.text)

def concurrent_requests_ddl_db(concur=80):
    global my_token
    url = base_url + "/v3/sqle/sql_audit_task/add"
    headers = {
        "Authorization":my_token
    }

    form_data = {
        "sql_audit_task_title":"",
        "sql_audit_task_type":"DDL",
        "mysql_group_id":"",
        "sql_audit_task_description":"desc",
        "sql_audit_task_input_sqls":"create database db1"
    }

    for i in range(1,concur):
        form_data["sql_audit_task_title"] = "task_no{0}".format(i)
        form_data["mysql_group_id"] = "mysql-group-9-{}".format(i)

        # do_request(url, form_data, headers)
        # break

        thd = Thread(target=do_request, args=(url, form_data, headers))
        thd.start()
        thd.join()

def concurrent_requests_ddl_table(concur=80):
    global my_token
    url = base_url + "/v3/sqle/sql_audit_task/add"
    headers = {
        "Authorization":my_token
    }

    form_data = {
        "sql_audit_task_title":"",
        "sql_audit_task_type":"DDL",
        "mysql_group_id":"",
        "sql_audit_task_description":"desc",
        "mysql_instance_schema":"db1",
        "sql_audit_task_input_sqls":"CREATE TABLE if not exists `sbtest1` (`id` bigint unsigned NOT NULL AUTO_INCREMENT,`k` int(11) NOT NULL DEFAULT '0',`c` varchar(120) COLLATE utf8mb4_bin NOT NULL DEFAULT '',`pad` varchar(60) COLLATE utf8mb4_bin NOT NULL DEFAULT '',PRIMARY KEY (`id`),KEY `idx_k_1` (`k`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin"
    }

    for i in range(1,concur):
        form_data["sql_audit_task_title"] = "task create table no{0}".format(i)
        form_data["mysql_group_id"] = "mysql-group-9-{}".format(i)

        thd = Thread(target=do_request, args=(url, form_data, headers))
        thd.start()
        thd.join()

def concurrent_requests_dml_insert(concur=80):
    global my_token
    url = base_url + "/v3/sqle/sql_audit_task/add"
    headers = {
        "Authorization":my_token
    }

    form_data = {
        "sql_audit_task_title":"",
        "sql_audit_task_type":"DML",
        "mysql_group_id":"",
        "sql_audit_task_description":"desc",
        "mysql_instance_schema":"db1",
        "sql_audit_task_input_sqls":"INSERT INTO `sbtest1` VALUES (3,13231,'75174321148-49485865060-07867590268-11713647447-55783902304-15729068813-93789332667-19111946546-96474020372-22303419925','61107537806-87302173439-75421856184-25535227860-96689052374')"
    }

    for i in range(1,concur):
        form_data["sql_audit_task_title"] = "task insert into table no{0}".format(i)
        form_data["mysql_group_id"] = "mysql-group-9-{}".format(i)

        thd = Thread(target=do_request, args=(url, form_data, headers))
        thd.start()
        thd.join()

def concurrent_requests_dml_insert_file(concur=80):
    global my_token
    url = base_url + "/v3/sqle/sql_audit_task/add"
    headers = {
        "Authorization":my_token
    }

    form_data = {
        "sql_audit_task_title":"",
        "sql_audit_task_type":"DML",
        "mysql_group_id":"",
        "sql_audit_task_description":"desc",
        "mysql_instance_schema":"db1",
    }

    for i in range(1,concur):
        form_data["sql_audit_task_title"] = "task insert into table with file no{0}".format(i)
        form_data["mysql_group_id"] = "mysql-group-9-{}".format(i)

        files = [('sql_audit_task_input_sql_file', open("./my_insert.sql", 'rb'))]

        thd = Thread(target=do_request, args=(url, form_data, headers, files))
        thd.start()
        thd.join()

def concurrent_requests_same_title_(concur=80):
    global my_token
    url = base_url + "/v3/sqle/sql_audit_task/add"
    headers = {
        "Authorization":my_token
    }

    form_data = {
        "sql_audit_task_title":"task same title6",
        "sql_audit_task_type":"DDL",
        "mysql_group_id":"",
        "sql_audit_task_description":"desc",
        "sql_audit_task_input_sqls":"create database db1"
    }

    for i in range(1,concur):
        form_data["mysql_group_id"] = "mysql-group-9-1".format(i)

        # do_request(url, form_data, headers)
        # break

        thd = Thread(target=do_request, args=(url, form_data, headers))
        thd.start()
        thd.join()

if __name__ == "__main__":
    base_url = ""
    login_in()
    # concurrent_requests_ddl_db(81)
    # concurrent_requests_ddl_table(81)
    # concurrent_requests_dml_insert(81)
    # concurrent_requests_dml_insert_file(81)
    concurrent_requests_same_title_(50)
