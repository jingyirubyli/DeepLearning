#================================================================
# csmc.py
# module file for CONTEC Motor Control device
#                                                CONTEC.Co., Ltd.
#================================================================
import ctypes
import ctypes.wintypes

csmc_dll = ctypes.windll.LoadLibrary('csmc.dll')


#----------------------------------------
# Prototype definition
#----------------------------------------
#----------------------------------------
# Initialization Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWInit(char * DeviceName, short *DevId);
SmcWInit = csmc_dll.SmcWInit
SmcWInit.restype = ctypes.c_long
SmcWInit.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWExit(short DevId);
SmcWExit = csmc_dll.SmcWExit
SmcWExit.restype = ctypes.c_long
SmcWExit.argtypes = [ctypes.c_short]

# C Prototype: long WINAPI SmcWGetErrorString(long ErrorCode, char *ErrorString);
SmcWGetErrorString = csmc_dll.SmcWGetErrorString
SmcWGetErrorString.restype = ctypes.c_long
SmcWGetErrorString.argtypes = [ctypes.c_long, ctypes.c_char_p]

#----------------------------------------
# Initial Parameters Setting Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetPulseType(short DevId, short AxisNo, short PulseMode, short DirTimer);
SmcWSetPulseType = csmc_dll.SmcWSetPulseType
SmcWSetPulseType.restype = ctypes.c_long
SmcWSetPulseType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulseType(short DevId, short AxisNo, short *PulseMode, short *DirTimer);
SmcWGetPulseType = csmc_dll.SmcWGetPulseType
SmcWGetPulseType.restype = ctypes.c_long
SmcWGetPulseType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetPulseDuty(short DevId, short AxisNo, short Duty);
SmcWSetPulseDuty = csmc_dll.SmcWSetPulseDuty
SmcWSetPulseDuty.restype = ctypes.c_long
SmcWSetPulseDuty.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulseDuty(short DevId, short AxisNo, short *Duty);
SmcWGetPulseDuty = csmc_dll.SmcWGetPulseDuty
SmcWGetPulseDuty.restype = ctypes.c_long
SmcWGetPulseDuty.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetEncType(short DevId, short AxisNo, short EncType);
SmcWSetEncType = csmc_dll.SmcWSetEncType
SmcWSetEncType.restype = ctypes.c_long
SmcWSetEncType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetEncType(short DevId, short AxisNo, short *EncType);
SmcWGetEncType = csmc_dll.SmcWGetEncType
SmcWGetEncType.restype = ctypes.c_long
SmcWGetEncType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetCtrlTypeOut(short DevId, short AxisNo, short CtrlOut1, short CtrlOut2, short CtrlOut3);
SmcWSetCtrlTypeOut = csmc_dll.SmcWSetCtrlTypeOut
SmcWSetCtrlTypeOut.restype = ctypes.c_long
SmcWSetCtrlTypeOut.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetCtrlTypeOut(short DevId, short AxisNo, short *CtrlOut1, short *CtrlOut2, short *CtrlOut3);
SmcWGetCtrlTypeOut = csmc_dll.SmcWGetCtrlTypeOut
SmcWGetCtrlTypeOut.restype = ctypes.c_long
SmcWGetCtrlTypeOut.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetCtrlTypeIn(short DevId, short AxisNo, short CtrlIn);
SmcWSetCtrlTypeIn = csmc_dll.SmcWSetCtrlTypeIn
SmcWSetCtrlTypeIn.restype = ctypes.c_long
SmcWSetCtrlTypeIn.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetCtrlTypeIn(short DevId, short AxisNo, short *CtrlIn);
SmcWGetCtrlTypeIn = csmc_dll.SmcWGetCtrlTypeIn
SmcWGetCtrlTypeIn.restype = ctypes.c_long
SmcWGetCtrlTypeIn.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetOrgLog(short DevId, short AxisNo, short OrgLog);
SmcWSetOrgLog = csmc_dll.SmcWSetOrgLog
SmcWSetOrgLog.restype = ctypes.c_long
SmcWSetOrgLog.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetOrgLog(short DevId, short AxisNo, short *OrgLog);
SmcWGetOrgLog = csmc_dll.SmcWGetOrgLog
SmcWGetOrgLog.restype = ctypes.c_long
SmcWGetOrgLog.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetCtrlInOutLog(short DevId, short AxisNo, short CtrlInOutLog);
SmcWSetCtrlInOutLog = csmc_dll.SmcWSetCtrlInOutLog
SmcWSetCtrlInOutLog.restype = ctypes.c_long
SmcWSetCtrlInOutLog.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetCtrlInOutLog(short DevId, short AxisNo, short* CtrlInOutLog);
SmcWGetCtrlInOutLog = csmc_dll.SmcWGetCtrlInOutLog
SmcWGetCtrlInOutLog.restype = ctypes.c_long
SmcWGetCtrlInOutLog.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetErcMode(short DevId, short AxisNo, short ErcMode);
SmcWSetErcMode = csmc_dll.SmcWSetErcMode
SmcWSetErcMode.restype = ctypes.c_long
SmcWSetErcMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetErcMode(short DevId, short AxisNo, short *ErcMode);
SmcWGetErcMode = csmc_dll.SmcWGetErcMode
SmcWGetErcMode.restype = ctypes.c_long
SmcWGetErcMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetErcAlmClearTime(short DevId, short AxisNo, short ErcTime, short ErcOffTimer, short AlmTime);
SmcWSetErcAlmClearTime = csmc_dll.SmcWSetErcAlmClearTime
SmcWSetErcAlmClearTime.restype = ctypes.c_long
SmcWSetErcAlmClearTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetErcAlmClearTime(short DevId, short AxisNo, short *ErcTime, short *ErcOffTimer, short *AlmTime);
SmcWGetErcAlmClearTime = csmc_dll.SmcWGetErcAlmClearTime
SmcWGetErcAlmClearTime.restype = ctypes.c_long
SmcWGetErcAlmClearTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetOrgMode(short DevId, short AxisNo, short LimitTurn, short OrgType, short EndDir, short ZCount);
SmcWSetOrgMode = csmc_dll.SmcWSetOrgMode
SmcWSetOrgMode.restype = ctypes.c_long
SmcWSetOrgMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetOrgMode(short DevId, short AxisNo, short *LimitTurn, short *OrgType, short *EndDir, short *ZCount);
SmcWGetOrgMode = csmc_dll.SmcWGetOrgMode
SmcWGetOrgMode.restype = ctypes.c_long
SmcWGetOrgMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetSAccelType(short DevId, short AxisNo, short SAccelType);
SmcWSetSAccelType = csmc_dll.SmcWSetSAccelType
SmcWSetSAccelType.restype = ctypes.c_long
SmcWSetSAccelType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetSAccelType(short DevId, short AxisNo, short *SAccelType);
SmcWGetSAccelType = csmc_dll.SmcWGetSAccelType
SmcWGetSAccelType.restype = ctypes.c_long
SmcWGetSAccelType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetInFilterType(short DevId, short AxisNo, short FilterType);
SmcWSetInFilterType = csmc_dll.SmcWSetInFilterType
SmcWSetInFilterType.restype = ctypes.c_long
SmcWSetInFilterType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetInFilterType(short DevId, short AxisNo, short *FilterType);
SmcWGetInFilterType = csmc_dll.SmcWGetInFilterType
SmcWGetInFilterType.restype = ctypes.c_long
SmcWGetInFilterType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetSDMode(short DevId, short AxisNo, short SDMode);
SmcWSetSDMode = csmc_dll.SmcWSetSDMode
SmcWSetSDMode.restype = ctypes.c_long
SmcWSetSDMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetSDMode(short DevId, short AxisNo, short *SDMode);
SmcWGetSDMode = csmc_dll.SmcWGetSDMode
SmcWGetSDMode.restype = ctypes.c_long
SmcWGetSDMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetCounterMode(short DevId, short AxisNo, short ClrCounterLtc, short LtcMode, short ClrCounterClr, short ClrMode);
SmcWSetCounterMode = csmc_dll.SmcWSetCounterMode
SmcWSetCounterMode.restype = ctypes.c_long
SmcWSetCounterMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetCounterMode(short DevId, short AxisNo, short *ClrCounterLtc, short *LtcMode, short *ClrCounterClr, short *ClrMode);
SmcWGetCounterMode = csmc_dll.SmcWGetCounterMode
SmcWGetCounterMode.restype = ctypes.c_long
SmcWGetCounterMode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetSoftLimit(short DevId, short AxisNo, short PLimMode, short MLimMode, long PLimCount, long MLimCount);
SmcWSetSoftLimit = csmc_dll.SmcWSetSoftLimit
SmcWSetSoftLimit.restype = ctypes.c_long
SmcWSetSoftLimit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetSoftLimit(short DevId, short AxisNo, short *PLimMode, short *MLimMode, long *PLimCount, long *MLimCount);
SmcWGetSoftLimit = csmc_dll.SmcWGetSoftLimit
SmcWGetSoftLimit.restype = ctypes.c_long
SmcWGetSoftLimit.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWSetInitParam(short DevId, short AxisNo);
SmcWSetInitParam = csmc_dll.SmcWSetInitParam
SmcWSetInitParam.restype = ctypes.c_long
SmcWSetInitParam.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetInitParam(short DevId, short AxisNo, short *InitParam);
SmcWGetInitParam = csmc_dll.SmcWGetInitParam
SmcWGetInitParam.restype = ctypes.c_long
SmcWGetInitParam.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

