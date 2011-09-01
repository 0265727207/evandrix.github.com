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

#line 34 "sip/qscilexermatlab.sip"
#include <Qsci/qscilexermatlab.h>
#line 39 "./sipQsciQsciLexerMatlab.cpp"

#line 39 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qobject.sip"
#include <qobject.h>
#line 43 "./sipQsciQsciLexerMatlab.cpp"
#line 41 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qstring.sip"
#include <qstring.h>
#line 46 "./sipQsciQsciLexerMatlab.cpp"
#line 40 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtGui/qfont.sip"
#include <qfont.h>
#line 49 "./sipQsciQsciLexerMatlab.cpp"
#line 40 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtGui/qcolor.sip"
#include <qcolor.h>
#line 52 "./sipQsciQsciLexerMatlab.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qsettings.sip"
#include <qsettings.h>
#line 55 "./sipQsciQsciLexerMatlab.cpp"
#line 34 "sip/qsciabstractapis.sip"
#include <Qsci/qsciabstractapis.h>
#line 58 "./sipQsciQsciLexerMatlab.cpp"
#line 34 "sip/qsciscintilla.sip"
#include <Qsci/qsciscintilla.h>
#line 61 "./sipQsciQsciLexerMatlab.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 64 "./sipQsciQsciLexerMatlab.cpp"
#line 315 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 67 "./sipQsciQsciLexerMatlab.cpp"
#line 303 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 70 "./sipQsciQsciLexerMatlab.cpp"
#line 243 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qvariant.sip"
#include <qvariant.h>
#line 73 "./sipQsciQsciLexerMatlab.cpp"
#line 38 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 76 "./sipQsciQsciLexerMatlab.cpp"
#line 42 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qbytearray.sip"
#include <qbytearray.h>
#line 79 "./sipQsciQsciLexerMatlab.cpp"
#line 40 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 82 "./sipQsciQsciLexerMatlab.cpp"
#line 125 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qlist.sip"
#include <qlist.h>
#line 85 "./sipQsciQsciLexerMatlab.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qthread.sip"
#include <qthread.h>
#line 88 "./sipQsciQsciLexerMatlab.cpp"
#line 40 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qregexp.sip"
#include <qregexp.h>
#line 91 "./sipQsciQsciLexerMatlab.cpp"
#line 36 "/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/QtCore/qobjectdefs.sip"
#include <qobjectdefs.h>
#line 94 "./sipQsciQsciLexerMatlab.cpp"


class sipQsciLexerMatlab : public QsciLexerMatlab
{
public:
    sipQsciLexerMatlab(QObject *);
    virtual ~sipQsciLexerMatlab();

    int qt_metacall(QMetaObject::Call,int,void **);
    void *qt_metacast(const char *);
    const QMetaObject *metaObject() const;

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    const char * language() const;
    const char * lexer() const;
    int lexerId() const;
    QColor color(int) const;
    bool eolFill(int) const;
    QFont font(int) const;
    const char * keywords(int) const;
    QString description(int) const;
    QColor paper(int) const;
    QColor defaultColor(int) const;
    bool defaultEolFill(int) const;
    QFont defaultFont(int) const;
    QColor defaultPaper(int) const;
    void refreshProperties();
    int styleBitsNeeded() const;
    void setAutoIndentStyle(int);
    void setColor(const QColor&,int);
    void setEolFill(bool,int);
    void setFont(const QFont&,int);
    void setPaper(const QColor&,int);
    bool readProperties(QSettings&,const QString&);
    bool writeProperties(QSettings&,const QString&) const;
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
    sipQsciLexerMatlab(const sipQsciLexerMatlab &);
    sipQsciLexerMatlab &operator = (const sipQsciLexerMatlab &);

    char sipPyMethods[29];
};

