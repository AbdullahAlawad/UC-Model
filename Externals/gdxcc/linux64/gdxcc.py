# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gdxcc', [dirname(__file__)])
        except ImportError:
            import _gdxcc
            return _gdxcc
        if fp is not None:
            try:
                _mod = imp.load_module('_gdxcc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gdxcc = swig_import_helper()
    del swig_import_helper
else:
    import _gdxcc
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gdxcc.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdxcc.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _gdxcc.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _gdxcc.intArray___setitem__(self, *args)
    def cast(self): return _gdxcc.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gdxcc.intArray_frompointer
    if _newclass:frompointer = staticmethod(_gdxcc.intArray_frompointer)
intArray_swigregister = _gdxcc.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _gdxcc.intArray_frompointer(*args)
intArray_frompointer = _gdxcc.intArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gdxcc.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gdxcc.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _gdxcc.doubleArray___getitem__(self, *args)
    def __setitem__(self, *args): return _gdxcc.doubleArray___setitem__(self, *args)
    def cast(self): return _gdxcc.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gdxcc.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_gdxcc.doubleArray_frompointer)
doubleArray_swigregister = _gdxcc.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(*args):
  return _gdxcc.doubleArray_frompointer(*args)
doubleArray_frompointer = _gdxcc.doubleArray_frompointer


def new_intp():
  return _gdxcc.new_intp()
new_intp = _gdxcc.new_intp

def copy_intp(*args):
  return _gdxcc.copy_intp(*args)
copy_intp = _gdxcc.copy_intp

def delete_intp(*args):
  return _gdxcc.delete_intp(*args)
delete_intp = _gdxcc.delete_intp

def intp_assign(*args):
  return _gdxcc.intp_assign(*args)
intp_assign = _gdxcc.intp_assign

def intp_value(*args):
  return _gdxcc.intp_value(*args)
intp_value = _gdxcc.intp_value

def new_doublep():
  return _gdxcc.new_doublep()
new_doublep = _gdxcc.new_doublep

def copy_doublep(*args):
  return _gdxcc.copy_doublep(*args)
copy_doublep = _gdxcc.copy_doublep

def delete_doublep(*args):
  return _gdxcc.delete_doublep(*args)
delete_doublep = _gdxcc.delete_doublep

def doublep_assign(*args):
  return _gdxcc.doublep_assign(*args)
doublep_assign = _gdxcc.doublep_assign

def doublep_value(*args):
  return _gdxcc.doublep_value(*args)
doublep_value = _gdxcc.doublep_value

def new_gdxHandle_tp():
  return _gdxcc.new_gdxHandle_tp()
new_gdxHandle_tp = _gdxcc.new_gdxHandle_tp

def copy_gdxHandle_tp(*args):
  return _gdxcc.copy_gdxHandle_tp(*args)
copy_gdxHandle_tp = _gdxcc.copy_gdxHandle_tp

def delete_gdxHandle_tp(*args):
  return _gdxcc.delete_gdxHandle_tp(*args)
delete_gdxHandle_tp = _gdxcc.delete_gdxHandle_tp

def gdxHandle_tp_assign(*args):
  return _gdxcc.gdxHandle_tp_assign(*args)
gdxHandle_tp_assign = _gdxcc.gdxHandle_tp_assign

def gdxHandle_tp_value(*args):
  return _gdxcc.gdxHandle_tp_value(*args)
gdxHandle_tp_value = _gdxcc.gdxHandle_tp_value

def new_TDataStoreProc_tp():
  return _gdxcc.new_TDataStoreProc_tp()
new_TDataStoreProc_tp = _gdxcc.new_TDataStoreProc_tp

def copy_TDataStoreProc_tp(*args):
  return _gdxcc.copy_TDataStoreProc_tp(*args)
copy_TDataStoreProc_tp = _gdxcc.copy_TDataStoreProc_tp

def delete_TDataStoreProc_tp(*args):
  return _gdxcc.delete_TDataStoreProc_tp(*args)
delete_TDataStoreProc_tp = _gdxcc.delete_TDataStoreProc_tp

def TDataStoreProc_tp_assign(*args):
  return _gdxcc.TDataStoreProc_tp_assign(*args)
TDataStoreProc_tp_assign = _gdxcc.TDataStoreProc_tp_assign