#----------------------------------------
# Basic Operation Setting Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetReady(short DevId, short AxisNo, short MotionType, short StartDir);
SmcWSetReady = csmc_dll.SmcWSetReady
SmcWSetReady.restype = ctypes.c_long
SmcWSetReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetReady(short DevId, short AxisNo, short *MotionType, short *StartDir);
SmcWGetReady = csmc_dll.SmcWGetReady
SmcWGetReady.restype = ctypes.c_long
SmcWGetReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetResolveSpeed(short DevId, short AxisNo, double ResolveSpeed);
SmcWSetResolveSpeed = csmc_dll.SmcWSetResolveSpeed
SmcWSetResolveSpeed.restype = ctypes.c_long
SmcWSetResolveSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetResolveSpeed(short DevId, short AxisNo, double *ResolveSpeed);
SmcWGetResolveSpeed = csmc_dll.SmcWGetResolveSpeed
SmcWGetResolveSpeed.restype = ctypes.c_long
SmcWGetResolveSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetStartSpeed(short DevId, short AxisNo, double StartSpeed);
SmcWSetStartSpeed = csmc_dll.SmcWSetStartSpeed
SmcWSetStartSpeed.restype = ctypes.c_long
SmcWSetStartSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetStartSpeed(short DevId, short AxisNo, double *StartSpeed);
SmcWGetStartSpeed = csmc_dll.SmcWGetStartSpeed
SmcWGetStartSpeed.restype = ctypes.c_long
SmcWGetStartSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetTargetSpeed(short DevId, short AxisNo, double TargetSpeed);
SmcWSetTargetSpeed = csmc_dll.SmcWSetTargetSpeed
SmcWSetTargetSpeed.restype = ctypes.c_long
SmcWSetTargetSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetTargetSpeed(short DevId, short AxisNo, double *TargetSpeed);
SmcWGetTargetSpeed = csmc_dll.SmcWGetTargetSpeed
SmcWGetTargetSpeed.restype = ctypes.c_long
SmcWGetTargetSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetAccelTime(short DevId, short AxisNo, double AccelTime);
SmcWSetAccelTime = csmc_dll.SmcWSetAccelTime
SmcWSetAccelTime.restype = ctypes.c_long
SmcWSetAccelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetAccelTime(short DevId, short AxisNo, double *AccelTime);
SmcWGetAccelTime = csmc_dll.SmcWGetAccelTime
SmcWGetAccelTime.restype = ctypes.c_long
SmcWGetAccelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetDecelTime(short DevId, short AxisNo, double DecelTime);
SmcWSetDecelTime = csmc_dll.SmcWSetDecelTime
SmcWSetDecelTime.restype = ctypes.c_long
SmcWSetDecelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetDecelTime(short DevId, short AxisNo, double *DecelTime);
SmcWGetDecelTime = csmc_dll.SmcWGetDecelTime
SmcWGetDecelTime.restype = ctypes.c_long
SmcWGetDecelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetSSpeed(short DevId, short AxisNo, double SSpeed);
SmcWSetSSpeed = csmc_dll.SmcWSetSSpeed
SmcWSetSSpeed.restype = ctypes.c_long
SmcWSetSSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetSSpeed(short DevId, short AxisNo, double *SSpeed);
SmcWGetSSpeed = csmc_dll.SmcWGetSSpeed
SmcWGetSSpeed.restype = ctypes.c_long
SmcWGetSSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetStopPosition(short DevId, short AxisNo, short Coodinate, long StopPosition);
SmcWSetStopPosition = csmc_dll.SmcWSetStopPosition
SmcWSetStopPosition.restype = ctypes.c_long
SmcWSetStopPosition.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetStopPosition(short DevId, short AxisNo, short Coodinate, long *StopPosition);
SmcWGetStopPosition = csmc_dll.SmcWGetStopPosition
SmcWGetStopPosition.restype = ctypes.c_long
SmcWGetStopPosition.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWSetSync(short DevId, short SyncAxis, short SyncChip, short SyncBoard);
SmcWSetSync = csmc_dll.SmcWSetSync
SmcWSetSync.restype = ctypes.c_long
SmcWSetSync.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetSync(short DevId, short *SyncAxis, short *SyncChip, short *SyncBoard);
SmcWGetSync = csmc_dll.SmcWGetSync
SmcWGetSync.restype = ctypes.c_long
SmcWGetSync.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetZCountMotion(short DevId, short AxisNo, short ZMoveCount, short ZLog);
SmcWSetZCountMotion = csmc_dll.SmcWSetZCountMotion
SmcWSetZCountMotion.restype = ctypes.c_long
SmcWSetZCountMotion.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetZCountMotion(short DevId, short AxisNo, short *ZMoveCount, short *ZLog);
SmcWGetZCountMotion = csmc_dll.SmcWGetZCountMotion
SmcWGetZCountMotion.restype = ctypes.c_long
SmcWGetZCountMotion.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