sipQsciLexerMatlab::sipQsciLexerMatlab(QObject *a0): QsciLexerMatlab(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQsciLexerMatlab::~sipQsciLexerMatlab()
{
    sipCommonDtor(sipPySelf);
}

const QMetaObject *sipQsciLexerMatlab::metaObject() const
{
    return sip_Qsci_qt_metaobject(sipPySelf,sipType_QsciLexerMatlab);
}

int sipQsciLexerMatlab::qt_metacall(QMetaObject::Call _c,int _id,void **_a)
{
    _id = QsciLexerMatlab::qt_metacall(_c,_id,_a);

    if (_id >= 0)
        _id = sip_Qsci_qt_metacall(sipPySelf,sipType_QsciLexerMatlab,_c,_id,_a);

    return _id;
}

void *sipQsciLexerMatlab::qt_metacast(const char *_clname)
{
    return (sip_Qsci_qt_metacast && sip_Qsci_qt_metacast(sipPySelf,sipType_QsciLexerMatlab,_clname)) ? this : QsciLexerMatlab::qt_metacast(_clname);
}

const char * sipQsciLexerMatlab::language() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[0]),sipPySelf,NULL,sipName_language);

    if (!sipMeth)
        return QsciLexerMatlab::language();

    extern const char * sipVH_Qsci_13(sip_gilstate_t,PyObject *,int,sipSimpleWrapper *);

    return sipVH_Qsci_13(sipGILState,sipMeth,-50,sipPySelf);
}

const char * sipQsciLexerMatlab::lexer() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[1]),sipPySelf,NULL,sipName_lexer);

    if (!sipMeth)
        return QsciLexerMatlab::lexer();

    extern const char * sipVH_Qsci_13(sip_gilstate_t,PyObject *,int,sipSimpleWrapper *);

    return sipVH_Qsci_13(sipGILState,sipMeth,-51,sipPySelf);
}

int sipQsciLexerMatlab::lexerId() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[2]),sipPySelf,NULL,sipName_lexerId);

    if (!sipMeth)
        return QsciLexer::lexerId();

    typedef int (*sipVH_QtCore_6)(sip_gilstate_t,PyObject *);

    return ((sipVH_QtCore_6)(sipModuleAPI_Qsci_QtCore->em_virthandlers[6]))(sipGILState,sipMeth);
}

QColor sipQsciLexerMatlab::color(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[3]),sipPySelf,NULL,sipName_color);

    if (!sipMeth)
        return QsciLexer::color(a0);

    extern QColor sipVH_Qsci_11(sip_gilstate_t,PyObject *,int);

    return sipVH_Qsci_11(sipGILState,sipMeth,a0);
}

bool sipQsciLexerMatlab::eolFill(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[4]),sipPySelf,NULL,sipName_eolFill);

    if (!sipMeth)
        return QsciLexer::eolFill(a0);

    typedef bool (*sipVH_QtCore_23)(sip_gilstate_t,PyObject *,int);

    return ((sipVH_QtCore_23)(sipModuleAPI_Qsci_QtCore->em_virthandlers[23]))(sipGILState,sipMeth,a0);
}

QFont sipQsciLexerMatlab::font(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[5]),sipPySelf,NULL,sipName_font);

    if (!sipMeth)
        return QsciLexer::font(a0);

    extern QFont sipVH_Qsci_12(sip_gilstate_t,PyObject *,int);

    return sipVH_Qsci_12(sipGILState,sipMeth,a0);
}

const char * sipQsciLexerMatlab::keywords(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[6]),sipPySelf,NULL,sipName_keywords);

    if (!sipMeth)
        return QsciLexerMatlab::keywords(a0);

    typedef const char * (*sipVH_QtGui_146)(sip_gilstate_t,PyObject *,int,int,sipSimpleWrapper *);

    return ((sipVH_QtGui_146)(sipModuleAPI_Qsci_QtGui->em_virthandlers[146]))(sipGILState,sipMeth,a0,-52,sipPySelf);
}

QString sipQsciLexerMatlab::description(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[7]),sipPySelf,NULL,sipName_description);

    if (!sipMeth)
        return QsciLexerMatlab::description(a0);

    typedef QString (*sipVH_QtGui_111)(sip_gilstate_t,PyObject *,int);

    return ((sipVH_QtGui_111)(sipModuleAPI_Qsci_QtGui->em_virthandlers[111]))(sipGILState,sipMeth,a0);
}

QColor sipQsciLexerMatlab::paper(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[8]),sipPySelf,NULL,sipName_paper);

    if (!sipMeth)
        return QsciLexer::paper(a0);

    extern QColor sipVH_Qsci_11(sip_gilstate_t,PyObject *,int);

    return sipVH_Qsci_11(sipGILState,sipMeth,a0);
}