def TDataStoreProc_tp_value(*args):
  return _gdxcc.TDataStoreProc_tp_value(*args)
TDataStoreProc_tp_value = _gdxcc.TDataStoreProc_tp_value

def new_TDataStoreFiltProc_tp():
  return _gdxcc.new_TDataStoreFiltProc_tp()
new_TDataStoreFiltProc_tp = _gdxcc.new_TDataStoreFiltProc_tp

def copy_TDataStoreFiltProc_tp(*args):
  return _gdxcc.copy_TDataStoreFiltProc_tp(*args)
copy_TDataStoreFiltProc_tp = _gdxcc.copy_TDataStoreFiltProc_tp

def delete_TDataStoreFiltProc_tp(*args):
  return _gdxcc.delete_TDataStoreFiltProc_tp(*args)
delete_TDataStoreFiltProc_tp = _gdxcc.delete_TDataStoreFiltProc_tp

def TDataStoreFiltProc_tp_assign(*args):
  return _gdxcc.TDataStoreFiltProc_tp_assign(*args)
TDataStoreFiltProc_tp_assign = _gdxcc.TDataStoreFiltProc_tp_assign

def TDataStoreFiltProc_tp_value(*args):
  return _gdxcc.TDataStoreFiltProc_tp_value(*args)
TDataStoreFiltProc_tp_value = _gdxcc.TDataStoreFiltProc_tp_value

def new_TDomainIndexProc_tp():
  return _gdxcc.new_TDomainIndexProc_tp()
new_TDomainIndexProc_tp = _gdxcc.new_TDomainIndexProc_tp

def copy_TDomainIndexProc_tp(*args):
  return _gdxcc.copy_TDomainIndexProc_tp(*args)
copy_TDomainIndexProc_tp = _gdxcc.copy_TDomainIndexProc_tp

def delete_TDomainIndexProc_tp(*args):
  return _gdxcc.delete_TDomainIndexProc_tp(*args)
delete_TDomainIndexProc_tp = _gdxcc.delete_TDomainIndexProc_tp

def TDomainIndexProc_tp_assign(*args):
  return _gdxcc.TDomainIndexProc_tp_assign(*args)
TDomainIndexProc_tp_assign = _gdxcc.TDomainIndexProc_tp_assign

def TDomainIndexProc_tp_value(*args):
  return _gdxcc.TDomainIndexProc_tp_value(*args)
TDomainIndexProc_tp_value = _gdxcc.TDomainIndexProc_tp_value

def gdxHandleToPtr(*args):
  """gdxHandleToPtr(pgdx) -> void *"""
  return _gdxcc.gdxHandleToPtr(*args)

def ptrTogdxHandle(*args):
  """ptrTogdxHandle(vptr) -> gdxHandle_t"""
  return _gdxcc.ptrTogdxHandle(*args)

def gdxGetReady(*args):
  """gdxGetReady(msgBufSize) -> int"""
  return _gdxcc.gdxGetReady(*args)

def gdxGetReadyD(*args):
  """gdxGetReadyD(dirName, msgBufSize) -> int"""
  return _gdxcc.gdxGetReadyD(*args)

def gdxGetReadyL(*args):
  """gdxGetReadyL(libName, msgBufSize) -> int"""
  return _gdxcc.gdxGetReadyL(*args)

def gdxCreate(*args):
  """gdxCreate(pgdx, msgBufSize) -> int"""
  return _gdxcc.gdxCreate(*args)

def gdxCreateD(*args):
  """gdxCreateD(pgdx, dirName, msgBufSize) -> int"""
  return _gdxcc.gdxCreateD(*args)

def gdxCreateL(*args):
  """gdxCreateL(pgdx, libName, msgBufSize) -> int"""
  return _gdxcc.gdxCreateL(*args)

def gdxFree(*args):
  """gdxFree(pgdx) -> int"""
  return _gdxcc.gdxFree(*args)

def gdxLibraryLoaded():
  """gdxLibraryLoaded() -> int"""
  return _gdxcc.gdxLibraryLoaded()

def gdxLibraryUnload():
  """gdxLibraryUnload() -> int"""
  return _gdxcc.gdxLibraryUnload()

def gdxGetScreenIndicator():
  """gdxGetScreenIndicator() -> int"""
  return _gdxcc.gdxGetScreenIndicator()

