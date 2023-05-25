#================================================================
#================================================================
# API-SMC(WDM)
# basemoveサンプル
#                                                CONTEC Co., Ltd.
#================================================================
#================================================================

import ctypes
import ctypes.wintypes
import sys
import csmc

#================================================================
# マクロ定義
#================================================================
CSMC_PTP = 1
CSMC_JOG = 2
CSMC_ORG = 3
CSMC_CW = 0
CSMC_CCW = 1
CSMC_ABS = 0
CSMC_INC = 1


#================================================================
# 外部変数
#================================================================
smc_id          = ctypes.c_short(0)
axis_no         = ctypes.c_short(0)
resolve_speed   = ctypes.c_double(0)
start_speed     = ctypes.c_double(0)
target_speed    = ctypes.c_double(0)
accel_time      = ctypes.c_double(0)
decel_time      = ctypes.c_double(0)
s_speed         = ctypes.c_double(0)
coordinate      = ctypes.c_short(0)
distance        = ctypes.c_int(0)
motion_type     = ctypes.c_short(0)
start_dir       = ctypes.c_short(0)
change          = ctypes.c_short(0)


#================================================================
# 文字列を浮動小数型データに変換できるかどうか確認する関数
#================================================================
def isfloat(str):
    try:
        float(str)
    except:
        return False
    return True


#================================================================
# パラメータ設定
#================================================================
def set_move_param():
    global smc_id, axis_no, resolve_speed, start_speed, target_speed, accel_time, decel_time, s_speed, coordinate, distance, motion_type, start_dir
    err_str = ctypes.create_string_buffer(256)

    #----------------------------------------
    # 速度分解能を設定
    #----------------------------------------
    lret = csmc.SmcWSetResolveSpeed(smc_id, axis_no, resolve_speed)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetResolveSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # パルス出力開始速度を設定
    #----------------------------------------
    lret = csmc.SmcWSetStartSpeed(smc_id, axis_no, start_speed)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetStartSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # パルス出力目標速度を設定
    #----------------------------------------
    lret = csmc.SmcWSetTargetSpeed(smc_id, axis_no, target_speed)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetTargetSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # 加速時間を設定
    #----------------------------------------
    lret = csmc.SmcWSetAccelTime(smc_id, axis_no, accel_time)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetAccelTime = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # 減速時間を設定
    #----------------------------------------
    lret = csmc.SmcWSetDecelTime(smc_id, axis_no, decel_time)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetDecelTime = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # S字区間を設定
    #----------------------------------------
    lret = csmc.SmcWSetSSpeed(smc_id, axis_no, s_speed)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetSSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # モータの停止位置を設定
    #----------------------------------------
    if motion_type.value == CSMC_PTP and coordinate.value == CSMC_INC:
        distance.value = abs(distance.value)
        if start_dir.value == CSMC_CCW:
            distance.value = -1 * (distance.value)
    lret = csmc.SmcWSetStopPosition(smc_id, axis_no, coordinate, distance)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetStopPosition = {lret}: {err_str.value.decode('sjis')}")
        return -1
    return 0


#================================================================
# パラメータ取得
#================================================================
def get_move_param():
    global smc_id, axis_no, resolve_speed, start_speed, target_speed, accel_time, decel_time, s_speed, coordinate, distance
    err_str = ctypes.create_string_buffer(256)

    #----------------------------------------
    # 速度分解能を取得
    #----------------------------------------
    lret = csmc.SmcWGetResolveSpeed(smc_id, axis_no, ctypes.byref(resolve_speed))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetResolveSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # パルス出力開始速度を取得
    #----------------------------------------
    lret = csmc.SmcWGetStartSpeed(smc_id, axis_no, ctypes.byref(start_speed))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetStartSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # パルス出力目標速度を取得
    #----------------------------------------
    lret = csmc.SmcWGetTargetSpeed(smc_id, axis_no, ctypes.byref(target_speed))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetTargetSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # 加速時間を取得
    #----------------------------------------
    lret = csmc.SmcWGetAccelTime(smc_id, axis_no, ctypes.byref(accel_time))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetAccelTime = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # 減速時間を取得
    #----------------------------------------
    lret = csmc.SmcWGetDecelTime(smc_id, axis_no, ctypes.byref(decel_time))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetDecelTime = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # S字区間を取得
    #----------------------------------------
    lret = csmc.SmcWGetSSpeed(smc_id, axis_no, ctypes.byref(s_speed))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetSSpeed = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # モータの停止位置を取得
    #----------------------------------------
    lret = csmc.SmcWGetStopPosition(smc_id, axis_no, coordinate, ctypes.byref(distance))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWGetStopPosition = {lret}: {err_str.value.decode('sjis')}")
        return -1
    return 0