QColor sipQsciLexerMatlab::defaultColor(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[9]),sipPySelf,NULL,sipName_defaultColor);

    if (!sipMeth)
        return QsciLexerMatlab::defaultColor(a0);

    extern QColor sipVH_Qsci_11(sip_gilstate_t,PyObject *,int);

    return sipVH_Qsci_11(sipGILState,sipMeth,a0);
}

bool sipQsciLexerMatlab::defaultEolFill(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[10]),sipPySelf,NULL,sipName_defaultEolFill);

    if (!sipMeth)
        return QsciLexer::defaultEolFill(a0);

    typedef bool (*sipVH_QtCore_23)(sip_gilstate_t,PyObject *,int);

    return ((sipVH_QtCore_23)(sipModuleAPI_Qsci_QtCore->em_virthandlers[23]))(sipGILState,sipMeth,a0);
}

QFont sipQsciLexerMatlab::defaultFont(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[11]),sipPySelf,NULL,sipName_defaultFont);

    if (!sipMeth)
        return QsciLexerMatlab::defaultFont(a0);

    extern QFont sipVH_Qsci_12(sip_gilstate_t,PyObject *,int);

    return sipVH_Qsci_12(sipGILState,sipMeth,a0);
}

QColor sipQsciLexerMatlab::defaultPaper(int a0) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[12]),sipPySelf,NULL,sipName_defaultPaper);

    if (!sipMeth)
        return QsciLexer::defaultPaper(a0);

    extern QColor sipVH_Qsci_11(sip_gilstate_t,PyObject *,int);

    return sipVH_Qsci_11(sipGILState,sipMeth,a0);
}

void sipQsciLexerMatlab::refreshProperties()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[13],sipPySelf,NULL,sipName_refreshProperties);

    if (!sipMeth)
    {
        QsciLexer::refreshProperties();
        return;
    }

    typedef void (*sipVH_QtCore_11)(sip_gilstate_t,PyObject *);

    ((sipVH_QtCore_11)(sipModuleAPI_Qsci_QtCore->em_virthandlers[11]))(sipGILState,sipMeth);
}

int sipQsciLexerMatlab::styleBitsNeeded() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[14]),sipPySelf,NULL,sipName_styleBitsNeeded);

    if (!sipMeth)
        return QsciLexer::styleBitsNeeded();

    typedef int (*sipVH_QtCore_6)(sip_gilstate_t,PyObject *);

    return ((sipVH_QtCore_6)(sipModuleAPI_Qsci_QtCore->em_virthandlers[6]))(sipGILState,sipMeth);
}

void sipQsciLexerMatlab::setAutoIndentStyle(int a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[15],sipPySelf,NULL,sipName_setAutoIndentStyle);

    if (!sipMeth)
    {
        QsciLexer::setAutoIndentStyle(a0);
        return;
    }

    typedef void (*sipVH_QtCore_4)(sip_gilstate_t,PyObject *,int);

    ((sipVH_QtCore_4)(sipModuleAPI_Qsci_QtCore->em_virthandlers[4]))(sipGILState,sipMeth,a0);
}

void sipQsciLexerMatlab::setColor(const QColor& a0,int a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[16],sipPySelf,NULL,sipName_setColor);

    if (!sipMeth)
    {
        QsciLexer::setColor(a0,a1);
        return;
    }

    extern void sipVH_Qsci_8(sip_gilstate_t,PyObject *,const QColor&,int);

    sipVH_Qsci_8(sipGILState,sipMeth,a0,a1);
}

void sipQsciLexerMatlab::setEolFill(bool a0,int a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[17],sipPySelf,NULL,sipName_setEolFill);

    if (!sipMeth)
    {
        QsciLexer::setEolFill(a0,a1);
        return;
    }

    extern void sipVH_Qsci_10(sip_gilstate_t,PyObject *,bool,int);

    sipVH_Qsci_10(sipGILState,sipMeth,a0,a1);
}

void sipQsciLexerMatlab::setFont(const QFont& a0,int a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[18],sipPySelf,NULL,sipName_setFont);

    if (!sipMeth)
    {
        QsciLexer::setFont(a0,a1);
        return;
    }

    extern void sipVH_Qsci_9(sip_gilstate_t,PyObject *,const QFont&,int);

    sipVH_Qsci_9(sipGILState,sipMeth,a0,a1);
}

