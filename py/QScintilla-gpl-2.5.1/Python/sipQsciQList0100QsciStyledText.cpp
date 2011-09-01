/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.12.5-snapshot-c2987628087f on Thu Sep  1 02:20:43 2011
 *
 * Copyright (c) 2011 Riverbank Computing Limited <info@riverbankcomputing.com>
 * 
 * This file is part of QScintilla.
 * 
 * This file may be used under the terms of the GNU General Public
 * License versions 2.0 or 3.0 as published by the Free Software
 * Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
 * included in the packaging of this file.  Alternatively you may (at
 * your option) use any later version of the GNU General Public
 * License if such license has been publicly approved by Riverbank
 * Computing Limited (or its successors, if any) and the KDE Free Qt
 * Foundation. In addition, as a special exception, Riverbank gives you
 * certain additional rights. These rights are described in the Riverbank
 * GPL Exception version 1.1, which can be found in the file
 * GPL_EXCEPTION.txt in this package.
 * 
 * Please review the following information to ensure GNU General
 * Public Licensing requirements will be met:
 * http://trolltech.com/products/qt/licenses/licensing/opensource/. If
 * you are unsure which license is appropriate for your use, please
 * review the following information:
 * http://trolltech.com/products/qt/licenses/licensing/licensingoverview
 * or contact the sales department at sales@riverbankcomputing.com.
 * 
 * This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
 * WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 */

#include "sipAPIQsci.h"

#line 38 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 39 "./sipQsciQList0100QsciStyledText.cpp"

#line 34 "sip/qscistyledtext.sip"
#include <Qsci/qscistyledtext.h>
#line 43 "./sipQsciQList0100QsciStyledText.cpp"


extern "C" {static void assign_QList_0100QsciStyledText(void *, SIP_SSIZE_T, const void *);}
static void assign_QList_0100QsciStyledText(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QList<QsciStyledText> *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QList<QsciStyledText> *>(sipSrc);
}


extern "C" {static void *array_QList_0100QsciStyledText(SIP_SSIZE_T);}
static void *array_QList_0100QsciStyledText(SIP_SSIZE_T sipNrElem)
{
    return new QList<QsciStyledText>[sipNrElem];
}


extern "C" {static void *copy_QList_0100QsciStyledText(const void *, SIP_SSIZE_T);}
static void *copy_QList_0100QsciStyledText(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QList<QsciStyledText>(reinterpret_cast<const QList<QsciStyledText> *>(sipSrc)[sipSrcIdx]);
}


/* Call the mapped type's destructor. */
extern "C" {static void release_QList_0100QsciStyledText(void *, int);}
static void release_QList_0100QsciStyledText(void *ptr, int)
{
    Py_BEGIN_ALLOW_THREADS
    delete reinterpret_cast<QList<QsciStyledText> *>(ptr);
    Py_END_ALLOW_THREADS
}



extern "C" {static int convertTo_QList_0100QsciStyledText(PyObject *, void **, int *, PyObject *);}
static int convertTo_QList_0100QsciStyledText(PyObject *sipPy,void **sipCppPtrV,int *sipIsErr,PyObject *sipTransferObj)
{
    QList<QsciStyledText> **sipCppPtr = reinterpret_cast<QList<QsciStyledText> **>(sipCppPtrV);

#line 69 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
    SIP_SSIZE_T len;

    // Check the type if that is all that is required.
    if (sipIsErr == NULL)
    {
        if (!PySequence_Check(sipPy) || (len = PySequence_Size(sipPy)) < 0)
            return 0;

        for (SIP_SSIZE_T i = 0; i < len; ++i)
        {
            PyObject *itm = PySequence_ITEM(sipPy, i);
            bool ok = (itm && sipCanConvertToType(itm, sipType_QsciStyledText, SIP_NOT_NONE));

            Py_XDECREF(itm);

            if (!ok)
                return 0;
        }

        return 1;
    }

    QList<QsciStyledText> *ql = new QList<QsciStyledText>;
    len = PySequence_Size(sipPy);
 
    for (SIP_SSIZE_T i = 0; i < len; ++i)
    {
        PyObject *itm = PySequence_ITEM(sipPy, i);
        int state;
        QsciStyledText *t = reinterpret_cast<QsciStyledText *>(sipConvertToType(itm, sipType_QsciStyledText, sipTransferObj, SIP_NOT_NONE, &state, sipIsErr));

        Py_DECREF(itm);
 
        if (*sipIsErr)
        {
            sipReleaseType(t, sipType_QsciStyledText, state);

            delete ql;
            return 0;
        }

        ql->append(*t);

        sipReleaseType(t, sipType_QsciStyledText, state);
    }
 
    *sipCppPtr = ql;
 
    return sipGetState(sipTransferObj);
#line 133 "./sipQsciQList0100QsciStyledText.cpp"
}


extern "C" {static PyObject *convertFrom_QList_0100QsciStyledText(void *, PyObject *);}
static PyObject *convertFrom_QList_0100QsciStyledText(void *sipCppV,PyObject *sipTransferObj)
{
   QList<QsciStyledText> *sipCpp = reinterpret_cast<QList<QsciStyledText> *>(sipCppV);

#line 42 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
    // Create the list.
    PyObject *l;

    if ((l = PyList_New(sipCpp->size())) == NULL)
        return NULL;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        QsciStyledText *t = new QsciStyledText(sipCpp->at(i));
        PyObject *tobj;

        if ((tobj = sipConvertFromNewType(t, sipType_QsciStyledText, sipTransferObj)) == NULL)
        {
            Py_DECREF(l);
            delete t;

            return NULL;
        }

        PyList_SET_ITEM(l, i, tobj);
    }

    return l;
#line 167 "./sipQsciQList0100QsciStyledText.cpp"
}


sipMappedTypeDef sipTypeDef_Qsci_QList_0100QsciStyledText = {
    {
        -1,
        0,
        0,
        SIP_TYPE_MAPPED,
        sipNameNr_7614,
        {0}
    },
    {
        -1,
        {0, 0, 1},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    },
    assign_QList_0100QsciStyledText,
    array_QList_0100QsciStyledText,
    copy_QList_0100QsciStyledText,
    release_QList_0100QsciStyledText,
    convertTo_QList_0100QsciStyledText,
    convertFrom_QList_0100QsciStyledText
};
