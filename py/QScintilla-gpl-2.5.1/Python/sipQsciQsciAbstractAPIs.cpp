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

#line 34 "sip/qsciabstractapis.sip"
#include <Qsci/qsciabstractapis.h>
#line 39 "./sipQsciQsciAbstractAPIs.cpp"

#line 34 "sip/qscilexer.sip"
#include <Qsci/qscilexer.h>
#line 43 "./sipQsciQsciAbstractAPIs.cpp"
#line 41 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qstringlist.sip"
#include <qstringlist.h>
#line 46 "./sipQsciQsciAbstractAPIs.cpp"
#line 34 "sip/qsciscintilla.sip"
#include <Qsci/qsciscintilla.h>
#line 49 "./sipQsciQsciAbstractAPIs.cpp"
#line 633 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 52 "./sipQsciQsciAbstractAPIs.cpp"
#line 41 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qstring.sip"
#include <qstring.h>
#line 55 "./sipQsciQsciAbstractAPIs.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 58 "./sipQsciQsciAbstractAPIs.cpp"
#line 315 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 61 "./sipQsciQsciAbstractAPIs.cpp"
#line 303 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 64 "./sipQsciQsciAbstractAPIs.cpp"
#line 39 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qobject.sip"
#include <qobject.h>
#line 67 "./sipQsciQsciAbstractAPIs.cpp"
#line 243 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qvariant.sip"
#include <qvariant.h>
#line 70 "./sipQsciQsciAbstractAPIs.cpp"
#line 38 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 73 "./sipQsciQsciAbstractAPIs.cpp"
#line 42 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qbytearray.sip"
#include <qbytearray.h>
#line 76 "./sipQsciQsciAbstractAPIs.cpp"
#line 40 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 79 "./sipQsciQsciAbstractAPIs.cpp"
#line 125 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 82 "./sipQsciQsciAbstractAPIs.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qthread.sip"
#include <qthread.h>
#line 85 "./sipQsciQsciAbstractAPIs.cpp"
#line 40 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qregexp.sip"
#include <qregexp.h>
#line 88 "./sipQsciQsciAbstractAPIs.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qobjectdefs.sip"
#include <qobjectdefs.h>
#line 91 "./sipQsciQsciAbstractAPIs.cpp"


class sipQsciAbstractAPIs : public QsciAbstractAPIs
{
public:
    sipQsciAbstractAPIs(QsciLexer *);
    virtual ~sipQsciAbstractAPIs();

    int qt_metacall(QMetaObject::Call,int,void **);
    void *qt_metacast(const char *);
    const QMetaObject *metaObject() const;

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    void updateAutoCompletionList(const QStringList&,QStringList&);
    void autoCompletionSelected(const QString&);
    QStringList callTips(const QStringList&,int,QsciScintilla::CallTipsStyle,QList<int>&);
    bool event(QEvent *);
    bool eventFilter(QObject *,QEvent *);
    void timerEvent(QTimerEvent *);
    void childEvent(QChildEvent *);
    void customEvent(QEvent *);
    void connectNotify(const char *);
    void disconnectNotify(const char *);

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQsciAbstractAPIs(const sipQsciAbstractAPIs &);
    sipQsciAbstractAPIs &operator = (const sipQsciAbstractAPIs &);

    char sipPyMethods[10];
};

sipQsciAbstractAPIs::sipQsciAbstractAPIs(QsciLexer *a0): QsciAbstractAPIs(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQsciAbstractAPIs::~sipQsciAbstractAPIs()
{
    sipCommonDtor(sipPySelf);
}

const QMetaObject *sipQsciAbstractAPIs::metaObject() const
{
    return sip_Qsci_qt_metaobject(sipPySelf,sipType_QsciAbstractAPIs);
}

int sipQsciAbstractAPIs::qt_metacall(QMetaObject::Call _c,int _id,void **_a)
{
    _id = QsciAbstractAPIs::qt_metacall(_c,_id,_a);

    if (_id >= 0)
        _id = sip_Qsci_qt_metacall(sipPySelf,sipType_QsciAbstractAPIs,_c,_id,_a);

    return _id;
}

void *sipQsciAbstractAPIs::qt_metacast(const char *_clname)
{
    return (sip_Qsci_qt_metacast && sip_Qsci_qt_metacast(sipPySelf,sipType_QsciAbstractAPIs,_clname)) ? this : QsciAbstractAPIs::qt_metacast(_clname);
}

void sipQsciAbstractAPIs::updateAutoCompletionList(const QStringList& a0,QStringList& a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[0],sipPySelf,sipName_QsciAbstractAPIs,sipName_updateAutoCompletionList);

    if (!sipMeth)
        return;

    extern void sipVH_Qsci_15(sip_gilstate_t,PyObject *,const QStringList&,QStringList&);

    sipVH_Qsci_15(sipGILState,sipMeth,a0,a1);
}