void sipQsciLexerMatlab::setPaper(const QColor& a0,int a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[19],sipPySelf,NULL,sipName_setPaper);

    if (!sipMeth)
    {
        QsciLexer::setPaper(a0,a1);
        return;
    }

    extern void sipVH_Qsci_8(sip_gilstate_t,PyObject *,const QColor&,int);

    sipVH_Qsci_8(sipGILState,sipMeth,a0,a1);
}

bool sipQsciLexerMatlab::readProperties(QSettings& a0,const QString& a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[20],sipPySelf,NULL,sipName_readProperties);

    if (!sipMeth)
        return QsciLexer::readProperties(a0,a1);

    extern bool sipVH_Qsci_7(sip_gilstate_t,PyObject *,QSettings&,const QString&);

    return sipVH_Qsci_7(sipGILState,sipMeth,a0,a1);
}

bool sipQsciLexerMatlab::writeProperties(QSettings& a0,const QString& a1) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,const_cast<char *>(&sipPyMethods[21]),sipPySelf,NULL,sipName_writeProperties);

    if (!sipMeth)
        return QsciLexer::writeProperties(a0,a1);

    extern bool sipVH_Qsci_7(sip_gilstate_t,PyObject *,QSettings&,const QString&);

    return sipVH_Qsci_7(sipGILState,sipMeth,a0,a1);
}

bool sipQsciLexerMatlab::event(QEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[22],sipPySelf,NULL,sipName_event);

    if (!sipMeth)
        return QObject::event(a0);

    typedef bool (*sipVH_QtCore_5)(sip_gilstate_t,PyObject *,QEvent *);

    return ((sipVH_QtCore_5)(sipModuleAPI_Qsci_QtCore->em_virthandlers[5]))(sipGILState,sipMeth,a0);
}

bool sipQsciLexerMatlab::eventFilter(QObject *a0,QEvent *a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[23],sipPySelf,NULL,sipName_eventFilter);

    if (!sipMeth)
        return QObject::eventFilter(a0,a1);

    typedef bool (*sipVH_QtCore_18)(sip_gilstate_t,PyObject *,QObject *,QEvent *);

    return ((sipVH_QtCore_18)(sipModuleAPI_Qsci_QtCore->em_virthandlers[18]))(sipGILState,sipMeth,a0,a1);
}

void sipQsciLexerMatlab::timerEvent(QTimerEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[24],sipPySelf,NULL,sipName_timerEvent);

    if (!sipMeth)
    {
        QObject::timerEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_9)(sip_gilstate_t,PyObject *,QTimerEvent *);

    ((sipVH_QtCore_9)(sipModuleAPI_Qsci_QtCore->em_virthandlers[9]))(sipGILState,sipMeth,a0);
}

void sipQsciLexerMatlab::childEvent(QChildEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[25],sipPySelf,NULL,sipName_childEvent);

    if (!sipMeth)
    {
        QObject::childEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_25)(sip_gilstate_t,PyObject *,QChildEvent *);

    ((sipVH_QtCore_25)(sipModuleAPI_Qsci_QtCore->em_virthandlers[25]))(sipGILState,sipMeth,a0);
}

void sipQsciLexerMatlab::customEvent(QEvent *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[26],sipPySelf,NULL,sipName_customEvent);

    if (!sipMeth)
    {
        QObject::customEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_17)(sip_gilstate_t,PyObject *,QEvent *);

    ((sipVH_QtCore_17)(sipModuleAPI_Qsci_QtCore->em_virthandlers[17]))(sipGILState,sipMeth,a0);
}

void sipQsciLexerMatlab::connectNotify(const char *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[27],sipPySelf,NULL,sipName_connectNotify);

    if (!sipMeth)
    {
        QObject::connectNotify(a0);
        return;
    }

    typedef void (*sipVH_QtCore_24)(sip_gilstate_t,PyObject *,const char *);

    ((sipVH_QtCore_24)(sipModuleAPI_Qsci_QtCore->em_virthandlers[24]))(sipGILState,sipMeth,a0);
}

void sipQsciLexerMatlab::disconnectNotify(const char *a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[28],sipPySelf,NULL,sipName_disconnectNotify);

    if (!sipMeth)
    {
        QObject::disconnectNotify(a0);
        return;
    }

    typedef void (*sipVH_QtCore_24)(sip_gilstate_t,PyObject *,const char *);

    ((sipVH_QtCore_24)(sipModuleAPI_Qsci_QtCore->em_virthandlers[24]))(sipGILState,sipMeth,a0);
}