#================================================================
# パラメータ表示
#================================================================
def disp_move_param():
    print("\nパラメータ-------------------------------")
    #----------------------------------------
    # 速度分解能を表示
    #----------------------------------------
    print(f"【速度分解能】:\t\t\t: {resolve_speed.value:.1f}[PPS]")
    #----------------------------------------
    # パルス出力開始速度を表示
    #----------------------------------------
    print(f"【パルス出力開始速度】:\t\t: {start_speed.value:.1f}[PPS]")
    #----------------------------------------
    # パルス出力目標速度を表示
    #----------------------------------------
    print(f"【パルス出力目標速度】:\t\t: {target_speed.value:.1f}[PPS]")
    #----------------------------------------
    # 加速時間を表示
    #----------------------------------------
    print(f"【加速時間】:\t\t\t: {accel_time.value:.1f}[ms]")
    #----------------------------------------
    # 減速時間を表示
    #----------------------------------------
    print(f"【減速時間】:\t\t\t: {decel_time.value:.1f}[ms]")
    #----------------------------------------
    # S字区間を表示
    #----------------------------------------
    print(f"【S字区間】:\t\t\t: {s_speed.value:.1f}[PPS]")
    #----------------------------------------
    # モータの停止位置を表示
    #----------------------------------------
    print(f"【モータの停止位置】:\t\t: {distance.value}[pulse]")
    print("-----------------------------------------")


#================================================================
# モータ停止位置を設定
#================================================================
def set_stop_position():
    global coordinate, distance

    #----------------------------------------
    # 設定変更
    #----------------------------------------
    while True:
        print("\n【モーター停止位置設定メニュー】---------")
        print("  1:絶対座標")
        print("  2:相対座標")
        print("  q:戻る")
        print("-----------------------------------------")
        menu = input("番号を入力してください。:")
        if menu == '1':
            coordinate.value = CSMC_ABS
            menu = input("停止位置を入力してください。[pulse]:")
            #----------------------------------------
            # 入力データが数値かを確認
            #----------------------------------------
            if menu.isdigit() != True:
                continue
            distance.value = int(menu)
            break
        if menu == '2':
            coordinate.value = CSMC_INC
            menu = input("停止位置を入力してください。[pulse]:")
            #----------------------------------------
            # 入力データが数値かを確認
            #----------------------------------------
            if menu.isdigit() != True:
                continue
            distance.value = int(menu)
            break
        if menu == 'q':
            break