#----------------------------------------
# Extended Operation Setting Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetBankNumber(short DevId, short AxisNo, short BankNum);
SmcWSetBankNumber = csmc_dll.SmcWSetBankNumber
SmcWSetBankNumber.restype = ctypes.c_long
SmcWSetBankNumber.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetBankNumber(short DevId, short AxisNo, short *BankNum);
SmcWGetBankNumber = csmc_dll.SmcWGetBankNumber
SmcWGetBankNumber.restype = ctypes.c_long
SmcWGetBankNumber.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetBankReady(short DevId, short AxisNo, short MotionType);
SmcWSetBankReady = csmc_dll.SmcWSetBankReady
SmcWSetBankReady.restype = ctypes.c_long
SmcWSetBankReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetBankReady(short DevId, short AxisNo, short *MotionType);
SmcWGetBankReady = csmc_dll.SmcWGetBankReady
SmcWGetBankReady.restype = ctypes.c_long
SmcWGetBankReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetBankDistance(short DevId, short AxisNo, short BankNo, long StopPosition);
SmcWSetBankDistance = csmc_dll.SmcWSetBankDistance
SmcWSetBankDistance.restype = ctypes.c_long
SmcWSetBankDistance.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetBankDistance(short DevId, short AxisNo, short BankNo, long *StopPosition);
SmcWGetBankDistance = csmc_dll.SmcWGetBankDistance
SmcWGetBankDistance.restype = ctypes.c_long
SmcWGetBankDistance.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWSetBankResolveSpeed(short DevId, short AxisNo, short BankNo, double ResolveSpeed);
SmcWSetBankResolveSpeed = csmc_dll.SmcWSetBankResolveSpeed
SmcWSetBankResolveSpeed.restype = ctypes.c_long
SmcWSetBankResolveSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetBankResolveSpeed(short DevId, short AxisNo, short BankNo, double *ResolveSpeed);
SmcWGetBankResolveSpeed = csmc_dll.SmcWGetBankResolveSpeed
SmcWGetBankResolveSpeed.restype = ctypes.c_long
SmcWGetBankResolveSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetBankStartSpeed(short DevId, short AxisNo, short BankNo, double StartSpeed);
SmcWSetBankStartSpeed = csmc_dll.SmcWSetBankStartSpeed
SmcWSetBankStartSpeed.restype = ctypes.c_long
SmcWSetBankStartSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetBankStartSpeed(short DevId, short AxisNo, short BankNo, double *StartSpeed);
SmcWGetBankStartSpeed = csmc_dll.SmcWGetBankStartSpeed
SmcWGetBankStartSpeed.restype = ctypes.c_long
SmcWGetBankStartSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetBankTargetSpeed(short DevId, short AxisNo, short BankNo, double TargetSpeed);
SmcWSetBankTargetSpeed = csmc_dll.SmcWSetBankTargetSpeed
SmcWSetBankTargetSpeed.restype = ctypes.c_long
SmcWSetBankTargetSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetBankTargetSpeed(short DevId, short AxisNo, short BankNo, double *TargetSpeed);
SmcWGetBankTargetSpeed = csmc_dll.SmcWGetBankTargetSpeed
SmcWGetBankTargetSpeed.restype = ctypes.c_long
SmcWGetBankTargetSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetBankAccelTime(short DevId, short AxisNo, short BankNo, double AccelTime);
SmcWSetBankAccelTime = csmc_dll.SmcWSetBankAccelTime
SmcWSetBankAccelTime.restype = ctypes.c_long
SmcWSetBankAccelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetBankAccelTime(short DevId, short AxisNo, short BankNo, double *AccelTime);
SmcWGetBankAccelTime = csmc_dll.SmcWGetBankAccelTime
SmcWGetBankAccelTime.restype = ctypes.c_long
SmcWGetBankAccelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetBankDecelTime(short DevId, short AxisNo, short BankNo, double DecelTime);
SmcWSetBankDecelTime = csmc_dll.SmcWSetBankDecelTime
SmcWSetBankDecelTime.restype = ctypes.c_long
SmcWSetBankDecelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetBankDecelTime(short DevId, short AxisNo, short BankNo, double *DecelTime);
SmcWGetBankDecelTime = csmc_dll.SmcWGetBankDecelTime
SmcWGetBankDecelTime.restype = ctypes.c_long
SmcWGetBankDecelTime.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetBankSSpeed(short DevId, short AxisNo, short BankNo, double SSpeed);
SmcWSetBankSSpeed = csmc_dll.SmcWSetBankSSpeed
SmcWSetBankSSpeed.restype = ctypes.c_long
SmcWSetBankSSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double]