PyDoc_STRVAR(doc_QsciLexerMatlab_language, "QsciLexerMatlab.language() -> str");

extern "C" {static PyObject *meth_QsciLexerMatlab_language(PyObject *, PyObject *);}
static PyObject *meth_QsciLexerMatlab_language(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        QsciLexerMatlab *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QsciLexerMatlab, &sipCpp))
        {
            const char *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->QsciLexerMatlab::language() : sipCpp->language());
            Py_END_ALLOW_THREADS

            if (sipRes == NULL)
            {
                Py_INCREF(Py_None);
                return Py_None;
            }

            return SIPBytes_FromString(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciLexerMatlab, sipName_language, doc_QsciLexerMatlab_language);

    return NULL;
}


PyDoc_STRVAR(doc_QsciLexerMatlab_lexer, "QsciLexerMatlab.lexer() -> str");

extern "C" {static PyObject *meth_QsciLexerMatlab_lexer(PyObject *, PyObject *);}
static PyObject *meth_QsciLexerMatlab_lexer(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        QsciLexerMatlab *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QsciLexerMatlab, &sipCpp))
        {
            const char *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->QsciLexerMatlab::lexer() : sipCpp->lexer());
            Py_END_ALLOW_THREADS

            if (sipRes == NULL)
            {
                Py_INCREF(Py_None);
                return Py_None;
            }

            return SIPBytes_FromString(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciLexerMatlab, sipName_lexer, doc_QsciLexerMatlab_lexer);

    return NULL;
}


PyDoc_STRVAR(doc_QsciLexerMatlab_defaultColor, "QsciLexerMatlab.defaultColor(int) -> QColor");

extern "C" {static PyObject *meth_QsciLexerMatlab_defaultColor(PyObject *, PyObject *);}
static PyObject *meth_QsciLexerMatlab_defaultColor(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        int a0;
        QsciLexerMatlab *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QsciLexerMatlab, &sipCpp, &a0))
        {
            QColor *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QColor((sipSelfWasArg ? sipCpp->QsciLexerMatlab::defaultColor(a0) : sipCpp->defaultColor(a0)));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QColor,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciLexerMatlab, sipName_defaultColor, doc_QsciLexerMatlab_defaultColor);

    return NULL;
}


PyDoc_STRVAR(doc_QsciLexerMatlab_defaultFont, "QsciLexerMatlab.defaultFont(int) -> QFont");

extern "C" {static PyObject *meth_QsciLexerMatlab_defaultFont(PyObject *, PyObject *);}
static PyObject *meth_QsciLexerMatlab_defaultFont(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        int a0;
        QsciLexerMatlab *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QsciLexerMatlab, &sipCpp, &a0))
        {
            QFont *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QFont((sipSelfWasArg ? sipCpp->QsciLexerMatlab::defaultFont(a0) : sipCpp->defaultFont(a0)));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QFont,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciLexerMatlab, sipName_defaultFont, doc_QsciLexerMatlab_defaultFont);

    return NULL;
}


PyDoc_STRVAR(doc_QsciLexerMatlab_keywords, "QsciLexerMatlab.keywords(int) -> str");

extern "C" {static PyObject *meth_QsciLexerMatlab_keywords(PyObject *, PyObject *);}
static PyObject *meth_QsciLexerMatlab_keywords(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        int a0;
        QsciLexerMatlab *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QsciLexerMatlab, &sipCpp, &a0))
        {
            const char *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->QsciLexerMatlab::keywords(a0) : sipCpp->keywords(a0));
            Py_END_ALLOW_THREADS

            if (sipRes == NULL)
            {
                Py_INCREF(Py_None);
                return Py_None;
            }

            return SIPBytes_FromString(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciLexerMatlab, sipName_keywords, doc_QsciLexerMatlab_keywords);

    return NULL;
}


PyDoc_STRVAR(doc_QsciLexerMatlab_description, "QsciLexerMatlab.description(int) -> QString");

extern "C" {static PyObject *meth_QsciLexerMatlab_description(PyObject *, PyObject *);}
static PyObject *meth_QsciLexerMatlab_description(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        int a0;
        QsciLexerMatlab *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bi", &sipSelf, sipType_QsciLexerMatlab, &sipCpp, &a0))
        {
            QString *sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QString((sipSelfWasArg ? sipCpp->QsciLexerMatlab::description(a0) : sipCpp->description(a0)));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QsciLexerMatlab, sipName_description, doc_QsciLexerMatlab_description);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QsciLexerMatlab(void *, const sipTypeDef *);}
