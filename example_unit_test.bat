@echo off
REM # ============ Cleanup: remove the Output directory and all its contents ==================================
cls
del /s /q Output\*.*
del *.log
rmdir /s /q Output\

REM # ============ Input path: Get the input arguemnt path ==================================
REM set default output directory
set out="R:/Output"

del /s /q %out%*.*
del %out%*.log
rmdir /s /q %out%\

REM check if command-line argument is provided and update output directory
REM if "%1" neq "" 
REM (
  REM set out=%1
REM )

REM print output directory
echo Gloval Output directory: %out%
echo ==================================================


REM RUN in the TERMINAL: example_unit_test.bat | tee example_unit_test.log 
REM RUN in the TERMINAL: example_unit_test.bat > example_unit_test.log 


REM # ============ UNIT test: This part is a test script =====================================================
REM cls
REM : trim.py
REM python ./Image_Process_Scripts/trim.py
python ./Image_Process_Scripts/trim.py 10 20 30 40 ./Input/FX_08_VirtualDrummerSolid.png %out%/Test_trimmed_file.png
python ./Image_Process_Scripts/trim.py 11 21 31 41 %out%/Test_trimmed_file.png
python ./Image_Process_Scripts/trim.py 12 22 32 42 ./Input %out%/Test_trim_dir
python ./Image_Process_Scripts/trim.py 13 23 33 43 %out%/Test_trim_dir


REM : resize.py
REM python ./Image_Process_Scripts/resize.py
python ./Image_Process_Scripts/resize.py 300 400 ./Input/FX_08_VirtualDrummerSolid.png %out%/Test_resized_file.png
python ./Image_Process_Scripts/resize.py 390 480 %out%/Test_resized_file.png
python ./Image_Process_Scripts/resize.py 320 420 ./Input %out%/Test_resize_dir
python ./Image_Process_Scripts/resize.py 380 490 %out%/Test_resize_dir


REM : blur.py
REM python ./Image_Process_Scripts/blur.py
python ./Image_Process_Scripts/blur.py ./Input/FX_08_VirtualDrummerSolid.png  	5  %out%/Test_blur_file.png
python ./Image_Process_Scripts/blur.py %out%/Test_blur_file.png  5 
python ./Image_Process_Scripts/blur.py ./Input/ 2 %out%/Test_blur_dir         
python ./Image_Process_Scripts/blur.py %out%/Test_blur_dir   10 

REM : brightness.py
REM python ./Image_Process_Scripts/brightness.py
python ./Image_Process_Scripts/brightness.py ./Input/FX_08_VirtualDrummerSolid.png 0.5 %out%/Test_brightness_0.5_file.png
python ./Image_Process_Scripts/brightness.py %out%/Test_brightness_0.5_file.png -0.2
python ./Image_Process_Scripts/brightness.py ./Input/ 0.7 %out%/Test_brightness_0.7_dir
python ./Image_Process_Scripts/brightness.py %out%/Test_brightness_0.7_dir -0.3
python ./Image_Process_Scripts/brightness.py ./Input/FX_08_VirtualDrummerSolid.png 1.5 %out%/Test_brightness_1.5_file.png
python ./Image_Process_Scripts/brightness.py %out%/Test_brightness_1.5_file.png 0.3
python ./Image_Process_Scripts/brightness.py ./Input/ 1.2 %out%/Test_brightness_1.2_dir
python ./Image_Process_Scripts/brightness.py %out%/Test_brightness_1.2_dir 0.4


REM : rotate.py
REM python ./Image_Process_Scripts/rotate.py
python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	1  %out%/Test_rotate_1_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_1_file.png  1
python ./Image_Process_Scripts/rotate.py ./Input/ 1 %out%/Test_rotate_1_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_1_dir   1 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	-1  %out%/Test_rotate_neg1_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_neg1_file.png  -1
python ./Image_Process_Scripts/rotate.py ./Input/ -1 %out%/Test_rotate_neg1_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_neg1_dir   -1 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	5  %out%/Test_rotate_5_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_5_file.png  5
python ./Image_Process_Scripts/rotate.py ./Input/ 5 %out%/Test_rotate_5_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_5_dir   5 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	-5  %out%/Test_rotate_neg5_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_neg5_file.png  -5
python ./Image_Process_Scripts/rotate.py ./Input/ -5 %out%/Test_rotate_neg5_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_neg5_dir   -5 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	10  %out%/Test_rotate_10_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_10_file.png  10
python ./Image_Process_Scripts/rotate.py ./Input/ 10 %out%/Test_rotate_10_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_10_dir   10 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	-10  %out%/Test_rotate_neg10_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_neg10_file.png  -10
python ./Image_Process_Scripts/rotate.py ./Input/ -10 %out%/Test_rotate_neg10_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_neg10_dir   -10 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	15  %out%/Test_rotate_15_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_15_file.png  15
python ./Image_Process_Scripts/rotate.py ./Input/ 15 %out%/Test_rotate_15_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_15_dir   15 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 30 %out%/Test_rotate_30_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_30_file.png 30
python ./Image_Process_Scripts/rotate.py ./Input/ 30 %out%/Test_rotate_30_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_30_dir 30

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 45 %out%/Test_rotate_45_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_45_file.png 45
python ./Image_Process_Scripts/rotate.py ./Input/ 45 %out%/Test_rotate_45_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_45_dir 45

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 60 %out%/Test_rotate_60_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_60_file.png 60
python ./Image_Process_Scripts/rotate.py ./Input/ 60 %out%/Test_rotate_60_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_60_dir 60

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 90 %out%/Test_rotate_90_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_90_file.png 90
python ./Image_Process_Scripts/rotate.py ./Input/ 90 %out%/Test_rotate_90_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_90_dir 

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 135 %out%/Test_rotate_135_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_135_file.png 135
python ./Image_Process_Scripts/rotate.py ./Input/ 135 %out%/Test_rotate_135_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_135_dir 135

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 180 %out%/Test_rotate_180_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_180_file.png 180
python ./Image_Process_Scripts/rotate.py ./Input/ 180 %out%/Test_rotate_180_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_180_dir 180

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 270 %out%/Test_rotate_270_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_270_file.png 270
python ./Image_Process_Scripts/rotate.py ./Input/ 270 %out%/Test_rotate_270_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_270_dir 270

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png 360 %out%/Test_rotate_360_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_360_file.png 360
python ./Image_Process_Scripts/rotate.py ./Input/ 360 %out%/Test_rotate_360_dir
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_360_dir 360

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	400  %out%/Test_rotate_400_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_400_file.png  400
python ./Image_Process_Scripts/rotate.py ./Input/ 400 %out%/Test_rotate_400_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_400_dir   400