# C Prototype: long WINAPI SmcWGetBankSSpeed(short DevId, short AxisNo, short BankNo, double *SSpeed);
SmcWGetBankSSpeed = csmc_dll.SmcWGetBankSSpeed
SmcWGetBankSSpeed.restype = ctypes.c_long
SmcWGetBankSSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWSetBankInterpolation(short DevId, short AxisNo, short BankNo, short InterType, short InterAxis, short Reserved);
SmcWSetBankInterpolation = csmc_dll.SmcWSetBankInterpolation
SmcWSetBankInterpolation.restype = ctypes.c_long
SmcWSetBankInterpolation.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetBankInterpolation(short DevId, short AxisNo, short BankNo, short *InterType, short *InterAxis, short *Reserved);
SmcWGetBankInterpolation = csmc_dll.SmcWGetBankInterpolation
SmcWGetBankInterpolation.restype = ctypes.c_long
SmcWGetBankInterpolation.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetBankArcPoint(short DevId, short AxisNo, short BankNo, double ArcSpeed, long Center_X, long Center_Y, long End_X, long End_Y);
SmcWSetBankArcPoint = csmc_dll.SmcWSetBankArcPoint
SmcWSetBankArcPoint.restype = ctypes.c_long
SmcWSetBankArcPoint.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetBankArcPoint(short DevId, short AxisNo, short BankNo, double *ArcSpeed, long *Center_X, long *Center_Y, long *End_X, long *End_Y);
SmcWGetBankArcPoint = csmc_dll.SmcWGetBankArcPoint
SmcWGetBankArcPoint.restype = ctypes.c_long
SmcWGetBankArcPoint.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWSetBankArcParam(short DevId, short AxisNo, short BankNo, short ArcStrtDir, short AutoEndPointPull);
SmcWSetBankArcParam = csmc_dll.SmcWSetBankArcParam
SmcWSetBankArcParam.restype = ctypes.c_long
SmcWSetBankArcParam.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetBankArcParam(short DevId, short AxisNo, short BankNo, short *ArcStrtDir, short *AutoEndPointPull);
SmcWGetBankArcParam = csmc_dll.SmcWGetBankArcParam
SmcWGetBankArcParam.restype = ctypes.c_long
SmcWGetBankArcParam.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

