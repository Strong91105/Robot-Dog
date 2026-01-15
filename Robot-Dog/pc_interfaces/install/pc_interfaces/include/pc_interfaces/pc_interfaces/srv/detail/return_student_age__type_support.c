// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "pc_interfaces/srv/detail/return_student_age__rosidl_typesupport_introspection_c.h"
#include "pc_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "pc_interfaces/srv/detail/return_student_age__functions.h"
#include "pc_interfaces/srv/detail/return_student_age__struct.h"


// Include directives for member types
// Member `student`
#include "pc_interfaces/msg/student.h"
// Member `student`
#include "pc_interfaces/msg/detail/student__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pc_interfaces__srv__ReturnStudentAge_Request__init(message_memory);
}

void pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_fini_function(void * message_memory)
{
  pc_interfaces__srv__ReturnStudentAge_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_member_array[1] = {
  {
    "student",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pc_interfaces__srv__ReturnStudentAge_Request, student),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_members = {
  "pc_interfaces__srv",  // message namespace
  "ReturnStudentAge_Request",  // message name
  1,  // number of fields
  sizeof(pc_interfaces__srv__ReturnStudentAge_Request),
  pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_member_array,  // message members
  pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_type_support_handle = {
  0,
  &pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pc_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge_Request)() {
  pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, msg, Student)();
  if (!pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_type_support_handle.typesupport_identifier) {
    pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pc_interfaces__srv__ReturnStudentAge_Request__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__rosidl_typesupport_introspection_c.h"
// already included above
// #include "pc_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__functions.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pc_interfaces__srv__ReturnStudentAge_Response__init(message_memory);
}

void pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_fini_function(void * message_memory)
{
  pc_interfaces__srv__ReturnStudentAge_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_member_array[1] = {
  {
    "age",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pc_interfaces__srv__ReturnStudentAge_Response, age),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_members = {
  "pc_interfaces__srv",  // message namespace
  "ReturnStudentAge_Response",  // message name
  1,  // number of fields
  sizeof(pc_interfaces__srv__ReturnStudentAge_Response),
  pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_member_array,  // message members
  pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_type_support_handle = {
  0,
  &pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pc_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge_Response)() {
  if (!pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_type_support_handle.typesupport_identifier) {
    pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pc_interfaces__srv__ReturnStudentAge_Response__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "pc_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "pc_interfaces/srv/detail/return_student_age__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_members = {
  "pc_interfaces__srv",  // service namespace
  "ReturnStudentAge",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_Request_message_type_support_handle,
  NULL  // response message
  // pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_Response_message_type_support_handle
};

static rosidl_service_type_support_t pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_type_support_handle = {
  0,
  &pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pc_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge)() {
  if (!pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_type_support_handle.typesupport_identifier) {
    pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pc_interfaces, srv, ReturnStudentAge_Response)()->data;
  }

  return &pc_interfaces__srv__detail__return_student_age__rosidl_typesupport_introspection_c__ReturnStudentAge_service_type_support_handle;
}
