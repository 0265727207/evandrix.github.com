TARGET = Qsci.so
OFILES = sipQscicmodule.o sipQsciQList0101QsciCommand.o sipQsciQList0100QsciStyledText.o sipQsciQsciStyledText.o sipQsciQsciStyle.o sipQsciQsciPrinter.o sipQsciQsciMacro.o sipQsciQsciLexerYAML.o sipQsciQsciLexerXML.o sipQsciQsciLexerVHDL.o sipQsciQsciLexerVerilog.o sipQsciQsciLexerTeX.o sipQsciQsciLexerTCL.o sipQsciQsciLexerSQL.o sipQsciQsciLexerSpice.o sipQsciQsciLexerRuby.o sipQsciQsciLexerPython.o sipQsciQsciLexerProperties.o sipQsciQsciLexerPOV.o sipQsciQsciLexerPostScript.o sipQsciQsciLexerPerl.o sipQsciQsciLexerPascal.o sipQsciQsciLexerOctave.o sipQsciQsciLexerMatlab.o sipQsciQsciLexerMakefile.o sipQsciQsciLexerLua.o sipQsciQsciLexerJavaScript.o sipQsciQsciLexerJava.o sipQsciQsciLexerIDL.o sipQsciQsciLexerHTML.o sipQsciQsciLexerFortran.o sipQsciQsciLexerFortran77.o sipQsciQsciLexerDiff.o sipQsciQsciLexerD.o sipQsciQsciLexerCustom.o sipQsciQsciLexerCSS.o sipQsciQsciLexerCSharp.o sipQsciQsciLexerCPP.o sipQsciQsciLexerCMake.o sipQsciQsciLexerBatch.o sipQsciQsciLexerBash.o sipQsciQsciLexer.o sipQsciQsciDocument.o sipQsciQsciCommandSet.o sipQsciQsciCommand.o sipQsciQsciAPIs.o sipQsciQsciAbstractAPIs.o sipQsciQsciScintilla.o sipQsciQsciScintillaBase.o
HFILES = sipAPIQsci.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_CORE_LIB -DQT_GUI_LIB -I. -I/usr/local/Trolltech/Qt-4.8.0/include -I/opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/usr/local/Trolltech/Qt-4.8.0/mkspecs/default -I/usr/local/Trolltech/Qt-4.8.0/lib/QtCore.framework/Headers -I/usr/local/Trolltech/Qt-4.8.0/lib/QtGui.framework/Headers -F/usr/local/Trolltech/Qt-4.8.0/lib
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS =  -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = -F/usr/local/Trolltech/Qt-4.8.0/lib -L/usr/local/Trolltech/Qt-4.8.0/lib -lqscintilla2 -framework QtCore -L/usr/local/Trolltech/Qt-4.8.0/lib -framework QtGui -L/usr/local/Trolltech/Qt-4.8.0/lib -F/usr/local/Trolltech/Qt-4.8.0/lib -framework QtCore -L/usr/local/Trolltech/Qt-4.8.0/lib
MOC = /usr/local/Trolltech/Qt-4.8.0/bin/moc
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/Library/Python/2.7/site-packages/PyQt4 || mkdir -p $(DESTDIR)/Library/Python/2.7/site-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/Library/Python/2.7/site-packages/PyQt4/$(TARGET)
	install_name_tool -change libqscintilla2.6.dylib /usr/local/Trolltech/Qt-4.8.0/lib/libqscintilla2.6.dylib $(DESTDIR)/Library/Python/2.7/site-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci || mkdir -p $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci
	cp -f sip/qsciabstractapis.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qsciabstractapis.sip
	cp -f sip/qsciapis.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qsciapis.sip
	cp -f sip/qscicommand.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscicommand.sip
	cp -f sip/qscicommandset.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscicommandset.sip
	cp -f sip/qscidocument.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscidocument.sip
	cp -f sip/qscilexer.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexer.sip
	cp -f sip/qscilexerbash.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerbash.sip
	cp -f sip/qscilexerbatch.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerbatch.sip
	cp -f sip/qscilexercmake.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexercmake.sip
	cp -f sip/qscilexercpp.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexercpp.sip
	cp -f sip/qscilexercsharp.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexercsharp.sip
	cp -f sip/qscilexercss.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexercss.sip
	cp -f sip/qscilexercustom.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexercustom.sip
	cp -f sip/qscilexerd.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerd.sip
	cp -f sip/qscilexerdiff.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerdiff.sip
	cp -f sip/qscilexerfortran.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerfortran.sip
	cp -f sip/qscilexerfortran77.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerfortran77.sip
	cp -f sip/qscilexerhtml.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerhtml.sip
	cp -f sip/qscilexeridl.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexeridl.sip
	cp -f sip/qscilexerjava.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerjava.sip
	cp -f sip/qscilexerjavascript.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerjavascript.sip
	cp -f sip/qscilexerlua.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerlua.sip
	cp -f sip/qscilexermakefile.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexermakefile.sip
	cp -f sip/qscilexermatlab.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexermatlab.sip
	cp -f sip/qscilexeroctave.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexeroctave.sip
	cp -f sip/qscilexerpascal.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerpascal.sip
	cp -f sip/qscilexerperl.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerperl.sip
	cp -f sip/qscilexerpostscript.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerpostscript.sip
	cp -f sip/qscilexerpov.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerpov.sip
	cp -f sip/qscilexerproperties.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerproperties.sip
	cp -f sip/qscilexerpython.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerpython.sip
	cp -f sip/qscilexerruby.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerruby.sip
	cp -f sip/qscilexerspice.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerspice.sip
	cp -f sip/qscilexersql.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexersql.sip
	cp -f sip/qscilexertcl.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexertcl.sip
	cp -f sip/qscilexertex.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexertex.sip
	cp -f sip/qscilexerverilog.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerverilog.sip
	cp -f sip/qscilexervhdl.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexervhdl.sip
	cp -f sip/qscilexerxml.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexerxml.sip
	cp -f sip/qscilexeryaml.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscilexeryaml.sip
	cp -f sip/qscimacro.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscimacro.sip
	cp -f sip/qscimod3.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscimod3.sip
	cp -f sip/qscimod4.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscimod4.sip
	cp -f sip/qscimodcommon.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscimodcommon.sip
	cp -f sip/qsciprinter.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qsciprinter.sip
	cp -f sip/qsciscintilla.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qsciscintilla.sip
	cp -f sip/qsciscintillabase3.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qsciscintillabase3.sip
	cp -f sip/qsciscintillabase4.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qsciscintillabase4.sip
	cp -f sip/qscistyle.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscistyle.sip
	cp -f sip/qscistyledtext.sip $(DESTDIR)/System/Library/Frameworks/Python.framework/Versions/2.7/share/sip/PyQt4/Qsci/qscistyledtext.sip
	@test -d $(DESTDIR)/usr/local/Trolltech/Qt-4.8.0/qsci/api/python || mkdir -p $(DESTDIR)/usr/local/Trolltech/Qt-4.8.0/qsci/api/python
	cp -f QScintilla2.api $(DESTDIR)/usr/local/Trolltech/Qt-4.8.0/qsci/api/python/QScintilla2.api

