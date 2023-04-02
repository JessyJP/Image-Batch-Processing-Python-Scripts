(define (cut-top-70 image)
  (let* ((width (car (gimp-image-width image)))
         (height (car (gimp-image-height image)))
         (layer (car (gimp-image-get-active-layer image))))
    (gimp-layer-resize layer
                       width (- height 70)
                       0 70)
    (gimp-displays-flush)))