python ./Image_Process_Scripts/rotate.py ./Input/FX_08_VirtualDrummerSolid.png  	-400  %out%/Test_rotate_n400_file.png
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_n400_file.png  -400
python ./Image_Process_Scripts/rotate.py ./Input/ -400 %out%/Test_rotate_n400_dir         
python ./Image_Process_Scripts/rotate.py %out%/Test_rotate_n400_dir   -400







REM : auto_balance.py
REM python ./Image_Process_Scripts/auto_balance.py
python ./Image_Process_Scripts/auto_balance.py ./Input/FX_08_VirtualDrummerSolid.png  %out%/Test_autobalance_file.png
python ./Image_Process_Scripts/auto_balance.py %out%/Test_autobalance_file.png  
python ./Image_Process_Scripts/auto_balance.py ./Input/  								%out%/Test_auto_balance_dir         
python ./Image_Process_Scripts/auto_balance.py %out%/Test_auto_balance_dir   


REM : resize_by_ref.py
REM python ./Image_Process_Scripts/resize_by_ref.py
python ./Image_Process_Scripts/resize_by_ref.py ./Input/FX_06_ReaSynth.png 		   ./Input/FX_08_VirtualDrummerSolid.png 		%out%/Test_resized_by_ref_file_image.png
python ./Image_Process_Scripts/resize_by_ref.py ./Input/FX_07_Resamplamatic5000.png. %out%/Test_resized_by_ref_file_image.png
python ./Image_Process_Scripts/resize_by_ref.py ./Input/FX_06_ReaSynth.png 		   ./Input 										%out%/Test_resize_by_ref_file_dir
python ./Image_Process_Scripts/resize_by_ref.py ./Input/FX_07_Resamplamatic5000.png  %out%/Test_resize_by_ref_file_dir
REM TODO:	!!!!!! REM python ./Image_Process_Scripts/resize_by_ref.py %out%/Test_resize_by_ref_file_dir %out%/Test_trim_dir						./Test_resize_by_ref_file_one2one_dir
REM TODO:	!!!!!! REM python ./Image_Process_Scripts/resize_by_ref.py %out%/Test_resize_by_ref_file_dir %out%/Test_trim_dir						./Test_resize_by_ref_file_one2one_dir


REM : append.py
REM python ./Image_Process_Scripts/append.py
python ./Image_Process_Scripts/append.py -v %out%/test_append_file_h.png ./Input/FX_08_VirtualDrummerSolid.png 3
python ./Image_Process_Scripts/append.py -v %out%/test_append_file_h2.png ./Input/FX_06_ReaSynth.png ./Input/FX_07_Resamplamatic5000.png ./Input/FX_08_VirtualDrummerSolid.png
python ./Image_Process_Scripts/append.py -h %out%/test_append_file_v.png ./Input/FX_08_VirtualDrummerSolid.png 3
python ./Image_Process_Scripts/append.py -h %out%/test_append_file_v2.png ./Input/FX_06_ReaSynth.png ./Input/FX_07_Resamplamatic5000.png ./Input/FX_08_VirtualDrummerSolid.png
python ./Image_Process_Scripts/append.py -h %out%/Test_Append_1_h ./Input/ 1
python ./Image_Process_Scripts/append.py -h %out%/Test_Append_2_h ./Input/ 2
python ./Image_Process_Scripts/append.py -h %out%/Test_Append_3_h ./Input/ 3
python ./Image_Process_Scripts/append.py -h %out%/Test_Append_4_h ./Input/ 4
python ./Image_Process_Scripts/append.py -h %out%/Test_Append_5_h ./Input/ 5
python ./Image_Process_Scripts/append.py -v %out%/Test_Append_1_v ./Input/ 1
python ./Image_Process_Scripts/append.py -v %out%/Test_Append_2_v ./Input/ 2
python ./Image_Process_Scripts/append.py -v %out%/Test_Append_3_v ./Input/ 3
python ./Image_Process_Scripts/append.py -v %out%/Test_Append_4_v ./Input/ 4
python ./Image_Process_Scripts/append.py -v %out%/Test_Append_5_v ./Input/ 5
python ./Image_Process_Scripts/append.py -v %out%/Test_append_Combined_v %out%/Test_auto_balance_dir/ %out%/Test_blur_dir/ %out%/Test_resize_by_ref_file_dir %out%/Test_resize_dir  %out%/Test_trim_dir
python ./Image_Process_Scripts/append.py -h %out%/Test_append_Combined_h %out%/Test_auto_balance_dir/ %out%/Test_blur_dir/ %out%/Test_resize_by_ref_file_dir %out%/Test_resize_dir 	%out%/Test_trim_dir

