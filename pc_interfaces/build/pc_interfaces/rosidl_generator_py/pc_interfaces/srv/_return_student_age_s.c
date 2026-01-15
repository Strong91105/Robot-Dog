// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "pc_interfaces/srv/detail/return_student_age__struct.h"
#include "pc_interfaces/srv/detail/return_student_age__functions.h"

bool pc_interfaces__msg__student__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * pc_interfaces__msg__student__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool pc_interfaces__srv__return_student_age__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[63];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("pc_interfaces.srv._return_student_age.ReturnStudentAge_Request", full_classname_dest, 62) == 0);
  }
  pc_interfaces__srv__ReturnStudentAge_Request * ros_message = _ros_message;
  {  // student
    PyObject * field = PyObject_GetAttrString(_pymsg, "student");
    if (!field) {
      return false;
    }
    if (!pc_interfaces__msg__student__convert_from_py(field, &ros_message->student)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * pc_interfaces__srv__return_student_age__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ReturnStudentAge_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("pc_interfaces.srv._return_student_age");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ReturnStudentAge_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  pc_interfaces__srv__ReturnStudentAge_Request * ros_message = (pc_interfaces__srv__ReturnStudentAge_Request *)raw_ros_message;
  {  // student
    PyObject * field = NULL;
    field = pc_interfaces__msg__student__convert_to_py(&ros_message->student);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "student", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__struct.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool pc_interfaces__srv__return_student_age__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[64];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("pc_interfaces.srv._return_student_age.ReturnStudentAge_Response", full_classname_dest, 63) == 0);
  }
  pc_interfaces__srv__ReturnStudentAge_Response * ros_message = _ros_message;
  {  // age
    PyObject * field = PyObject_GetAttrString(_pymsg, "age");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->age = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * pc_interfaces__srv__return_student_age__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ReturnStudentAge_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("pc_interfaces.srv._return_student_age");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ReturnStudentAge_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  pc_interfaces__srv__ReturnStudentAge_Response * ros_message = (pc_interfaces__srv__ReturnStudentAge_Response *)raw_ros_message;
  {  // age
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->age);
    {
      int rc = PyObject_SetAttrString(_pymessage, "age", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