#----------------------------------------
# Motor Operation Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWMotionStart(short DevId, short AxisNo);
SmcWMotionStart = csmc_dll.SmcWMotionStart
SmcWMotionStart.restype = ctypes.c_long
SmcWMotionStart.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWMotionStop(short DevId, short AxisNo);
SmcWMotionStop = csmc_dll.SmcWMotionStop
SmcWMotionStop.restype = ctypes.c_long
SmcWMotionStop.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWMotionDecStop(short DevId, short AxisNo);
SmcWMotionDecStop = csmc_dll.SmcWMotionDecStop
SmcWMotionDecStop.restype = ctypes.c_long
SmcWMotionDecStop.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWSetMotionChangeReady(short DevId, short AxisNo, short ChangeType);
SmcWSetMotionChangeReady = csmc_dll.SmcWSetMotionChangeReady
SmcWSetMotionChangeReady.restype = ctypes.c_long
SmcWSetMotionChangeReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetMotionChangeReady(short DevId, short AxisNo, short *ChangeType);
SmcWGetMotionChangeReady = csmc_dll.SmcWGetMotionChangeReady
SmcWGetMotionChangeReady.restype = ctypes.c_long
SmcWGetMotionChangeReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWMotionChange(short DevId, short AxisNo);
SmcWMotionChange = csmc_dll.SmcWMotionChange
SmcWMotionChange.restype = ctypes.c_long
SmcWMotionChange.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWSyncMotionStart(short DevId, short AxisNo);
SmcWSyncMotionStart = csmc_dll.SmcWSyncMotionStart
SmcWSyncMotionStart.restype = ctypes.c_long
SmcWSyncMotionStart.argtypes = [ctypes.c_short, ctypes.c_short]

#----------------------------------------
# Operation Status Read/Write Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetOutPulse(short DevId, short AxisNo, long OutPulse);
SmcWSetOutPulse = csmc_dll.SmcWSetOutPulse
SmcWSetOutPulse.restype = ctypes.c_long
SmcWSetOutPulse.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetOutPulse(short DevId, short AxisNo, long *OutPulse);
SmcWGetOutPulse = csmc_dll.SmcWGetOutPulse
SmcWGetOutPulse.restype = ctypes.c_long
SmcWGetOutPulse.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWSetCountPulse(short DevId, short AxisNo, long CountPulse);
SmcWSetCountPulse = csmc_dll.SmcWSetCountPulse
SmcWSetCountPulse.restype = ctypes.c_long
SmcWSetCountPulse.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetCountPulse(short DevId, short AxisNo, long *CountPulse);
SmcWGetCountPulse = csmc_dll.SmcWGetCountPulse
SmcWGetCountPulse.restype = ctypes.c_long
SmcWGetCountPulse.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWGetPulseStatus(short DevId, short AxisNo, short *PulseSts);
SmcWGetPulseStatus = csmc_dll.SmcWGetPulseStatus
SmcWGetPulseStatus.restype = ctypes.c_long
SmcWGetPulseStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetMoveStatus(short DevId, short AxisNo, short *MoveSts);
SmcWGetMoveStatus = csmc_dll.SmcWGetMoveStatus
SmcWGetMoveStatus.restype = ctypes.c_long
SmcWGetMoveStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetStopStatus(short DevId, short AxisNo, short *StopSts);
SmcWGetStopStatus = csmc_dll.SmcWGetStopStatus
SmcWGetStopStatus.restype = ctypes.c_long
SmcWGetStopStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetLimitStatus(short DevId, short AxisNo, short *LimitSts);
SmcWGetLimitStatus = csmc_dll.SmcWGetLimitStatus
SmcWGetLimitStatus.restype = ctypes.c_long
SmcWGetLimitStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetLatchOutPulse(short DevId, short AxisNo, long *OutPulse);
SmcWGetLatchOutPulse = csmc_dll.SmcWGetLatchOutPulse
SmcWGetLatchOutPulse.restype = ctypes.c_long
SmcWGetLatchOutPulse.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWGetLatchCountPulse(short DevId, short AxisNo, long *CountPulse);
SmcWGetLatchCountPulse = csmc_dll.SmcWGetLatchCountPulse
SmcWGetLatchCountPulse.restype = ctypes.c_long
SmcWGetLatchCountPulse.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWGetBankNo(short DevId, short AxisNo, short *BankNo);
SmcWGetBankNo = csmc_dll.SmcWGetBankNo
SmcWGetBankNo.restype = ctypes.c_long
SmcWGetBankNo.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetMoveSpeed(short DevId, short AxisNo, double *MoveSpeed);
SmcWGetMoveSpeed = csmc_dll.SmcWGetMoveSpeed
SmcWGetMoveSpeed.restype = ctypes.c_long
SmcWGetMoveSpeed.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double)]