void sipQsciAbstractAPIs::autoCompletionSelected(const QString& a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[1],sipPySelf,NULL,sipName_autoCompletionSelected);

    if (!sipMeth)
    {
        QsciAbstractAPIs::autoCompletionSelected(a0);
        return;
    }

    typedef void (*sipVH_QtCore_33)(sip_gilstate_t,PyObject *,const QString&);

    ((sipVH_QtCore_33)(sipModuleAPI_Qsci_QtCore->em_virthandlers[33]))(sipGILState,sipMeth,a0);
}

QStringList sipQsciAbstractAPIs::callTips(const QStringList& a0,int a1,QsciScintilla::CallTipsStyle a2,QList<int>& a3)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[2],sipPySelf,sipName_QsciAbstractAPIs,sipName_callTips);

    if (!sipMeth)
        return QStringList();

    extern QStringList sipVH_Qsci_14(sip_gilstate_t,PyObject *,const QStringList&,int,QsciScintilla::CallTipsStyle,QList<int>&);

    return sipVH_Qsci_14(sipGILState,sipMeth,a0,a1,a2,a3);
}

bool sipQsciAbstractAPIs::event(QEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[3],sipPySelf,NULL,sipName_event);

    if (!sipMeth)
        return QObject::event(a0);

    typedef bool (*sipVH_QtCore_5)(sip_gilstate_t,PyObject *,QEvent *);

    return ((sipVH_QtCore_5)(sipModuleAPI_Qsci_QtCore->em_virthandlers[5]))(sipGILState,sipMeth,a0);
}

bool sipQsciAbstractAPIs::eventFilter(QObject *a0,QEvent *a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[4],sipPySelf,NULL,sipName_eventFilter);

    if (!sipMeth)
        return QObject::eventFilter(a0,a1);

    typedef bool (*sipVH_QtCore_18)(sip_gilstate_t,PyObject *,QObject *,QEvent *);

    return ((sipVH_QtCore_18)(sipModuleAPI_Qsci_QtCore->em_virthandlers[18]))(sipGILState,sipMeth,a0,a1);
}

void sipQsciAbstractAPIs::timerEvent(QTimerEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[5],sipPySelf,NULL,sipName_timerEvent);

    if (!sipMeth)
    {
        QObject::timerEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_9)(sip_gilstate_t,PyObject *,QTimerEvent *);

    ((sipVH_QtCore_9)(sipModuleAPI_Qsci_QtCore->em_virthandlers[9]))(sipGILState,sipMeth,a0);
}

void sipQsciAbstractAPIs::childEvent(QChildEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[6],sipPySelf,NULL,sipName_childEvent);

    if (!sipMeth)
    {
        QObject::childEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_25)(sip_gilstate_t,PyObject *,QChildEvent *);

    ((sipVH_QtCore_25)(sipModuleAPI_Qsci_QtCore->em_virthandlers[25]))(sipGILState,sipMeth,a0);
}

void sipQsciAbstractAPIs::customEvent(QEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[7],sipPySelf,NULL,sipName_customEvent);

    if (!sipMeth)
    {
        QObject::customEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_17)(sip_gilstate_t,PyObject *,QEvent *);

    ((sipVH_QtCore_17)(sipModuleAPI_Qsci_QtCore->em_virthandlers[17]))(sipGILState,sipMeth,a0);
}

