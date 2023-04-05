@echo off
REM # ============ Cleanup: remove the Output directory and all its contents ==================================
cls
del /s /q Output\*.*
del *.log
rmdir /s /q Output\

REM # ============ Input path: Get the input arguemnt path ==================================
REM set default output directory
set imod="./Image_Process_Scripts"
set in="./Input"
set out="R:/Output"

REM Example Single Images
set A="FX_08_VirtualDrummerSolid.png"
set B="FX_07_Resamplamatic5000.png"
set C="FX_06_ReaSynth.png"

del /s /q %out%*.*
del %out%*.log
rmdir /s /q %out%\

REM check if command-line argument is provided and update output directory
REM TODO:::   	if "%1" neq "" 
REM TODO:::   	(
REM TODO:::   	  set out=%1
REM TODO:::   	)

REM print output directory
echo Gloval Output directory: %out%
echo ==================================================


REM RUN in the TERMINAL: example_unit_test.bat | tee example_unit_test.log 
REM RUN in the TERMINAL: example_unit_test.bat > example_unit_test.log 


REM # ============ UNIT test: This part is a test script =====================================================
REM cls
REM : trim.py
REM python %imod%/trim.py
python %imod%/trim.py 10 20 30 40 %in%/%A% %out%/Test_trimmed_file.png
python %imod%/trim.py 11 21 31 41 %out%/Test_trimmed_file.png
python %imod%/trim.py 12 22 32 42 %in% %out%/Test_trim_dir
python %imod%/trim.py 13 23 33 43 %out%/Test_trim_dir


REM : resize.py
REM python %imod%/resize.py
python %imod%/resize.py 300 400 %in%/%A% %out%/Test_resized_file.png
python %imod%/resize.py 390 480 %out%/Test_resized_file.png
python %imod%/resize.py 320 420 %in% %out%/Test_resize_dir
python %imod%/resize.py 380 490 %out%/Test_resize_dir


REM : blur.py
REM python %imod%/blur.py
python %imod%/blur.py %in%/%A%  	5  %out%/Test_blur_file.png
python %imod%/blur.py %out%/Test_blur_file.png  5 
python %imod%/blur.py %in%/ 2 %out%/Test_blur_dir         
python %imod%/blur.py %out%/Test_blur_dir   10 


