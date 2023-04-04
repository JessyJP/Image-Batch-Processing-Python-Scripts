#!/bin/sh
python ./Image_Process_Scripts/image_trim.py 	71 1 2 1 		./Input/ 		 ./Output/VstThumbnails/
python ./Image_Process_Scripts/image_adjust_colour_balance.py 255 255 255 ./Output/VstThumbnails ./Output/red_shift
REM python ./Image_Process_Scripts/image_append.py -h 				./Output/Combined 		 ./Output/VstThumbnails 3
python ./Image_Process_Scripts/image_resize.py 	300 200  		./Output/VstThumbnails/  ./Output/VstThumbnails/
