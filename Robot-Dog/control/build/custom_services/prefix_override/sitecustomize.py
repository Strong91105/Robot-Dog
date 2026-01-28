import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nuc-lassie/practical_course/group_ws/src/control/install/custom_services'
