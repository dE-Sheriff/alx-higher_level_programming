#include <stdio.h>
#include "/usr/include/python3.4/Python.h"

/**
* print_obj_repr - prints a representation of python object
* @str: string representation
* @n: number of bytes
* Return: Nothing
*/
void print_obj_repr(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
	{
		printf("%02x ", (unsigned char) str[i]);
	}

	printf("%02x", str[i]);
}

/**
* print_python_bytes - prints bytes repr. of python object
* @p: The python object
* Return: Nothing
*/
void print_python_bytes(PyObject *p)
{
	int calc_bytes, bytes_size = 0;
	PyBytesObject *obj_copy = (PyBytesObject *) p;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(obj_copy))
	{
		bytes_size = PyBytes_Size(p);
		calc_bytes = bytes_size + 1;

		if (calc_bytes >= 10)
		{
			calc_bytes = 10;
		}
		printf("  size: %d\n", bytes_size);
		printf("  trying string: %s\n", obj_copy->ob_sval);
		printf("  first %d bytes: ", calc_bytes);
		print_obj_repr(obj_copy->ob_sval, calc_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
* print_python_list - prints list info of python object
* @p: The python object
* Return: Nothing
*/
void print_python_list(PyObject *p)
{
	int list_items_count = 0, i = 0;
	PyObject *item;
	PyListObject *obj_copy = (PyListObject *) p;

	printf("[*] Python list info\n");
	list_items_count = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_items_count);
	printf("[*] Allocated = %d\n", (int) obj_copy->allocated);

	for (; i < list_items_count; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