def gdxSetScreenIndicator(*args):
  """gdxSetScreenIndicator(scrind)"""
  return _gdxcc.gdxSetScreenIndicator(*args)

def gdxGetExceptionIndicator():
  """gdxGetExceptionIndicator() -> int"""
  return _gdxcc.gdxGetExceptionIndicator()

def gdxSetExceptionIndicator(*args):
  """gdxSetExceptionIndicator(excind)"""
  return _gdxcc.gdxSetExceptionIndicator(*args)

def gdxGetExitIndicator():
  """gdxGetExitIndicator() -> int"""
  return _gdxcc.gdxGetExitIndicator()

def gdxSetExitIndicator(*args):
  """gdxSetExitIndicator(extind)"""
  return _gdxcc.gdxSetExitIndicator(*args)

def gdxGetErrorCallback():
  """gdxGetErrorCallback() -> gdxErrorCallback_t"""
  return _gdxcc.gdxGetErrorCallback()

def gdxSetErrorCallback(*args):
  """gdxSetErrorCallback(func)"""
  return _gdxcc.gdxSetErrorCallback(*args)

def gdxGetAPIErrorCount():
  """gdxGetAPIErrorCount() -> int"""
  return _gdxcc.gdxGetAPIErrorCount()

def gdxSetAPIErrorCount(*args):
  """gdxSetAPIErrorCount(ecnt)"""
  return _gdxcc.gdxSetAPIErrorCount(*args)

def gdxErrorHandling(*args):
  """gdxErrorHandling(msg)"""
  return _gdxcc.gdxErrorHandling(*args)

def gdxAcronymAdd(*args):
  """gdxAcronymAdd(pgdx, AName, Txt, AIndx) -> int"""
  return _gdxcc.gdxAcronymAdd(*args)

def gdxAcronymCount(*args):
  """gdxAcronymCount(pgdx) -> int"""
  return _gdxcc.gdxAcronymCount(*args)

def gdxAcronymGetInfo(*args):
  """gdxAcronymGetInfo(pgdx, N) -> int"""
  return _gdxcc.gdxAcronymGetInfo(*args)

def gdxAcronymGetMapping(*args):
  """gdxAcronymGetMapping(pgdx, N) -> int"""
  return _gdxcc.gdxAcronymGetMapping(*args)

def gdxAcronymIndex(*args):
  """gdxAcronymIndex(pgdx, V) -> int"""
  return _gdxcc.gdxAcronymIndex(*args)

def gdxAcronymName(*args):
  """gdxAcronymName(pgdx, V) -> int"""
  return _gdxcc.gdxAcronymName(*args)

def gdxAcronymNextNr(*args):
  """gdxAcronymNextNr(pgdx, NV) -> int"""
  return _gdxcc.gdxAcronymNextNr(*args)

def gdxAcronymSetInfo(*args):
  """gdxAcronymSetInfo(pgdx, N, AName, Txt, AIndx) -> int"""
  return _gdxcc.gdxAcronymSetInfo(*args)

def gdxAcronymValue(*args):
  """gdxAcronymValue(pgdx, AIndx) -> double"""
  return _gdxcc.gdxAcronymValue(*args)

def gdxAddAlias(*args):
  """gdxAddAlias(pgdx, Id1, Id2) -> int"""
  return _gdxcc.gdxAddAlias(*args)

def gdxAddSetText(*args):
  """gdxAddSetText(pgdx, Txt) -> int"""
  return _gdxcc.gdxAddSetText(*args)

def gdxAutoConvert(*args):
  """gdxAutoConvert(pgdx, NV) -> int"""
  return _gdxcc.gdxAutoConvert(*args)

def gdxClose(*args):
  """gdxClose(pgdx) -> int"""
  return _gdxcc.gdxClose(*args)

def gdxDataErrorCount(*args):
  """gdxDataErrorCount(pgdx) -> int"""
  return _gdxcc.gdxDataErrorCount(*args)

def gdxDataErrorRecord(*args):
  """gdxDataErrorRecord(pgdx, RecNr) -> int"""
  return _gdxcc.gdxDataErrorRecord(*args)

def gdxDataReadDone(*args):
  """gdxDataReadDone(pgdx) -> int"""
  return _gdxcc.gdxDataReadDone(*args)