# C Prototype: long WINAPI SmcWGetZCount(short DevId, short AxisNo, short *MoveZCount);
SmcWGetZCount = csmc_dll.SmcWGetZCount
SmcWGetZCount.restype = ctypes.c_long
SmcWGetZCount.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetCtrlInOutStatus(short DevId, short AxisNo, short *CtrlSts );
SmcWGetCtrlInOutStatus = csmc_dll.SmcWGetCtrlInOutStatus
SmcWGetCtrlInOutStatus.restype = ctypes.c_long
SmcWGetCtrlInOutStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

#----------------------------------------
# Control Signal Setting Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetAlarmClear(short DevId, short AxisNo);
SmcWSetAlarmClear = csmc_dll.SmcWSetAlarmClear
SmcWSetAlarmClear.restype = ctypes.c_long
SmcWSetAlarmClear.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWSetLimitMask(short DevId, short AxisNo, short LimitMask, short LimitMaskEnable);
SmcWSetLimitMask = csmc_dll.SmcWSetLimitMask
SmcWSetLimitMask.restype = ctypes.c_long
SmcWSetLimitMask.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetLimitMask(short DevId, short AxisNo, short *LimitMask);
SmcWGetLimitMask = csmc_dll.SmcWGetLimitMask
SmcWGetLimitMask.restype = ctypes.c_long
SmcWGetLimitMask.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetDigitalOut(short DevId, short AxisNo, short OutData, short OutDataEnable);
SmcWSetDigitalOut = csmc_dll.SmcWSetDigitalOut
SmcWSetDigitalOut.restype = ctypes.c_long
SmcWSetDigitalOut.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetDigitalOut(short DevId, short AxisNo, short *OutData);
SmcWGetDigitalOut = csmc_dll.SmcWGetDigitalOut
SmcWGetDigitalOut.restype = ctypes.c_long
SmcWGetDigitalOut.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetDigitalIn(short DevId, short AxisNo, short *InData);
SmcWGetDigitalIn = csmc_dll.SmcWGetDigitalIn
SmcWGetDigitalIn.restype = ctypes.c_long
SmcWGetDigitalIn.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetHoldOff(short DevId, short AxisNo, short HoldOff);
SmcWSetHoldOff = csmc_dll.SmcWSetHoldOff
SmcWSetHoldOff.restype = ctypes.c_long
SmcWSetHoldOff.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetHoldOff(short DevId, short AxisNo, short *HoldOff);
SmcWGetHoldOff = csmc_dll.SmcWGetHoldOff
SmcWGetHoldOff.restype = ctypes.c_long
SmcWGetHoldOff.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetErcOut(short DevId, short AxisNo, short ErcOn);
SmcWSetErcOut = csmc_dll.SmcWSetErcOut
SmcWSetErcOut.restype = ctypes.c_long
SmcWSetErcOut.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetAlarmCode(short DevId, short AxisNo, short *AlarmCode);
SmcWGetAlarmCode = csmc_dll.SmcWGetAlarmCode
SmcWGetAlarmCode.restype = ctypes.c_long
SmcWGetAlarmCode.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

#----------------------------------------
# Event Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWStopEvent(short DevId, short AxisNo, HWND hMsgWnd, short EventMode);
SmcWStopEvent = csmc_dll.SmcWStopEvent
SmcWStopEvent.restype = ctypes.c_long
SmcWStopEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.wintypes.HANDLE, ctypes.c_short]

# C Prototype: long WINAPI SmcWBankEvent(short DevId, short AxisNo, HWND hMsgWnd, short EventMode, short BankNo);
SmcWBankEvent = csmc_dll.SmcWBankEvent
SmcWBankEvent.restype = ctypes.c_long
SmcWBankEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.wintypes.HANDLE, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWCountEvent(short DevId, short AxisNo, HWND hMsgWnd, short EventMode, short CountType, long Count);
SmcWCountEvent = csmc_dll.SmcWCountEvent
SmcWCountEvent.restype = ctypes.c_long
SmcWCountEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.wintypes.HANDLE, ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long WINAPI SmcWIrqEvent(short DevId, short AxisNo, HWND hMsgWnd, short EventMode, short EventType);
SmcWIrqEvent = csmc_dll.SmcWIrqEvent
SmcWIrqEvent.restype = ctypes.c_long
SmcWIrqEvent.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.wintypes.HANDLE, ctypes.c_short, ctypes.c_short]

#----------------------------------------
# FIFOLatch Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWResetLatchFIFO(short DevId);
SmcWResetLatchFIFO = csmc_dll.SmcWResetLatchFIFO
SmcWResetLatchFIFO.restype = ctypes.c_long
SmcWResetLatchFIFO.argtypes = [ctypes.c_short]