REM : convert.py
REM TODO:: THE some formats are not supported! 
REM # formats = ["JPG", "JPEG",  "EPS",  "MPO", "SVG", "PDF","PSD","XCF","RAW"]# NOT SUPPORTED
REM python %imod%/convert.py
python %imod%/convert.py %in%/%A% 						BMP 	%out%/Test_Convert_bmp_file.bmp
python %imod%/convert.py %out%/Test_Convert_bmp_file.bmp 		PNG 	
python %imod%/convert.py %in%/ 							BMP 	%out%/Test_Convert_bmp_dir
python %imod%/convert.py %out%/Test_Convert_bmp_dir/ 			PNG 	
REM Test case set for EPS
REM python %imod%/convert.py %in%/%A% 						EPS 	%out%/Test_Convert_eps_file.eps
REM python %imod%/convert.py %out%/Test_Convert_eps_file.eps 		PNG 	
REM python %imod%/convert.py %in%/ 							EPS 	%out%/Test_Convert_eps_dir 	
REM python %imod%/convert.py %out%/Test_Convert_eps_dir/ 			PNG 	
REM Test case set for GIF	
python %imod%/convert.py %in%/%A% 						GIF 	%out%/Test_Convert_gif_file.gif
python %imod%/convert.py %out%/Test_Convert_gif_file.gif 		PNG 	
python %imod%/convert.py %in%/ 							GIF 	%out%/Test_Convert_gif_dir	
python %imod%/convert.py %out%/Test_Convert_gif_dir/ 			PNG 	
REM Test case set for ICO	
python %imod%/convert.py %in%/%A% 						ICO 	%out%/Test_Convert_ico_file.ico
python %imod%/convert.py %out%/Test_Convert_ico_file.ico 		PNG 	
python %imod%/convert.py %in%/ 							ICO 	%out%/Test_Convert_ico_dir 		
python %imod%/convert.py %out%/Test_Convert_ico_dir/ 			PNG 	
REM Test case set for JPEG
REM python %imod%/convert.py %in%/%A% 						JPEG 	%out%/Test_Convert_jpeg_file.jpeg
REM python %imod%/convert.py %out%/Test_Convert_jpeg_file.jpeg 		PNG 	
REM python %imod%/convert.py %in%/ 							JPEG 	%out%/Test_Convert_jpeg_dir
REM python %imod%/convert.py %out%/Test_Convert_jpeg_dir/ 			PNG 	
REM Test case set for MPO
REM python %imod%/convert.py %in%/%A% 						MPO 	%out%/Test_Convert_mpo_file.mpo
REM python %imod%/convert.py %out%/Test_Convert_mpo_file.mpo 		PNG 	
REM python %imod%/convert.py %in%/ 							MPO 	%out%/Test_Convert_mpo_dir	
REM python %imod%/convert.py %out%/Test_Convert_mpo_dir/ 			PNG 	
REM Test case set for TIFF (Tagged Image File Format)
python %imod%/convert.py %in%/%A% 						TIFF 	%out%/Test_Convert_tiff_file.tiff
python %imod%/convert.py %out%/Test_Convert_tiff_file.tiff 		PNG 	
python %imod%/convert.py %in%/ 							TIFF 	%out%/Test_Convert_tiff_dir	
python %imod%/convert.py %out%/Test_Convert_tiff_dir/ 			PNG 	
REM WEBP (Web Picture Format)
python %imod%/convert.py %in%/%A% 						WEBP 	%out%/Test_Convert_webp_file.webp
python %imod%/convert.py %out%/Test_Convert_webp_file.webp 		PNG 	
python %imod%/convert.py %in%/ 							WEBP 	%out%/Test_Convert_webp_dir
python %imod%/convert.py %out%/Test_Convert_webp_dir/ 			PNG 	
REM SVG (Scalable Vector Graphics)
REM python %imod%/convert.py %in%/%A% 						SVG 	%out%/Test_Convert_svg_file.svg
REM python %imod%/convert.py %out%/Test_Convert_svg_file.svg 		PNG 	
REM python %imod%/convert.py %in%/ 							SVG 	%out%/Test_Convert_svg_dir
REM python %imod%/convert.py %out%/Test_Convert_svg_dir/ 			PNG 	
REM Test case set for PDF TODO: Currently the produced files are empty i.e. a fix is needed!
REM python %imod%/convert.py %in%/%A% 						PDF 	%out%/Test_Convert_pdf_file.pdf
REM python %imod%/convert.py %out%/Test_Convert_pdf_file.pdf 		PNG 	
REM python %imod%/convert.py %in%/ 							PDF 	%out%/Test_Convert_pdf_dir
REM python %imod%/convert.py %out%/Test_Convert_pdf_dir/ 			PNG 	


REM : flip.py
REM python %imod%/flip.py
python %imod%/flip.py %in%/%A% -h %out%/Test_flip_file_h.png
python %imod%/flip.py %out%/Test_flip_file_h.png -v 
python %imod%/flip.py %in%/ -h %out%/Test_flip_dir_h         
python %imod%/flip.py %out%/Test_flip_dir_h -h 
python %imod%/flip.py %in%/%A% -v %out%/Test_flip_file_v.png
python %imod%/flip.py %out%/Test_flip_file_v.png -h 
python %imod%/flip.py %in%/ -v %out%/Test_flip_dir_v         
python %imod%/flip.py %out%/Test_flip_dir_v -v 