static void *cast_QsciLexerMatlab(void *ptr, const sipTypeDef *targetType)
{
    void *res;

    if (targetType == sipType_QsciLexerMatlab)
        return ptr;

    if ((res = ((const sipClassTypeDef *)sipType_QsciLexer)->ctd_cast((QsciLexer *)(QsciLexerMatlab *)ptr,targetType)) != NULL)
        return res;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QsciLexerMatlab(void *, int);}
static void release_QsciLexerMatlab(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    QsciLexerMatlab *sipCpp = reinterpret_cast<QsciLexerMatlab *>(sipCppV);

    if (QThread::currentThread() == sipCpp->thread())
        delete sipCpp;
    else
        sipCpp->deleteLater();

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QsciLexerMatlab(sipSimpleWrapper *);}
static void dealloc_QsciLexerMatlab(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerived(sipSelf))
        reinterpret_cast<sipQsciLexerMatlab *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsPyOwned(sipSelf))
    {
        release_QsciLexerMatlab(sipGetAddress(sipSelf),sipSelf->flags);
    }
}


extern "C" {static void *init_QsciLexerMatlab(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_QsciLexerMatlab(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **sipOwner, PyObject **sipParseErr)
{
    sipQsciLexerMatlab *sipCpp = 0;

    {
        QObject * a0 = 0;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|JH", sipType_QObject, &a0, sipOwner))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQsciLexerMatlab(a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QsciLexerMatlab[] = {{7, 255, 1}};


static PyMethodDef methods_QsciLexerMatlab[] = {
    {SIP_MLNAME_CAST(sipName_defaultColor), meth_QsciLexerMatlab_defaultColor, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciLexerMatlab_defaultColor)},
    {SIP_MLNAME_CAST(sipName_defaultFont), meth_QsciLexerMatlab_defaultFont, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciLexerMatlab_defaultFont)},
    {SIP_MLNAME_CAST(sipName_description), meth_QsciLexerMatlab_description, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciLexerMatlab_description)},
    {SIP_MLNAME_CAST(sipName_keywords), meth_QsciLexerMatlab_keywords, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciLexerMatlab_keywords)},
    {SIP_MLNAME_CAST(sipName_language), meth_QsciLexerMatlab_language, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciLexerMatlab_language)},
    {SIP_MLNAME_CAST(sipName_lexer), meth_QsciLexerMatlab_lexer, METH_VARARGS, SIP_MLDOC_CAST(doc_QsciLexerMatlab_lexer)}
};

static sipEnumMemberDef enummembers_QsciLexerMatlab[] = {
    {sipName_Command, QsciLexerMatlab::Command, -1},
    {sipName_Comment, QsciLexerMatlab::Comment, -1},
    {sipName_Default, QsciLexerMatlab::Default, -1},
    {sipName_DoubleQuotedString, QsciLexerMatlab::DoubleQuotedString, -1},
    {sipName_Identifier, QsciLexerMatlab::Identifier, -1},
    {sipName_Keyword, QsciLexerMatlab::Keyword, -1},
    {sipName_Number, QsciLexerMatlab::Number, -1},
    {sipName_Operator, QsciLexerMatlab::Operator, -1},
    {sipName_SingleQuotedString, QsciLexerMatlab::SingleQuotedString, -1},
};

PyDoc_STRVAR(doc_QsciLexerMatlab, "\1QsciLexerMatlab(QObject parent=None)");


pyqt4ClassTypeDef sipTypeDef_Qsci_QsciLexerMatlab = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QsciLexerMatlab,
        {0}
    },
    {
        sipNameNr_QsciLexerMatlab,
        {0, 0, 1},
        6, methods_QsciLexerMatlab,
        9, enummembers_QsciLexerMatlab,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QsciLexerMatlab,
    -1,
    -1,
    supers_QsciLexerMatlab,
    0,
    init_QsciLexerMatlab,
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
    dealloc_QsciLexerMatlab,
    0,
    0,
    0,
    release_QsciLexerMatlab,
    cast_QsciLexerMatlab,
    0,
    0,
    0
},
    &QsciLexerMatlab::staticMetaObject,
    0,
    0
};