# C Prototype: long WINAPI SmcWSetFIFOLatchSrc(short DevId, short AxisNo, short LatchAxisNo, short Enable);
SmcWSetFIFOLatchSrc = csmc_dll.SmcWSetFIFOLatchSrc
SmcWSetFIFOLatchSrc.restype = ctypes.c_long
SmcWSetFIFOLatchSrc.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetFIFOLatchSrc(short DevId, short AxisNo, short *LatchAxisNo, short *Enable);
SmcWGetFIFOLatchSrc = csmc_dll.SmcWGetFIFOLatchSrc
SmcWGetFIFOLatchSrc.restype = ctypes.c_long
SmcWGetFIFOLatchSrc.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetLatchDataFromBuffer(short DevId, short BufferNo, short *AxisCounterNo, short *LatchDataCnt, long *LatchDataTable);
SmcWGetLatchDataFromBuffer = csmc_dll.SmcWGetLatchDataFromBuffer
SmcWGetLatchDataFromBuffer.restype = ctypes.c_long
SmcWGetLatchDataFromBuffer.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWGetLatchFIFOLength(short DevId, short AxisNo, short *length);
SmcWGetLatchFIFOLength = csmc_dll.SmcWGetLatchFIFOLength
SmcWGetLatchFIFOLength.restype = ctypes.c_long
SmcWGetLatchFIFOLength.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetLatchDataFromBufferEx(short DevId, short BufferNo, short *AxisCounterNo, short *LatchDataCnt, long *LatchDataTable, short *UpCnt, short *DownCnt);
SmcWGetLatchDataFromBufferEx = csmc_dll.SmcWGetLatchDataFromBufferEx
SmcWGetLatchDataFromBufferEx.restype = ctypes.c_long
SmcWGetLatchDataFromBufferEx.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWResetAxisLatchFIFO( short DevId, short AxisBitNo, short Reserved );
SmcWResetAxisLatchFIFO = csmc_dll.SmcWResetAxisLatchFIFO
SmcWResetAxisLatchFIFO.restype = ctypes.c_long
SmcWResetAxisLatchFIFO.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWResetFIFOLatchSrc( short DevId, short AxisNo );
SmcWResetFIFOLatchSrc = csmc_dll.SmcWResetFIFOLatchSrc
SmcWResetFIFOLatchSrc.restype = ctypes.c_long
SmcWResetFIFOLatchSrc.argtypes = [ctypes.c_short, ctypes.c_short]

#----------------------------------------
# TriggerOut Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetTrgOutCPWidth( short DevId, short AxisNo, short Width );
SmcWSetTrgOutCPWidth = csmc_dll.SmcWSetTrgOutCPWidth
SmcWSetTrgOutCPWidth.restype = ctypes.c_long
SmcWSetTrgOutCPWidth.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetTrgOutCPWidth( short DevId, short AxisNo, short *Width );
SmcWGetTrgOutCPWidth = csmc_dll.SmcWGetTrgOutCPWidth
SmcWGetTrgOutCPWidth.restype = ctypes.c_long
SmcWGetTrgOutCPWidth.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetTrgOutCPDelay( short DevId, short AxisNo, short DelayTime );
SmcWSetTrgOutCPDelay = csmc_dll.SmcWSetTrgOutCPDelay
SmcWSetTrgOutCPDelay.restype = ctypes.c_long
SmcWSetTrgOutCPDelay.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetTrgOutCPDelay( short DevId, short AxisNo, short *DelayTime );
SmcWGetTrgOutCPDelay = csmc_dll.SmcWGetTrgOutCPDelay
SmcWGetTrgOutCPDelay.restype = ctypes.c_long
SmcWGetTrgOutCPDelay.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetTrgOutData (short DevId, short FifoNo, short CntType, short OutAxisEnable, long FifoData);
SmcWSetTrgOutData = csmc_dll.SmcWSetTrgOutData
SmcWSetTrgOutData.restype = ctypes.c_long
SmcWSetTrgOutData.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_long]

