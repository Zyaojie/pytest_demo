# -*- coding: utf-8 -*-
# @Time : 2023/10/7 19:23
# @Author : 17507
# @File : run
# @Project : pytest_demo
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    # pytest.main(["--html=Report/report.html"])
    pytest.main(["testcases/denglu.py", "--html=testoutput/report.html"])

