void sipQsciAbstractAPIs::connectNotify(const char *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[8],sipPySelf,NULL,sipName_connectNotify);

    if (!sipMeth)
    {
        QObject::connectNotify(a0);
        return;
    }

    typedef void (*sipVH_QtCore_24)(sip_gilstate_t,PyObject *,const char *);

    ((sipVH_QtCore_24)(sipModuleAPI_Qsci_QtCore->em_virthandlers[24]))(sipGILState,sipMeth,a0);
}

void sipQsciAbstractAPIs::disconnectNotify(const char *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[9],sipPySelf,NULL,sipName_disconnectNotify);

    if (!sipMeth)
    {
        QObject::disconnectNotify(a0);
        return;
    }

    typedef void (*sipVH_QtCore_24)(sip_gilstate_t,PyObject *,const char *);

    ((sipVH_QtCore_24)(sipModuleAPI_Qsci_QtCore->em_virthandlers[24]))(sipGILState,sipMeth,a0);
}


PyDoc_STRVAR(doc_QsciAbstractAPIs_lexer, "QsciAbstractAPIs.lexer() -> QsciLexer");

extern "C" {static PyObject *meth_QsciAbstractAPIs_lexer(PyObject *, PyObject *);}
static PyObject *meth_QsciAbstractAPIs_lexer(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        QsciAbstractAPIs *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QsciAbstractAPIs, &sipCpp))
        {
            QsciLexer *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->lexer();
            Py_END_ALLOW_THREADS

            return sipConvertFromType(sipRes,sipType_QsciLexer,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciAbstractAPIs, sipName_lexer, doc_QsciAbstractAPIs_lexer);

    return NULL;
}


PyDoc_STRVAR(doc_QsciAbstractAPIs_updateAutoCompletionList, "QsciAbstractAPIs.updateAutoCompletionList(QStringList, QStringList)");

extern "C" {static PyObject *meth_QsciAbstractAPIs_updateAutoCompletionList(PyObject *, PyObject *);}
static PyObject *meth_QsciAbstractAPIs_updateAutoCompletionList(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    PyObject *sipOrigSelf = sipSelf;

    {
        const QStringList * a0;
        int a0State = 0;
        QStringList * a1;
        int a1State = 0;
        QsciAbstractAPIs *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1J1", &sipSelf, sipType_QsciAbstractAPIs, &sipCpp, sipType_QStringList,&a0, &a0State, sipType_QStringList,&a1, &a1State))
        {
            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_QsciAbstractAPIs, sipName_updateAutoCompletionList);
                return NULL;
            }

            Py_BEGIN_ALLOW_THREADS
            sipCpp->updateAutoCompletionList(*a0,*a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QStringList *>(a0),sipType_QStringList,a0State);
            sipReleaseType(a1,sipType_QStringList,a1State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciAbstractAPIs, sipName_updateAutoCompletionList, doc_QsciAbstractAPIs_updateAutoCompletionList);

    return NULL;
}


PyDoc_STRVAR(doc_QsciAbstractAPIs_autoCompletionSelected, "QsciAbstractAPIs.autoCompletionSelected(QString)");

extern "C" {static PyObject *meth_QsciAbstractAPIs_autoCompletionSelected(PyObject *, PyObject *);}
static PyObject *meth_QsciAbstractAPIs_autoCompletionSelected(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        const QString * a0;
        int a0State = 0;
        QsciAbstractAPIs *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1", &sipSelf, sipType_QsciAbstractAPIs, &sipCpp, sipType_QString,&a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->QsciAbstractAPIs::autoCompletionSelected(*a0) : sipCpp->autoCompletionSelected(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciAbstractAPIs, sipName_autoCompletionSelected, doc_QsciAbstractAPIs_autoCompletionSelected);

    return NULL;
}


PyDoc_STRVAR(doc_QsciAbstractAPIs_callTips, "QsciAbstractAPIs.callTips(QStringList, int, QsciScintilla.CallTipsStyle, list-of-int) -> QStringList");