# C Prototype: long WINAPI SmcWTrgOutEvent (short DevId, HWND hWnd, short EventMode, short EventType);
SmcWTrgOutEvent = csmc_dll.SmcWTrgOutEvent
SmcWTrgOutEvent.restype = ctypes.c_long
SmcWTrgOutEvent.argtypes = [ctypes.c_short, ctypes.wintypes.HANDLE, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetTrgOutStatus (short DevId, short *TrgOutSts, short *TrgOutErrSts);
SmcWGetTrgOutStatus = csmc_dll.SmcWGetTrgOutStatus
SmcWGetTrgOutStatus.restype = ctypes.c_long
SmcWGetTrgOutStatus.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWResetTrgOutStatus (short DevId, short EnableStsReset, short EnableErrStsReset, short *TrgOutSts, short *TrgOutErrSts);
SmcWResetTrgOutStatus = csmc_dll.SmcWResetTrgOutStatus
SmcWResetTrgOutStatus.restype = ctypes.c_long
SmcWResetTrgOutStatus.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWGetTrgOutDataRemainNum (short DevId, short FifoNo, long *DataNum);
SmcWGetTrgOutDataRemainNum = csmc_dll.SmcWGetTrgOutDataRemainNum
SmcWGetTrgOutDataRemainNum.restype = ctypes.c_long
SmcWGetTrgOutDataRemainNum.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWResetTrgOutFIFO (short DevId, short FifoBitNo);
SmcWResetTrgOutFIFO = csmc_dll.SmcWResetTrgOutFIFO
SmcWResetTrgOutFIFO.restype = ctypes.c_long
SmcWResetTrgOutFIFO.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWSetTrgOutStart (short DevId);
SmcWSetTrgOutStart = csmc_dll.SmcWSetTrgOutStart
SmcWSetTrgOutStart.restype = ctypes.c_long
SmcWSetTrgOutStart.argtypes = [ctypes.c_short]

# C Prototype: long WINAPI SmcWSetTrgOutStop (short DevId);
SmcWSetTrgOutStop = csmc_dll.SmcWSetTrgOutStop
SmcWSetTrgOutStop.restype = ctypes.c_long
SmcWSetTrgOutStop.argtypes = [ctypes.c_short]

# C Prototype: long WINAPI SmcWSetTrgOutAxis (short DevId, short FifoNo, short CmpAxis, short OutAxis);
SmcWSetTrgOutAxis = csmc_dll.SmcWSetTrgOutAxis
SmcWSetTrgOutAxis.restype = ctypes.c_long
SmcWSetTrgOutAxis.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetTrgOutAxis (short DevId, short FifoNo, short *CmpAxis, short *OutAxis);
SmcWGetTrgOutAxis = csmc_dll.SmcWGetTrgOutAxis
SmcWGetTrgOutAxis.restype = ctypes.c_long
SmcWGetTrgOutAxis.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWResetTrgOutAxis (short DevId, short FifoBitNo);
SmcWResetTrgOutAxis = csmc_dll.SmcWResetTrgOutAxis
SmcWResetTrgOutAxis.restype = ctypes.c_long
SmcWResetTrgOutAxis.argtypes = [ctypes.c_short, ctypes.c_short]

#----------------------------------------
# Manual Pulser Functions
#----------------------------------------
# C Prototype: long WINAPI SmcWSetPulserType (short DevId, short AxisNo, short InputType, short PulserDir);
SmcWSetPulserType = csmc_dll.SmcWSetPulserType
SmcWSetPulserType.restype = ctypes.c_long
SmcWSetPulserType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulserType (short DevId, short AxisNo, short *InputType, short *PulserDir);
SmcWGetPulserType = csmc_dll.SmcWGetPulserType
SmcWGetPulserType.restype = ctypes.c_long
SmcWGetPulserType.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetPulserParam (short DevId, short AxisNo, double SpeedLimit, long Distance);
SmcWSetPulserParam = csmc_dll.SmcWSetPulserParam
SmcWSetPulserParam.restype = ctypes.c_long
SmcWSetPulserParam.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_double, ctypes.c_long]

# C Prototype: long WINAPI SmcWGetPulserParam (short DevId, short AxisNo, double *SpeedLimit, long *Distance);
SmcWGetPulserParam = csmc_dll.SmcWGetPulserParam
SmcWGetPulserParam.restype = ctypes.c_long
SmcWGetPulserParam.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_long)]

# C Prototype: long WINAPI SmcWSetPulserRatio (short DevId, short AxisNo, short Magnification, short Division);
SmcWSetPulserRatio = csmc_dll.SmcWSetPulserRatio
SmcWSetPulserRatio.restype = ctypes.c_long
SmcWSetPulserRatio.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulserRatio (short DevId, short AxisNo, short *Magnification, short *Division);
SmcWGetPulserRatio = csmc_dll.SmcWGetPulserRatio
SmcWGetPulserRatio.restype = ctypes.c_long
SmcWGetPulserRatio.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetPulserReady (short DevId, short AxisNo, short PulserMode);
SmcWSetPulserReady = csmc_dll.SmcWSetPulserReady
SmcWSetPulserReady.restype = ctypes.c_long
SmcWSetPulserReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulserReady (short DevId, short AxisNo, short *PulserMode);
SmcWGetPulserReady = csmc_dll.SmcWGetPulserReady
SmcWGetPulserReady.restype = ctypes.c_long
SmcWGetPulserReady.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWStartPulser (short DevId, short AxisNo);
SmcWStartPulser = csmc_dll.SmcWStartPulser
SmcWStartPulser.restype = ctypes.c_long
SmcWStartPulser.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWStopPulser (short DevId, short AxisNo);
SmcWStopPulser = csmc_dll.SmcWStopPulser
SmcWStopPulser.restype = ctypes.c_long
SmcWStopPulser.argtypes = [ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWSetPulserLine (short DevId, short AxisNo, short InterAxis);
SmcWSetPulserLine = csmc_dll.SmcWSetPulserLine
SmcWSetPulserLine.restype = ctypes.c_long
SmcWSetPulserLine.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulserLine (short DevId, short AxisNo, short *InterAxis);
SmcWGetPulserLine = csmc_dll.SmcWGetPulserLine
SmcWGetPulserLine.restype = ctypes.c_long
SmcWGetPulserLine.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short)]

# C Prototype: long WINAPI SmcWSetPulserArc (short DevId, short AxisNo, short InterAxis, long Center_X, long Center_Y, long End_X, long End_Y, double ArcSpeedLimit, short ArcStrtDir);
SmcWSetPulserArc = csmc_dll.SmcWSetPulserArc
SmcWSetPulserArc.restype = ctypes.c_long
SmcWSetPulserArc.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_short, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.c_short]

# C Prototype: long WINAPI SmcWGetPulserArc (short DevId, short AxisNo, short *InterAxis, long *Center_X, long *Center_Y, long *End_X, long *End_Y, double *ArcSpeedLimit, short *ArcStrtDir);
SmcWGetPulserArc = csmc_dll.SmcWGetPulserArc
SmcWGetPulserArc.restype = ctypes.c_long
SmcWGetPulserArc.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_short)]