#================================================================
# パラメータ設定用メニュー
#================================================================
def param_main():
    global smc_id, axis_no, resolve_speed, start_speed, target_speed, accel_time, decel_time, s_speed

    #----------------------------------------
    # 設定変更
    #----------------------------------------
    while True:
        print("\n【パラメータ設定メニュー】---------------")
        print("  1:速度分解能")
        print("  2:パルス出力開始速度")
        print("  3:パルス出力目標速度")
        print("  4:加速時間")
        print("  5:減速時間")
        print("  6:S字区間")
        print("  7:停止位置")
        print("  q:戻る")
        print("-----------------------------------------")
        menu = input("番号を入力してください。:")
        if menu == '1':
            while True:
                menu = input("速度分解能を入力してください。[PPS]:")
                #----------------------------------------
                # 入力データが浮動小数型データかを確認
                #----------------------------------------
                if isfloat(menu) != True:
                    continue
                resolve_speed.value = float(menu)
                break
        if menu == '2':
            while True:
                menu = input("パルス出力開始速度を入力してください。[PPS]:")
                #----------------------------------------
                # 入力データが浮動小数型データかを確認
                #----------------------------------------
                if isfloat(menu) != True:
                    continue
                start_speed.value = float(menu)
                break
        if menu == '3':
            while True:
                menu = input("パルス出力目標速度を入力してください。[PPS]:")
                #----------------------------------------
                # 入力データが浮動小数型データかを確認
                #----------------------------------------
                if isfloat(menu) != True:
                    continue
                target_speed.value = float(menu)
                break
        if menu == '4':
            while True:
                menu = input("加速時間を入力してください。[ms]:")
                #----------------------------------------
                # 入力データが浮動小数型データかを確認
                #----------------------------------------
                if isfloat(menu) != True:
                    continue
                accel_time.value = float(menu)
                break
        if menu == '5':
            while True:
                menu = input("減速時間を入力してください。[ms]:")
                #----------------------------------------
                # 入力データが浮動小数型データかを確認
                #----------------------------------------
                if isfloat(menu) != True:
                    continue
                decel_time.value = float(menu)
                break
        if menu == '6':
            while True:
                menu = input("S字区間を入力してください。[PPS]:")
                #----------------------------------------
                # 入力データが浮動小数型データかを確認
                #----------------------------------------
                if isfloat(menu) != True:
                    continue
                s_speed.value = float(menu)
                break
        if menu == '7':
            set_stop_position()
        if menu == 'q':
            #----------------------------------------
            # 終了
            #----------------------------------------
            break


#================================================================
# モーションタイプ設定
#================================================================
def set_motion_type():
    global motion_type

    #----------------------------------------
    # 設定変更
    #----------------------------------------
    while True:
        print("\n【モーションタイプ設定メニュー】---------")
        print("  1:PTP動作")
        print("  2:JOG動作")
        print("  3:原点復帰動作")
        print("  q:戻る")
        print("-----------------------------------------")
        menu = input("番号を入力してください。:")
        if menu == '1':
            motion_type.value = CSMC_PTP
            break
        if menu == '2':
            motion_type.value = CSMC_JOG
            break
        if menu == '3':
            motion_type.value = CSMC_ORG
            break
        #----------------------------------------
        # 終了
        #----------------------------------------
        if menu == 'q':
            return -1
    return 0


#================================================================
# CW
#================================================================
def cw_motion():
    global smc_id, axis_no, motion_type, start_dir
    err_str = ctypes.create_string_buffer(256)

    start_dir.value = CSMC_CW
    lret = set_motion_type()
    if lret != 0:
        return -1
    #----------------------------------------
    # パラメータをドライバに設定
    #----------------------------------------
    lret = set_move_param()
    if lret != 0:
        return -1
    #----------------------------------------
    # 基本動作の開始準備
    #----------------------------------------
    lret = csmc.SmcWSetReady(smc_id, axis_no, motion_type, start_dir)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetReady = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # モータ動作を開始
    #----------------------------------------
    lret = csmc.SmcWMotionStart(smc_id, axis_no)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWMotionStart = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # ドライバからパラメータを取得
    #----------------------------------------
    lret = get_move_param()
    if lret != 0:
        return -1
    return 0


#================================================================
# CCW
#================================================================
def ccw_motion():
    global smc_id, axis_no, motion_type, start_dir
    err_str = ctypes.create_string_buffer(256)

    start_dir.value = CSMC_CCW
    lret = set_motion_type()
    if lret != 0:
        return -1
    #----------------------------------------
    # パラメータをドライバに設定
    #----------------------------------------
    lret = set_move_param()
    if lret != 0:
        return -1
    #----------------------------------------
    # 基本動作の開始準備
    #----------------------------------------
    lret = csmc.SmcWSetReady(smc_id, axis_no, motion_type, start_dir)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetReady = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # モータ動作を開始
    #----------------------------------------
    lret = csmc.SmcWMotionStart(smc_id, axis_no)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWMotionStart = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # ドライバからパラメータを取得
    #----------------------------------------
    lret = get_move_param()
    if lret != 0:
        return -1
    return 0