clean:
	-rm -f $(TARGET)
	-rm -f sipQscicmodule.o
	-rm -f sipQsciQList0101QsciCommand.o
	-rm -f sipQsciQList0100QsciStyledText.o
	-rm -f sipQsciQsciStyledText.o
	-rm -f sipQsciQsciStyle.o
	-rm -f sipQsciQsciPrinter.o
	-rm -f sipQsciQsciMacro.o
	-rm -f sipQsciQsciLexerYAML.o
	-rm -f sipQsciQsciLexerXML.o
	-rm -f sipQsciQsciLexerVHDL.o
	-rm -f sipQsciQsciLexerVerilog.o
	-rm -f sipQsciQsciLexerTeX.o
	-rm -f sipQsciQsciLexerTCL.o
	-rm -f sipQsciQsciLexerSQL.o
	-rm -f sipQsciQsciLexerSpice.o
	-rm -f sipQsciQsciLexerRuby.o
	-rm -f sipQsciQsciLexerPython.o
	-rm -f sipQsciQsciLexerProperties.o
	-rm -f sipQsciQsciLexerPOV.o
	-rm -f sipQsciQsciLexerPostScript.o
	-rm -f sipQsciQsciLexerPerl.o
	-rm -f sipQsciQsciLexerPascal.o
	-rm -f sipQsciQsciLexerOctave.o
	-rm -f sipQsciQsciLexerMatlab.o
	-rm -f sipQsciQsciLexerMakefile.o
	-rm -f sipQsciQsciLexerLua.o
	-rm -f sipQsciQsciLexerJavaScript.o
	-rm -f sipQsciQsciLexerJava.o
	-rm -f sipQsciQsciLexerIDL.o
	-rm -f sipQsciQsciLexerHTML.o
	-rm -f sipQsciQsciLexerFortran.o
	-rm -f sipQsciQsciLexerFortran77.o
	-rm -f sipQsciQsciLexerDiff.o
	-rm -f sipQsciQsciLexerD.o
	-rm -f sipQsciQsciLexerCustom.o
	-rm -f sipQsciQsciLexerCSS.o
	-rm -f sipQsciQsciLexerCSharp.o
	-rm -f sipQsciQsciLexerCPP.o
	-rm -f sipQsciQsciLexerCMake.o
	-rm -f sipQsciQsciLexerBatch.o
	-rm -f sipQsciQsciLexerBash.o
	-rm -f sipQsciQsciLexer.o
	-rm -f sipQsciQsciDocument.o
	-rm -f sipQsciQsciCommandSet.o
	-rm -f sipQsciQsciCommand.o
	-rm -f sipQsciQsciAPIs.o
	-rm -f sipQsciQsciAbstractAPIs.o
	-rm -f sipQsciQsciScintilla.o
	-rm -f sipQsciQsciScintillaBase.o