REM : contrast.py
REM python %imod%/contrast.py
python %imod%/contrast.py %in%/%A% 2 %out%/Test_high_contrast_file.png
python %imod%/contrast.py %out%/Test_high_contrast_file.png 1.5
python %imod%/contrast.py %in%/ 2 %out%/Test_high_contrast_dir         
python %imod%/contrast.py %out%/Test_high_contrast_dir 3
python %imod%/contrast.py %in%/%A% 0.5 %out%/Test_low_contrast_file.png
python %imod%/contrast.py %out%/Test_low_contrast_file.png 0.3
python %imod%/contrast.py %in%/ 0.5 %out%/Test_low_contrast_dir         
python %imod%/contrast.py %out%/Test_low_contrast_dir 0.2


REM : brightness.py
REM python %imod%/brightness.py
python %imod%/brightness.py %in%/%A% 0.5 %out%/Test_brightness_0.5_file.png
python %imod%/brightness.py %out%/Test_brightness_0.5_file.png -0.2
python %imod%/brightness.py %in%/ 0.7 %out%/Test_brightness_0.7_dir
python %imod%/brightness.py %out%/Test_brightness_0.7_dir -0.3
python %imod%/brightness.py %in%/%A% 1.5 %out%/Test_brightness_1.5_file.png
python %imod%/brightness.py %out%/Test_brightness_1.5_file.png 0.3
python %imod%/brightness.py %in%/ 1.2 %out%/Test_brightness_1.2_dir
python %imod%/brightness.py %out%/Test_brightness_1.2_dir 0.4