#================================================================
# 動作変更
#================================================================
def change_motion():
    global smc_id, axis_no, resolve_speed, start_speed, target_speed, accel_time, decel_time, s_speed, coordinate, distance
    err_str = ctypes.create_string_buffer(256)

    change.value = 4
    #----------------------------------------
    # 設定変更
    #----------------------------------------
    while True:
        print("\n【モータ動作変更タイプメニュー】---------")
        print("  1:瞬時に開始速度(FL速度)へ変更")
        print("  2:瞬時に目標速度(FH速度)へ変更")
        print("  3:減速して開始速度(FL速度)へ変更")
        print("  4:加速して目標速度(FH速度)へ変更")
        print("  5:動作速度と加減速時間を変更")
        print("  6:モータ停止位置変更")
        print("  7:PCS信号によるモータ停止位置変更")
        print("  q:戻る")
        print("-----------------------------------------")
        menu = input("番号を入力してください。:")
        #----------------------------------------
        # 瞬時に開始速度(FL速度)へ変更
        #----------------------------------------
        if menu == '1':
            change.value = 0
            break
        #----------------------------------------
        # 瞬時に目標速度(FH速度)へ変更
        #----------------------------------------
        if menu == '2':
            change.value = 1
            break
        #----------------------------------------
        # 減速して開始速度(FL速度)へ変更
        #----------------------------------------
        if menu == '3':
            change.value = 2
            break
        #----------------------------------------
        # 加速して目標速度(FH速度)へ変更
        #----------------------------------------
        if menu == '4':
            change.value = 3
            break
        #----------------------------------------
        # 動作速度と加減速時間を変更
        #----------------------------------------
        if menu == '5':
            change.value = 4
            break
        #----------------------------------------
        # モータ停止位置変更 (目標位置オーバーライド１)
        #----------------------------------------
        if menu == '6':
            change.value = 5
            break
        #----------------------------------------
        # PCS信号によるモータ停止位置変更設定 (目標位置オーバーライド２)
        #----------------------------------------
        if menu == '7':
            change.value = 6
            break
        #----------------------------------------
        # 終了
        #----------------------------------------
        if menu == 'q':
            return -1
    if change.value == 4:
        #----------------------------------------
        # パルス出力目標速度を設定
        #----------------------------------------
        lret = csmc.SmcWSetTargetSpeed(smc_id, axis_no, target_speed)
        if lret != 0:
            csmc.SmcWGetErrorString(lret, err_str)
            print(f"SmcWSetTargetSpeed = {lret}: {err_str.value.decode('sjis')}")
            return -1
        #----------------------------------------
        # 加速時間を設定
        #----------------------------------------
        lret = csmc.SmcWSetAccelTime(smc_id, axis_no, accel_time)
        if lret != 0:
            csmc.SmcWGetErrorString(lret, err_str)
            print(f"SmcWSetAccelTime = {lret}: {err_str.value.decode('sjis')}")
            return -1
        #----------------------------------------
        # 減速時間を設定
        #----------------------------------------
        lret = csmc.SmcWSetDecelTime(smc_id, axis_no, decel_time)
        if lret != 0:
            csmc.SmcWGetErrorString(lret, err_str)
            print(f"SmcWSetDecelTime = {lret}: {err_str.value.decode('sjis')}")
            return -1
    if change.value == 5 or change.value == 6:
        #----------------------------------------
        # モータの停止位置を設定
        #----------------------------------------
        if motion_type.value == CSMC_PTP and coordinate.value == CSMC_INC:
            distance.value = abs(distance.value)
            if start_dir.value == CSMC_CCW:
                distance.value = -1 * (distance.value)
        lret = csmc.SmcWSetStopPosition(smc_id, axis_no, coordinate, distance)
        if lret != 0:
            csmc.SmcWGetErrorString(lret, err_str)
            print(f"SmcWSetStopPosition = {lret}: {err_str.value.decode('sjis')}")
            return -1
    #----------------------------------------
    # モータ動作変更タイプを設定
    #----------------------------------------
    lret = csmc.SmcWSetMotionChangeReady(smc_id, axis_no, change)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetMotionChangeReady = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # 動作変更
    #----------------------------------------
    lret = csmc.SmcWMotionChange(smc_id, axis_no)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWMotionChange = {lret}: {err_str.value.decode('sjis')}")
        return -1
    #----------------------------------------
    # ドライバからパラメータを取得
    #----------------------------------------
    lret = get_move_param()
    if lret != 0:
        return -1
    return 0