def gdxDataReadFilteredStart(*args):
  """gdxDataReadFilteredStart(pgdx, SyNr, FilterAction) -> int"""
  return _gdxcc.gdxDataReadFilteredStart(*args)

def gdxDataReadMap(*args):
  """gdxDataReadMap(pgdx, RecNr) -> int"""
  return _gdxcc.gdxDataReadMap(*args)

def gdxDataReadMapStart(*args):
  """gdxDataReadMapStart(pgdx, SyNr) -> int"""
  return _gdxcc.gdxDataReadMapStart(*args)

def gdxDataReadRaw(*args):
  """gdxDataReadRaw(pgdx) -> int"""
  return _gdxcc.gdxDataReadRaw(*args)

def gdxDataReadRawFast(*args):
  """gdxDataReadRawFast(pgdx, SyNr, DP) -> int"""
  return _gdxcc.gdxDataReadRawFast(*args)

def gdxDataReadRawFastFilt(*args):
  """gdxDataReadRawFastFilt(pgdx, SyNr, UelFilterStr_in, DP) -> int"""
  return _gdxcc.gdxDataReadRawFastFilt(*args)

def gdxDataReadRawStart(*args):
  """gdxDataReadRawStart(pgdx, SyNr) -> int"""
  return _gdxcc.gdxDataReadRawStart(*args)

def gdxDataReadSlice(*args):
  """gdxDataReadSlice(pgdx, UelFilterStr_in, DP) -> int"""
  return _gdxcc.gdxDataReadSlice(*args)

def gdxDataReadSliceStart(*args):
  """gdxDataReadSliceStart(pgdx, SyNr) -> int"""
  return _gdxcc.gdxDataReadSliceStart(*args)

def gdxDataReadStr(*args):
  """gdxDataReadStr(pgdx) -> int"""
  return _gdxcc.gdxDataReadStr(*args)

def gdxDataReadStrStart(*args):
  """gdxDataReadStrStart(pgdx, SyNr) -> int"""
  return _gdxcc.gdxDataReadStrStart(*args)

def gdxDataSliceUELS(*args):
  """gdxDataSliceUELS(pgdx, SliceKeyInt) -> int"""
  return _gdxcc.gdxDataSliceUELS(*args)

def gdxDataWriteDone(*args):
  """gdxDataWriteDone(pgdx) -> int"""
  return _gdxcc.gdxDataWriteDone(*args)

def gdxDataWriteMap(*args):
  """gdxDataWriteMap(pgdx, KeyInt, Values) -> int"""
  return _gdxcc.gdxDataWriteMap(*args)

def gdxDataWriteMapStart(*args):
  """gdxDataWriteMapStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo) -> int"""
  return _gdxcc.gdxDataWriteMapStart(*args)

def gdxDataWriteRaw(*args):
  """gdxDataWriteRaw(pgdx, KeyInt, Values) -> int"""
  return _gdxcc.gdxDataWriteRaw(*args)

def gdxDataWriteRawStart(*args):
  """gdxDataWriteRawStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo) -> int"""
  return _gdxcc.gdxDataWriteRawStart(*args)

def gdxDataWriteStr(*args):
  """gdxDataWriteStr(pgdx, KeyStr_in, Values) -> int"""
  return _gdxcc.gdxDataWriteStr(*args)

def gdxDataWriteStrStart(*args):
  """gdxDataWriteStrStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo) -> int"""
  return _gdxcc.gdxDataWriteStrStart(*args)

def gdxGetDLLVersion(*args):
  """gdxGetDLLVersion(pgdx) -> int"""
  return _gdxcc.gdxGetDLLVersion(*args)

def gdxErrorCount(*args):
  """gdxErrorCount(pgdx) -> int"""
  return _gdxcc.gdxErrorCount(*args)

def gdxErrorStr(*args):
  """gdxErrorStr(pgdx, ErrNr) -> int"""
  return _gdxcc.gdxErrorStr(*args)

def gdxFileInfo(*args):
  """gdxFileInfo(pgdx) -> int"""
  return _gdxcc.gdxFileInfo(*args)

def gdxFileVersion(*args):
  """gdxFileVersion(pgdx) -> int"""
  return _gdxcc.gdxFileVersion(*args)

def gdxFilterExists(*args):
  """gdxFilterExists(pgdx, FilterNr) -> int"""
  return _gdxcc.gdxFilterExists(*args)