REM : rotate.py
REM python %imod%/rotate.py
REM Rotate at 1 degree
python %imod%/rotate.py %in%/%A%  	1  %out%/Test_rotate_1_file.png
python %imod%/rotate.py %out%/Test_rotate_1_file.png  1
python %imod%/rotate.py %in%/ 1 %out%/Test_rotate_1_dir         
python %imod%/rotate.py %out%/Test_rotate_1_dir   1 
REM Rotate at -1 degree
python %imod%/rotate.py %in%/%A%  	-1  %out%/Test_rotate_neg1_file.png
python %imod%/rotate.py %out%/Test_rotate_neg1_file.png  -1
python %imod%/rotate.py %in%/ -1 %out%/Test_rotate_neg1_dir         
python %imod%/rotate.py %out%/Test_rotate_neg1_dir   -1 
REM Rotate at 5 degrees
python %imod%/rotate.py %in%/%A%  	5  %out%/Test_rotate_5_file.png
python %imod%/rotate.py %out%/Test_rotate_5_file.png  5
python %imod%/rotate.py %in%/ 5 %out%/Test_rotate_5_dir         
python %imod%/rotate.py %out%/Test_rotate_5_dir   5 
REM Rotate at -5 degrees
python %imod%/rotate.py %in%/%A%  	-5  %out%/Test_rotate_neg5_file.png
python %imod%/rotate.py %out%/Test_rotate_neg5_file.png  -5
python %imod%/rotate.py %in%/ -5 %out%/Test_rotate_neg5_dir         
python %imod%/rotate.py %out%/Test_rotate_neg5_dir   -5 
REM Rotate at 10 degrees
python %imod%/rotate.py %in%/%A%  	10  %out%/Test_rotate_10_file.png
python %imod%/rotate.py %out%/Test_rotate_10_file.png  10
python %imod%/rotate.py %in%/ 10 %out%/Test_rotate_10_dir         
python %imod%/rotate.py %out%/Test_rotate_10_dir   10 
REM Rotate at -10 degrees
python %imod%/rotate.py %in%/%A%  	-10  %out%/Test_rotate_neg10_file.png
python %imod%/rotate.py %out%/Test_rotate_neg10_file.png  -10
python %imod%/rotate.py %in%/ -10 %out%/Test_rotate_neg10_dir         
python %imod%/rotate.py %out%/Test_rotate_neg10_dir   -10 
REM Rotate at 15 degrees
python %imod%/rotate.py %in%/%A%  	15  %out%/Test_rotate_15_file.png
python %imod%/rotate.py %out%/Test_rotate_15_file.png  15
python %imod%/rotate.py %in%/ 15 %out%/Test_rotate_15_dir         
python %imod%/rotate.py %out%/Test_rotate_15_dir   15 
REM Rotate at 30 degrees
python %imod%/rotate.py %in%/%A% 30 %out%/Test_rotate_30_file.png
python %imod%/rotate.py %out%/Test_rotate_30_file.png 30
python %imod%/rotate.py %in%/ 30 %out%/Test_rotate_30_dir
python %imod%/rotate.py %out%/Test_rotate_30_dir 30
REM Rotate at 45 degrees
python %imod%/rotate.py %in%/%A% 45 %out%/Test_rotate_45_file.png
python %imod%/rotate.py %out%/Test_rotate_45_file.png 45
python %imod%/rotate.py %in%/ 45 %out%/Test_rotate_45_dir
python %imod%/rotate.py %out%/Test_rotate_45_dir 45
REM Rotate at 60 degrees
python %imod%/rotate.py %in%/%A% 60 %out%/Test_rotate_60_file.png
python %imod%/rotate.py %out%/Test_rotate_60_file.png 60
python %imod%/rotate.py %in%/ 60 %out%/Test_rotate_60_dir
python %imod%/rotate.py %out%/Test_rotate_60_dir 60
REM Rotate at 90 degrees
python %imod%/rotate.py %in%/%A% 90 %out%/Test_rotate_90_file.png
python %imod%/rotate.py %out%/Test_rotate_90_file.png 90
python %imod%/rotate.py %in%/ 90 %out%/Test_rotate_90_dir
python %imod%/rotate.py %out%/Test_rotate_90_dir 
REM Rotate at 135 degrees
python %imod%/rotate.py %in%/%A% 135 %out%/Test_rotate_135_file.png
python %imod%/rotate.py %out%/Test_rotate_135_file.png 135
python %imod%/rotate.py %in%/ 135 %out%/Test_rotate_135_dir
python %imod%/rotate.py %out%/Test_rotate_135_dir 135
REM Rotate at 180 degrees
python %imod%/rotate.py %in%/%A% 180 %out%/Test_rotate_180_file.png
python %imod%/rotate.py %out%/Test_rotate_180_file.png 180
python %imod%/rotate.py %in%/ 180 %out%/Test_rotate_180_dir
python %imod%/rotate.py %out%/Test_rotate_180_dir 180
REM Rotate at 270 degrees
python %imod%/rotate.py %in%/%A% 270 %out%/Test_rotate_270_file.png
python %imod%/rotate.py %out%/Test_rotate_270_file.png 270
python %imod%/rotate.py %in%/ 270 %out%/Test_rotate_270_dir
python %imod%/rotate.py %out%/Test_rotate_270_dir 270
REM Rotate at 360 degrees
python %imod%/rotate.py %in%/%A% 360 %out%/Test_rotate_360_file.png
python %imod%/rotate.py %out%/Test_rotate_360_file.png 360
python %imod%/rotate.py %in%/ 360 %out%/Test_rotate_360_dir
python %imod%/rotate.py %out%/Test_rotate_360_dir 360
REM Rotate at 400 degrees
python %imod%/rotate.py %in%/%A%  	400  %out%/Test_rotate_400_file.png
python %imod%/rotate.py %out%/Test_rotate_400_file.png  400
python %imod%/rotate.py %in%/ 400 %out%/Test_rotate_400_dir         
python %imod%/rotate.py %out%/Test_rotate_400_dir   400
REM Rotate at -400 degrees
python %imod%/rotate.py %in%/%A%  	-400  %out%/Test_rotate_n400_file.png
python %imod%/rotate.py %out%/Test_rotate_n400_file.png  -400
python %imod%/rotate.py %in%/ -400 %out%/Test_rotate_n400_dir         
python %imod%/rotate.py %out%/Test_rotate_n400_dir   -400



REM : auto_balance.py
REM python %imod%/auto_balance.py
python %imod%/auto_balance.py %in%/%A%  %out%/Test_autobalance_file.png
python %imod%/auto_balance.py %out%/Test_autobalance_file.png  
python %imod%/auto_balance.py %in%/  								%out%/Test_auto_balance_dir         
python %imod%/auto_balance.py %out%/Test_auto_balance_dir   