#================================================================
# 減速停止
#================================================================
def sd_stop_motion():
    global smc_id, axis_no
    err_str = ctypes.create_string_buffer(256)

    lret = csmc.SmcWMotionDecStop(smc_id, axis_no)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWMotionDecStop = {lret}: {err_str.value.decode('sjis')}")
        return -1
    return 0


#================================================================
# 停止
#================================================================
def stop_motion():
    global smc_id, axis_no
    err_str = ctypes.create_string_buffer(256)

    lret = csmc.SmcWMotionStop(smc_id, axis_no)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWMotionStop = {lret}: {err_str.value.decode('sjis')}")
        return -1
    return 0


#================================================================
# main関数
#================================================================
def main():
    global smc_id, axis_no, motion_type, coordinate, distance
    err_str = ctypes.create_string_buffer(256)

    motion_type.value = CSMC_PTP
    coordinate.value = CSMC_INC
    distance.value = 1000
    #----------------------------------------
    # タイトルの表示
    #----------------------------------------
    print("----------------------------------")
    print("<<< basemoveサンプル >>>")
    print("----------------------------------")
    #----------------------------------------
    # デバイス名の入力確認
    #----------------------------------------
    device_name = input("使用するボードのデバイス名を入力してください。\nデバイス名:")
    #----------------------------------------
    # デバイスの初期化
    #----------------------------------------
    lret = csmc.SmcWInit(device_name.encode(), ctypes.byref(smc_id))
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWInit = {lret}: {err_str.value.decode('sjis')}")
        sys.exit()
    axis_no.value = 1
    lret = csmc.SmcWSetStopPosition(smc_id, axis_no, coordinate, distance)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWSetStopPosition = {lret}: {err_str.value.decode('sjis')}")
        sys.exit()
    #----------------------------------------
    # パラメータ取得
    #----------------------------------------
    lret = get_move_param()
    if lret != 0:
        sys.exit()
    #----------------------------------------
    # 設定変更
    #----------------------------------------
    while True:
        print("\n【基本動作メニュー】---------------------")
        print("  1:軸の変更")
        print("  2:パラメータ表示")
        print("  3:パラメータ変更")
        print("  4:CW方向に動作")
        print("  5:CCW方向に動作")
        print("  6:動作変更")
        print("  7:停止")
        print("  8:減速停止")
        print("  q:終了")
        print("-----------------------------------------")
        menu = input("番号を入力してください。:")
        #----------------------------------------
        # 軸の変更
        #----------------------------------------
        if menu == '1':
            while True:
                menu = input("軸番号を入力してください。:")
                #----------------------------------------
                # 入力データが数値かを確認
                #----------------------------------------
                if menu.isdigit() == True:
                    axis_no.value = int(menu)
                    if axis_no.value < 1:
                        continue
                    else:
                        break
            continue
        #----------------------------------------
        # パラメータ表示
        #----------------------------------------
        if menu == '2':
            disp_move_param()
        #----------------------------------------
        # パラメータ設定
        #----------------------------------------
        if menu == '3':
            param_main()
        #----------------------------------------
        # CW
        #----------------------------------------
        if menu == '4':
            cw_motion()
        #----------------------------------------
        # CCW
        #----------------------------------------
        if menu == '5':
            ccw_motion()
        #----------------------------------------
        # 動作変更
        #----------------------------------------
        if menu == '6':
            change_motion()
        #----------------------------------------
        # 停止
        #----------------------------------------
        if menu == '7':
            stop_motion()
        #----------------------------------------
        # SD停止
        #----------------------------------------
        if menu == '8':
            sd_stop_motion()
        #----------------------------------------
        # 終了
        #----------------------------------------
        if menu == 'q':
            break
    #----------------------------------------
    # デバイスの終了処理
    #---------------------------------------- 
    lret = csmc.SmcWExit(smc_id)
    if lret != 0:
        csmc.SmcWGetErrorString(lret, err_str)
        print(f"SmcWExit = {lret}: {err_str.value.decode('sjis')}")
        sys.exit()
    #----------------------------------------
    # アプリケーション終了
    #----------------------------------------
    sys.exit()


#----------------------------------------
# main関数呼び出し
#----------------------------------------
if __name__ == "__main__":
    main()
