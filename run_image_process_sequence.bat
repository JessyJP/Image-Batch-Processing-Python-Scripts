@echo off
REM # ============ Cleanup: remove the Output directory and all its contents ==================================
cls
del /s /q Output\*.*
rmdir /s /q Output\

REM # ============ Main Sequence ==============================================================================
REM python ./Image_Process_Scripts/image_trim.py 	71 1 2 1 		./Input/ 		 ./Output/Step_1_NoWindowBorders/
REM python ./Image_Process_Scripts/image_blur.py  	./Output/Step_2_blur/  ./Output/Step_1_NoWindowBorders/  10

REM python ./Image_Process_Scripts/image_adjust_colour_balance.py 0 0 0 ./Output/Step_1_NoWindowBorders ./Output/Step2_B
REM python ./Image_Process_Scripts/image_append.py -h 				./Output/Combined 		 ./Output/Step_1_NoWindowBorders 3
REM python ./Image_Process_Scripts/image_resize.py 	300 200  		./Output/Step_1_NoWindowBorders/  ./Output/Step_1_NoWindowBorders/


REM # ============ UNIT test: This part is a test script =====================================================
REM cls
REM : image_trim.py
REM python ./Image_Process_Scripts/image_trim.py
python ./Image_Process_Scripts/image_trim.py 10 20 30 40 ./Input/FX_08_VirtualDrummerSolid.png ./Output/Test_trimmed_file.png
python ./Image_Process_Scripts/image_trim.py 11 21 31 41 ./Output/Test_trimmed_file.png
python ./Image_Process_Scripts/image_trim.py 12 22 32 42 ./Input Output/Test_trim_dir
python ./Image_Process_Scripts/image_trim.py 13 23 33 43 ./Output/Test_trim_dir


REM : image_resize.py
REM python ./Image_Process_Scripts/image_resize.py
python ./Image_Process_Scripts/image_resize.py 300 400 ./Input/FX_08_VirtualDrummerSolid.png ./Output/Test_resized_file.png
python ./Image_Process_Scripts/image_resize.py 390 480 ./Output/Test_resized_file.png
python ./Image_Process_Scripts/image_resize.py 320 420 ./Input Output/Test_resize_dir
python ./Image_Process_Scripts/image_resize.py 380 490 ./Output/Test_resize_dir


REM : image_blur.py
REM python ./Image_Process_Scripts/image_blur.py
python ./Image_Process_Scripts/image_blur.py ./Input/FX_08_VirtualDrummerSolid.png  	5  ./Output/Test_blur_file.png
python ./Image_Process_Scripts/image_blur.py ./Output/Test_blur_file.png  5 
python ./Image_Process_Scripts/image_blur.py ./Input/ 2 ./Output/Test_blur_dir         
python ./Image_Process_Scripts/image_blur.py ./Output/Test_blur_dir   10 

REM : image_auto_balance.py
REM python ./Image_Process_Scripts/image_auto_balance.py
python ./Image_Process_Scripts/image_auto_balance.py ./Input/FX_08_VirtualDrummerSolid.png  ./Output/Test_autobalance_file.png
python ./Image_Process_Scripts/image_auto_balance.py ./Output/Test_autobalance_file.png  
python ./Image_Process_Scripts/image_auto_balance.py ./Input/  								./Output/Test_auto_balance_dir         
python ./Image_Process_Scripts/image_auto_balance.py ./Output/Test_auto_balance_dir   


REM : image_resize_by_ref.py
REM python ./Image_Process_Scripts/image_resize_by_ref.py
python ./Image_Process_Scripts/image_resize_by_ref.py ./Input/FX_06_ReaSynth.png 		   ./Input/FX_08_VirtualDrummerSolid.png 		./Output/Test_resized_by_ref_file_image.png
python ./Image_Process_Scripts/image_resize_by_ref.py ./Input/FX_07_Resamplamatic5000.png. ./Output/Test_resized_by_ref_file_image.png
python ./Image_Process_Scripts/image_resize_by_ref.py ./Input/FX_06_ReaSynth.png 		   ./Input 										./Output/Test_resize_by_ref_file_dir
python ./Image_Process_Scripts/image_resize_by_ref.py ./Input/FX_07_Resamplamatic5000.png  ./Output/Test_resize_by_ref_file_dir
REM python ./Image_Process_Scripts/image_resize_by_ref.py ./Output/Test_resize_by_ref_file_dir ./Output/Test_trim_dir						./Test_resize_by_ref_file_one2one_dir
REM python ./Image_Process_Scripts/image_resize_by_ref.py ./Output/Test_resize_by_ref_file_dir ./Output/Test_trim_dir						./Test_resize_by_ref_file_one2one_dir


REM : image_append.py
REM python ./Image_Process_Scripts/image_append.py
REM python ./Image_Process_Scripts/image_append.py -h test1.png i1.png 3
REM python ./Image_Process_Scripts/image_append.py -v test2.png i1.png 3
REM python ./Image_Process_Scripts/image_append.py -v test3.png i1.png i2.png i3.png 
REM python ./Image_Process_Scripts/image_append.py -v test4.png i2.png i2.png  
REM python ./Image_Process_Scripts/image_append.py -h ./Output/test1 ./Output/Step_1_NoWindowBorders 5
REM python ./Image_Process_Scripts/image_append.py -v ./Output/test2 ./Output/Step_1_NoWindowBorders 4
REM python ./Image_Process_Scripts/image_append.py -v ./Output/test3 ./Output/Step_1_NoWindowBorders/ ./Output/Step2_B/ ./Output/Step_1_NoWindowBorders ./Output/Step2_B


REM python ./Image_Process_Scripts/image_auto_balance.py test1.png balance.png