def gdxFilterRegister(*args):
  """gdxFilterRegister(pgdx, UelMap) -> int"""
  return _gdxcc.gdxFilterRegister(*args)

def gdxFilterRegisterDone(*args):
  """gdxFilterRegisterDone(pgdx) -> int"""
  return _gdxcc.gdxFilterRegisterDone(*args)

def gdxFilterRegisterStart(*args):
  """gdxFilterRegisterStart(pgdx, FilterNr) -> int"""
  return _gdxcc.gdxFilterRegisterStart(*args)

def gdxFindSymbol(*args):
  """gdxFindSymbol(pgdx, SyId) -> int"""
  return _gdxcc.gdxFindSymbol(*args)

def gdxGetElemText(*args):
  """gdxGetElemText(pgdx, TxtNr) -> int"""
  return _gdxcc.gdxGetElemText(*args)

def gdxGetLastError(*args):
  """gdxGetLastError(pgdx) -> int"""
  return _gdxcc.gdxGetLastError(*args)

def gdxGetMemoryUsed(*args):
  """gdxGetMemoryUsed(pgdx) -> INT64"""
  return _gdxcc.gdxGetMemoryUsed(*args)

def gdxGetSpecialValues(*args):
  """gdxGetSpecialValues(pgdx, AVals) -> int"""
  return _gdxcc.gdxGetSpecialValues(*args)

def gdxGetUEL(*args):
  """gdxGetUEL(pgdx, UelNr) -> int"""
  return _gdxcc.gdxGetUEL(*args)

def gdxMapValue(*args):
  """gdxMapValue(pgdx, D) -> int"""
  return _gdxcc.gdxMapValue(*args)

def gdxOpenAppend(*args):
  """gdxOpenAppend(pgdx, FileName, Producer) -> int"""
  return _gdxcc.gdxOpenAppend(*args)

def gdxOpenRead(*args):
  """gdxOpenRead(pgdx, FileName) -> int"""
  return _gdxcc.gdxOpenRead(*args)

def gdxOpenWrite(*args):
  """gdxOpenWrite(pgdx, FileName, Producer) -> int"""
  return _gdxcc.gdxOpenWrite(*args)

def gdxOpenWriteEx(*args):
  """gdxOpenWriteEx(pgdx, FileName, Producer, Compr) -> int"""
  return _gdxcc.gdxOpenWriteEx(*args)

def gdxResetSpecialValues(*args):
  """gdxResetSpecialValues(pgdx) -> int"""
  return _gdxcc.gdxResetSpecialValues(*args)

