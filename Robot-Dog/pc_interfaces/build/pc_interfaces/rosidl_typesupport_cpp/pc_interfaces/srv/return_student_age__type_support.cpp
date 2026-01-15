// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "pc_interfaces/srv/detail/return_student_age__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace pc_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _ReturnStudentAge_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _ReturnStudentAge_Request_type_support_ids_t;

static const _ReturnStudentAge_Request_type_support_ids_t _ReturnStudentAge_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _ReturnStudentAge_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _ReturnStudentAge_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _ReturnStudentAge_Request_type_support_symbol_names_t _ReturnStudentAge_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pc_interfaces, srv, ReturnStudentAge_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, pc_interfaces, srv, ReturnStudentAge_Request)),
  }
};

typedef struct _ReturnStudentAge_Request_type_support_data_t
{
  void * data[2];
} _ReturnStudentAge_Request_type_support_data_t;

static _ReturnStudentAge_Request_type_support_data_t _ReturnStudentAge_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _ReturnStudentAge_Request_message_typesupport_map = {
  2,
  "pc_interfaces",
  &_ReturnStudentAge_Request_message_typesupport_ids.typesupport_identifier[0],
  &_ReturnStudentAge_Request_message_typesupport_symbol_names.symbol_name[0],
  &_ReturnStudentAge_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t ReturnStudentAge_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_ReturnStudentAge_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace pc_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<pc_interfaces::srv::ReturnStudentAge_Request>()
{
  return &::pc_interfaces::srv::rosidl_typesupport_cpp::ReturnStudentAge_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, pc_interfaces, srv, ReturnStudentAge_Request)() {
  return get_message_type_support_handle<pc_interfaces::srv::ReturnStudentAge_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace pc_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _ReturnStudentAge_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _ReturnStudentAge_Response_type_support_ids_t;

static const _ReturnStudentAge_Response_type_support_ids_t _ReturnStudentAge_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _ReturnStudentAge_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _ReturnStudentAge_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _ReturnStudentAge_Response_type_support_symbol_names_t _ReturnStudentAge_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pc_interfaces, srv, ReturnStudentAge_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, pc_interfaces, srv, ReturnStudentAge_Response)),
  }
};

typedef struct _ReturnStudentAge_Response_type_support_data_t
{
  void * data[2];
} _ReturnStudentAge_Response_type_support_data_t;

static _ReturnStudentAge_Response_type_support_data_t _ReturnStudentAge_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _ReturnStudentAge_Response_message_typesupport_map = {
  2,
  "pc_interfaces",
  &_ReturnStudentAge_Response_message_typesupport_ids.typesupport_identifier[0],
  &_ReturnStudentAge_Response_message_typesupport_symbol_names.symbol_name[0],
  &_ReturnStudentAge_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t ReturnStudentAge_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_ReturnStudentAge_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace pc_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<pc_interfaces::srv::ReturnStudentAge_Response>()
{
  return &::pc_interfaces::srv::rosidl_typesupport_cpp::ReturnStudentAge_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, pc_interfaces, srv, ReturnStudentAge_Response)() {
  return get_message_type_support_handle<pc_interfaces::srv::ReturnStudentAge_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace pc_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _ReturnStudentAge_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _ReturnStudentAge_type_support_ids_t;

static const _ReturnStudentAge_type_support_ids_t _ReturnStudentAge_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _ReturnStudentAge_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _ReturnStudentAge_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _ReturnStudentAge_type_support_symbol_names_t _ReturnStudentAge_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pc_interfaces, srv, ReturnStudentAge)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, pc_interfaces, srv, ReturnStudentAge)),
  }
};

typedef struct _ReturnStudentAge_type_support_data_t
{
  void * data[2];
} _ReturnStudentAge_type_support_data_t;

static _ReturnStudentAge_type_support_data_t _ReturnStudentAge_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _ReturnStudentAge_service_typesupport_map = {
  2,
  "pc_interfaces",
  &_ReturnStudentAge_service_typesupport_ids.typesupport_identifier[0],
  &_ReturnStudentAge_service_typesupport_symbol_names.symbol_name[0],
  &_ReturnStudentAge_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t ReturnStudentAge_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_ReturnStudentAge_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace pc_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<pc_interfaces::srv::ReturnStudentAge>()
{
  return &::pc_interfaces::srv::rosidl_typesupport_cpp::ReturnStudentAge_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, pc_interfaces, srv, ReturnStudentAge)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<pc_interfaces::srv::ReturnStudentAge>();
}

#ifdef __cplusplus
}
#endif
