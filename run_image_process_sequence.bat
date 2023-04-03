REM Cleanup

REM Main Sequence
python ./Image_Process_Scripts/image_trim.py 	71 1 2 1 		./VstScreenshots/ 		 ./Output/VstThumbnails/
python ./Image_Process_Scripts/image_adjust_colour_balance.py 255 255 255 ./Output/VstThumbnails ./Output/red_shift
python ./Image_Process_Scripts/image_append.py -h 				./Output/Combined 		 ./Output/VstThumbnails 3
python ./Image_Process_Scripts/image_resize.py 	300 200  		./Output/VstThumbnails/  ./Output/VstThumbnails/

REM This part is a test script
python ./Image_Process_Scripts/image_append.py -h test1.png i1.png 3
python ./Image_Process_Scripts/image_append.py -v test2.png i1.png 3
python ./Image_Process_Scripts/image_append.py -v test3.png i1.png i2.png i3.png 
python ./Image_Process_Scripts/image_append.py -v test4.png i2.png i2.png  
python ./Image_Process_Scripts/image_append.py -h ./Output/test1 ./Output/VstThumbnails 5
python ./Image_Process_Scripts/image_append.py -v ./Output/test2 ./Output/VstThumbnails 4
python ./Image_Process_Scripts/image_append.py -v ./Output/test3 ./Output/VstThumbnails/ ./Output/red_shift/ ./Output/VstThumbnails ./Output/red_shift