extern "C" {static PyObject *meth_QsciAbstractAPIs_callTips(PyObject *, PyObject *);}
static PyObject *meth_QsciAbstractAPIs_callTips(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    PyObject *sipOrigSelf = sipSelf;

    {
        const QStringList * a0;
        int a0State = 0;
        int a1;
        QsciScintilla::CallTipsStyle a2;
        QList<int> * a3;
        int a3State = 0;
        QsciAbstractAPIs *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ1iEJ1", &sipSelf, sipType_QsciAbstractAPIs, &sipCpp, sipType_QStringList,&a0, &a0State, &a1, sipType_QsciScintilla_CallTipsStyle, &a2, sipType_QList_1800,&a3, &a3State))
        {
            QStringList *sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_QsciAbstractAPIs, sipName_callTips);
                return NULL;
            }

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QStringList(sipCpp->callTips(*a0,a1,a2,*a3));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QStringList *>(a0),sipType_QStringList,a0State);
            sipReleaseType(a3,sipType_QList_1800,a3State);

            return sipConvertFromNewType(sipRes,sipType_QStringList,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciAbstractAPIs, sipName_callTips, doc_QsciAbstractAPIs_callTips);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QsciAbstractAPIs(void *, const sipTypeDef *);}
static void *cast_QsciAbstractAPIs(void *ptr, const sipTypeDef *targetType)
{
    void *res;

    if (targetType == sipType_QsciAbstractAPIs)
        return ptr;

    if ((res = ((const sipClassTypeDef *)sipType_QObject)->ctd_cast((QObject *)(QsciAbstractAPIs *)ptr,targetType)) != NULL)
        return res;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QsciAbstractAPIs(void *, int);}
static void release_QsciAbstractAPIs(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    QsciAbstractAPIs *sipCpp = reinterpret_cast<QsciAbstractAPIs *>(sipCppV);

    if (QThread::currentThread() == sipCpp->thread())
        delete sipCpp;
    else
        sipCpp->deleteLater();

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QsciAbstractAPIs(sipSimpleWrapper *);}
static void dealloc_QsciAbstractAPIs(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerived(sipSelf))
        reinterpret_cast<sipQsciAbstractAPIs *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsPyOwned(sipSelf))
    {
        release_QsciAbstractAPIs(sipGetAddress(sipSelf),sipSelf->flags);
    }
}


extern "C" {static void *init_QsciAbstractAPIs(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_QsciAbstractAPIs(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **sipOwner, PyObject **sipParseErr)
{
    sipQsciAbstractAPIs *sipCpp = 0;

    {
        QsciLexer * a0 = 0;

        static const char *sipKwdList[] = {
            sipName_lexer,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|JH", sipType_QsciLexer, &a0, sipOwner))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQsciAbstractAPIs(a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QsciAbstractAPIs[] = {{134, 0, 1}};


static PyMethodDef methods_QsciAbstractAPIs[] = {
    {SIP_MLNAME_CAST(sipName_autoCompletionSelected), meth_QsciAbstractAPIs_autoCompletionSelected, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciAbstractAPIs_autoCompletionSelected)},
    {SIP_MLNAME_CAST(sipName_callTips), meth_QsciAbstractAPIs_callTips, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciAbstractAPIs_callTips)},
    {SIP_MLNAME_CAST(sipName_lexer), meth_QsciAbstractAPIs_lexer, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciAbstractAPIs_lexer)},
    {SIP_MLNAME_CAST(sipName_updateAutoCompletionList), meth_QsciAbstractAPIs_updateAutoCompletionList, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciAbstractAPIs_updateAutoCompletionList)}
};

PyDoc_STRVAR(doc_QsciAbstractAPIs, "\1QsciAbstractAPIs(QsciLexer lexer=None)");


pyqt4ClassTypeDef sipTypeDef_Qsci_QsciAbstractAPIs = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_ABSTRACT|SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QsciAbstractAPIs,
        {0}
    },
    {
        sipNameNr_QsciAbstractAPIs,
        {0, 0, 1},
        4, methods_QsciAbstractAPIs,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QsciAbstractAPIs,
    -1,
    -1,
    supers_QsciAbstractAPIs,
    0,
    init_QsciAbstractAPIs,
    0,
    0,
#if PY_MAJOR_VERSION >= 3
    0,
    0,
#else
    0,
    0,
    0,
    0,
#endif
    dealloc_QsciAbstractAPIs,
    0,
    0,
    0,
    release_QsciAbstractAPIs,
    cast_QsciAbstractAPIs,
    0,
    0,
    0
},
    &QsciAbstractAPIs::staticMetaObject,
    0,
    0
};
