# Image-Batch-Processing-Python-Scripts
Image Batch Processing Python Scripts useful for catalog and icon making
This is effectivley set of scripts/commandline tools which  wrap the functionality of the Pillow library in Python.
The library is also known as PLI: https://github.com/python-pillow/Pillow

The scripts are very useful when the image processing can be broken down into set of simple image ateration operations.
This is indispensible when the operations have to be performed in batch.

Photoshop can perform batch processing, so can GIMP, however Photoshop is paid GIMP is not too easy to script.
Rather than that, all you need is to have python installed and run the script.
Naturally for anything more complex or where you have to makde decision based on the content of the image, well known image editing software should be used.


Originally this was intended all the necessary funtionalty for icon making. 


	Currently:
		TODO: would be nice to include more information about the min and max and type for the parameter.
		For now just look at the example script.
		TODO: generally more checks and input validation should be done. 
		TODO: For completeness crop.py and slipt.py should also be implemented 

			* adjust_colour_balance.py (Needs to be reviewd to have more logical input and output)
			* alpha_blend.py (More work needed here)
			* append.py
			* auto_balance.py (More work needed here)
			* blur.py
			* brightness.py		
			* contrast.py 
			* convert.py  (Would be nice to include more formats)
			* flip.py
			* resize.py
			* resize_by_ref.py
			* rotate.py (Looks a bit ugly when rotated. Better interpolation is needed.)
			* trim.py

				TODO: cropping
			 removeImages with specific substring
			 insert Text

			