def gdxSetHasText(*args):
  """gdxSetHasText(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSetHasText(*args)

def gdxSetReadSpecialValues(*args):
  """gdxSetReadSpecialValues(pgdx, AVals) -> int"""
  return _gdxcc.gdxSetReadSpecialValues(*args)

def gdxSetSpecialValues(*args):
  """gdxSetSpecialValues(pgdx, AVals) -> int"""
  return _gdxcc.gdxSetSpecialValues(*args)

def gdxSetTextNodeNr(*args):
  """gdxSetTextNodeNr(pgdx, TxtNr, Node) -> int"""
  return _gdxcc.gdxSetTextNodeNr(*args)

def gdxSetTraceLevel(*args):
  """gdxSetTraceLevel(pgdx, N, s) -> int"""
  return _gdxcc.gdxSetTraceLevel(*args)

def gdxSymbIndxMaxLength(*args):
  """gdxSymbIndxMaxLength(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSymbIndxMaxLength(*args)

def gdxSymbMaxLength(*args):
  """gdxSymbMaxLength(pgdx) -> int"""
  return _gdxcc.gdxSymbMaxLength(*args)

def gdxSymbolAddComment(*args):
  """gdxSymbolAddComment(pgdx, SyNr, Txt) -> int"""
  return _gdxcc.gdxSymbolAddComment(*args)

def gdxSymbolGetComment(*args):
  """gdxSymbolGetComment(pgdx, SyNr, N) -> int"""
  return _gdxcc.gdxSymbolGetComment(*args)

def gdxSymbolGetDomain(*args):
  """gdxSymbolGetDomain(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSymbolGetDomain(*args)

def gdxSymbolGetDomainX(*args):
  """gdxSymbolGetDomainX(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSymbolGetDomainX(*args)

def gdxSymbolDim(*args):
  """gdxSymbolDim(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSymbolDim(*args)

def gdxSymbolInfo(*args):
  """gdxSymbolInfo(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSymbolInfo(*args)

def gdxSymbolInfoX(*args):
  """gdxSymbolInfoX(pgdx, SyNr) -> int"""
  return _gdxcc.gdxSymbolInfoX(*args)

def gdxSymbolSetDomain(*args):
  """gdxSymbolSetDomain(pgdx, DomainIDs_in) -> int"""
  return _gdxcc.gdxSymbolSetDomain(*args)

def gdxSymbolSetDomainX(*args):
  """gdxSymbolSetDomainX(pgdx, SyNr, DomainIDs_in) -> int"""
  return _gdxcc.gdxSymbolSetDomainX(*args)

def gdxSystemInfo(*args):
  """gdxSystemInfo(pgdx) -> int"""
  return _gdxcc.gdxSystemInfo(*args)

def gdxUELMaxLength(*args):
  """gdxUELMaxLength(pgdx) -> int"""
  return _gdxcc.gdxUELMaxLength(*args)

def gdxUELRegisterDone(*args):
  """gdxUELRegisterDone(pgdx) -> int"""
  return _gdxcc.gdxUELRegisterDone(*args)

def gdxUELRegisterMap(*args):
  """gdxUELRegisterMap(pgdx, UMap, Uel) -> int"""
  return _gdxcc.gdxUELRegisterMap(*args)

def gdxUELRegisterMapStart(*args):
  """gdxUELRegisterMapStart(pgdx) -> int"""
  return _gdxcc.gdxUELRegisterMapStart(*args)

def gdxUELRegisterRaw(*args):
  """gdxUELRegisterRaw(pgdx, Uel) -> int"""
  return _gdxcc.gdxUELRegisterRaw(*args)

def gdxUELRegisterRawStart(*args):
  """gdxUELRegisterRawStart(pgdx) -> int"""
  return _gdxcc.gdxUELRegisterRawStart(*args)

def gdxUELRegisterStr(*args):
  """gdxUELRegisterStr(pgdx, Uel) -> int"""
  return _gdxcc.gdxUELRegisterStr(*args)

def gdxUELRegisterStrStart(*args):
  """gdxUELRegisterStrStart(pgdx) -> int"""
  return _gdxcc.gdxUELRegisterStrStart(*args)

def gdxUMFindUEL(*args):
  """gdxUMFindUEL(pgdx, Uel) -> int"""
  return _gdxcc.gdxUMFindUEL(*args)

def gdxUMUelGet(*args):
  """gdxUMUelGet(pgdx, UelNr) -> int"""
  return _gdxcc.gdxUMUelGet(*args)

def gdxUMUelInfo(*args):
  """gdxUMUelInfo(pgdx) -> int"""
  return _gdxcc.gdxUMUelInfo(*args)

def gdxGetDomainElements(*args):
  """gdxGetDomainElements(pgdx, SyNr, DimPos, FilterNr, DP, Uptr) -> int"""
  return _gdxcc.gdxGetDomainElements(*args)

def gdxCurrentDim(*args):
  """gdxCurrentDim(pgdx) -> int"""
  return _gdxcc.gdxCurrentDim(*args)

def gdxRenameUEL(*args):
  """gdxRenameUEL(pgdx, OldName, NewName) -> int"""
  return _gdxcc.gdxRenameUEL(*args)
GLOBAL_MAX_INDEX_DIM = _gdxcc.GLOBAL_MAX_INDEX_DIM
GLOBAL_UEL_IDENT_SIZE = _gdxcc.GLOBAL_UEL_IDENT_SIZE
ITERLIM_INFINITY = _gdxcc.ITERLIM_INFINITY
GMS_MAX_INDEX_DIM = _gdxcc.GMS_MAX_INDEX_DIM
GMS_UEL_IDENT_SIZE = _gdxcc.GMS_UEL_IDENT_SIZE
GMS_SSSIZE = _gdxcc.GMS_SSSIZE
GMS_VARTYPE_UNKNOWN = _gdxcc.GMS_VARTYPE_UNKNOWN
GMS_VARTYPE_BINARY = _gdxcc.GMS_VARTYPE_BINARY
GMS_VARTYPE_INTEGER = _gdxcc.GMS_VARTYPE_INTEGER
GMS_VARTYPE_POSITIVE = _gdxcc.GMS_VARTYPE_POSITIVE
GMS_VARTYPE_NEGATIVE = _gdxcc.GMS_VARTYPE_NEGATIVE
GMS_VARTYPE_FREE = _gdxcc.GMS_VARTYPE_FREE
GMS_VARTYPE_SOS1 = _gdxcc.GMS_VARTYPE_SOS1
GMS_VARTYPE_SOS2 = _gdxcc.GMS_VARTYPE_SOS2
GMS_VARTYPE_SEMICONT = _gdxcc.GMS_VARTYPE_SEMICONT
GMS_VARTYPE_SEMIINT = _gdxcc.GMS_VARTYPE_SEMIINT
GMS_VARTYPE_MAX = _gdxcc.GMS_VARTYPE_MAX
GMS_EQUTYPE_E = _gdxcc.GMS_EQUTYPE_E
GMS_EQUTYPE_G = _gdxcc.GMS_EQUTYPE_G
GMS_EQUTYPE_L = _gdxcc.GMS_EQUTYPE_L
GMS_EQUTYPE_N = _gdxcc.GMS_EQUTYPE_N
GMS_EQUTYPE_X = _gdxcc.GMS_EQUTYPE_X
GMS_EQUTYPE_C = _gdxcc.GMS_EQUTYPE_C
GMS_EQUTYPE_MAX = _gdxcc.GMS_EQUTYPE_MAX
GMS_VAL_LEVEL = _gdxcc.GMS_VAL_LEVEL
GMS_VAL_MARGINAL = _gdxcc.GMS_VAL_MARGINAL
GMS_VAL_LOWER = _gdxcc.GMS_VAL_LOWER
GMS_VAL_UPPER = _gdxcc.GMS_VAL_UPPER
GMS_VAL_SCALE = _gdxcc.GMS_VAL_SCALE
GMS_VAL_MAX = _gdxcc.GMS_VAL_MAX
sv_valund = _gdxcc.sv_valund
sv_valna = _gdxcc.sv_valna
sv_valpin = _gdxcc.sv_valpin
sv_valmin = _gdxcc.sv_valmin
sv_valeps = _gdxcc.sv_valeps
sv_normal = _gdxcc.sv_normal
sv_acronym = _gdxcc.sv_acronym
GMS_SVIDX_UNDEF = _gdxcc.GMS_SVIDX_UNDEF
GMS_SVIDX_NA = _gdxcc.GMS_SVIDX_NA
GMS_SVIDX_PINF = _gdxcc.GMS_SVIDX_PINF
GMS_SVIDX_MINF = _gdxcc.GMS_SVIDX_MINF
GMS_SVIDX_EPS = _gdxcc.GMS_SVIDX_EPS
GMS_SVIDX_NORMAL = _gdxcc.GMS_SVIDX_NORMAL
GMS_SVIDX_ACR = _gdxcc.GMS_SVIDX_ACR
GMS_SVIDX_MAX = _gdxcc.GMS_SVIDX_MAX
dt_set = _gdxcc.dt_set
dt_par = _gdxcc.dt_par
dt_var = _gdxcc.dt_var
dt_equ = _gdxcc.dt_equ
dt_alias = _gdxcc.dt_alias
GMS_DT_SET = _gdxcc.GMS_DT_SET
GMS_DT_PAR = _gdxcc.GMS_DT_PAR
GMS_DT_VAR = _gdxcc.GMS_DT_VAR
GMS_DT_EQU = _gdxcc.GMS_DT_EQU
GMS_DT_ALIAS = _gdxcc.GMS_DT_ALIAS
GMS_DT_MAX = _gdxcc.GMS_DT_MAX
GMS_SV_UNDEF = _gdxcc.GMS_SV_UNDEF
GMS_SV_NA = _gdxcc.GMS_SV_NA
GMS_SV_PINF = _gdxcc.GMS_SV_PINF
GMS_SV_MINF = _gdxcc.GMS_SV_MINF
GMS_SV_EPS = _gdxcc.GMS_SV_EPS
GMS_SV_ACR = _gdxcc.GMS_SV_ACR
GMS_SV_NAINT = _gdxcc.GMS_SV_NAINT
# This file is compatible with both classic and new-style classes.


