# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 PM3:49
# @Author  : zhaohongjie@actionsky.com
# -*- coding: utf-8 -*-

import uuid

def generate_load_data_source_file(file,filter_column_file):

    with open(file,'w',newline='\n') as a, open(filter_column_file,'w') as b:
        for i in range(0,50000):
        # for i in range(0,5):
            col1=uuid.uuid1()
            col2=uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
            org_id='test'

            if i%3==0:
                filter_col="'{0}',".format(col1)
                b.writelines(filter_col)
                # org_id="test"

            row = "{0},{1},{2},{2},{3}\n".format(col1, col2, i,org_id)
            a.writelines(row)


if __name__ == "__main__":
  generate_load_data_source_file("output/load_data_source.csv", "output/filter_file.csv")

# CREATE TABLE `feedback_templates` (
#   `id` varchar(64) DEFAULT NULL,
#   `deleted` tinyint(4) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1

# CREATE TABLE `interview_rounds` (
#   `id` varchar(64) DEFAULT NULL,
#   `visible` tinyint(4) DEFAULT NULL,
#   `name` varchar(20) DEFAULT NULL,
#   `round_id` int(11) DEFAULT NULL,
#   `supplementary_locales` varchar(20) DEFAULT NULL,
#   `colour` int(11) DEFAULT NULL,
#   `color` int(11) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1

# CREATE TABLE `job_round_feedback_connections` (
#   `job_id` varchar(64) DEFAULT NULL,
#   `interview_round_id` varchar(64) DEFAULT NULL,
#   `sort` int(11) DEFAULT NULL,
#   `feedback_template_id` int(11) DEFAULT NULL,
#   `org_id` varchar(10) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1

# load data infile "/init_assets/load_data_source.csv" into table job_round_feedback_connections fields terminated by ',' lines terminated by '\n';