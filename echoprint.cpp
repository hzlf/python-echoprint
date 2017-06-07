#include <Common.h>
#include <Codegen.h>
#include <Python.h>
#include <stdio.h>

static PyObject * echoprint_codegen(PyObject *self, PyObject *args) {
    PyObject *py_samples;
    int start_offset = 0;
    PyObject *item;
    float *samples;
    uint num_samples;
    uint i;
    Codegen *pCodegen;
    PyObject *result;

    if (!PyArg_ParseTuple(args, "O|i", &py_samples, &start_offset)) {
        return NULL;
    }
    if (!PySequence_Check(py_samples)) {
        PyErr_SetString(PyExc_TypeError, "expected sequence");
        return NULL;
    }
    num_samples = PySequence_Size(py_samples);
    samples = new float[num_samples];

    for (i = 0; i < num_samples; i++) {
        item = PySequence_GetItem(py_samples, i);
        if (!PyFloat_Check(item)) {
            delete[] samples;
            PyErr_SetString(PyExc_TypeError, "expected sequence of floats");
            return NULL;
        }
        samples[i] = (float)PyFloat_AsDouble(item);
        Py_DECREF(item);
    }
    pCodegen = new Codegen(samples, num_samples, start_offset);
    result = Py_BuildValue("{s:s,s:f}",
        "code", pCodegen->getCodeString().c_str(),
        "version", pCodegen->getVersion()
    );
    delete pCodegen;
    delete[] samples;
    return result;
}




static PyMethodDef echoprint_methods[] = {
    {"codegen", echoprint_codegen, METH_VARARGS,
     "Generates a echoprint code for a list of floating point PCM data sampled at 11025 Hz and mono."},
    {NULL, NULL, 0, NULL}
};


// python 2.7 version
#if PY_MAJOR_VERSION == 2
PyMODINIT_FUNC
initechoprint(void)
{
    (void) Py_InitModule("echoprint", echoprint_methods);
}
#endif


// python 3.x version
// https://stackoverflow.com/questions/28305731/compiler-cant-find-py-initmodule-is-it-deprecated-and-if-so-what-should-i
// https://docs.python.org/3/howto/cporting.html#cporting-howto
#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef echoprint =
{
    PyModuleDef_HEAD_INIT,
    "echoprint",
    "",
    -1,
    echoprint_methods
};

PyMODINIT_FUNC PyInit_echoprint(void)
{
    return PyModule_Create(&echoprint);
}
#endif
