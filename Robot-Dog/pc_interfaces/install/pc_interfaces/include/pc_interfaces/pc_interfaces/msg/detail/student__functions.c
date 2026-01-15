// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pc_interfaces:msg/Student.idl
// generated code does not contain a copyright notice
#include "pc_interfaces/msg/detail/student__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
pc_interfaces__msg__Student__init(pc_interfaces__msg__Student * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
pc_interfaces__msg__Student__fini(pc_interfaces__msg__Student * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
pc_interfaces__msg__Student__are_equal(const pc_interfaces__msg__Student * lhs, const pc_interfaces__msg__Student * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
pc_interfaces__msg__Student__copy(
  const pc_interfaces__msg__Student * input,
  pc_interfaces__msg__Student * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

pc_interfaces__msg__Student *
pc_interfaces__msg__Student__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__msg__Student * msg = (pc_interfaces__msg__Student *)allocator.allocate(sizeof(pc_interfaces__msg__Student), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pc_interfaces__msg__Student));
  bool success = pc_interfaces__msg__Student__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pc_interfaces__msg__Student__destroy(pc_interfaces__msg__Student * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pc_interfaces__msg__Student__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pc_interfaces__msg__Student__Sequence__init(pc_interfaces__msg__Student__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__msg__Student * data = NULL;

  if (size) {
    data = (pc_interfaces__msg__Student *)allocator.zero_allocate(size, sizeof(pc_interfaces__msg__Student), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pc_interfaces__msg__Student__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pc_interfaces__msg__Student__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
pc_interfaces__msg__Student__Sequence__fini(pc_interfaces__msg__Student__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      pc_interfaces__msg__Student__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

pc_interfaces__msg__Student__Sequence *
pc_interfaces__msg__Student__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__msg__Student__Sequence * array = (pc_interfaces__msg__Student__Sequence *)allocator.allocate(sizeof(pc_interfaces__msg__Student__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pc_interfaces__msg__Student__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pc_interfaces__msg__Student__Sequence__destroy(pc_interfaces__msg__Student__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pc_interfaces__msg__Student__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pc_interfaces__msg__Student__Sequence__are_equal(const pc_interfaces__msg__Student__Sequence * lhs, const pc_interfaces__msg__Student__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pc_interfaces__msg__Student__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pc_interfaces__msg__Student__Sequence__copy(
  const pc_interfaces__msg__Student__Sequence * input,
  pc_interfaces__msg__Student__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pc_interfaces__msg__Student);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pc_interfaces__msg__Student * data =
      (pc_interfaces__msg__Student *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pc_interfaces__msg__Student__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pc_interfaces__msg__Student__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pc_interfaces__msg__Student__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
