# generated from rosidl_generator_py/resource/_idl.py.em
# with input from pc_interfaces:srv/ReturnStudentAge.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ReturnStudentAge_Request(type):
    """Metaclass of message 'ReturnStudentAge_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pc_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pc_interfaces.srv.ReturnStudentAge_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__return_student_age__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__return_student_age__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__return_student_age__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__return_student_age__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__return_student_age__request

            from pc_interfaces.msg import Student
            if Student.__class__._TYPE_SUPPORT is None:
                Student.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ReturnStudentAge_Request(metaclass=Metaclass_ReturnStudentAge_Request):
    """Message class 'ReturnStudentAge_Request'."""

    __slots__ = [
        '_student',
    ]

    _fields_and_field_types = {
        'student': 'pc_interfaces/Student',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['pc_interfaces', 'msg'], 'Student'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from pc_interfaces.msg import Student
        self.student = kwargs.get('student', Student())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.student != other.student:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def student(self):
        """Message field 'student'."""
        return self._student

    @student.setter
    def student(self, value):
        if __debug__:
            from pc_interfaces.msg import Student
            assert \
                isinstance(value, Student), \
                "The 'student' field must be a sub message of type 'Student'"
        self._student = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ReturnStudentAge_Response(type):
    """Metaclass of message 'ReturnStudentAge_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pc_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pc_interfaces.srv.ReturnStudentAge_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__return_student_age__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__return_student_age__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__return_student_age__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__return_student_age__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__return_student_age__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ReturnStudentAge_Response(metaclass=Metaclass_ReturnStudentAge_Response):
    """Message class 'ReturnStudentAge_Response'."""

    __slots__ = [
        '_age',
    ]

    _fields_and_field_types = {
        'age': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.age = kwargs.get('age', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.age != other.age:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def age(self):
        """Message field 'age'."""
        return self._age

    @age.setter
    def age(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'age' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'age' field must be an integer in [-2147483648, 2147483647]"
        self._age = value


class Metaclass_ReturnStudentAge(type):
    """Metaclass of service 'ReturnStudentAge'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pc_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pc_interfaces.srv.ReturnStudentAge')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__return_student_age

            from pc_interfaces.srv import _return_student_age
            if _return_student_age.Metaclass_ReturnStudentAge_Request._TYPE_SUPPORT is None:
                _return_student_age.Metaclass_ReturnStudentAge_Request.__import_type_support__()
            if _return_student_age.Metaclass_ReturnStudentAge_Response._TYPE_SUPPORT is None:
                _return_student_age.Metaclass_ReturnStudentAge_Response.__import_type_support__()


class ReturnStudentAge(metaclass=Metaclass_ReturnStudentAge):
    from pc_interfaces.srv._return_student_age import ReturnStudentAge_Request as Request
    from pc_interfaces.srv._return_student_age import ReturnStudentAge_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