REM : resize_by_ref.py
REM python %imod%/resize_by_ref.py
python %imod%/resize_by_ref.py %in%/%C% 	%in%/%A% 		%out%/Test_resized_by_ref_file_image.png
python %imod%/resize_by_ref.py %in%/%B% 	%out%/Test_resized_by_ref_file_image.png
python %imod%/resize_by_ref.py %in%/%C% 	%in% 			%out%/Test_resize_by_ref_file_dir
python %imod%/resize_by_ref.py %in%/%B%  	%out%/Test_resize_by_ref_file_dir
REM TODO:	!!!!!! REM python %imod%/resize_by_ref.py %out%/Test_resize_by_ref_file_dir %out%/Test_trim_dir						./Test_resize_by_ref_file_one2one_dir
REM TODO:	!!!!!! REM python %imod%/resize_by_ref.py %out%/Test_resize_by_ref_file_dir %out%/Test_trim_dir						./Test_resize_by_ref_file_one2one_dir


REM : append.py
REM python %imod%/append.py
python %imod%/append.py -v %out%/test_append_file_h.png %in%/%A% 3
python %imod%/append.py -v %out%/test_append_file_h2.png %in%/%C% %in%/%B% %in%/%A%
python %imod%/append.py -h %out%/test_append_file_v.png %in%/%A% 3
python %imod%/append.py -h %out%/test_append_file_v2.png %in%/%C% %in%/%B% %in%/%A%
python %imod%/append.py -va %out%/test_append_file_h.png %in%/%A% 3
python %imod%/append.py -va %out%/test_append_file_h2.png %in%/%C% %in%/%B% %in%/%A%
python %imod%/append.py -ha %out%/test_append_file_v.png %in%/%A% 3
python %imod%/append.py -ha %out%/test_append_file_v2.png %in%/%C% %in%/%B% %in%/%A%
REM Combine repeat from 1 to 5. Include alpha layer -ha or -va
python %imod%/append.py -h %out%/Test_Append_1_h %in%/ 1
python %imod%/append.py -h %out%/Test_Append_2_h %in%/ 2
python %imod%/append.py -h %out%/Test_Append_3_h %in%/ 3
python %imod%/append.py -h %out%/Test_Append_4_h %in%/ 4
python %imod%/append.py -h %out%/Test_Append_5_h %in%/ 5
python %imod%/append.py -ha %out%/Test_Append_5_h %in%/ 5
python %imod%/append.py -v %out%/Test_Append_1_v %in%/ 1
python %imod%/append.py -v %out%/Test_Append_2_v %in%/ 2
python %imod%/append.py -v %out%/Test_Append_3_v %in%/ 3
python %imod%/append.py -v %out%/Test_Append_4_v %in%/ 4
python %imod%/append.py -v %out%/Test_Append_5_v %in%/ 5
python %imod%/append.py -va %out%/Test_Append_5_v %in%/ 5
REM Test non-continuous and Continuous mode where we go to the next if files are missing
python %imod%/append.py -v %out%/Test_append_Combined_v %out%/Test_auto_balance_dir/ %out%/Test_blur_dir/ %out%/Test_resize_by_ref_file_dir %out%/Test_resize_dir  %out%/Test_trim_dir
python %imod%/append.py -h %out%/Test_append_Combined_h %out%/Test_auto_balance_dir/ %out%/Test_blur_dir/ %out%/Test_resize_by_ref_file_dir %out%/Test_resize_dir 	%out%/Test_trim_dir
python %imod%/append.py -vc %out%/Test_append_Combined_v %out%/Test_auto_balance_dir/ %out%/Test_blur_dir/ %out%/Test_resize_by_ref_file_dir %out%/Test_resize_dir  %out%/Test_trim_dir
python %imod%/append.py -hc %out%/Test_append_Combined_h %out%/Test_auto_balance_dir/ %out%/Test_blur_dir/ %out%/Test_resize_by_ref_file_dir %out%/Test_resize_dir 	%out%/Test_trim_dir

