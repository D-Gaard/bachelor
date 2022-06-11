# Bachelor Thesis Repository
Contains all code written durring bachelor project regarding "Sparse angle reconstruction using angio-
graphic images" by Andreas Leerbeck, Mads Daugaard \& Emil Riis-Jacobsen

Handed in: June 13. 2022


# File explanation
Note that all provided carm imaging data has been removed from the github.

File explaniations Weka:
wekaEvaluation.ipynb - File for calculating weka model metrics.

Folders explained
WekaOut - Folder of Weka model predictions on test dataset.

File explaniations Unet:
getData - File responsible for creating Test/Train/Validation and retriving the files.
createThresholds4All.ipynb - File for thresholding images.
createHistograms4All.ipynb - Create histograms for image sequences.

Folder
Prototype - Contains files used to prototype and test functionality
Visualisation - Contains files used to create visuals for the report
TestSegmentations - Best trained models prediction on test data 


File explaniations 3D:
project3dTo2d.ipynb - File for creating perspective projections of digital 3D model
reconstructionUncertainty.ipynb - File for visualizing and calculating the metrics for the 9 angle reconstruction.
reconstructionTranslationRotation.ipynb - File for calculating the translation and rotational metrics.
solid_400001-segmentation-solid_400001-label.nrrd - Bitmap for 3D digital model.
projectionTranslation.ipynb - File for creating the translational offset back-projections.
projectionTotal.ipynb - File for creating the 9 back-projections.
projectionRotation.ipynb - File for creating the rotational offset back-projections.
projectionDocAngles.ipynb - File for creating the back-projections with the doctor angles.
lineRenderWorldSetup.py - File containing all logic for 2D -> 3D back-projections.
lineRenderAlgo.py - File containing the Bresenham implementation.
_3dTo2dSetup.py - File for handeling all 3D -> 2D logic.

Folders explained
Snapshots - Contains output images from 3D reconstruction.
Prototype - Contains files used to prototype and test functionality
Visualisation - Contains files used to create visuals for the report
Data - The segmentations for the chosen frames
3dTo2d - Outputs of 2D projected images used