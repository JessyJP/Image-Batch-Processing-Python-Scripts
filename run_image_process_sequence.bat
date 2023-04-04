@echo off
REM # ============ Cleanup: remove the Output directory and all its contents ==================================
cls
del /s /q Output\*.*
rmdir /s /q Output\

REM # ============ Main Sequence ==============================================================================
REM python ./Image_Process_Scripts/trim.py 	71 1 2 1 		./Input/ 		 ./Output/Step_1_NoWindowBorders/
REM python ./Image_Process_Scripts/blur.py  	./Output/Step_2_blur/  ./Output/Step_1_NoWindowBorders/  10

REM python ./Image_Process_Scripts/adjust_colour_balance.py 0 0 0 ./Output/Step_1_NoWindowBorders ./Output/Step2_B
REM python ./Image_Process_Scripts/append.py -h 				./Output/Combined 		 ./Output/Step_1_NoWindowBorders 3
REM python ./Image_Process_Scripts/resize.py 	300 200  		./Output/Step_1_NoWindowBorders/  ./Output/Step_1_NoWindowBorders/


